ADR-008 — Clarification Over Guessing

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational
Domain: Intent / Resolution / Safety
Canonical Path: decisions/ADRs/ADR-008-clarification-over-guessing.md

⸻

1. Context

Noema converts human expressions into canonical Intent representations that may ultimately become executable Actions.

Human expressions are frequently incomplete, ambiguous, underspecified, or dependent on context.

Examples include:

* “Send the report to John.”
* “Cancel the subscription.”
* “Use the usual account.”
* “Book it for tomorrow.”
* “Transfer the money to Alex.”
* “Renew my card.”

The expression may be understandable to a human conversational partner while remaining insufficiently precise for deterministic execution.

A probabilistic model can often infer a likely interpretation from context.

However, a likely interpretation is not necessarily the intended interpretation.

If Noema silently converts ambiguity into an assumed value, the resulting error can propagate through:

Intent
  ↓
Validation
  ↓
Trust
  ↓
Action
  ↓
Execution

The later stages may correctly operate on an incorrectly resolved Intent.

Therefore Noema requires an explicit rule governing unresolved semantic uncertainty.

⸻

2. Decision

When material ambiguity or missing information prevents Noema from establishing the intended Intent with sufficient semantic certainty, Noema must request clarification rather than guess.

Clarification is a legitimate lifecycle state, not an error condition.

The canonical flow is:

Human Expression
       ↓
Interpretation
       ↓
Resolution
       ↓
    ┌───────────────┐
    │ Sufficiently   │
    │ established?   │
    └───────┬───────┘
            │
       ┌────┴────┐
       │         │
      YES        NO
       │         │
       ▼         ▼
   Validation  Clarify
       │         │
       │         ▼
       │     New information
       │         │
       │         ▼
       │      Resolution
       │
       ▼
     Trust

Noema must not convert uncertainty into authority merely because one interpretation appears more probable.

⸻

3. Core Principle

The governing principle is:

When a material Intent parameter cannot be established reliably, Noema should ask rather than infer.

The distinction is:

Probable meaning
      ≠
Established meaning

and:

Model confidence
      ≠
Semantic authorization to choose

⸻

4. What Constitutes Material Ambiguity

Not every ambiguity requires clarification.

The relevant question is whether the unresolved ambiguity could materially affect what Noema understands, validates, trusts, or executes.

Material ambiguity may involve:

* Actor
* Action
* Target
* Resource
* Recipient
* Amount
* Currency
* Account
* Time
* Scope
* Destination
* Quantity
* Execution mode
* Required capability
* Relevant business entity
* Constraint
* Approval requirement

For example:

"Send ₦50,000 to John."

If there are three possible recipients named John, the recipient identity is material.

Noema must not select one merely because it appears statistically more likely.

⸻

5. Example — Ambiguous Recipient

User:

Send ₦50,000 to John.

Available entities:

John_1
John_2
John_3

The model may assign different probabilities:

John_1 = 0.65
John_2 = 0.25
John_3 = 0.10

Those probabilities do not establish:

recipient = John_1

The correct state is:

WAITING_FOR_CLARIFICATION

until the recipient is established through an appropriate source of information.

⸻

6. Example — Missing Amount

User:

Transfer the money to John.

If no deterministic context establishes the amount, the Intent remains incomplete.

Noema must not infer:

amount = last_transfer_amount

merely because that value appears plausible.

Instead:

amount = unresolved

and clarification may be required.

⸻

7. Example — Ambiguous Resource

User:

Cancel the subscription.

The Actor has:

Subscription A
Subscription B
Subscription C

If the available context does not deterministically establish which subscription is intended, Noema must not select one based solely on recency, probability, or convenience.

The appropriate state is:

WAITING_FOR_CLARIFICATION

⸻

8. Context May Resolve Ambiguity

Clarification is not required whenever natural language is incomplete.

Authoritative context may establish the intended value.

For example:

User:
"Cancel my subscription."

