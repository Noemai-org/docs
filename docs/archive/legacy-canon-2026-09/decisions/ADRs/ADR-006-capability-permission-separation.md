> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

ADR-006 — Separate Validation from Trust

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational Architecture
Domain: Trust / Intent Lifecycle
Canonical Path: decisions/ADR/006-validation-vs-trust.md

⸻

1. Context

Noema must determine whether an Intent can proceed toward execution.

Several distinct questions arise during that process:

1. What does the Actor mean?
2. Is the resulting Intent structurally and semantically valid?
3. Does the Actor have the authority to perform the requested Action?
4. Does policy permit the Action?
5. Are the required capabilities, evidence, constraints, and contextual conditions satisfied?
6. May the Intent cross the execution boundary?

These questions must not collapse into a single evaluation.

In particular, Validation and Trust perform different functions.

Validation establishes whether the canonical Intent is sufficiently well-formed and applicable for the next lifecycle transition.

Trust establishes whether the valid Intent may proceed toward execution under the current authorization, policy, evidence, capability, risk, constraint, and contextual conditions.

Without this separation, the Trust Engine risks becoming responsible for basic semantic and structural correctness, while Validation risks becoming an implicit authorization system.

⸻

2. Problem

If Validation and Trust are treated as the same concept, Noema loses important distinctions.

For example:

Intent:
Transfer ₦10,000,000 to John

The Intent may be:

* structurally valid
* semantically complete
* applicable to the requested resource

while still being:

* unauthorized
* subject to an approval requirement
* prohibited by policy
* outside the Actor’s permitted scope

Therefore:

VALID ≠ TRUSTED

Likewise, an Intent may be trusted in principle but fail structural validation because required information is missing.

Noema therefore requires an explicit architectural boundary between the two.

⸻

3. Decision

Noema will maintain Validation and Trust Evaluation as separate canonical layers.

The canonical lifecycle is:

Intent Interpretation
        ↓
Intent Resolution
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

Validation answers:

Is this Intent structurally complete, semantically applicable, and valid for its next lifecycle transition?

Trust answers:

Given this Intent and its current conditions, may it proceed toward execution?

⸻

4. Validation

Validation is deterministic verification of the canonical Intent.

Validation may establish:

* required fields exist
* field types are correct
* references are well formed
* references resolve where required
* domain rules are satisfied
* hard constraints are satisfied
* cross-field relationships are valid
* contextual applicability is established
* temporal conditions are valid
* required evidence is available and sufficiently fresh

Validation produces a structured result rather than merely a boolean.

Conceptually:

ValidationResult {
    status
    errors
    warnings
    requirements
    evidence
}

Canonical validation states include:

VALID
INVALID
INCOMPLETE
UNKNOWN

⸻

5. Trust

Trust evaluation operates after sufficient validation has been established.

Trust may evaluate:

* authorization
* policy
* risk
* capability
* constraints
* context
* evidence
* freshness
* approval requirements
* confirmation requirements
* execution eligibility

The Trust Engine determines the appropriate Trust State.

Canonical Trust states include:

UNRESOLVED
EVALUATING
WAITING
BLOCKED
READY

Execution state is treated separately where appropriate.

⸻

6. Relationship Between Validation and Trust

The canonical relationship is:

Resolved Intent
      ↓
Validation
      │
      ├── INCOMPLETE → WAITING
      │
      ├── INVALID    → BLOCKED
      │
      ├── UNKNOWN   → NOT READY
      │
      └── VALID
            ↓
      Trust Evaluation
            │
            ├── WAITING
            ├── BLOCKED
            └── READY

This means:

Validation
    ↓
establishes validity
Trust
    ↓
establishes execution eligibility

Neither layer replaces the other.

⸻

7. Validation Must Not Authorize

Validation must not transform:

Valid Intent

into:

Authorized Intent

For example:

Transfer ₦10M

may pass all structural and semantic validation.

A policy may nevertheless require secondary approval.

The resulting state may therefore be:

Validation = VALID
Trust = WAITING_FOR_APPROVAL

Validation does not grant the approval.

⸻

8. Trust Must Not Resolve Meaning

Trust must not compensate for unresolved semantic information.

For example:

"Send the report to John."

where several Johns exist.

The system must not select one recipient merely because the Trust Engine can evaluate authorization for one of them.

The correct sequence is:

Ambiguous Intent
      ↓
Resolution / Clarification
      ↓
Resolved Intent
      ↓
Validation
      ↓
Trust

Meaning must be established before consequential Trust evaluation.

⸻

9. Unknown Is Not Valid

An unavailable external dependency must not be interpreted as evidence that a condition is satisfied.

For example:

Customer Registry unavailable

does not establish:

recipient_exists = true

The result must remain:

UNKNOWN

and the Intent must not become:

READY

solely because the system could not determine the answer.

This applies to both Validation and Trust.

⸻

10. Determinism

Both Validation and Trust must be deterministic with respect to their authoritative inputs.

For Validation:

Validation(
    Intent,
    Context,
    Evidence,
    Rules
)

must produce a deterministic result for the same inputs and rule versions.

For Trust:

TrustEvaluation(
    Intent,
    Context,
    Evidence,
    Authorization,
    Policy,
    Capability,
    Constraints,
    Risk,
    RuleVersions
)

must likewise produce a deterministic result.

LLM confidence must not substitute for either decision.

⸻

11. Validation Does Not Guarantee Execution

Even when:

Validation = VALID
Trust = READY

execution may still fail.

Business state can change between:

T1: Validation
T2: Trust
T3: Execution

The execution consumer may therefore perform final authoritative checks.

For example:

Noema:
VALID + READY
Payment Service:
Account balance has changed
Result:
Execution rejected

This does not necessarily invalidate the earlier Validation result.

It demonstrates that business systems remain authoritative over their current state.

⸻

12. Revalidation

Validation is not necessarily a one-time operation.

Revalidation may be required when:

* the Intent changes
* relevant context changes
* a referenced resource changes
* evidence changes
* evidence expires
* capability changes
* time-sensitive conditions change
* applicable rules change

Similarly, Trust must be re-evaluated when material Trust dependencies change.

Therefore:

Material Change
      ↓
Revalidation / Re-evaluation
      ↓
Current Decision

Noema must not rely indefinitely on stale decisions.

⸻

13. Provenance

Both Validation and Trust decisions must be reconstructible.

Validation provenance should identify, where applicable:

* rule
* rule version
* input
* evidence
* timestamp
* result

Trust provenance should identify, where applicable:

* evaluation
* relevant authorization
* policy
* evidence
* capability
* constraints
* risk conditions
* timestamp
* resulting Trust State
* reason

This allows Noema to distinguish:

Why was this Intent considered valid?

from:

Why was this Intent permitted to proceed?

⸻

14. Consequences

Positive

This separation provides:

* clearer architectural boundaries
* deterministic semantic validation
* deterministic authorization and Trust evaluation
* more precise failure states
* better auditability
* clearer responsibility between engines
* easier testing
* more targeted re-evaluation
* reduced risk of implicit authorization
* reduced risk of LLM-generated authority

Negative

The architecture introduces additional concepts and lifecycle stages.

Implementations must maintain distinctions between:

Resolution
Validation
Trust
Execution
Outcome

This may initially require more explicit state and provenance than a single validation/authorization function.

The additional complexity is intentional because these concepts represent materially different system responsibilities.

⸻

15. Rejected Alternatives

15.1 Combine Validation and Trust

Rejected because:

valid

and:

permitted

are different claims.

Combining them would make it difficult to determine whether an Intent failed because it was malformed, incomplete, unauthorized, prohibited, or otherwise untrusted.

⸻

15.2 Let the LLM Perform Validation

Rejected as the authoritative mechanism.

An LLM may assist with:

* interpretation
* normalization
* candidate Intent generation
* clarification generation

but consequential validation must be grounded in explicit rules and authoritative evidence.

⸻

15.3 Treat Validation Failure as Universal Rejection

Rejected because:

INCOMPLETE

and:

INVALID

are materially different.

For example:

destination missing

may be recoverable through clarification.

Whereas:

amount < 0

may be deterministically invalid.

Noema must preserve this distinction.

⸻

15.4 Allow Unknown Conditions to Pass

Rejected.

Unknown conditions cannot establish the predicates required for execution eligibility.

Therefore:

UNKNOWN ≠ VALID
UNKNOWN ≠ AUTHORIZED
UNKNOWN ≠ READY

⸻

16. Canonical Invariants

The following invariants are established by this decision:

1. Validation and Trust are separate concepts.
2. Validation operates on canonical Intent semantics.
3. Validation does not authorize an Intent.
4. Trust does not resolve ambiguous Intent meaning.
5. Validation does not execute Actions.
6. Trust does not guarantee execution success.
7. Unknown mandatory information cannot establish validity or readiness.
8. Validation must distinguish incomplete from invalid.
9. Validation and Trust decisions must be deterministic.
10. Both Validation and Trust must be auditable and provenance-aware.
11. Material changes may require revalidation and/or Trust re-evaluation.
12. The execution consumer remains authoritative for final business-state validation where required.

⸻

17. Canonical Mental Model

The distinction can be reduced to:

Resolution
"What does the Actor mean?"
        ↓
Validation
"Is that Intent valid?"
        ↓
Trust
"May that Intent proceed?"
        ↓
Execution
"Perform the Action."
        ↓
Outcome
"What happened?"

The critical boundary is:

VALID ≠ TRUSTED ≠ SUCCESSFUL

⸻

18. Decision Summary

Noema will treat Validation as the deterministic verification layer for the canonical Intent and Trust as the deterministic execution-eligibility layer operating on that Intent and its surrounding conditions.

Validation establishes that Noema understands a sufficiently complete and applicable Intent representation.

Trust establishes whether that Intent may cross the execution boundary.

Neither layer may substitute for the other.