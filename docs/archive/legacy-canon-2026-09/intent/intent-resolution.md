> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Intent Resolution

Status: Foundational
Version: 0.1
Domain: Intent
Canonical Path: intent/intent-resolution.md

⸻

1. Definition

Intent Resolution is the governed process by which Noema transforms an admitted candidate Intent into a sufficiently complete, grounded, and semantically determined Intent that can become Executable Intent and be evaluated by Trust.

Resolution answers:

“Do we know what the Actor means well enough to proceed to deterministic evaluation?”

It does not answer:

“May Noema execute it?”

That is the responsibility of Trust, using applicable authority, policy, current state, constraints, capabilities, contracts, and other governance conditions.

⸻

2. Why Resolution Exists

A Model can produce a plausible interpretation without that interpretation being sufficiently established for consequential execution.

For example:

"Cancel my subscription."

If the Actor has:

Subscription#123
Subscription#456

a Model may select one.

Noema must not treat plausibility as semantic resolution.

Instead:

Source of Intent
       ↓
Candidate Semantic Representation
       ↓
Hard Schema Validation / Admission
       ↓
Canonical Intent
       ↓
Resolution
       ↓
Material Ambiguity?
   ┌───┴───┐
  Yes      No
   ↓        ↓
Clarify   Resolved
            ↓
       Executable Intent
            ↓
          Trust

Resolution is therefore a primary deterministic commitment boundary in Noema.

⸻

3. Resolution vs Interpretation

These are distinct activities.

Interpretation

Determines:

What might the Actor mean?

Resolution

Determines:

Which meaning is sufficiently established to become the canonical semantic interpretation of the Intent?

For example:

Expression:
"Renew the card I used yesterday."

Interpretation may produce:

Objective:
RenewCard
Candidate Resources:
Card#123
Card#456

Resolution determines whether available Context, evidence, relationships, and authoritative state establish one of those Resources.

The Model may generate candidates.

Noema determines whether semantic commitment is justified.

⸻

4. Resolution vs Hard Validation and Admission

Resolution occurs after the candidate semantic representation has passed the hard schema validation and admission boundary.

These concerns must remain distinct:

Hard Validation / Admission
    =
Is this candidate structurally valid and admissible?
Resolution
    =
What does this admitted Intent mean, given available evidence?

A malformed or schema-invalid candidate should not enter canonical Intent semantics merely because its meaning appears understandable.

The architectural sequence is:

Expression
   ↓
Candidate Representation
   ↓
Hard Schema Validation
   ↓
Admission
   ↓
Canonical Intent
   ↓
Resolution

⸻

5. Resolution vs Clarification

Clarification is one mechanism used when resolution cannot otherwise establish material meaning.

Therefore:

Resolution
    ↓
Can meaning be established?
    ├── Yes → Resolved
    └── No
         ↓
     Clarification

Clarification is part of the Intent-resolution process.

It does not replace resolution.

A clarification response must itself be validated and resolved before it can change the canonical semantic interpretation.

A material clarification normally creates a new Intent version with an explicit supersedes relationship.

⸻

6. Resolution vs Confidence

Confidence expresses the strength of support for a candidate interpretation.

Resolution determines whether the evidence is sufficient to establish that interpretation as canonical.

These are not equivalent.

Example:

Candidate:
Card#123
Model confidence:
0.97
Competing candidate:
Card#456

If both remain materially valid:

Resolution:
Material ambiguity

despite high Model confidence.

Conversely, a candidate with modest Model confidence may become resolved if authoritative evidence deterministically establishes the intended Resource.

Confidence therefore supports resolution but does not perform semantic commitment.

⸻

7. Resolution vs Trust

Resolution asks:

What does the Actor mean?

Trust asks:

May the resolved Intent proceed under current governance conditions?

The canonical relationship is:

Interpretation
      ↓
Hard Validation / Admission
      ↓
