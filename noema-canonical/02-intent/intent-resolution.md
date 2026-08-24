Intent Resolution

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: 02-intent/intent-resolution.md

⸻

1. Definition

Intent Resolution is the deterministic process by which Noema transforms a candidate Intent into a sufficiently complete, grounded, and unambiguous Intent that can be evaluated for executability and Trust.

Resolution answers:

“Do we know what the Actor means well enough to proceed?”

It does not answer:

“Should we execute it?”

That is the responsibility of Trust and Policy.

⸻

2. Why Resolution Exists

A Model can produce a plausible interpretation of a request without that interpretation being sufficiently reliable for execution.

For example:

“Cancel my subscription.”

If the Actor has:

Subscription#123
Subscription#456

the Model may select one.

Noema must not treat plausibility as resolution.

Instead:

Natural Language
       ↓
Candidate Intent
       ↓
Resolution
       ↓
Ambiguity?
   ┌───┴───┐
  Yes      No
   ↓        ↓
Clarify   Resolved
            ↓
        Executability

Resolution is therefore one of the primary deterministic boundaries in Noema.

⸻

3. Resolution vs Interpretation

These are distinct stages.

Interpretation

What might the Actor mean?

Resolution

Which interpretation is sufficiently established to become the canonical Intent?

For example:

Expression:
"Renew the card I used yesterday."

Interpretation:

RenewCard

Candidate Resources:

Card#123
Card#456

Resolution determines whether available evidence establishes one of those cards.

⸻

4. Resolution vs Clarification

Clarification is one mechanism used when resolution cannot otherwise be achieved.

Resolution
    ↓
Can meaning be established?
    ├── Yes → RESOLVED
    └── No
         ↓
     Clarification

Therefore:

Clarification is a resolution mechanism, not a substitute for resolution.

⸻

5. Resolution vs Confidence

Confidence expresses the strength of an interpretation.

Resolution determines whether the available evidence is sufficient to proceed.

These are not equivalent.

Example:

Candidate:
Card#123
Model confidence:
0.97
Competing candidate:
Card#456

If both remain materially plausible:

Resolution:
FAILED / AMBIGUOUS

despite high Model confidence.

Conversely, an interpretation may have modest Model confidence but become deterministically resolved by authoritative evidence.

⸻

6. Resolution vs Trust

Resolution asks:

"What does the Actor mean?"

Trust asks:

"May this Intent be executed?"

The canonical sequence is:

Interpretation
      ↓
Resolution
      ↓
Executability
      ↓
Trust
      ↓
Execution

Trust should not compensate for unresolved semantic ambiguity.

⸻

7. Resolution Inputs

Intent Resolution may consume:

Candidate Intent
Actor
Conversation Context
Domain Context
Entities
Resources
Relationships
Constraints
Preferences
Policies
Authoritative data
External evidence
Actor clarification
System state

The exact evidence depends on the Intent.

⸻

8. Resolution Output

Resolution should produce one of several outcomes.

Resolved

