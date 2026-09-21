ADR-009 — Preserve the Separation Between Validation and Trust

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational Architecture
Domain: Validation / Trust / Intent
Canonical Path: decisions/ADRs/009-separate-validation-from-trust.md

⸻

1. Context

Noema requires a deterministic boundary between:

1. understanding what an Actor intends,
2. establishing whether the resulting Intent is structurally and semantically valid, and
3. determining whether that valid Intent may proceed toward execution.

These concerns are related but are not equivalent.

The canonical lifecycle is:

User Expression
       ↓
Interpretation
       ↓
Resolution
       ↓
Validation
       ↓
Trust Evaluation
       ↓
Execution Eligibility
       ↓
Execution
       ↓
Outcome

Without an explicit architectural separation, Validation can gradually become an authorization mechanism, while Trust can become a duplicate validation layer.

That would make it unclear:

* whether an Intent is malformed or merely unauthorized,
* whether missing information requires clarification or approval,
* whether a policy violation is an invalid Intent or a blocked execution,
* which subsystem owns a particular decision,
* which evidence was used for validation versus authorization,
* and which state transition should occur when conditions change.

Noema therefore requires a formal separation.

⸻

2. Decision

Noema will treat Validation and Trust as distinct canonical layers.

Validation asks:

Is this Intent structurally complete, semantically applicable, and valid for the next lifecycle stage?

Trust asks:

Given this valid Intent and its current conditions, may it proceed toward execution?

Therefore:

VALID ≠ TRUSTED

and:

INVALID ≠ UNAUTHORIZED

Validation establishes validity.

Trust establishes execution eligibility.

Neither layer may silently assume the responsibilities of the other.

⸻

3. Canonical Relationship

The canonical relationship is:

                 Intent
                    │
                    ▼
               Validation
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
   INCOMPLETE     INVALID      VALID
        │           │           │
        ▼           ▼           ▼
     WAITING      BLOCKED    Trust Engine
                                │
                    ┌───────────┼───────────┐
                    ▼           ▼           ▼
                 WAITING      BLOCKED      READY

The exact state transition depends on the relevant reason and lifecycle semantics, but the architectural boundary remains fixed.

⸻

4. Why Validation Must Be Separate

Validation answers questions such as:

* Are required fields present?
* Are values of the correct type?
* Do references resolve?
* Are domain values supported?
* Are hard constraints satisfied?
* Is the Intent applicable to the current object?
* Is required evidence available and sufficiently fresh?
* Is the canonical Intent internally consistent?

Examples:

amount = "a lot"

may be structurally invalid when a concrete Money value is required.

Or:

destination = missing

may make the Intent incomplete.

Or:

source_account = destination_account

may violate a cross-field constraint.

These are validation concerns.

⸻

5. Why Trust Must Be Separate

Trust answers questions such as:

* Is the Actor authorized?
* Does policy permit this Action?
* Is approval required?
* Has required approval been granted?
* Is the risk within the permitted boundary?
* Is the required capability currently available?
* Is the Actor within the permitted scope?
* Are authorization and policy conditions currently satisfied?

An Intent may therefore be completely valid while remaining untrusted.

Example:

Intent:
Transfer ₦10,000,000 to Account B
Validation:
VALID
Policy:
Transfers above ₦5,000,000 require approval
Trust:
WAITING_FOR_APPROVAL

The Intent is not malformed.

It simply cannot yet cross the execution boundary.

⸻

6. Validation Does Not Authorize

Validation must never convert:

valid = true

into:

authorized = true

For example:

Intent:
Delete employee record
Validation:
VALID
Authorization:
DENIED

The resulting Trust state may be:

BLOCKED_BY_AUTHORIZATION

The validation result remains:

VALID

This preserves the distinction between:

“The request is well formed.”

and:

“The Actor is permitted to perform it.”

⸻

7. Trust Does Not Repair Invalid Intent

Trust evaluation must not be used to compensate for unresolved or invalid semantics.

Example:

Intent:
Transfer money to John
Three John records exist.

Validation/resolution cannot establish a unique destination.

The system must not proceed to:

Trust → READY

merely because the Actor appears authorized to make transfers.

The correct lifecycle is to preserve the unresolved condition and obtain the information required to establish the canonical Intent.

⸻

8. Validation Result

Validation must produce a structured result rather than a bare boolean.

Conceptually:

ValidationResult {
    status
    errors
    warnings
    requirements
    evidence
}

Canonical conceptual statuses are:

VALID
INVALID
INCOMPLETE
UNKNOWN