Resolution
      ↓
Executable Intent
      ↓
Trust
      ↓
Action
      ↓
Execution

Trust must not compensate for unresolved material semantic ambiguity.

Likewise, resolution must not rewrite an Actor’s Intent merely to make Trust or execution succeed.

⸻

8. Resolution Inputs

Intent Resolution may consume:

* admitted Intent
* Actor identity
* Source of Intent
* conversation Context
* Intent Context
* domain Context
* Entities
* Resources
* relationships
* Parameters
* Scope
* Constraints
* Preferences
* authoritative enterprise state
* State Reconciliation results
* external evidence
* prior admitted Intent versions
* Actor clarification
* deterministic domain rules

The exact inputs depend on the Intent type and the semantic question being resolved.

Not every source has equal authority.

⸻

9. Resolution Outputs

Resolution should make the semantic result explicit.

Conceptually, results may include:

RESOLVED
AMBIGUOUS
INCOMPLETE
INVALID
CONTRADICTORY
UNVERIFIABLE

These describe semantic resolution conditions.

UNSUPPORTED is different: the Intent may be semantically clear while no applicable Capability exists. That is an executability or capability condition, not necessarily a resolution condition.

The exact lifecycle encoding is governed by intent-lifecycle.md.

⸻

10. Resolution Is Evidence-Based

Noema should resolve Intent components using evidence rather than intuition.

Evidence may include:

* explicit Actor statements
* prior Actor statements
* conversation Context
* validated Intent Context
* canonical ontology
* authoritative enterprise records
* State Reconciliation
* Resource relationships
* deterministic domain rules
* explicit references
* previous Intent versions
* Actor clarification

Evidence must be evaluated for:

* authority
* scope
* freshness
* relevance
* consistency
* Fact Status

Retrieval alone does not make evidence authoritative.

⸻

11. Evidence Hierarchy

A useful conceptual hierarchy is:

1. Explicit current Actor statement
2. Explicit prior Actor statement
3. Authoritative domain state
4. Validated and applicable Context
5. Deterministic domain relationship
6. Derived semantic inference
7. Model inference

This is not an absolute ordering for every domain.

Different semantic claims may have different authoritative sources.

When evidence conflicts, Noema must not silently select the most convenient interpretation.

The resolution rule must be explicit or the conflict must remain unresolved.

⸻

12. Explicit Actor Intent Has Primacy

Where the Actor explicitly specifies a material value, Noema should not replace it with an inferred value merely because another value appears more typical.

Example:

"Send the invoice to Sarah."

If the system normally sends invoices to the account owner, that default does not replace the explicit recipient.

If policy or domain state prevents the requested action, the Intent remains:

SendInvoice → Sarah

and the governance or execution layer determines whether it may proceed.

Resolution should preserve meaning rather than optimize it away.

⸻

13. Current Context Has Temporal Relevance

Later explicit Actor statements may supersede earlier semantic commitments.

Example:

"Book the flight for Friday."
Later:
"Actually, Saturday."

The later statement establishes a new semantic value:

Date:
Saturday

If the change is material, the new meaning should be represented as a new Intent version rather than silently mutating the historical version.

Resolution therefore considers temporal provenance and explicit correction.

⸻

14. Authoritative State

When an Intent references external Resources, Noema should resolve against authoritative domain state where the relevant state is material.

Example:

"Cancel my active subscription."

The enterprise subscription system may establish:

Subscription#123 → ACTIVE
Subscription#456 → CANCELLED

The Resource may therefore resolve to:

Subscription#123

The enterprise system remains authoritative for the actual subscription state.

Noema may use that state to resolve meaning without becoming the owner of the Business State.

⸻

15. State Reconciliation

Resolution may require State Reconciliation across multiple enterprise systems.

For example:

"Renew the card I used yesterday."

may require:

Transaction System
        ↓
Transaction#789
        ↓
Card Record
        ↓