Intent:
RenewCard(Card#123)

Ambiguous

Intent:
RenewCard(Card#123 | Card#456)

Missing Information

Intent:
TransferFunds
Destination:
UNKNOWN

Invalid

Intent:
TransferFunds
Amount:
INVALID

Unsupported

Intent:
TeleportPerson

The resolution result should make the reason for non-resolution explicit.

⸻

9. Resolution Is Evidence-Based

Noema should resolve Intent components using evidence rather than intuition.

Evidence may come from:

explicit Actor statements
conversation history
Context
canonical ontology
authoritative system records
Resource relationships
domain rules
previously established Intent state

The strongest available evidence should generally take precedence over weaker inference.

⸻

10. Evidence Hierarchy

A useful canonical ordering is:

1. Explicit current Actor statement
2. Explicit prior Actor statement
3. Authoritative domain state
4. Established Context
5. Deterministic domain relationship
6. Derived semantic inference
7. Model inference

This is a conceptual hierarchy rather than an absolute rule for every domain.

When evidence conflicts, Noema must not silently select the most convenient interpretation.

⸻

11. Explicit Actor Intent Has Primacy

If the Actor explicitly specifies a value, Noema should not replace it with an inferred value.

Example:

“Send the invoice to Sarah.”

Even if the system normally sends invoices to the account owner, the explicit recipient should remain Sarah unless Policy or domain rules prevent it.

⸻

12. Current Context Has Temporal Relevance

More recent explicit information may supersede older context.

Example:

“Book the flight for Friday.”

Later:

“Actually, Saturday.”

Resolution should produce:

Date:
Saturday

rather than combining both values.

⸻

13. Authoritative State

When an Intent references an external Resource, Noema should resolve against authoritative domain state where possible.

Example:

“Cancel my active subscription.”

Noema may query the subscription system to determine:

Subscription#123 → Active
Subscription#456 → Cancelled

The Resource resolves to:

Subscription#123

The business system remains authoritative for the subscription’s actual state.

⸻

14. Grounding

Resolution often requires grounding.

Example:

“Renew the card I used yesterday.”

The phrase:

"card I used yesterday"

must be grounded through evidence:

Transaction history
      ↓
Transaction#789
      ↓
Card#123

Result:

RenewCard(Card#123)

Grounding converts references into canonical Entities or Resources.

⸻

15. Entity Resolution

Entity resolution determines which canonical Entity a linguistic reference denotes.

Example:

“Send it to Sarah.”

Possible entities:

Sarah#123
Sarah#456
Sarah#789

If Context establishes:

Sarah = Sarah#123

the reference is resolved.

Otherwise:

AMBIGUOUS

⸻

16. Resource Resolution

Resource resolution identifies the domain object affected by the Intent.

Example:

“Delete the project.”

Possible Resources:

Project#1
Project#2
Project#3

If the Actor has one currently active project in Context:

Project#1

may be resolved.

If several remain plausible:

CLARIFICATION_REQUIRED

⸻

17. Reference Resolution

Natural language frequently uses references:

it
that
them
the previous one
my account
the card
the other project

Noema should resolve these against Context and canonical relationships.

Example:

User:
Create a project called Noema.
User:
Add Sarah to it.

“It” resolves to:

Project#Noema

⸻

18. Scope Resolution

Resolution must determine the intended scope.

Example:

“Delete the inactive projects.”

Potential interpretations:

one project
all inactive projects
all projects

The canonical interpretation is:

Scope:
Collection
Filter:
State = Inactive

Scope ambiguity can be execution-critical and must not be ignored.

⸻

19. Quantifier Resolution

Terms such as:

all
any
every
one
the
a
each
none

may materially alter the Intent.

Example:

“Notify all administrators.”

is not:

NotifyAdministrator(single)

The Intent Model must preserve quantification.

⸻

20. Temporal Resolution

Relative time expressions require Context.

Examples:

today
tomorrow
next Friday
yesterday
in two hours
later
before lunch

Resolution should normalize these against the appropriate temporal Context.

Example:

"next Friday"

becomes a concrete temporal value once the relevant timezone and current date are established.

⸻

21. Spatial Resolution

Likewise:

near me
at the office
in London
the Lagos branch
the warehouse

may require Context or authoritative location data.

Resolution should convert these expressions into canonical locations where necessary.

⸻

22. Constraint Resolution

Constraints themselves may require interpretation.

Example:

“Book something cheap.”

What does “cheap” mean?

Possible interpretations:

Price < $500
lowest available price
below Actor's historical average

If the domain provides a deterministic definition, it may be resolved.

If not, Noema may need clarification.

Noema must not invent a material threshold merely because one seems reasonable.

⸻

23. Preference Resolution

Preferences may also require semantic normalization.

Example:

“I’d rather leave in the afternoon.”

This might resolve to:

Preference:
DepartureTime ∈ Afternoon

rather than:

Constraint:
DepartureTime >= 12:00

unless the Actor establishes a hard requirement.

⸻

24. Resolution of Defaults

Defaults may resolve missing values when they are:

canonical
known
safe
non-material

Example:

Project visibility:
Private

if Private is the explicit system default.

Defaults must not be used to hide material uncertainty.

⸻

25. Materiality

Not every unresolved value requires clarification.

Resolution should ask:

Would choosing between the possible values materially change the Intent, its execution, its risk, or its Outcome?

Example:

Email formatting:
HTML vs plain text

may not be material.

But:

Bank account:
Savings vs Emergency

is material.

Material ambiguity must block progression.

⸻

26. Deterministic Resolution

Where deterministic evidence exists, Noema should prefer deterministic resolution.

Example:

Actor:
User#123
Only active subscription:
Subscription#456
Request:
"Cancel my active subscription."

Resolution:

Subscription#456

No clarification is necessary.

⸻

27. Non-Deterministic Resolution

Where multiple materially plausible interpretations remain, Noema should not force resolution.

Example:

Actor owns:
Card#123
Card#456
Request:
"Renew my card."

Resolution:

AMBIGUOUS

The correct behavior is clarification.

⸻

28. No Guessing Across Material Ambiguity

This is a core Noema invariant.

If materially different interpretations remain plausible and cannot be deterministically distinguished, Noema must not select one merely because it is more probable.

Instead:

AMBIGUOUS
    ↓
CLARIFICATION_REQUIRED

This is the practical expression of Noema’s deterministic Trust boundary.

⸻

29. Resolution of Composite Intents

Each constituent Intent must be independently resolved.

Example:

“Refund the payment and close the account.”

RefundPayment
    → Resolved
CloseAccount
    → Resolved

If:

RefundPayment
    → Resolved
CloseAccount
    → Ambiguous

the parent Composite Intent cannot be treated as fully resolved.

⸻

30. Dependency-Aware Resolution

Some Intent components depend on others.

Example:

“Transfer the balance to my other account.”

The phrase:

"other account"

cannot be resolved until the current source account is established.

Resolution may therefore proceed:

Resolve source
      ↓
Identify other eligible accounts
      ↓
Resolve destination

Resolution is consequently a dependency-aware process.

⸻

31. Resolution Order

There is no universal mandatory order, but a useful canonical pattern is:

Actor
  ↓
Objective
  ↓
Context
  ↓
Entities
  ↓
Resources
  ↓
Constraints
  ↓
Preferences
  ↓
Relationships
  ↓
Expected Outcome

The actual order may vary where dependencies require it.

⸻

32. Resolution and Context Propagation

Context should propagate only where semantically valid.

Example:

User:
Create project Noema.
User:
Add Sarah to it.

The project reference propagates.

But unrelated Context should not automatically contaminate the new Intent.

Noema should avoid broad, implicit context inheritance.

⸻

33. Context Boundaries

A useful distinction is:

Conversation Context
Session Context
Intent Context
Domain Context
Execution Context

Resolution should know which Context layer is authoritative for a given field.

This prevents an old conversational fact from overriding current authoritative domain state.

⸻

34. Conflict Resolution

Evidence may conflict.

Example:

Actor:
"Send it to Sarah."
CRM:
Sarah's account is inactive.
Policy:
Inactive accounts cannot receive invoices.

The semantic Intent may still be:

SendInvoice → Sarah

while Policy later blocks execution.

Resolution should not alter the Actor’s meaning merely because execution may be prohibited.

This preserves the distinction between:

Resolution

and:

Trust / Policy

⸻

35. Resolution Must Not Optimize Away Intent

Suppose the Actor says:

“Transfer $5,000 to savings.”

Noema discovers that transferring $5,000 would violate a daily transfer limit.

Resolution should remain:

TransferFunds($5,000)

not silently transform it into:

TransferFunds($2,000)

The latter is a different Intent.

Policy or execution constraints must not silently rewrite Actor intent.

⸻

36. Resolution and Capability Discovery

Capability discovery can help establish whether an Intent is executable.

However, absence of a Capability does not necessarily mean the Intent is semantically unresolved.

Example:

Intent:
TeleportPerson

The meaning is clear.

There is simply no Capability.

Therefore:

Resolution:
SUCCESS
Executability:
UNSUPPORTED

⸻

37. Resolution and Business State

Business State may provide evidence for resolution.

Example:

“Cancel my active subscription.”

The subscription system provides:

Subscription#123 = Active
Subscription#456 = Cancelled

This helps resolve the Resource.

But Noema does not become the owner of that Business State.

⸻

38. Resolution and Intent State

Resolution modifies the Intent’s semantic completeness and therefore may drive lifecycle transitions.

For example:

AMBIGUOUS
    ↓
Actor clarifies
    ↓
RESOLVED

But the lifecycle state itself remains governed by intent-lifecycle.md.

⸻

39. Resolution Evidence

A resolution decision should ideally record:

candidate
selected value
rejected alternatives
evidence
evidence source
resolution rule
timestamp

Example:

Resource:
Card#123
Evidence:
Transaction#789
Rule:
"card I used yesterday" resolved to the card
associated with the most recent qualifying transaction.
Rejected:
Card#456

This makes resolution explainable.

⸻

40. Resolution Provenance

Resolution provenance answers:

Why was this semantic value selected?

Example:

"the card I used yesterday"
        ↓
Transaction#789
        ↓
Card#123

This chain should remain available where material to the decision.

⸻

41. Resolution and Auditability

Every material resolution should be reproducible from its evidence.

Given the same:

Intent
Context
Ontology
Authoritative State
Evidence
Resolution Rules

Noema should reach the same resolution result.

This is a core deterministic property.

⸻

42. Resolution and Model Role

The Model may propose:

candidate Intent
candidate Entity
candidate Resource
candidate Constraint
candidate interpretation

Noema determines whether the candidate is sufficiently established.

Conceptually:

Model
  ↓
Hypothesis
Noema
  ↓
Resolution

The Model generates possibilities.

Noema governs semantic commitment.

⸻

43. Resolution as a Commitment Boundary

Before resolution:

Candidate meaning

After resolution:

Canonical meaning

This is one of the most important boundaries in Noema.

PROBABILISTIC
      │
      ▼
Candidate Intent
      │
      ▼
   RESOLUTION
      │
      ▼
DETERMINISTIC
      │
      ▼
Canonical Intent

⸻

44. Resolution and Trust

Trust should consume the resolved Intent rather than raw Model output.

Bad architecture:

Model
 ↓
Action

Better:

Model
 ↓
Candidate Intent
 ↓
Resolution
 ↓
Canonical Intent
 ↓
Trust
 ↓
Action

This is the architectural mechanism by which Noema prevents Model uncertainty from becoming uncontrolled execution.

⸻

45. Resolution Failure Classes

Noema should distinguish at least:

Ambiguous

Multiple valid interpretations remain.

Incomplete

Required information is missing.

Invalid

The candidate violates semantic rules.

Contradictory

The supplied information conflicts internally.

Unsupported

The meaning is clear but no applicable Capability exists.

Unverifiable

The system cannot obtain sufficient evidence to establish a material claim.

These conditions should not collapse into a generic “failed.”

⸻

46. Ambiguous vs Incomplete

These are related but distinct.

Ambiguous

“Cancel my subscription.”

Two subscriptions exist.

Multiple plausible values

Incomplete

“Transfer money.”

No amount or destination has been supplied.

Required information absent

The appropriate clarification differs.

⸻

47. Invalid vs Contradictory

Invalid

The value itself violates a semantic rule.

Amount = "banana"

Contradictory

Two valid statements conflict.

Departure:
Friday
Constraint:
Departure must be Saturday

Noema must determine whether the contradiction can be resolved through recency, explicit correction, or clarification.

⸻

48. Resolution and Clarification Generation

When clarification is required, the question should target the smallest unresolved semantic unit.

Bad:

“Can you clarify your request?”

Better:

“Which subscription do you want to cancel: Premium or Business?”

The Intent Model allows Noema to know exactly what is missing.

⸻

49. Minimal Clarification Principle

Ask only for information necessary to resolve material ambiguity or satisfy semantic completeness.

Noema should not ask:

"What exactly do you want?"

when it already knows:

Objective
Actor
Resource candidates
Context

and only needs:

which Resource

⸻

50. Resolution Should Be Monotonic

Where possible, resolution should add information rather than repeatedly reinterpret established information.

Example:

Initial:
RenewCard
After grounding:
RenewCard(Card#123)
After clarification:
RenewCard(Card#123, expedited=true)

New evidence should extend or correct the model only where justified.

Previously established facts should not be casually discarded.

⸻

51. Resolution and Actor Corrections

The Actor may explicitly correct a previous interpretation.

Example:

Noema: “Do you mean your personal account?”

Actor: “No, the business account.”

The new explicit statement supersedes the previous candidate interpretation.

Resolution becomes:

Account:
BusinessAccount

The correction should be recorded as provenance.

⸻

52. Resolution and External Changes

The world can change while an Intent is being resolved.

Example:

09:00:
Card#123 = Active
09:05:
Card#123 = Cancelled

The resolution system must distinguish:

semantic resolution

from:

current domain state

A resolved Resource may later become unavailable.

That is an execution/state problem, not necessarily a resolution failure.

⸻

53. Resolution and Staleness

Evidence can become stale.

For example:

Yesterday's account state

may not be sufficient to establish:

Current authorization

Noema should consider evidence freshness where the domain makes freshness material.

⸻

54. Resolution and Deterministic Reproducibility

A resolution decision should ideally be reproducible.

For:

Candidate Intent
+
Evidence
+
Resolution Rules

Noema should produce:

Resolved Intent

without relying on an uncontrolled probabilistic decision at the final commitment boundary.

⸻

55. Resolution Invariants

Invariant 1

No materially ambiguous Intent may become Resolved through confidence alone.

Invariant 2

No material assumption may be silently introduced during resolution.

Invariant 3

Explicit Actor corrections supersede prior inferred interpretations.

Invariant 4

Authoritative domain evidence may ground Resources and Entities.

Invariant 5

Resolution must not rewrite Actor intent to satisfy Policy.

Invariant 6

Resolution must precede Trust-dependent execution.

Invariant 7

Every material resolution should have explainable provenance.

Invariant 8

The absence of a Capability does not imply semantic ambiguity.

Invariant 9

Business State and Intent State remain separate.

Invariant 10

If resolution cannot safely establish meaning, Noema must transition to clarification, rejection, or another explicitly defined non-executable state.

⸻

56. Canonical Resolution Flow

                 Actor Expression
                       │
                       ▼
                Candidate Intent
                       │
                       ▼
                 Ground References
                       │
                       ▼
                Gather Evidence
                       │
                       ▼
              Evaluate Alternatives
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
      One sufficient        Multiple material
       interpretation          interpretations
             │                   │
             ▼                   ▼
         RESOLVED             AMBIGUOUS
             │                   │
             │                   ▼
             │             CLARIFICATION
             │                   │
             │                   ▼
             │              New Evidence
             │                   │
             └───────────┬───────┘
                         ▼
                     RESOLVED
                         │
                         ▼
                   EXECUTABLE
                         │
                         ▼
                      TRUST

⸻

57. Example: Card Renewal

Expression

“Renew the card I used yesterday.”

Candidate Intent

Objective:
RenewCard
Resource:
Card used yesterday

Evidence

Transaction#789 → Card#123
Transaction#790 → Card#456

If only Transaction#789 qualifies:

Resource:
Card#123

Result

RESOLVED

If both qualify:

AMBIGUOUS

Noema asks:

“Which card do you mean: the Visa ending in 1234 or the Mastercard ending in 5678?”

⸻

58. Example: Transfer

Expression

“Send $500 to my other account.”

Candidate:

Objective:
TransferFunds
Amount:
$500
Source:
CurrentAccount
Destination:
OtherAccount

Evidence:

Savings#1
Investment#2

Both qualify.

Result:

AMBIGUOUS

Clarification:

“Which account should receive the $500: Savings or Investment?”

⸻

59. Example: Clear but Unsupported

Expression:

“Teleport me to London.”

Candidate:

Objective:
TeleportPerson
Destination:
London

Resolution:

SUCCESS

Executability:

UNSUPPORTED

This illustrates why semantic resolution and Capability availability must remain separate.

⸻

60. Example: Clear but Policy-Blocked

Expression:

“Refund this $50,000 payment.”

Resolution:

RefundPayment(Payment#123)

Executability:

SUPPORTED

Policy:

ManagerApprovalRequired

Result:

POLICY_BLOCKED

The Intent itself was never ambiguous.

⸻

61. Resolution and Noema’s Thesis

Intent Resolution operationalizes one of Noema’s central principles:

The model may be probabilistic; the commitment to executable meaning must be governed.

The Model can say:

"I think this is what the user means."

Noema must determine:

"This is sufficiently established to proceed."

That distinction is foundational to Noema.

⸻

62. Final Definition

Intent Resolution is the governed process of grounding, completing, and disambiguating a candidate Intent using explicit Actor input, Context, authoritative evidence, and deterministic semantic rules until Noema can either establish a canonical meaning or explicitly determine that clarification, rejection, or another non-executable state is required.

The shortest canonical formulation is:

Resolution is the point at which Noema stops guessing what the Actor might mean and establishes what it can safely treat as the Actor’s Intent.