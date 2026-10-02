> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

# Intent Generation
Status: Foundational
Version: 0.1
Domain: AI
Canonical Path: ai/intent-generation.md
⸻
## 1. Definition
Intent Generation is the process by which Noema uses probabilistic AI systems to transform human expressions and available context into a candidate Intent representation.
Intent Generation answers:
"What Intent representation should Noema evaluate as a candidate interpretation of this expression?"
It does not answer:
"What does the user definitively mean?"
That is Intent Resolution.
It does not answer:
"Is the resulting Intent structurally and semantically valid?"
That is Validation.
It does not answer:
"May this Intent proceed toward execution?"
That is Trust Evaluation.
Therefore:
AI Generation
      ↓
Candidate Intent
      ↓
Resolution
      ↓
Validation
      ↓
Trust
      ↓
Execution
Intent Generation is a proposal mechanism, not an authority mechanism.
⸻
## 2. Purpose
The purpose of Intent Generation is to provide Noema with a structured candidate representation of a human objective from inputs that may include:
- natural-language expressions
- conversational context
- structured application input
- relevant retrieved context
- previously established Intent state
- authorized contextual information
- available domain information
The generated representation provides material for subsequent deterministic processing.
The generated Intent is not automatically canonical.
⸻
## 3. Core Principle
The core principle is:
> AI may generate a candidate Intent, but Noema must independently establish whether that Intent is acceptable.
Therefore:
```text
Human Expression
       ↓
AI Intent Generation
       ↓
Candidate Intent
       ↓
Intent Resolution
       ↓
Validation
       ↓
Trust Evaluation

The AI model must never be treated as the final authority for the semantic or operational consequences of its own output.

⸻

4. Candidate Intent

Intent Generation produces a Candidate Intent.

Conceptually:

CandidateIntent {
    actor
    objective
    action
    subject
    parameters
    context
    constraints
    desired_outcome
    temporal_requirements
    provenance
}

The exact canonical Intent schema is defined by the Intent ontology and Intent specification.

The AI generation layer must conform to that schema rather than inventing an independent semantic model.

⸻

5. Generation Is Not Resolution

Generation and resolution must remain distinct.

Generation asks:

“What candidate Intent could represent this expression?”

Resolution asks:

“Which Intent, if any, is sufficiently established to represent what the Actor means?”

Example:

User:

“Send John the report.”

The model may generate:

Action:
SEND
Object:
REPORT
Recipient:
JOHN

If multiple people named John are possible recipients, the generated representation does not establish which John is intended.

Resolution must therefore identify the ambiguity.

The resulting state may be:

UNRESOLVED

or:

WAITING_FOR_CLARIFICATION

The model must not silently select a recipient merely because one appears statistically likely.

⸻

6. Generation Is Not Validation

A generated Intent may be syntactically well formed while still being invalid.

For example:

{
    action: TRANSFER,
    amount: -5000,
    currency: NGN
}

The model may generate this structure successfully.

Validation must independently determine whether the values satisfy the applicable rules.

Therefore:

Generated
    ≠
Valid

Generation provides candidate semantics.

Validation establishes whether those semantics satisfy explicit validation rules.

⸻

7. Generation Is Not Trust

A model may generate an Intent with high confidence.

That confidence does not establish Trust.

For example:

Model confidence:
0.99

does not mean:

Trust:
READY

Trust may still depend on:

* authorization
* policy
* evidence
* risk
* capability
* constraints
* context
* freshness
* approval
* confirmation

Therefore:

Model confidence
      ≠
Trust

⸻

8. Generation Is Not Authorization

Intent Generation must never infer authorization from the Actor’s request.

For example:

“Transfer ₦10M from the company account.”

The model may generate:

Action = TRANSFER
Amount = ₦10M
Account = company_account

It must not generate:

Authorized = true

unless authorization is represented as externally established evidence and subsequently evaluated by the Trust system.

Authorization is not a semantic property that the model may manufacture.

⸻

9. Generation Is Not Execution

Generated Intent must never directly invoke an Action.

The prohibited conceptual flow is:

User
 ↓
LLM
 ↓
Tool Call

The canonical flow is:

User Expression
      ↓
Intent Generation
      ↓
Candidate Intent
      ↓
Resolution
      ↓
Validation
      ↓
Trust
      ↓
Action Selection
      ↓
Execution Contract
      ↓
Execution Consumer

The AI model does not cross the execution boundary merely because it generated a plausible Action.

⸻

10. Inputs to Intent Generation

Intent Generation may consume several classes of input.

10.1 User Expression

The primary source may be:

* natural language
* voice transcription
* structured interaction
* application input
* conversational continuation

10.2 Authorized Context

Generation may use context made available to the model by Noema.

Examples include:

* current conversation context
* relevant Intent history
* Actor context
* domain context
* retrieved information
* available capabilities
* relevant application state

Context must be explicitly scoped.

10.3 Prior Intent State

Where permitted, an existing Intent may be supplied to help interpret subsequent user input.

Example:

Existing Intent:
Transfer ₦50,000 to John
New expression:
"Actually make it ₦75,000."

The model may generate a candidate update to the existing Intent.

The resulting Intent must still pass the appropriate resolution, validation, and Trust processes.

⸻

11. Context Must Not Become Authority

Context can improve semantic interpretation.

It must not silently expand authority.

For example:

Context:
Actor previously transferred money to John.

does not establish:

Actor is authorized to transfer money now.

Similarly:

Context:
John was the last recipient.

does not establish:

John is the intended recipient.

Context may provide evidence.

It does not automatically provide permission or semantic certainty.

⸻

12. Structured Generation

Where possible, Intent Generation should produce structured output conforming to the canonical Intent representation.

Conceptually:

Generate(
    expression,
    context,
    intent_schema
)
→ CandidateIntent

Structured generation reduces ambiguity in the interface between probabilistic AI and deterministic Noema components.

The structure itself does not establish correctness.

The generated object remains subject to downstream validation.

⸻

13. Schema Conformance

Generated output should be checked against the expected Intent schema.

The AI model must not be allowed to redefine:

* field meanings
* required semantics
* authority boundaries
* canonical types
* Trust states
* execution contracts

The canonical schema remains owned by Noema.

Therefore:

Canonical Schema
       ↓
AI Generation Constraint
       ↓
Candidate Intent
       ↓
Deterministic Validation

not:

AI
 ↓
New Schema
 ↓
Noema

⸻

14. Missing Information

Intent Generation must preserve missing information.

If the expression does not provide a required value, the generated Intent should represent that absence explicitly.

Example:

“Send the invoice.”

Candidate:

{
    action: SEND,
    object: INVOICE,
    recipient: UNKNOWN
}

The system must not invent a recipient merely to produce a complete-looking object.

The missing information may subsequently result in:

INCOMPLETE

and:

WAITING_FOR_CLARIFICATION

⸻

15. Ambiguity

Generation must preserve material ambiguity.

Example:

“Cancel my subscription.”

If the Actor has multiple subscriptions, generation should not silently select one.

The candidate representation may identify:

action = CANCEL
resource_type = SUBSCRIPTION
resource = AMBIGUOUS

Resolution must determine whether available context can establish the intended resource.

If not, Noema should request clarification.

⸻

16. Unknown Values

Unknown must remain distinct from known values.

The following are not equivalent:

recipient = UNKNOWN

and:

recipient = John

Likewise:

authorization = UNKNOWN

must not become:

authorization = GRANTED

The AI generation layer must preserve epistemic uncertainty rather than converting uncertainty into fabricated facts.

⸻

17. Defaults

AI Generation must not apply implicit defaults unless the canonical semantics explicitly permit them.

For example, if an Action defines:

currency:
    default = account.currency

the default may be deterministically established from the authoritative account context.

But:

recipient = most_recent_contact

must not be introduced merely because it is statistically plausible.

Defaults are semantic rules, not opportunities for model improvisation.

⸻

18. Entity Resolution

AI may assist with identifying candidate entities.

Example:

“Send it to John.”

The model may identify:

candidate_recipient:
John

However, authoritative entity resolution should establish the actual entity where required.

If multiple entities match:

John_123
John_456
John_789

the Intent must not be resolved by arbitrary selection.

Entity ambiguity must remain explicit until resolved through authoritative evidence or clarification.

⸻

19. Parameter Extraction

AI may extract parameters from natural language.

Example:

“Transfer fifty thousand naira to John tomorrow.”

Candidate:

action = TRANSFER
amount = 50000
currency = NGN
recipient = John
requested_time = tomorrow

Each extracted value remains subject to deterministic validation.

Extraction is not validation.

⸻

20. Natural-Language Normalization

AI may normalize equivalent expressions into canonical representations.

Examples:

"five thousand naira"
        ↓
5000 NGN

or:

"tomorrow morning"
        ↓
candidate temporal expression

Normalization must preserve semantic uncertainty where the source expression is itself ambiguous.

For example:

"later"

must not automatically become:

18:00

unless an explicit deterministic convention establishes that mapping.

⸻

21. Temporal Expressions

Temporal language may require interpretation.

Examples:

* today
* tomorrow
* next week
* after lunch
* immediately
* before close of business

AI may generate candidate temporal semantics.

Where exact temporal semantics are required, Noema must establish them through deterministic context and rules.

The model must not silently convert vague temporal language into precise execution authority.

⸻

22. Constraint Extraction

AI may identify constraints expressed by the Actor.

Example:

“Book the cheapest available flight, but don’t use a connection longer than three hours.”

Candidate:

objective:
    book_flight
constraints:
    price = minimize
    connection_duration <= 3 hours

These constraints must subsequently be represented according to the canonical Intent and Constraint models.

The model must not silently discard material constraints.

⸻

23. Desired Outcome

Generation should distinguish the requested outcome from the mechanism used to achieve it.

Example:

“I need the customer to have a working card before Friday.”

The underlying objective may be:

desired_outcome:
    customer_card_operational

rather than prematurely selecting:

action:
    REPLACE_CARD

Action selection belongs downstream where the available capabilities and context can be evaluated.

Intent Generation should preserve the distinction between:

what the Actor wants

and:

how the system might accomplish it

⸻

24. Avoid Premature Action Selection

Where the user’s expression specifies an objective rather than a mechanism, the AI should not unnecessarily commit to a particular execution Action.

For example:

“Make sure my card works again.”

The candidate Intent may represent:

objective:
    restore_card_functionality

rather than assuming:

action:
    REPLACE_CARD

The eventual Action may depend on:

* card state
* eligibility
* available capabilities
* policy
* authorization
* operational context

Intent Generation should therefore preserve objective semantics where appropriate.

⸻

25. Candidate Alternatives

In genuinely ambiguous cases, Intent Generation may produce multiple candidate interpretations.

Conceptually:

Candidate A
Candidate B
Candidate C

Each candidate must remain explicitly identified as a candidate.

No candidate becomes canonical merely because the model assigned it the highest probability.

Resolution may use:

* additional context
* deterministic rules
* authoritative evidence
* clarification

to establish the appropriate interpretation.

⸻

26. Generation Confidence

A model may provide confidence or likelihood information.

Such information may be retained as model provenance.

It must not be treated as deterministic Trust authority.

For example:

candidate:
    recipient = John
model_confidence:
    0.93

does not establish:

recipient_verified = true

Confidence describes the model’s output.

Validation and Trust establish Noema’s decision.

⸻

27. Provenance

Every generated Candidate Intent should be traceable to the generation event.

Conceptually:

GenerationProvenance {
    generation_id
    model_id
    model_version
    input_reference
    context_reference
    schema_version
    timestamp
    configuration
}

The exact schema is implementation-dependent.

The principle is canonical:

Noema must be able to determine which AI generation produced a candidate Intent and under what relevant conditions.

⸻

28. Model Versioning

Model-generated Intent representations may change when models change.

Therefore generation provenance should identify the model and relevant version.

Conceptually:

model:
    provider/model-name
version:
    model-version
generation:
    generation-id

This allows Noema to distinguish:

same expression
different model
different candidate

and supports evaluation and historical reconstruction.

⸻

29. Prompt and Configuration Provenance

Where materially relevant, the generation record should identify the configuration that influenced the result.

This may include:

* system instruction version
* generation schema version
* tool configuration
* retrieval configuration
* model parameters
* context version

The purpose is reproducibility and auditability, not exposure of private chain-of-thought.

⸻

30. Tool Use During Generation

AI Generation may use tools when explicitly permitted by the Harness.

Tool use must remain bounded.

A tool may provide:

evidence
context
candidate information

but tool access must not automatically grant execution authority.

Where a tool can mutate external business state, that operation must be governed by the same execution boundary as any other Action.

The model must not bypass Trust by invoking a tool directly.

⸻

31. Retrieval During Generation

Retrieval may provide context relevant to Intent Generation.

Retrieved information should remain distinguishable from:

* user-provided information
* authoritative business state
* model inference
* validated facts

The provenance of retrieved information should be retained where material to downstream decisions.

Retrieval improves grounding.

It does not independently establish Trust.

⸻

32. Generation Errors

Intent Generation may fail.

Examples include:

* malformed model output
* schema violation
* unavailable model
* timeout
* context failure
* unsupported request
* generation refusal
* incomplete generation

These failures must be represented explicitly.

A generation failure must not be interpreted as:

Intent = valid

or:

Intent = trusted

The appropriate downstream state depends on the lifecycle context.

⸻

33. Retry Semantics

Retries may be used to recover from transient generation failures.

However, a retry must not silently change the semantic interpretation of the request merely to obtain a successful output.

A retry may produce a different candidate.

That candidate must still pass the normal Resolution, Validation, and Trust processes.

Random variation must never itself constitute a Trust transition.

⸻

34. Generation and Determinism

AI generation is inherently probabilistic.

Therefore the requirement for deterministic Noema behavior does not mean:

same input → identical model output

Instead, determinism applies to the authoritative downstream decisions.

Conceptually:

Probabilistic Generation
        ↓
Candidate Intent
        ↓
Deterministic Resolution / Validation / Trust
        ↓
Authoritative State

Where reproducibility is required for a specific implementation or evaluation context, generation configuration should be controlled and recorded.

⸻

35. Generation and Validation Boundary

The boundary should remain explicit:

AI Generation
    │
    │ candidate
    ▼
Validation
    │
    │ verified representation
    ▼
Trust

The AI model should not be responsible for declaring its own output valid.

The validator remains authoritative for validation.

⸻

36. Generation and Intent State

Generation may occur at multiple points during the Intent lifecycle.

Examples:

UNRESOLVED
    ↓
AI generates candidate
    ↓
EVALUATING

or:

WAITING_FOR_CLARIFICATION
    ↓
Actor provides clarification
    ↓
AI generates updated candidate
    ↓
EVALUATING

A new generation does not automatically imply a new Trust decision.

The resulting Intent must pass the relevant lifecycle stages again.

⸻

37. Intent Updates

When new user information changes an existing Intent, AI may generate a candidate update.

Example:

Initial:

Transfer ₦50,000 to John.

New instruction:

Actually, make it ₦75,000.

The candidate update may be:

amount:
    75000

The updated Intent must be treated as materially changed.

Any previously established Trust conditions that depend on the changed field must be re-evaluated.

For example, an approval threshold may now be exceeded.

⸻

38. No Silent Semantic Mutation

AI Generation must not silently change established Intent semantics.

If an Intent changes materially, the change must be represented as an Intent update or new Intent version.

Examples of material changes include:

* actor
* objective
* action
* target
* amount
* recipient
* resource
* constraints
* execution timing
* desired outcome

This ensures that Trust decisions cannot accidentally attach to a different Intent than the one evaluated.

⸻

39. Generation and Safety

The AI Harness may apply model-level safety controls.

However, model safety behavior must not be confused with Noema Trust.

For example:

Model safety:
    refuses to generate content

is different from:

Noema Trust:
    execution is prohibited by policy

Both may prevent progression, but they operate at different architectural layers.

⸻

40. Generation and Human Clarification

When the model identifies material ambiguity, it may propose a clarification question.

For example:

Ambiguity:
three matching recipients
Clarification:
"Which John do you want to send the report to?"

The clarification itself must not contain an invented assumption.

After the Actor responds, the new information becomes input to a subsequent generation and resolution cycle.

⸻

41. Generation and Evidence

Generated fields may be supported by evidence.

Example:

Candidate:
recipient = customer_123
Evidence:
customer registry result

The evidence must remain distinguishable from the model’s inference.

Conceptually:

Model:
"customer_123 appears to be John."
Authoritative evidence:
"customer_123 is registered as John Smith."
Validation:
reference is valid.

Generation proposes.

Evidence establishes.

Validation evaluates.

Trust determines execution eligibility.

⸻

42. Generation and External Business State

The AI model must not become the source of truth for external business state.

For example, if the model generates:

account_balance = ₦100,000

that value must not automatically be treated as authoritative.

Where current business state matters, Noema should obtain it through the appropriate authoritative system.

The model may reason over business state.

It does not own that state.

⸻

43. Generation Contract

Conceptually:

GenerateIntent(
    expression,
    context,
    schema,
    generation_configuration
)
→ CandidateIntent

The contract should establish:

* accepted inputs
* permitted context
* output schema
* provenance requirements
* failure semantics
* model configuration
* tool boundaries

The generated result remains non-authoritative until processed by downstream Noema components.

⸻

44. Example

User:

“Send ₦50,000 to John tomorrow.”

AI Generation:

CandidateIntent {
    objective: transfer_funds
    action: transfer
    recipient: John
    amount: 50000
    currency: NGN
    requested_time: tomorrow
}

The next stages are:

Candidate Intent
       ↓
Resolution
       ↓
Reference / Temporal Resolution
       ↓
Validation
       ↓
Trust Evaluation
       ↓
Execution Eligibility

If three Johns exist:

Resolution:
    ambiguous
State:
    WAITING_FOR_CLARIFICATION

The model must not select one merely because it is the most probable candidate.

⸻

45. Example: Missing Amount

User:

“Send John the usual amount.”

Generation:

CandidateIntent {
    action: transfer
    recipient: John
    amount: unknown
}

If no deterministic rule establishes what “usual amount” means:

Resolution:
    insufficient information
State:
    WAITING_FOR_CLARIFICATION

The system must not infer an amount from an arbitrary previous transaction.

⸻

46. Example: Objective Without Mechanism

User:

“Get my card working again.”

Generation may produce:

CandidateIntent {
    objective: restore_card_functionality
    desired_outcome: operational_card
}

Noema should not necessarily generate:

action: replace_card

because the appropriate mechanism may depend on the current card state and available capabilities.

Action selection belongs downstream.

⸻

47. Example: High Confidence, Low Trust

User:

“Transfer ₦20M from the company account.”

AI:

intent_confidence = 0.98

Validation:

VALID

Trust:

BLOCKED_BY_AUTHORIZATION

The high model confidence does not alter the Trust result.

This demonstrates the separation:

Confidence
    ≠
Validation
    ≠
Trust

⸻

48. Evaluation of Intent Generation

Intent Generation should be evaluated independently from Trust.

Relevant evaluation dimensions may include:

* semantic accuracy
* field extraction accuracy
* ambiguity preservation
* omission rate
* hallucination rate
* schema conformance
* constraint preservation
* context utilization
* temporal interpretation
* objective preservation
* action overcommitment
* provenance completeness

A strong generation result is not necessarily a trusted execution decision.

Evaluation belongs to the AI evaluation system.

⸻

49. Generation Quality Must Not Become Authority

A model may achieve high evaluation performance.

That does not eliminate deterministic validation and Trust.

The architectural rule remains:

Better model
    ≠
automatic authority

Improved generation reduces errors in candidate Intent construction.

It does not remove the need for downstream controls.

⸻

50. Auditability

A consequential generated Intent should be attributable to:

* source expression
* generation event
* model
* model version
* relevant context
* schema version
* generated candidate
* subsequent resolution
* validation result
* Trust evaluation

This enables Noema to reconstruct how a candidate Intent entered the lifecycle.

The audit record should describe system decisions and provenance without requiring storage of private chain-of-thought.

⸻

51. Generation Invariants

Invariant 1

Intent Generation produces candidate semantics, not authoritative semantics.

Invariant 2

AI confidence is not Trust.

Invariant 3

Generated output must not bypass Validation.

Invariant 4

Generated output must not bypass Trust.

Invariant 5

Generated output must not directly execute Actions.

Invariant 6

Material ambiguity must remain explicit.

Invariant 7

Missing information must not be fabricated.

Invariant 8

Unknown values must not be converted into known values without evidence.

Invariant 9

Context may support interpretation but must not silently create authority.

Invariant 10

AI must not silently mutate established Intent semantics.

Invariant 11

Generated Intent must conform to the canonical Intent representation.

Invariant 12

Generation provenance must be retained where required for reconstruction.

Invariant 13

External business systems remain authoritative for their business state.

Invariant 14

A model retry does not constitute a Trust transition.

Invariant 15

A high-quality or high-confidence generation does not eliminate deterministic downstream controls.

⸻

52. Canonical Generation Flow

                 Human Expression
                        │
                        ▼
               Context Preparation
                        │
                        ▼
                AI Intent Generation
                        │
                        ▼
                Candidate Intent
                        │
              ┌─────────┴─────────┐
              │                   │
        sufficient            insufficient /
        information             ambiguous
              │                   │
              ▼                   ▼
         Resolution         Clarification
              │                   │
              └─────────┬─────────┘
                        ▼
                    Validation
                        │
                        ▼
                  Trust Evaluation
                        │
               ┌────────┼────────┐
               ▼        ▼        ▼
            WAITING  BLOCKED    READY
                                  │
                                  ▼
                              Contract
                                  │
                                  ▼
                              Execution

The AI component participates in the semantic portion of the lifecycle.

It does not own the complete lifecycle.

⸻

53. Canonical Mental Model

Intent Generation can be reduced to five questions:

1. What did the Actor express?
2. What candidate Intent does that expression suggest?
3. What information is explicit, inferred, missing, or ambiguous?
4. What evidence or context supports the candidate?
5. What must Noema establish before accepting the candidate?

This produces:

Expression
    ↓
Candidate
    ↓
Evidence / Context
    ↓
Resolution
    ↓
Validation
    ↓
Trust

⸻

54. Final Definition

Intent Generation is Noema’s AI-assisted process for producing structured candidate representations of human intent from expressions and authorized context.

Its output is probabilistic and non-authoritative.

The canonical boundary is:

AI generates candidates. Noema resolves, validates, and establishes trust. Explicit contracts govern execution.

Noema therefore never treats a model’s generated Intent, confidence, reasoning, or proposed Action as sufficient authority to cross the execution boundary.