If the Actor has exactly one active subscription and the canonical semantics explicitly permit the active subscription to be referenced as “my subscription,” context may resolve the reference deterministically.

Then:

"my subscription"
       ↓
authoritative context
       ↓
subscription_123
       ↓
resolved Intent

The important distinction is:

Deterministic contextual resolution
        ≠
Probabilistic guessing

⸻

9. Defaults

Defaults may be used only when the Intent semantics explicitly permit them.

For example, if an Action contract defines:

currency defaults to the source account currency

and the source account is authoritative and unambiguous, applying that default is deterministic.

By contrast:

recipient defaults to most recent contact

should not be applied merely because it seems likely unless that behavior is explicitly part of the canonical Action semantics.

Defaults must therefore be:

* explicit
* deterministic
* documented
* applicable to the specific Action
* auditable

⸻

10. Clarification Is Not Rejection

Clarification means:

The Intent may be executable,
but Noema does not yet have enough information
to establish what the Actor intends.

This differs from rejection.

Clarification:
"I need more information."
Rejection / Blocking:
"I have sufficient information and the requested Action
cannot proceed under the applicable rules."

Therefore:

AMBIGUOUS
    ↓
WAITING_FOR_CLARIFICATION

rather than:

AMBIGUOUS
    ↓
BLOCKED

unless another independent condition makes the Intent prohibited.

⸻

11. Clarification Is Not Validation Failure

An incomplete Intent is not necessarily an invalid Intent.

For example:

Transfer to John

may have a missing recipient identity.

The canonical distinction is:

Resolution:
recipient unresolved
Validation:
Intent incomplete
Trust:
cannot become READY
State:
WAITING_FOR_CLARIFICATION

Noema should preserve the distinction between:

Incomplete

and:

Invalid

⸻

12. Clarification and Validation

Validation may identify missing information required for a valid canonical Intent.

For example:

Intent:
{
    action: TRANSFER,
    amount: 50000,
    destination: ?
}

Validation may return:

status: INCOMPLETE
requirement:
DESTINATION_REQUIRED

This can produce:

WAITING_FOR_CLARIFICATION

The clarification response supplies additional information.

The Intent is then re-resolved and revalidated.

⸻

13. Clarification and Trust

Trust must not convert unresolved information into READY.

Conceptually:

Intent unresolved
      ↓
Validation incomplete
      ↓
WAITING_FOR_CLARIFICATION
      ↓
Clarification received
      ↓
Intent updated
      ↓
Validation
      ↓
Trust Evaluation

The Trust Engine therefore receives an Intent whose relevant semantics have been established rather than one containing unresolved material ambiguity.

⸻

14. Clarification and the Trust State Machine

The canonical relationship is:

UNRESOLVED
     ↓
clarification requested
     ↓
WAITING_FOR_CLARIFICATION
     ↓
clarification received
     ↓
EVALUATING

If the clarification does not actually resolve the material ambiguity:

WAITING_FOR_CLARIFICATION
        ↓
insufficient clarification
        ↓
EVALUATING
        ↓
WAITING_FOR_CLARIFICATION

The State Machine must not transition to READY until all mandatory conditions have been established.

⸻

15. Clarification Must Be Targeted

A clarification request should identify the unresolved semantic requirement.

Instead of:

"Can you clarify?"

Noema should preferably ask a question that resolves the specific ambiguity.

For example:

"I found three contacts named John. Which one should receive the ₦50,000 transfer?"

The purpose is to obtain the missing semantic information necessary for deterministic resolution.

⸻

16. Clarification Should Not Introduce New Ambiguity

A clarification request should itself avoid introducing assumptions.

For example, if multiple accounts could be relevant, Noema should not ask:

"Should I use your normal account?"

unless “normal account” has an explicit canonical meaning.

Instead:

"Which account should the transfer come from?"

or present the deterministically identified eligible accounts.

⸻

17. Clarification and Actor Agency

Clarification preserves the Actor’s authority over unresolved Intent.

Instead of Noema silently choosing:

John_1

the Actor explicitly establishes:

John_2

This preserves the distinction between:

What Noema predicts the Actor means

and:

What the Actor has established they mean

⸻

18. Clarification Through Authoritative Context

Clarification does not always require a conversational question.

An unresolved reference may be established through an authoritative external fact.

For example:

User:
"Renew my card."
Context:
exactly one eligible card
        ↓
Deterministic resolution
        ↓
card = card_123

No conversational clarification is required because the ambiguity has been resolved by applicable authoritative context.

The governing principle remains:

Noema must establish the intended meaning; it must not merely select the most probable meaning.

⸻

19. Clarification and Historical Context

Previous interactions may provide useful contextual information.

However, historical behavior must not automatically become present Intent.

For example:

Previous transfer:
₦50,000 to John

does not establish that:

"Transfer to John"

means:

₦50,000

unless the canonical semantics explicitly define that contextual reference.

History is evidence.

It is not unrestricted permission to infer.

⸻

20. Clarification and Defaults Must Remain Separate

A deterministic default is an explicit semantic rule.

Clarification is required when no applicable rule establishes the missing value.

Therefore:

Explicit default
      ↓
deterministic resolution

whereas:

No applicable rule
      ↓
material ambiguity
      ↓
clarification

The model must not invent defaults.

⸻

21. Clarification and Model Confidence

A model may be highly confident in an interpretation.

That confidence may help identify what clarification to request, but it does not itself establish the answer.

For example:

Model:
John_1 = 97% likely

does not mean:

recipient = John_1

The system may instead ask:

"Do you mean John Smith or John Adeyemi?"

Model confidence may assist the resolution process.

It does not replace resolution.

⸻

22. Clarification Thresholds

Noema should distinguish between:

Non-material ambiguity

An ambiguity that cannot materially change the resulting Action or its safety conditions.

This may be resolved through canonical defaults or normalization where explicitly permitted.

Material ambiguity

An ambiguity that could change:

* the Action
* the target
* the resource
* the amount
* the recipient
* the authority
* the constraints
* the execution semantics
* the resulting business state

Material ambiguity must not be silently guessed.

⸻

23. Noema Must Not Guess Authority

The clarification principle applies particularly strongly to authorization-sensitive references.

For example:

"Use the company account."

If multiple eligible company accounts exist, Noema must not choose one based solely on:

* recent use
* frequency
* model probability
* account name similarity
* convenience

The account must be established through explicit semantics or clarification.

⸻

24. Noema Must Not Guess Business State

Similarly, Noema must not infer current business state where an authoritative source is required.

For example:

"Cancel the active subscription."

If current subscription state cannot be established because the authoritative system is unavailable, Noema should not assume that the most recently observed subscription remains active.

The relevant condition may become:

UNKNOWN

and prevent READY.

⸻

25. Clarification vs Unknown

These states should remain conceptually distinct.

Clarification

The required information can reasonably be obtained from the Actor or another deterministic resolution mechanism.

"Which John?"

Unknown

The system cannot currently establish the required fact because authoritative information is unavailable.

"Is John_123 an active customer?"
        ↓
Customer system unavailable
        ↓
UNKNOWN

Unknown should not be converted into a guess.

⸻

26. Clarification vs Blocked

Similarly:

Ambiguous
    ↓
WAITING_FOR_CLARIFICATION

whereas:

Policy prohibits Action
    ↓
BLOCKED

Clarification means the Action may become executable after the missing meaning is established.

Blocking means a known condition currently prohibits execution.

⸻

27. Clarification Lifecycle

The canonical lifecycle is:

UNRESOLVED
     ↓
Identify ambiguity
     ↓
Generate clarification requirement
     ↓
WAITING_FOR_CLARIFICATION
     ↓
Actor responds
     ↓
Update Intent
     ↓
Re-resolve
     ↓
Validate
     ↓
Trust Evaluation

The clarification itself should be represented as a lifecycle event and, where applicable, provenance.

⸻

28. Clarification Must Produce New Intent Information