Card#123

If multiple systems contain relevant observations, Noema may reconcile them before determining the semantic Resource.

State Reconciliation is a first-class platform capability.

It is not merely an integration detail.

Reconciliation may resolve an Intent, reveal ambiguity, expose stale information, or produce conflict.

⸻

16. Grounding

Resolution often requires grounding linguistic references in canonical Resources or Entities.

Example:

"Renew the card I used yesterday."

may become:

Transaction History
      ↓
Transaction#789
      ↓
Card#123

Result:

RenewCard(Card#123)

Grounding establishes a canonical reference.

Grounding does not necessarily establish uniqueness.

A reference may be grounded to multiple candidates and remain materially ambiguous.

⸻

17. Entity Resolution

Entity Resolution determines which canonical Entity a reference denotes.

Example:

"Send it to Sarah."

Possible Entities:

Sarah#123
Sarah#456
Sarah#789

If validated Context or authoritative records establish:

Sarah = Sarah#123

the Entity may be resolved.

Otherwise:

Entity:
AMBIGUOUS

Noema must not select an Entity merely because one candidate has a higher model score.

⸻

18. Resource Resolution

Resource Resolution identifies the domain object materially affected by the Intent.

Example:

"Delete the project."

Possible Resources:

Project#1
Project#2
Project#3

If valid Context and authoritative state establish one intended project:

Project#1

may be resolved.

If multiple materially valid candidates remain:

Resource:
AMBIGUOUS

and clarification may be required.

⸻

19. Reference Resolution

Natural language frequently uses references such as:

it
that
them
the previous one
my account
the card
the other project

Noema should resolve these against applicable Context and canonical relationships.

Example:

User:
Create a project called Noema.
User:
Add Sarah to it.

The reference:

"it"

may resolve to:

Project#Noema

Only the Context relevant to the current Intent should be propagated.

⸻

20. Scope Resolution

Resolution must establish the intended scope where scope materially affects meaning.

Example:

"Delete the inactive projects."

Possible interpretations include:

one project
all inactive projects
all projects

A resolved representation may be:

Scope:
Collection
Filter:
State = INACTIVE

Scope ambiguity is potentially execution-critical.

Noema must not broaden scope merely because a broader operation is technically available.

⸻

21. Quantifier Resolution

Terms such as:

all
any
every
one
the
a
each
none

may materially change an Intent.

Example:

"Notify all administrators."

is not equivalent to:

NotifyAdministrator(single)

Quantification must therefore be preserved in the Intent Model.

Where quantifier semantics are material, they must be resolved before the Intent becomes Executable.

⸻

22. Temporal Resolution

Relative temporal expressions require appropriate temporal Context.

Examples include:

today
tomorrow
next Friday
yesterday
in two hours
later
before lunch

Resolution should normalize these against the relevant:

* current date
* timezone
* locale where material
* temporal Context
* domain calendar semantics

Example:

"next Friday"

may become a concrete temporal value once the applicable date and timezone are established.

Temporal normalization must not silently change the Actor’s intended time semantics.

⸻

23. Spatial Resolution

Spatial references may also require Context or authoritative location data.

Examples include:

near me
at the office
in London
the Lagos branch
the warehouse

Resolution should establish canonical geographic or logical locations where those locations materially affect the Intent.

Location inference remains subject to evidence, scope, and authority requirements.

⸻

24. Constraint Resolution

Constraints may themselves require semantic resolution.

Example:

"Book something cheap."

Possible interpretations include:

Price < 500
lowest available price
below Actor's historical average

If the relevant domain defines “cheap” deterministically, that definition may establish the constraint.

If no valid definition exists and the threshold is material, Noema should not invent one merely because it appears reasonable.

The unresolved semantic dimension may require clarification.

⸻

25. Preference Resolution

Preferences may also require semantic normalization.

Example:

"I'd rather leave in the afternoon."

may resolve to:

Preference:
DepartureTime ∈ Afternoon

It should not become:

Constraint:
DepartureTime >= 12:00

unless the Actor explicitly establishes a hard requirement or the Intent type defines that semantic equivalence.

Preference semantics must remain distinct from constraint semantics.

⸻

26. Resolution of Defaults

Defaults may resolve non-material omissions when they are:

* explicitly defined
* deterministic
* domain-valid
* within scope
* policy-compatible
* non-material

Example:

Project visibility:
Private

may be valid if Private is the explicit system default for the relevant Intent type.

Defaults must not:

* hide material uncertainty
* choose between materially ambiguous alternatives
* expand scope
* invent material intent
* manufacture authority
* override explicit constraints

⸻

27. Materiality

Not every unresolved value requires clarification.

Resolution should ask:

Would choosing between the possible values materially change the Intent, its execution, its risk, or its Expected Outcome?

Example:

Email format:
HTML vs plain text

may be non-material.

But:

Bank account:
Savings vs Emergency

is material.

Material ambiguity must prevent the Intent from becoming Executable until it is resolved or otherwise eliminated by valid evidence.

⸻

28. Deterministic Resolution

Where valid deterministic evidence exists, Noema should prefer deterministic resolution.

Example:

Actor:
User#123
Only active subscription:
Subscription#456
Request:
"Cancel my active subscription."

Resolution:

Resource:
Subscription#456

No clarification is necessary if the evidence uniquely establishes the intended Resource.

Deterministic resolution must be based on defined semantic and domain rules rather than hidden model preference.

⸻

29. Non-Deterministic Resolution

Where multiple materially valid interpretations remain, Noema must not force resolution.

Example:

Actor owns:
Card#123
Card#456
Request:
"Renew my card."

If both cards remain materially valid:

Resolution:
AMBIGUOUS

The appropriate next step may be targeted clarification.

⸻

30. No Guessing Across Material Ambiguity

This is a core Noema invariant.

If materially different interpretations remain plausible and cannot be deterministically distinguished:

AMBIGUOUS
      ↓
CLARIFICATION_REQUIRED

Noema must not select one merely because it has the highest probability or model confidence.

The purpose of the resolution boundary is to prevent probabilistic preference from becoming an ungoverned semantic commitment.

⸻

31. Resolution of Composite Intents

Constituent Intents must be resolved according to the semantics of the composition.

Example:

"Refund the payment and close the account."

may produce:

RefundPayment
    → Resolved
CloseAccount
    → Resolved

If:

RefundPayment
    → Resolved
CloseAccount
    → Ambiguous

the Composite Intent is not fully resolved.

An independent child may still resolve or potentially proceed where the composition semantics explicitly permit independent progress.

Composition does not bypass the semantic requirements of its constituents.

⸻

32. Dependency-Aware Resolution

Some Intent components depend on others.

Example:

"Transfer the balance to my other account."

The phrase:

"other account"

cannot be resolved until the relevant source account is established.

Resolution may therefore proceed:

Resolve source
      ↓
Identify eligible other accounts
      ↓
Resolve destination

Resolution is consequently dependency-aware rather than necessarily field-order based.

⸻

33. Resolution Order

There is no universal mandatory resolution order.

A useful conceptual pattern is:

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
Parameters
  ↓
Scope
  ↓
Constraints
  ↓
Preferences
  ↓
Relationships
  ↓
Expected Outcome

Actual ordering may vary when dependencies require it.

For example, resolving one Resource may be necessary before resolving a dependent reference or constraint.

⸻

34. Resolution and Context Propagation

Context should propagate only where semantically valid.

Example:

User:
Create project Noema.
User:
Add Sarah to it.

The project reference can propagate.

Unrelated Context should not automatically propagate into the new Intent.

Noema should avoid broad, implicit Context inheritance because stale or irrelevant Context can create false semantic commitments.

⸻

35. Context Boundaries

Useful Context boundaries include:

Conversation Context
Session Context
Intent Context
Domain Context
Execution Context

Resolution should determine which Context layer is relevant and authoritative for each semantic claim.

An old conversational statement must not override current authoritative domain state merely because it appears earlier in the conversation.

Likewise, execution Context should not retroactively redefine the Actor’s original Intent.

⸻

36. Conflict Resolution

Evidence may conflict.

Example:

Actor:
"Send it to Sarah."
CRM:
Sarah's account is inactive.
Policy:
Inactive accounts cannot receive invoices.

The semantic Intent may remain:

SendInvoice → Sarah

Resolution should not change the recipient merely because execution may be prohibited.

Trust evaluates whether the resolved Intent may proceed under applicable governance conditions.

The distinction is:

Resolution
    =
What does the Actor mean?
Trust
    =
May the resolved path proceed?

⸻

37. Resolution Must Not Optimize Away Intent

Suppose the Actor says:

"Transfer $5,000 to savings."

Noema discovers that the amount exceeds a current transfer limit.

Resolution must remain:

TransferFunds
Amount:
$5,000

It must not silently transform the Intent into:

TransferFunds
Amount:
$2,000

The latter is a different Intent.

Policy and execution constraints may prevent or condition execution, but they must not silently rewrite Actor intent.

⸻

38. Resolution and Capability Availability

Capability availability can affect executability but is not itself semantic resolution.

Example:

Intent:
TeleportPerson
Destination:
London

The meaning is clear.

If Noema has no applicable Capability:

Resolution:
RESOLVED
Executability:
UNSUPPORTED

The exact execution/trust representation is governed by the relevant execution and Trust specifications.

The important distinction is:

Semantic clarity
    ≠
Capability availability

⸻

39. Resolution and Business State

Business State may provide evidence for resolution.

Example:

"Cancel my active subscription."

The subscription system provides:

Subscription#123 = ACTIVE
Subscription#456 = CANCELLED

This evidence may resolve the Resource.

The enterprise system remains the source of truth for the actual subscription state.

Noema does not acquire ownership of Business State through resolution.

⸻

40. Resolution and Intent State

Resolution establishes semantic completeness and may therefore drive lifecycle transitions.

Conceptually:

Material ambiguity
       ↓
Actor clarification
       ↓
New Intent version
       ↓
Resolution
       ↓
EXECUTABLE

The lifecycle state itself is governed by intent-lifecycle.md.

Resolution should not introduce a second independent lifecycle model.

⸻

41. Resolution Evidence Record

A material resolution decision should record, where practical:

* candidate value
* selected value
* rejected alternatives
* evidence references
* evidence source
* resolution rule
* relevant timestamps
* relevant ontology or domain-rule version

Example:

Resource:
Card#123
Evidence:
Transaction#789
Rule:
"card I used yesterday" resolves to the card
associated with the most recent qualifying transaction.
Rejected:
Card#456

The purpose is causal traceability and reproducibility.

⸻

42. Resolution Provenance

Resolution provenance answers:

Why was this semantic value selected?

Example:

"the card I used yesterday"
        ↓
Transaction#789
        ↓
Card#123

This causal chain should remain available where material to the semantic decision.

Provenance explains the basis of a resolution.

It does not itself establish that the underlying evidence is authoritative.

⸻

43. Resolution and Auditability

Material resolution decisions should be reproducible from their relevant inputs.

Given the same:

Intent Version
Context
Ontology Version
Authoritative State
Evidence
Resolution Rules

Noema should reach the same resolution result, assuming the referenced state and evidence are themselves unchanged.

Resolution therefore forms part of Noema’s deterministic semantic boundary.

⸻

44. Resolution and Model Role

The Model may propose:

candidate Intent
candidate Entity
candidate Resource
candidate Constraint
candidate reference
candidate interpretation

Noema determines whether that proposal is sufficiently established.

Conceptually:

Model
  ↓
Hypothesis
  ↓
Noema Resolution
  ↓
Canonical Semantic Commitment

The Model generates possibilities.

Noema governs semantic commitment.

⸻

45. Resolution as a Commitment Boundary

Before resolution:

Candidate meaning

After successful resolution:

Established canonical meaning

The architectural boundary is:

PROBABILISTIC
      │
      ▼
Candidate Semantic Representation
      │
      ▼
Hard Validation / Admission
      │
      ▼
Canonical Intent
      │
      ▼
    RESOLUTION
      │
      ▼
DETERMINISTIC
      │
      ▼
Resolved Intent
      │
      ▼
Executable Intent

This boundary prevents probabilistic interpretation from directly becoming consequential execution.

⸻

46. Resolution and Trust

Trust consumes the resolved Intent rather than raw Model output.

Bad architecture:

Model
  ↓
Action

Better:

Model
  ↓
Candidate Intent
  ↓
Hard Validation / Admission
  ↓
Resolution
  ↓
Executable Intent
  ↓
Trust
  ↓
Action

Trust does not resolve semantic ambiguity on behalf of the resolution layer.

Likewise, resolution does not make the Trust decision.

The four canonical Trust outcomes are:

EXECUTE
CLARIFY
ESCALATE
REJECT

A CLARIFY Trust outcome may indicate that a material semantic issue must be resolved before safe continuation, but clarification remains an Intent-resolution mechanism.

⸻

47. Resolution Failure Classes

Noema should distinguish at least:

Ambiguous

Multiple materially valid interpretations remain.

Incomplete

Required semantic information is absent.

Invalid

The candidate violates a semantic validity rule.

Contradictory

Supplied information contains incompatible semantic claims.

Unverifiable

A material claim cannot be established with sufficient evidence.

Unsupported

The meaning is sufficiently established but no applicable Capability or execution path exists.

These conditions should not collapse into a generic FAILED.

Their consequences belong to the relevant lifecycle, Trust, execution, or clarification semantics.

⸻

48. Ambiguous vs Incomplete

These are related but distinct.

Ambiguous

"Cancel my subscription."

Two subscriptions exist.

Multiple plausible values are present.

Incomplete

"Transfer money."

No amount or destination has been supplied.

Required information is absent.

The clarification required is therefore different.

Ambiguity asks:

Which valid interpretation?

Incompleteness asks:

What required information is missing?

⸻

49. Invalid vs Contradictory

Invalid

A value violates a semantic rule.

Example:

Amount:
"banana"

Contradictory

Two otherwise meaningful claims conflict.

Example:

Departure:
Friday
Constraint:
Departure must be Saturday

Noema should determine whether the contradiction can be resolved through:

* explicit recency
* explicit Actor correction
* authoritative state
* deterministic domain rules

If it cannot, the contradiction remains unresolved and may require clarification or another non-executable disposition.

⸻

50. Resolution and Clarification Generation

When clarification is required, the question should target the smallest unresolved semantic unit.

Bad:

"Can you clarify your request?"

Better:

"Which subscription do you want to cancel: Premium or Business?"

A resolved Intent structure allows Noema to identify exactly which semantic field remains unresolved.

Clarification should not unnecessarily reopen already resolved portions of the Intent.

⸻

51. Minimal Clarification Principle

Ask only for information necessary to:

* resolve material ambiguity
* establish required semantic information
* resolve a material contradiction
* satisfy the requirements of the relevant Intent type

Noema should not ask:

"What exactly do you want?"

when it already knows:

Actor
Objective
Resource candidates
Context
Constraints

and only needs:

Which Resource?

Clarification should be as narrow as the unresolved semantic dimension permits.

⸻

52. Resolution Should Preserve Established Meaning

Resolution should preserve established semantic commitments rather than repeatedly reinterpreting them.

Example:

Initial:
RenewCard
After grounding:
RenewCard(Card#123)
After clarification:
RenewCard(Card#123, expedited=true)

New evidence should extend or replace a semantic value only where the evidence justifies that change.

Previously established information should not be casually discarded.

Where a material change occurs, the resulting Intent should be represented as a new version.

⸻

53. Resolution and Actor Corrections

The Actor may explicitly correct a previous interpretation.

Example:

Noema:
"Do you mean your personal account?"
Actor:
"No, the business account."

The new explicit statement supersedes the previous candidate interpretation.

Resolution becomes:

Account:
BusinessAccount

The correction should be recorded through provenance and, where materially changing the admitted Intent, represented as a new Intent version.

⸻

54. Resolution and External Changes

The world can change while an Intent is being resolved.

Example:

09:00:
Card#123 = ACTIVE
09:05:
Card#123 = CANCELLED

Noema must distinguish:

semantic resolution

from:

current domain state

A Resource can be correctly resolved and subsequently become unavailable.

That does not necessarily invalidate the semantic resolution.

Current state must be re-evaluated where required before Trust and execution.

⸻

55. Resolution and Staleness

Evidence can become stale.

For example:

Yesterday's account state

may be insufficient to establish:

Current authorization

or:

Current account eligibility

where freshness is material.

Noema should therefore evaluate evidence freshness and Fact Status according to the relevant claim and domain.

A previously verified fact may no longer be sufficient for a current decision.

⸻

56. Resolution and Unknown

Unknown is a first-class epistemic condition.

Noema should distinguish:

UNKNOWN

from:

AMBIGUOUS

UNKNOWN means the relevant fact or value has not been established.

AMBIGUOUS means multiple materially valid interpretations remain.

Examples:

Destination:
UNKNOWN

versus:

Destination:
AMBIGUOUS
├── Account#1
└── Account#2

Unknown must not be converted into a guessed value merely to complete the structure.

⸻

57. Resolution and Conflicting Evidence

Conflicting evidence should remain explicit when no valid deterministic rule resolves the conflict.

For example:

Source A:
Account#123 = ACTIVE
Source B:
Account#123 = CLOSED

Noema should not treat the existence of two retrieved records as proof that either one is authoritative.

The relevant State Reconciliation and authority rules must determine whether the conflict can be resolved.

If it cannot, the material claim may remain:

CONFLICTED

and the Intent may remain non-executable.

⸻

58. Resolution and Deterministic Reproducibility

A resolution decision should be reproducible from its material inputs.

Conceptually:

Intent Version
+
Evidence
+
Validated Context
+
Authoritative State
+
Resolution Rules
+
Ontology Version

should produce a deterministic resolution result.

Any probabilistic component may generate candidates.

The final semantic commitment must not depend on uncontrolled model choice.

⸻

59. Resolution Invariants

Invariant 1

No materially ambiguous Intent may become resolved through confidence alone.

Invariant 2

No material assumption may be silently introduced during resolution.

Invariant 3

Explicit Actor corrections supersede prior inferred interpretations where the correction is valid and applicable.

Invariant 4

Authoritative domain evidence may ground Resources and Entities.

Invariant 5

Resolution must not rewrite Actor intent to satisfy Policy, Capability availability, or execution convenience.

Invariant 6

Material semantic resolution must precede Executable Intent.

Invariant 7

Every material resolution should have explainable provenance.

Invariant 8

The absence of a Capability does not by itself imply semantic ambiguity.

Invariant 9

Business State and Intent State remain separate.

Invariant 10

Evidence, Fact Status, and Confidence remain distinct.

Invariant 11

Unknown and Ambiguous must remain distinguishable.

Invariant 12

Material semantic changes must create a new Intent version rather than silently mutate historical meaning.

Invariant 13

If resolution cannot establish material meaning, Noema must not produce an Executable Intent from unsupported inference.

⸻

60. Canonical Resolution Flow

                    Source of Intent
                           │
                           ▼
               Candidate Semantic Meaning
                           │
                           ▼
              Hard Schema Validation /
                     Admission
                           │
                           ▼
                    Canonical Intent
                           │
                           ▼
               Context + State Reconciliation
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
       One materially valid       Multiple
       interpretation             material
       established                interpretations
                 │                   │
                 ▼                   ▼
             RESOLVED            AMBIGUOUS
                 │                   │
                 │                   ▼
                 │             CLARIFICATION
                 │                   │
                 │                   ▼
                 │              New Evidence /
                 │              New Intent Version
                 │                   │
                 └───────────┬───────┘
                             ▼
                    Resolved Intent
                             │
                             ▼
                    Executable Intent
                             │
                             ▼
                           TRUST

The flow may iterate where additional evidence or clarification is required.

⸻

61. Example: Card Renewal

Expression

"Renew the card I used yesterday."

Candidate Intent

Objective:
RenewCard
Resource:
Card used yesterday

Evidence

Transaction#789 → Card#123
Transaction#790 → Card#456

If only Transaction#789 satisfies the applicable temporal and semantic criteria:

Resource:
Card#123
Resolution:
RESOLVED

If both qualify:

Resolution:
AMBIGUOUS

Noema should ask a targeted clarification such as:

"Which card do you mean: the Visa ending in 1234 or the Mastercard ending in 5678?"

The clarification resolves the semantic reference.

It does not itself establish Trust or execution authority.

⸻

62. Example: Transfer

Expression

"Send $500 to my other account."

Candidate Intent

Objective:
TransferFunds
Amount:
$500
Source:
CurrentAccount
Destination:
OtherAccount

Evidence

Savings#1
Investment#2

If both accounts satisfy the reference:

Destination:
AMBIGUOUS

Clarification:

"Which account should receive the $500: Savings or Investment?"

After clarification, the resulting material semantic change is represented as a new Intent version.

Trust then evaluates the resolved Intent against current authority, policy, state, constraints, and applicable execution conditions.

⸻

63. Example: Clear but Unsupported

Expression

"Teleport me to London."

Candidate

Objective:
TeleportPerson
Destination:
London

If the meaning is established:

Resolution:
RESOLVED

If no applicable Capability exists:

Executability:
UNSUPPORTED

This illustrates why semantic resolution and Capability availability must remain separate.

The Intent can be semantically clear without being executable.

⸻

64. Example: Clear but Not Permitted

Expression

"Refund this $50,000 payment."

Resolution

RefundPayment(Payment#123)
Amount:
$50,000

The Intent may be fully resolved and executable in the semantic sense.

Suppose applicable governance conditions require manager approval.

The result is not a resolution failure.

Trust evaluates the resolved Intent and may return:

CLARIFY
ESCALATE
REJECT

as appropriate to the actual governance condition.

Resolution does not rewrite the amount or objective to avoid the requirement.

⸻

65. Resolution and Noema’s Thesis

Intent Resolution operationalizes one of Noema’s central principles:

The Model may be probabilistic; the commitment to executable meaning must be governed.

The Model can propose:

"I think this is what the Actor means."

Noema must determine:

"This interpretation is sufficiently established to become canonical."

Only then can the resolved semantic object become Executable Intent and enter the deterministic Trust boundary.

⸻

66. Final Definition

Intent Resolution is the governed process of grounding, completing, disambiguating, and reconciling a canonical Intent using explicit Actor input, validated Context, authoritative evidence, State Reconciliation, and deterministic semantic rules until Noema can either establish a sufficiently determined canonical meaning or explicitly determine that clarification or another non-executable disposition is required.

The shortest canonical formulation is:

Resolution is the point at which Noema stops treating an interpretation as a possibility and establishes what it can deterministically treat as the Actor’s Intent.