VALID

All mandatory validation conditions are satisfied.

INVALID

A deterministic validation rule has been violated.

INCOMPLETE

Required information is missing but potentially recoverable.

UNKNOWN

A required validation condition cannot currently be established.

⸻

9. UNKNOWN Is Not VALID

A central invariant is:

UNKNOWN ≠ VALID

For example:

recipient = customer_123

but the Customer Registry is unavailable.

Noema must not infer:

customer_123 exists = true

The result should remain:

UNKNOWN

and the Intent must not become READY when that information is mandatory.

This preserves the broader fail-closed principle.

⸻

10. Validation and Clarification

Validation may reveal that the Intent is incomplete.

Example:

User:
"Send the invoice."
Resolved Intent:
Action = SEND
Object = invoice
Recipient = missing

Validation produces:

INCOMPLETE

with a requirement such as:

RECIPIENT_REQUIRED

The lifecycle may then become:

INCOMPLETE
     ↓
WAITING_FOR_CLARIFICATION
     ↓
clarification received
     ↓
revalidation

Validation does not invent the missing recipient.

⸻

11. Validation and Policy

Policy is especially important because policy requirements do not necessarily make an Intent invalid.

Example:

Intent:
Transfer ₦10M
Validation:
VALID
Policy:
Transfers above ₦5M require approval
Trust:
WAITING_FOR_APPROVAL

The policy establishes a Trust requirement.

It does not necessarily invalidate the Intent.

This distinction prevents governance requirements from being incorrectly represented as semantic errors.

⸻

12. Validation and Authorization

Authorization has two different aspects that must remain distinguishable.

Validation may establish:

Is the authorization information well formed and applicable?

Trust establishes:

Does the current authorization permit this execution?

For example:

Authorization Record:
valid structure
Actor = A
Resource = R
Action = TRANSFER

Validation may establish that the authorization reference is applicable.

Trust then evaluates whether the authorization currently permits the requested Action.

⸻

13. Capability Validation vs Capability Trust

Capability also has multiple dimensions.

Validation may establish:

Action:
TRANSFER
Capability:
supports TRANSFER
Required parameters:
supported

Trust may subsequently establish:

Capability:
currently available

Therefore:

Capability existence/support

and:

Capability availability for execution

must not be conflated.

⸻

14. Context Validation

Validation may establish whether the Intent is applicable to the current domain object.

Example:

Intent:
Close Incident 123
Current Incident State:
RESOLVED

If the Action requires an open incident, the Intent may be invalid or no longer applicable.

This is different from:

Actor is not authorized to close incidents

which is a Trust concern.

⸻

15. Temporal and Freshness Conditions

Some conditions change with time.

For example:

approval expires
authorization expires
evidence becomes stale
resource reservation expires
execution window closes

The relevant condition may require validation, Trust re-evaluation, or both depending on its semantics.

The architecture therefore does not assume that validation happens exactly once.

Instead:

Material change
      ↓
Relevant condition identified
      ↓
Validation and/or Trust re-evaluation

⸻

16. Revalidation

Validation must be repeatable.

An Intent may require revalidation when:

* Intent semantics change
* referenced entities change
* relevant context changes
* resource state changes
* required evidence changes
* capability definitions change
* applicable rules change
* time-sensitive conditions expire

The result must be determined from the current:

Intent
Context
Evidence
Rules
Rule versions

⸻

17. Determinism

Validation must be deterministic.

Conceptually:

Validation(
    Intent,
    Context,
    Evidence,
    Rules
)
→
ValidationResult

Given the same inputs and rule versions, the result should be reproducible.

Likewise, Trust must independently remain deterministic with respect to its own required inputs.

Therefore:

Validation determinism

and:

Trust determinism

are separate requirements.

⸻

18. LLM Boundary

LLMs may assist with:

* interpretation
* extraction
* normalization
* candidate Intent generation
* contextual reasoning
* clarification generation

They must not be the authoritative validator for consequential conditions.

The canonical architecture is:

Natural Language
      ↓
LLM / Interpretation
      ↓
Candidate Intent
      ↓
Deterministic Resolution
      ↓
Deterministic Validation
      ↓
Trust Evaluation
      ↓
Execution

The model may propose.

The canonical system validates.

The Trust Engine evaluates authority.

⸻

19. No Silent Mutation

Validation must not silently modify an Intent to make it valid.

Example:

Input:
Transfer to John
Possible recipients:
John A
John B
John C

Validation must not silently select:

recipient = John B

because it appears statistically likely.