A clarification response is not merely conversational text.

It must contribute structured semantic information.

For example:

User:
"John Smith."
        ↓
Intent update:
recipient = customer_123

The resulting canonical Intent should be revalidated.

⸻

29. Clarification Must Not Silently Rewrite Intent

If the Actor provides information inconsistent with the prior Intent, Noema should not silently preserve the old interpretation.

Example:

Initial:

Transfer ₦50,000 to John.

Clarification:

"I meant ₦500,000."

The Intent has materially changed.

The updated Intent must undergo the applicable validation and Trust evaluation again.

⸻

30. Material Intent Changes Require Re-Evaluation

A clarification can change:

* Action
* target
* amount
* resource
* recipient
* constraints
* execution parameters

Therefore:

Clarification
     ↓
Intent version changes
     ↓
Revalidation
     ↓
Trust re-evaluation

Previous Trust must not automatically carry forward across a materially changed Intent.

⸻

31. Clarification History

Noema should retain sufficient provenance to reconstruct:

Initial expression
      ↓
Ambiguity identified
      ↓
Clarification requested
      ↓
Actor response
      ↓
Intent updated
      ↓
Validation
      ↓
Trust evaluation

This provides an auditable account of how the canonical Intent was established.

⸻

32. Clarification Events

Illustrative events include:

clarification.required
clarification.requested
clarification.received
clarification.resolved
clarification.insufficient
clarification.expired

The exact event vocabulary may evolve with the protocol.

⸻

33. Clarification Expiration

A clarification request may become stale.

For example:

WAITING_FOR_CLARIFICATION
        ↓
relevant context changes
        ↓
existing clarification no longer sufficient

The Intent should be re-evaluated before execution.

Clarification is not a permanent authorization artifact.

⸻

34. Repeated Clarification

Noema should avoid asking the same question repeatedly when the required information has already been established.

The system should retain the relevant clarification result as part of the Intent’s provenance and state.

However, if the underlying context materially changes, the requirement may need to be reconsidered.

⸻

35. Clarification and Composite Intents

Composite Intents may contain both resolved and unresolved components.

Example:

A = READY
B = WAITING_FOR_CLARIFICATION
C = READY

If execution is atomic:

Composite = WAITING_FOR_CLARIFICATION

Noema must not execute B based on an assumption merely because A and C are ready.

If partial execution is explicitly permitted by the Intent semantics, components may progress independently.

Noema must not infer permission for partial execution.

⸻

36. Clarification and High-Impact Actions

The greater the potential consequence of choosing the wrong interpretation, the less acceptable silent guessing becomes.

Examples may include:

* financial transfers
* deletion
* account closure
* access changes
* privileged operations
* sensitive-data disclosure
* irreversible Actions

The relevant rule remains semantic rather than merely numerical:

If an unresolved interpretation can materially alter the Action or its consequences, it must be established before execution.

⸻

37. Clarification and Low-Impact Actions

Not every uncertainty requires an explicit conversational interruption.

For non-consequential operations, canonical normalization or deterministic defaults may resolve harmless variations.

For example:

"Show me my transactions from last month."

If “last month” has an explicit temporal interpretation under the current date context, Noema may resolve it deterministically.

The principle is not:

Never infer anything.

It is:

Never silently guess a material semantic value.

⸻

38. Architectural Implication

Intent resolution should expose unresolved requirements explicitly.

Conceptually:

Intent {
    action
    actor
    target
    parameters
    constraints
    unresolved_requirements
    provenance
    state
}

This allows downstream systems to distinguish:

resolved Intent

from:

candidate Intent with unresolved semantics

The Trust Engine should not need to infer this distinction from model behavior.

⸻

39. Relationship to the AI Layer

AI models may:

* identify candidate interpretations
* detect ambiguity
* propose clarification questions
* extract possible entities
* rank possible interpretations
* normalize Actor responses

But deterministic Noema components establish the canonical Intent.

The architecture is:

Natural Language
       ↓
AI Interpretation
       ↓
