Intent Composition

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/intent-composition.md

⸻

1. Definition

Intent Composition is the process by which multiple related Intents are represented, ordered, constrained, or combined into a larger semantic objective without losing the identity of the individual Intents.

Composition exists because a human request may express more than one goal.

For example:

“Close my old account and move the remaining balance to my new account.”

This is not necessarily one atomic Intent.

It can be represented as:

Intent A:
TransferBalance
Intent B:
CloseAccount

with a semantic relationship:

TransferBalance
      ↓
must precede
      ↓
CloseAccount

The composed structure represents the Actor’s larger objective while preserving the individual semantic units.

⸻

2. Why Intent Composition Exists

Real-world human requests frequently contain:

multiple Actions
multiple Outcomes
dependencies
conditions
sequences
parallel goals
nested goals

Examples:

“Create a project, add Sarah, and send her the invitation.”

“Refund the payment and notify the customer.”

“Update my address everywhere.”

“Book a flight and add it to my calendar.”

Treating each sentence as an isolated Intent would lose relationships between the requested operations.

Noema therefore needs a canonical way to represent Intent relationships and composition.

⸻

3. Composition Does Not Mean Merging Everything

Composition should not collapse multiple Intents into one indistinguishable object.

For example:

"Refund the payment and email the customer."

contains at least two semantic objectives:

Intent A:
RefundPayment
Intent B:
NotifyCustomer

They may be composed:

Composite Intent
├── RefundPayment
└── NotifyCustomer

but each Intent retains its own:

Actor
Resources
Constraints
Outcome
Trust requirements
Lifecycle

Therefore:

Composition creates structure between Intents; it does not erase their identity.

⸻

4. Atomic Intent

An Atomic Intent is an Intent that represents a single semantic objective that Noema treats as indivisible for the relevant lifecycle.

Example:

RenewCard(Card#123)

or:

RefundPayment(Payment#8291)

Atomicity is contextual.

An Intent that is atomic at one abstraction level may contain multiple lower-level Actions.

For example:

Intent:
RenewCard
Actions:
VerifyEligibility
CreateReplacement
DeactivateOldCard

The Intent remains atomic from the Actor’s perspective even though execution may involve multiple Actions.

⸻

5. Composite Intent

A Composite Intent is an Intent structure containing multiple related Intents whose relationship is semantically meaningful.

Example:

Composite Intent:
PrepareEmployeeOnboarding
├── CreateEmployeeAccount
├── GrantRequiredAccess
├── CreateEmailMailbox
└── NotifyEmployee

The composite structure may define:

ordering
dependency
parallelism
conditions
shared context
shared constraints

⸻

6. Composition Is Semantic, Not Merely Procedural

A workflow is usually concerned with:

Step 1
Step 2
Step 3

Intent Composition is concerned with:

Goal A
Goal B
Goal C

and the semantic relationships between them.

For example:

“Transfer the balance and then close the account.”

The important semantic fact is:

CloseAccount
requires
TransferBalance completed

The exact API sequence is an execution concern.

Therefore:

Intent Composition ≠ Workflow Definition

⸻

7. Composition Relationships

A Composite Intent may contain relationships such as:

SEQUENCE
PARALLEL
DEPENDENCY
CONDITIONAL
OPTIONAL
ALTERNATIVE
NESTED
SHARED-CONTEXT

These relationships should be explicit rather than inferred repeatedly by downstream systems.

⸻

8. Sequential Composition

Sequential composition expresses an ordering relationship.

Example:

“Create the account and then send me the credentials.”

CreateAccount
      ↓
SendCredentials

The second Intent depends on the first.

The semantic relationship is:

SendCredentials
after
CreateAccount

The exact execution mechanism is separate.

⸻

9. Parallel Composition

Some Intents can be pursued independently.

Example:

“Update my address and change my notification preferences.”

UpdateAddress
      │
      ├──────────┐
      │          │
      ▼          ▼
   Complete   ChangePreferences

There may be no semantic dependency between them.

They can therefore be composed as parallel Intents.

Parallel composition does not require simultaneous execution.

It means:

Neither Intent semantically depends on the completion of the other.

⸻

10. Dependency Composition

An Intent may depend on another Intent without necessarily requiring strict sequential execution.

Example:

CreateProject
      ↓
AddMembers

AddMembers depends on the Project existing.

The dependency is semantic:

Project must exist

not necessarily:

API call A must finish exactly 100ms before API call B.

⸻

11. Conditional Composition

An Intent may depend on a condition.

Example:

“If the payment failed, retry it; otherwise send the receipt.”

Conceptually:

PaymentResult
      ↓
 ┌────┴────┐
 │         │
Failed   Successful
 │         │
 ▼         ▼
Retry    SendReceipt

The condition belongs to the semantic composition.

Execution logic determines how that condition is evaluated.

⸻

12. Optional Composition

An Intent may contain an optional subordinate Intent.

Example:

“Book the flight and, if possible, add it to my calendar.”

BookFlight
    │
    └── OPTIONAL → AddToCalendar

Failure of the optional Intent does not necessarily invalidate the primary Intent.

The semantics of optionality should be explicit.

⸻

13. Alternative Composition

An Intent may express alternatives.

Example:

“Either renew my card or issue a replacement, whichever is appropriate.”

Conceptually:

             Card Resolution
                  │
          ┌───────┴────────┐
          ▼                ▼
     RenewCard       IssueReplacement

The alternative is not a request to perform both.

Noema must establish a selection condition.

⸻

14. Nested Intent

An Intent may contain subordinate Intents.

Example:

“Prepare my employee onboarding.”

This may compose:

PrepareOnboarding
├── CreateAccount
├── ProvisionEmail
├── GrantAccess
└── NotifyEmployee

The parent Intent represents the higher-level Outcome.

The children represent semantic subgoals.

⸻

15. Parent and Child Intent

A parent Intent defines a broader objective.

A child Intent represents a subordinate objective required to satisfy it.

Example:

Parent:
OnboardEmployee
Children:
CreateEmployeeAccount
GrantAccess
SendWelcomeEmail

The relationship does not mean that the child is merely an implementation step.

Each child has its own semantic meaning.

⸻

16. Composition Must Preserve Intent Identity

Each child Intent should retain its own identity.

Conceptually:

CompositeIntent: CI-100
Intent: I-101
Intent: I-102
Intent: I-103

This allows Noema to independently track:

resolution
clarification
Trust
Action
Outcome
failure
retry

for each constituent Intent.

⸻

17. Shared Actor

Multiple Intents may share the same Actor.

Example:

“Update my address and change my phone number.”

Actor:
Alice
Intent A:
UpdateAddress
Intent B:
UpdatePhoneNumber

The Actor is common, but each Intent remains distinct.

⸻

18. Different Actors

Composition can also involve multiple Actors where the domain permits it.

Example:

“Ask Sarah to approve the invoice and then notify the customer.”

Potential structure:

Intent A:
RequestApproval
Actor:
System / Alice
Intent B:
ApproveInvoice
Actor:
Sarah
Intent C:
NotifyCustomer
Actor:
System

The Actor associated with each Intent must remain explicit.

Noema must not assume that the Actor of the parent automatically becomes the Actor of every child.

⸻

19. Shared Resources

Multiple Intents may operate on the same Resource.

Example:

“Update the customer’s address and notify them.”

Resource:
Customer#123
Intent A:
UpdateAddress
Intent B:
NotifyCustomer

The shared Resource relationship can be represented explicitly.

⸻

20. Resource Dependencies

One Intent may create or transform a Resource required by another.

Example:

CreateInvoice
      ↓
SendInvoice

The output Resource of the first Intent becomes an input Resource of the second.

This relationship should be explicit in the composition graph.

⸻

21. Shared Constraints

A Composite Intent may have constraints applying to all constituent Intents.

Example:

“Update everything before the end of the business day.”

Composite Intent
Constraint:
Deadline = Today 17:00
├── UpdateAddress
├── UpdatePhone
└── UpdatePreferences

Child Intents may additionally have their own constraints.

Therefore:

Composite Constraints
+
Child Constraints

must be evaluated according to their defined scope.

⸻

22. Shared Context

A Composite Intent may establish Context that applies to its children.

Example:

“For the Acme account, update the billing contact and notify the finance team.”

Shared Context:
Account = Acme
├── UpdateBillingContact
└── NotifyFinance

This avoids repeatedly reconstructing the same semantic context.

⸻

23. Composition and Clarification

A Composite Intent may contain one unresolved child while others are fully resolved.

Example:

Composite Intent
├── UpdateAddress       RESOLVED
├── UpdatePhone         RESOLVED
└── NotifyEmployer      AMBIGUOUS

Noema should not necessarily discard the entire composite structure.

Instead:

Composite
   ↓
Child Intent C
   ↓
CLARIFY

The unresolved child can be clarified independently.

⸻

24. Composition and Partial Resolution

Intent composition therefore supports partial resolution.

For example:

Intent A:
Resolved
Intent B:
Resolved
Intent C:
Clarification required

The Composite Intent is not fully Executable until its required constituents are resolved.

However, Noema may determine that some independent children can proceed if the composition semantics permit it.

This must be explicitly defined rather than assumed.

⸻

25. Composition and Executable Intent

A Composite Intent can become an Executable Composite Intent when all required constituent Intents are sufficiently resolved.

Conceptually:

Composite Intent
├── Executable Intent A
├── Executable Intent B
└── Executable Intent C

subject to:

dependencies
constraints
policy
authority
current state

The composite itself still requires Trust evaluation.

⸻

26. Composition and Trust

Trust may need to be evaluated at multiple levels.

For example:

Composite Intent:
CloseAccount
├── TransferBalance
└── CloseAccount

The Actor may have authority to transfer funds but not authority to close the account.

Therefore:

Trust(TransferBalance)
Trust(CloseAccount)

may produce different results.

A parent-level Trust decision must not automatically authorize every child Intent.

⸻

27. Composition and Policy

Policies may apply at:

Composite level
Child level
Action level
Resource level

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
No approval required.

Each child retains its own Policy requirements.

⸻

28. Composition and Authority

Authority should be evaluated according to the Actor and Action associated with each Intent.

A user may be authorized to:

UpdateCustomerAddress

but not:

DeleteCustomerAccount

even if both appear inside one Composite Intent.

Therefore:

Composition does not aggregate authority.

⸻

29. Composition and Failure

A Composite Intent may contain children with different failure semantics.

Example:

CreateAccount
GrantAccess
SendWelcomeEmail

If email delivery fails:

Account creation = successful
Access grant = successful
Email = failed

the parent Outcome may still be partially satisfied.

Noema therefore needs to distinguish:

Intent state
Action state
Outcome state

for each constituent Intent.

⸻

30. Composition and Compensation

Some compositions require compensating Actions when a later Intent fails.

Example:

CreateSubscription
      ↓
ChargeCustomer
      ↓
ProvisionService

If provisioning fails after payment succeeds, the system may need:

RefundPayment

This is primarily an execution concern.

However, the semantic composition should expose enough dependency information for the execution layer to determine appropriate compensation.

⸻

31. Composition Is Not Transactionality

Two Intents being composed does not mean they form one atomic transaction.

For example:

UpdateCRM
+
SendEmail

may not be transactionally coupled.

The composition defines the semantic relationship.

The execution system determines whether the underlying Actions support:

atomicity
rollback
compensation
retry
eventual consistency

Therefore:

Intent Composition ≠ Distributed Transaction

⸻

32. Composition and Outcome

A Composite Intent may have:

individual Outcomes

and:

a Composite Outcome

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

The parent Outcome should be derived from the semantic requirements of the composition, not simply from whether every Action returned HTTP 200.

⸻

33. Composition and Outcome Dependencies

Some parent Outcomes require specific child Outcomes.

Example:

Composite:
TransferAndCloseAccount
Required:
Transfer completed
AND
Account closed

If only the transfer succeeds:

Composite Outcome:
Not satisfied

even though one child succeeded.

This is why Outcome semantics must remain explicit.

⸻

34. Composition Graph

A useful canonical representation is a directed graph:

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

depends_on
precedes
enables
requires
conditional_on
alternative_to

This fits naturally with Noema’s broader ontology.

⸻

35. Composition Must Be Explicit

Noema should avoid reconstructing composition from execution logs after the fact.

If the Actor expressed:

“Transfer the balance and then close the account.”

the semantic relationship should exist before execution:

TransferBalance
    precedes
CloseAccount

The execution layer consumes that relationship.

⸻

36. Composition and Natural Language

Natural language can encode composition through:

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

For example:

“Update my address and notify my employer.”

UpdateAddress
AND
NotifyEmployer

“Update my address, then notify my employer.”

UpdateAddress
PRECEDES
NotifyEmployer

“Notify my employer if the address update succeeds.”

NotifyEmployer
CONDITIONAL_ON
UpdateAddress.Success

The linguistic relationship should be translated into a canonical semantic relationship.

⸻

37. Composition Must Preserve Human Intent

Noema should not create unnecessary composition merely because an Action happens to require multiple internal operations.

For example:

“Renew my card.”

The execution system may perform:

CheckEligibility
CreateReplacement
UpdateAccount
DeactivateOldCard

These do not automatically become four user-level Intents.

They may simply be Actions required to satisfy one Intent.

Therefore:

Intent composition is driven by semantic goals, not by implementation step count.

⸻

38. Composition vs Action Decomposition

These must remain distinct.

Intent Composition

Multiple semantic goals.

RefundPayment
+
NotifyCustomer

Action Decomposition

One semantic goal requiring multiple operations.

RenewCard
    ↓
VerifyEligibility
    ↓
CreateCard
    ↓
UpdateAccount

This distinction is critical to maintaining Noema’s abstraction boundary.

⸻

39. Composition and User Expression

A single sentence may contain:

one Intent

or:

multiple Intents

Conversely, multiple sentences may represent:

one Intent

Example:

“I need to replace my card. It’s expired.”

This is probably one Intent:

ReplaceCard

The second sentence provides Context or justification.

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

Noema should preserve that relationship where it matters.

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

This can produce:

Composite Intent
├── BookFlight
├── AddToCalendar
└── SendItinerary

with relevant dependencies.

Composition therefore operates over an Intent lifecycle, not merely a single user message.

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

Human:

“Actually, don’t notify Sarah.”

The resulting composition may become:

BookFlight
AddToCalendar
NotifySarah → CANCELLED

The remaining Intents should retain their identity and state.

⸻

43. Composition and Modification

The Actor may modify part of a Composite Intent.

Example:

“Book the flight and add it to my calendar.”

Then:

“Actually, don’t add it to my calendar.”

Noema should update:

AddToCalendar → CANCELLED

without necessarily invalidating:

BookFlight

provided there is no semantic dependency requiring the cancelled child.

⸻

44. Composition and Reuse

A resolved Intent may become a dependency or Context source for another Intent.

Example:

CreateCustomer
      ↓
SendWelcomeEmail

The output of the first Intent may provide:

Customer ID
Email address
Customer Context

to the second.

This allows Noema to construct semantic chains without forcing every downstream Action to independently rediscover state.

⸻

45. Composition and Idempotency

Each constituent Intent should have its own identity.

This allows the system to determine:

Intent A already satisfied
Intent B pending
Intent C failed

rather than treating the entire Composite Intent as an opaque unit.

This is especially important for retries and partial failures.

⸻

46. Composition and Audit

The audit trail should preserve:

Parent Intent
Child Intents
Composition relationships
Resolution history
Trust decisions
Actions
Outcomes

Example:

Composite: OffboardEmployee#123
├── RevokeGitHubAccess
│   ├── Trust: Permit
│   └── Outcome: Success
│
├── DisableEmail
│   ├── Trust: Permit
│   └── Outcome: Success
│
└── NotifyManager
    ├── Trust: Permit
    └── Outcome: Failed

This provides a complete semantic and operational history.

⸻

47. Composition and Re-evaluation

If a child Intent changes materially, the parent composition may need re-evaluation.

Example:

Parent:
CloseAccount
Child:
TransferBalance

If the transfer destination changes:

TransferBalance
Resource/Parameter changed

the parent may need to be revalidated because the dependency relationship could have changed.

Composition is therefore not merely static structure.

⸻

48. Composition and Determinism

The composition graph should be explicit enough that downstream systems can determine:

which Intents exist
which depend on which
which may execute independently
which are conditional
which are optional
which Outcomes are required

without asking the Model to reinterpret the original request.

⸻

49. Canonical Composition Model

Conceptually:

CompositeIntent
├── identity
├── actor
├── context
├── constraints
├── intents[]
│   ├── identity
│   ├── intent
│   ├── resources
│   ├── constraints
│   └── expected_outcome
├── relationships[]
│   ├── type
│   ├── source
│   ├── target
│   └── condition
└── expected_outcome

This is conceptual, not a required implementation schema.

⸻

50. Canonical Composition Rules

Noema should follow these rules:

Rule 1 — Preserve Intent Identity

Composing Intents must not erase their individual identities.

Rule 2 — Composition Is Semantic

Composition represents relationships between goals, not merely execution steps.

Rule 3 — Intent Boundaries Are Semantic

Sentence boundaries do not determine Intent boundaries.

Rule 4 — Dependencies Must Be Explicit

If one Intent depends on another, that dependency must be represented.

Rule 5 — Trust Is Not Automatically Inherited

A parent Trust decision does not automatically authorize every child Intent.

Rule 6 — Partial Resolution Is Permitted

Individual child Intents may resolve independently.

Rule 7 — Partial Execution Is Not Automatically Failure

The semantic meaning of partial completion depends on the composition.

Rule 8 — Parent Outcome Must Be Explicit

The Composite Outcome should define what constitutes successful completion.

Rule 9 — Implementation Steps Are Not Automatically Intents

Action decomposition must remain separate from Intent composition.

Rule 10 — Composition Must Be Auditable

The relationship between constituent Intents must survive through the lifecycle.

⸻

51. Canonical Example

Human:

“Close my old bank account, transfer the remaining balance to my savings account, and email me the confirmation.”

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

Old account closed
AND
remaining balance transferred
AND
confirmation delivered

This is substantially richer than simply generating three API calls.

⸻

52. The Key Architectural Distinction

Noema should maintain this hierarchy:

Actor
   ↓
Intent
   ↓
Intent Composition
   ↓
Executable Intent
   ↓
Trust
   ↓
Action
   ↓
Outcome

Where:

Intent

represents a goal,

Intent Composition

represents relationships between goals,

Executable Intent

represents a sufficiently resolved goal,

and:

Action

represents what the system actually does.

⸻

53. What Intent Composition Protects Against

Composition protects against:

Lost dependencies
Incorrect ordering
Unintended partial execution
Semantic drift between related operations
Incorrect parent/child relationships
Repeated interpretation of context
Loss of user-stated conditions

It gives Noema a formal representation of multi-intent requests.

⸻

54. What Intent Composition Does Not Do

Intent Composition does not:

execute Actions
authorize Actors
replace Policy
replace Constraints
define implementation workflows
guarantee transactionality
guarantee Outcome success

It defines the semantic structure of multiple related Intents.

⸻

55. Final Definition

Intent Composition is the canonical representation of multiple semantically related Intents and the dependencies, ordering, conditions, alternatives, shared Context, and Outcomes that connect them into a larger Actor objective.

The essential pipeline is:

Human Expression
       ↓
Intent Detection
       ↓
Intent Decomposition
       ↓
┌─────────────────────────────┐
│      Intent Composition     │
│                             │
│  Intent A ──→ Intent B      │
│      │            │         │
│      └────→ Intent C        │
└──────────────┬──────────────┘
               ↓
       Intent Resolution
               ↓
      Executable Intents
               ↓
             Trust
               ↓
            Actions
               ↓
           Outcomes

The shortest canonical formulation is:

A Composite Intent preserves what the Actor wants, while making explicit how the constituent goals relate to one another.