Instead, the system should preserve the ambiguity and obtain the information necessary to resolve it.

⸻

20. Evidence

Validation may consume evidence.

Example:

Customer Registry
    ↓
customer_123 exists

This may establish:

Validation:
VALID

Trust may consume separate or overlapping evidence.

For example:

Authorization Registry
    ↓
Actor A may perform Action X on Resource R

which supports a Trust decision.

The same external fact may sometimes support both layers, but its semantic role must remain explicit.

⸻

21. External Systems

External systems may perform additional authoritative validation.

Example:

Noema:
Intent validated
Trust = READY
Payment Consumer:
Account state changed
Consumer:
execution rejected

This does not necessarily mean Noema’s prior validation was wrong.

It demonstrates that:

Validation
      ↓
Trust
      ↓
Execution

are temporally separated and that business state may change between stages.

Final business-state validation may therefore remain the responsibility of the authoritative consumer.

⸻

22. Failure Modes

The separation allows Noema to distinguish:

INVALID

from:

UNAUTHORIZED

and:

UNKNOWN

from:

DENIED

For example:

Condition	Validation	Trust
Missing required field	INCOMPLETE	Not Ready
Invalid amount	INVALID	Blocked / cannot proceed
Recipient cannot currently be verified	UNKNOWN	Not Ready
Intent valid, authorization denied	VALID	BLOCKED
Intent valid, approval missing	VALID	WAITING
Intent valid, all conditions satisfied	VALID	READY

This distinction is foundational for safe recovery and observability.

⸻

23. State Transition Implications

Validation outcomes may influence Trust State Machine transitions.

Conceptually:

Validation = INCOMPLETE
        ↓
WAITING_FOR_CLARIFICATION
Validation = INVALID
        ↓
BLOCKED
Validation = UNKNOWN
        ↓
WAITING / NOT READY
Validation = VALID
        ↓
Trust Evaluation

However, these are lifecycle mappings rather than a replacement of one state machine with another.

Validation Result and Trust State remain separate concepts.

⸻

24. Auditability

Validation decisions must be reconstructible.

A validation record should conceptually identify:

validation_id
intent_id
intent_version
rule_id
rule_version
inputs
evidence
result
timestamp
reason

Trust evaluation should independently identify its own:

trust_evaluation_id
policy_versions
authorization evidence
risk inputs
capability state
decision
timestamp
reason

This allows Noema to answer:

Why was this Intent considered valid?

separately from:

Why was this Intent trusted?

⸻

25. Consequences

Positive consequences

This decision:

* creates a clean architectural boundary
* prevents Validation from becoming an authorization engine
* prevents Trust from becoming a semantic parser
* makes failure reasons more precise
* enables independent rule versioning
* improves auditability
* supports deterministic re-evaluation
* makes clarification behavior explicit
* preserves the distinction between validity and authority
* supports external authoritative validation
* reduces semantic ambiguity across the repository

Trade-offs

The separation introduces additional concepts and interfaces.

Implementations must preserve:

Intent
ValidationResult
TrustEvaluation
TrustState
ExecutionState

rather than collapsing them into a single status.

This additional structure is intentional.

⸻

26. Invariants

Invariant 1

Validation and Trust are distinct canonical layers.

Invariant 2

A valid Intent is not necessarily trusted.

Invariant 3

An invalid Intent cannot become executable merely because the Actor is authorized.

Invariant 4

Validation must not silently authorize an Action.

Invariant 5

Trust must not silently repair invalid or incomplete Intent semantics.

Invariant 6

Unknown validation conditions must not be treated as valid.

Invariant 7

Validation must not guess missing information.

Invariant 8

Policy requirements must not automatically be represented as semantic invalidity.

Invariant 9

Validation results must be structured and auditable.

Invariant 10

Validation rules must be versionable.

Invariant 11

Material changes may require revalidation.

Invariant 12

External execution consumers may perform additional authoritative validation.

Invariant 13

Validation does not execute Actions.

Invariant 14

Trust does not guarantee execution success.

⸻

27. Decision Summary

Noema will preserve the following canonical distinction:

Interpretation
"What might the Actor mean?"
        ↓
Resolution
"What does the Actor mean?"
        ↓
Validation
"Is that Intent well-formed and applicable?"
        ↓
Trust
"May that Intent proceed?"
        ↓
Execution
"Perform the Action."
        ↓
Outcome
"What happened?"

The architectural rule is:

Validation establishes whether an Intent is valid. Trust establishes whether that valid Intent may proceed. Neither layer may silently assume the authority or responsibilities of the other.