Candidate Intent
       ↓
Deterministic Resolution
       ↓
Clarification if required
       ↓
Canonical Intent
       ↓
Validation
       ↓
Trust

AI assists resolution.

It does not obtain authority merely by producing a confident interpretation.

⸻

40. Consequences

Positive consequences

This decision:

* prevents silent semantic errors
* protects Actor agency
* makes ambiguity explicit
* prevents probabilistic guesses from becoming executable parameters
* improves auditability
* creates a clean boundary between interpretation and authority
* supports deterministic Trust evaluation
* makes Intent lifecycle state observable
* reduces the risk of executing against the wrong resource or recipient

Negative consequences

This decision can:

* introduce additional conversational turns
* increase latency
* require more explicit Intent state
* require clarification-management infrastructure
* reduce apparent automation in ambiguous cases
* require careful design of deterministic defaults and contextual resolution

These consequences are accepted as necessary for reliable intent execution.

⸻

41. Alternatives Considered

Alternative A — Always choose the most probable interpretation

Rejected.

Probability does not establish Actor intent.

A high-probability interpretation can still be materially wrong.

⸻

Alternative B — Use model confidence thresholds

Rejected as the authority mechanism.

A threshold such as:

confidence > 0.90
    ↓
execute

does not establish that the selected interpretation is correct.

Model confidence may support reasoning but cannot replace semantic establishment.

⸻

Alternative C — Ask for clarification for every ambiguity

Rejected.

Not every ambiguity is material.

Explicit defaults, normalization rules, and authoritative context can resolve non-material ambiguity deterministically.

⸻

Alternative D — Let the execution consumer resolve ambiguity

Rejected as the default architecture.

The Intent should be sufficiently established before crossing the execution boundary.

Consumers may perform final validation, but Noema should not intentionally send materially ambiguous Actions to consumers and expect them to infer the Actor’s meaning.

⸻

42. Relationship to Canonical Principles

This ADR establishes the formal decision behind the principle:

Noema must not guess when Intent is materially ambiguous.

It reinforces:

* Intent as a first-class object
* deterministic Validation
* deterministic Trust
* explicit execution contracts
* bounded autonomy
* human intervention as a valid state
* provenance
* explicit lifecycle state

⸻

43. Invariants

Invariant 1

Noema must not silently guess a material Intent parameter.

Invariant 2

Material ambiguity must prevent the Intent from becoming READY until resolved.

Invariant 3

Clarification is a valid lifecycle state.

Invariant 4

Model confidence is not sufficient to establish material Intent semantics.

Invariant 5

Authoritative context may resolve ambiguity when canonical semantics permit it.

Invariant 6

Deterministic defaults must be explicitly defined.

Invariant 7

Clarification responses must update the canonical Intent.

Invariant 8

Materially changed Intent requires revalidation and Trust re-evaluation.

Invariant 9

Clarification is distinct from rejection and blocking.

Invariant 10

Unknown information must not be converted into an assumed value.

Invariant 11

Noema must preserve clarification provenance where it contributes to Intent resolution.

Invariant 12

Noema must not infer permission merely because an interpretation appears probable.

⸻

44. Canonical Mental Model

The decision can be reduced to:

User Expression
      ↓
Possible Meanings
      ↓
Can one meaning be established?
      │
   ┌──┴──┐
  YES    NO
   │      │
   ▼      ▼
Resolved  Clarify
   │      │
   │      ▼
   │   New Information
   │      │
   └──────┘
      ↓
Validation
      ↓
Trust
      ↓
Execution

The critical boundary is:

Likely
  ≠
Established

⸻

45. Final Decision

Noema will prefer clarification over guessing whenever material ambiguity prevents reliable establishment of the Actor’s intended Intent.

Probabilistic models may propose interpretations and assist in identifying ambiguity, but they must not silently convert uncertainty into executable semantic authority.

The canonical rule is:

If Noema does not know what the Actor means well enough to safely and deterministically establish the Intent, it must ask, not guess.