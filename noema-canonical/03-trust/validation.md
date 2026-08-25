Validation

Status: Foundational
Version: 0.1
Domain: Trust
Canonical Path: 03-trust/validation.md

⸻

1. Definition

Validation is the deterministic process by which Noema verifies that a resolved Intent satisfies the structural, semantic, authorization, policy, capability, constraint, and contextual conditions required for its next lifecycle transition.

Validation answers:

Is this Intent valid for what Noema is about to do with it?

This is distinct from asking:

What does the user mean?

That is Intent resolution.

And distinct from:

May this Intent execute?

That is Trust evaluation.

⸻

2. Validation’s Position in Noema

The canonical relationship is:

User Expression
       ↓
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

Validation therefore sits between semantic resolution and Trust evaluation.

However, validation may also occur continuously as the Intent moves through its lifecycle.

⸻

3. Validation vs Resolution

These must remain separate.

Resolution asks:

"What does the user mean?"

Validation asks:

"Is the resulting Intent structurally and semantically valid?"

Example:

"Transfer ₦50,000 to John."

Resolution determines:

Action = transfer
Amount = ₦50,000
Recipient = John

Validation determines whether:

Amount is valid
Recipient is valid
Currency is supported
Required fields exist
Action supports these parameters

⸻

4. Validation vs Trust

Validation and Trust are related but not equivalent.

Validation asks:

Is this Intent valid?

Trust asks:

Given this valid Intent and its surrounding conditions, may it cross the execution boundary?

Therefore:

Valid ≠ Trusted

An Intent can be valid but blocked:

Valid Intent
     ↓
Authorization denied
     ↓
BLOCKED

⸻

5. Validation vs Model Confidence

Model confidence is not validation.

A model may produce:

confidence = 0.98

while the Intent is structurally invalid.

Therefore:

Model confidence
      ≠
Validation

Validation must be deterministic.

⸻

6. Validation Principles

Validation in Noema follows several principles:

Deterministic
Explicit
Schema-aware
Context-aware
Fail-closed
Traceable
Composable
Re-evaluable

⸻

7. Structural Validation

Structural validation establishes that an Intent conforms to the expected Intent representation.

Example:

Intent {
    action: transfer
    actor: user_123
    resource: account_456
    amount: 50000
}

Validation checks:

action exists
actor exists
required fields exist
types are correct
references are well formed

⸻

8. Required Fields

Each Action may define required fields.

Example:

Transfer {
    source
    destination
    amount
    currency
}

An Intent such as:

Transfer {
    destination
    amount
}

is incomplete.

It should not proceed to execution.

Depending on whether the missing information can be obtained through clarification:

WAITING_FOR_CLARIFICATION

may be appropriate.

⸻

9. Type Validation

Values must conform to their canonical types.

Examples:

amount → Money
actor → Actor reference
resource → Resource reference
timestamp → Timestamp
quantity → Quantity

Invalid:

amount = "a lot"

if the Action requires a concrete monetary amount.

⸻

10. Domain Validation

A value may be structurally valid but semantically invalid within the domain.

Example:

currency = "XYZ"

may be a syntactically valid string but unsupported by the payment capability.

Therefore validation may include domain rules.

⸻

11. Referential Validation

References must resolve to valid entities where resolution is required.

Example:

recipient = customer_123

Validation may establish:

customer_123 exists

If multiple entities match an unresolved reference:

"John"

then the Intent may remain ambiguous.

This is not something Validation should resolve through guessing.

⸻

12. Capability Validation

The requested Action must correspond to an available capability.

Example:

Intent:
refund payment

Validation may establish:

refund capability exists
required parameters supported
consumer supports operation

Capability availability may subsequently be evaluated again by Trust.

⸻

13. Constraint Validation

Validation checks explicit constraints attached to the Intent or Action.

Examples:

amount > 0
amount <= maximum
source != destination
resource belongs to Actor

A violated hard constraint should prevent the Intent from becoming executable.

⸻

14. Policy Validation

Policies may impose requirements on the Intent.

Example:

Policy:
Transfers above ₦5M require approval.

The Intent:

Transfer ₦10M

may be valid.

The Policy does not necessarily invalidate the Intent.

Instead:

Intent valid
      ↓
approval required
      ↓
WAITING_FOR_APPROVAL

This distinction is important.

⸻

15. Authorization Validation

Authorization establishes whether the Actor is eligible to perform the requested Action.

However, authorization may be evaluated as part of Trust rather than basic validation.

The canonical distinction is:

Validation:
"Is the authorization reference/result well-formed and applicable?"
Trust:
"Does authorization permit this execution?"

This prevents Validation from becoming a duplicate Trust Engine.

⸻

16. Context Validation

An Intent may be valid only within certain contexts.

Example:

Action:
close incident
Context:
incident must be OPEN

If:

incident.state = RESOLVED

the Intent may be invalid or no longer applicable.

⸻

17. Temporal Validation

Time-sensitive values must be valid relative to the current context.

Examples:

approval has expired
authorization is not yet active
requested execution window has passed
resource reservation expired

Temporal validity may affect Trust even if the Intent’s static structure remains valid.

⸻

18. Freshness Validation

Evidence and context may become stale.

Example:

Account balance:
₦100,000

retrieved 30 minutes ago.

If the Action depends on the current balance, that evidence may no longer be sufficient.

Validation should therefore distinguish:

Evidence exists

from:

Evidence is sufficiently fresh

⸻

19. Cross-Field Validation

Some validation rules depend on relationships between fields.

Example:

source_account = A
destination_account = B

Validation may require:

A != B

Another example:

amount = 1,000,000
currency = NGN

must satisfy domain-specific monetary rules together.

⸻

20. Cross-Entity Validation

Some rules depend on multiple entities.

Example:

Actor
Resource
Action

may need to satisfy:

Actor owns Resource

or:

Actor manages Resource

or:

Actor is authorized for Resource

These relationships must be explicitly represented.

⸻

21. Validation Result

Validation should produce a structured result rather than a simple boolean.

Conceptually:

ValidationResult {
    valid
    errors
    warnings
    requirements
    evidence
}

For example:

valid = false
errors:
    [
        MISSING_DESTINATION
    ]
requirements:
    [
        DESTINATION_REQUIRED
    ]

⸻

22. Validation States

A useful conceptual result taxonomy is:

VALID
INVALID
INCOMPLETE
UNKNOWN

VALID

All required validation conditions are satisfied.

INVALID

A deterministic rule has been violated.

INCOMPLETE

Required information is missing but potentially recoverable.

UNKNOWN

Validation depends on unavailable external information.

⸻

23. UNKNOWN Must Not Become VALID

This is a foundational invariant.

If Noema cannot establish:

recipient exists

because the relevant system is unavailable, it must not conclude:

recipient exists = true

Instead:

UNKNOWN

and the Intent cannot become READY if that information is mandatory.

⸻

24. Validation Errors

Validation errors should be structured.

Example:

{
    code: "INVALID_AMOUNT",
    field: "amount",
    message: "Amount must be greater than zero"
}

The human-readable message is secondary.

The machine-readable code is canonical.

⸻

25. Validation Warnings

Warnings may identify conditions that do not prevent progression.

Example:

WARNING:
requested execution time is near expiration

Warnings must not silently become blocking conditions.

⸻

26. Validation Requirements

Validation may generate requirements.

Example:

Intent:
Transfer money
Validation:
VALID
Trust:
WAITING_FOR_APPROVAL

The distinction is:

Validation:
the Intent is well formed
Trust:
the Intent requires additional governance before execution

⸻

27. Validation Pipeline

A conceptual validation pipeline is:

Resolved Intent
      ↓
Schema Validation
      ↓
Type Validation
      ↓
Reference Validation
      ↓
Domain Validation
      ↓
Constraint Validation
      ↓
Context Validation
      ↓
Temporal/Freshness Validation
      ↓
Validation Result

The exact ordering may vary where dependencies require it.

⸻

28. Short-Circuiting

Some validation failures are definitive.

Example:

amount = -500

If negative amounts are categorically invalid:

INVALID_AMOUNT

No further validation of downstream execution semantics is necessary.

However, where multiple independent errors are useful, Noema may collect them in one evaluation.

The implementation should optimize for deterministic and useful diagnostics.

⸻

29. Validation and Clarification

If validation discovers missing information that can be supplied by the Actor:

INCOMPLETE

may transition to:

WAITING_FOR_CLARIFICATION

Example:

"Send the invoice."

Validation:

recipient missing

Noema should request clarification.

It should not invent a recipient.

⸻

30. Validation and Blocking

If validation discovers an impossible or prohibited condition:

INVALID

may result in:

BLOCKED

Example:

amount = -₦5,000

There is no useful clarification that can make the current Intent valid without changing the Intent itself.

⸻

31. Validation and Revalidation

Validation is not necessarily one-time.

An Intent may need revalidation when:

Intent changes
context changes
resource changes
policy changes
evidence changes
capability changes
time advances

⸻

32. Validation Dependency Graph

A future implementation may represent validation dependencies explicitly.

Example:

Amount Validation
      │
      └── Currency
Recipient Validation
      │
      └── Customer Registry
Authorization Validation
      │
      ├── Actor
      └── Resource

This allows Noema to selectively revalidate affected predicates.

⸻

33. Validation Provenance

Every validation result should be traceable to:

rule
input
evidence
version
timestamp
result

Example:

Rule:
TRANSFER_AMOUNT_POSITIVE
Input:
amount = -500
Result:
INVALID

This makes validation auditable.

⸻

34. Validation Rule Versioning

Validation rules can evolve.

Therefore a validation result should conceptually identify:

rule_id
rule_version

This is important for reconstructing historical decisions.

⸻

35. Validation and Determinism

Given the same:

Intent
Context
Evidence
Validation Rules
Rule Versions

validation must produce the same result.

Therefore:

Validation(I, X, E, R) = deterministic result

⸻

36. Validation and LLMs

LLMs may assist in producing or normalizing an Intent.

They should not be the authoritative validator for consequential conditions.

The architecture should be:

LLM
 ↓
Candidate Intent
 ↓
Deterministic Validation
 ↓
Trust

not:

LLM
 ↓
"I think this Intent is valid."
 ↓
Execution

⸻

37. Validation and Natural Language

Natural language is inherently flexible.

Validation operates on the canonical Intent representation produced after interpretation.

Example:

User:
"Send John the usual amount."
        ↓
Model interpretation
        ↓
Intent:
{
    action: TRANSFER,
    recipient: JOHN,
    amount: ?
}

Validation detects:

amount = missing

It should not infer the amount unless an explicit deterministic rule or contextual reference establishes it.

⸻

38. Validation and Defaults

Defaults require particular caution.

A default may be applied only when the canonical Intent semantics explicitly permit it.

For example:

currency = NGN

may be a valid deterministic default in a system where the account’s currency is authoritative.

But:

recipient = most_recent_contact

should not be inferred merely because it seems likely.

⸻

39. Validation and Evidence

Validation may consume evidence.

Example:

recipient_id = customer_123

Evidence:

Customer Registry:
customer_123 exists

The validation result can therefore be:

VALID

The evidence should be referenced rather than copied into the validation result unnecessarily.

⸻

40. Validation and Trust Evidence

The same evidence may support both Validation and Trust, but the semantics differ.

Example:

Customer Registry

may establish:

Validation:
recipient exists

while:

Authorization Registry

establishes:

Trust:
Actor may transfer to recipient

⸻

41. Validation and External Systems

External systems may provide authoritative facts.

Noema should distinguish:

Noema-owned validation

from:

External authoritative validation

For example:

Payment provider:
payment exists

Noema may consume that fact without claiming ownership of the provider’s business logic.

⸻

42. Consumer-Side Validation

The execution consumer may perform additional validation.

This is expected.

For example:

Noema:
Intent valid + trusted
Payment Service:
Account balance changed since evaluation

The consumer can reject execution.

This does not mean Noema’s earlier validation was incorrect.

It means:

Business state can change between Trust evaluation and execution.

⸻

43. Validation and Race Conditions

Consequential execution can encounter TOCTOU conditions:

Time T1:
Validation
Time T2:
Trust
Time T3:
Execution

A condition may change between these stages.

Therefore Noema should not assume that validation guarantees execution success.

Where required, execution consumers should perform final authoritative checks.

⸻

44. Validation Contract

Conceptually:

Validate(
    Intent,
    Context,
    Evidence,
    Rules
) → ValidationResult

The result should be deterministic and inspectable.

⸻

45. Validation Result Example

{
    "status": "INCOMPLETE",
    "errors": [],
    "requirements": [
        {
            "code": "DESTINATION_REQUIRED",
            "field": "destination"
        }
    ]
}

This result can drive:

INCOMPLETE
    ↓
WAITING_FOR_CLARIFICATION

⸻

46. Invalid Example

{
    "status": "INVALID",
    "errors": [
        {
            "code": "INVALID_AMOUNT",
            "field": "amount"
        }
    ]
}

The resulting Trust state may be:

BLOCKED

if the invalidity prevents execution.

⸻

47. Unknown Example

{
    "status": "UNKNOWN",
    "requirements": [
        {
            "code": "RECIPIENT_LOOKUP_REQUIRED"
        }
    ]
}

The resulting Trust state should not be READY.

⸻

48. Validation and Trust State Machine

The relationship is:

Intent
  ↓
Validation
  │
  ├── INCOMPLETE → WAITING
  ├── INVALID    → BLOCKED
  ├── UNKNOWN    → WAITING / NOT READY
  └── VALID      → Trust Evaluation
                         │
                         ├── WAITING
                         ├── BLOCKED
                         └── READY

This separation gives Noema a clean semantic boundary.

⸻

49. Validation Does Not Make Decisions About Intent Meaning

Validation must not silently modify the Intent to make it valid.

For example:

Input:
Transfer to John

If there are three Johns:

Validation:
AMBIGUOUS / INCOMPLETE

It must not mutate:

recipient = John_2

because John_2 appears statistically likely.

⸻

50. Validation Does Not Authorize

Validation cannot turn:

"valid transfer"

into:

"authorized transfer"

Authorization remains an independent Trust concern.

⸻

51. Validation Does Not Execute

Validation has no side effects on the target business system.

Its purpose is to determine:

Can this Intent proceed to the next stage?

not:

Perform the Action.

⸻

52. Validation Does Not Guarantee Success

Even:

VALID
+
TRUST = READY

does not guarantee:

EXECUTION = SUCCESS

The external system remains authoritative over actual business-state mutation.

⸻

53. Validation Invariants

Invariant 1

Validation is deterministic.

Invariant 2

Validation operates on canonical Intent semantics.

Invariant 3

Validation must not guess missing information.

Invariant 4

Unknown information must not be treated as valid.

Invariant 5

Validation does not equal authorization.

Invariant 6

Validation does not equal Trust.

Invariant 7

Validation does not execute Actions.

Invariant 8

Validation results must be explainable through structured reasons.

Invariant 9

Validation rules must be versionable.

Invariant 10

Material changes may require revalidation.

Invariant 11

Validation must preserve the distinction between incomplete and invalid.

Invariant 12

Validation must not silently mutate Intent semantics.

Invariant 13

External systems may perform additional authoritative validation.

Invariant 14

A valid Intent may still be blocked by Trust.

⸻

54. Canonical Validation Flow

                Resolved Intent
                       │
                       ▼
              Structural Validation
                       │
                       ▼
                 Type Validation
                       │
                       ▼
               Reference Validation
                       │
                       ▼
                 Domain Validation
                       │
                       ▼
              Constraint Validation
                       │
                       ▼
                Context Validation
                       │
                       ▼
             Temporal / Freshness
                       │
                       ▼
                Validation Result
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    INCOMPLETE       INVALID        VALID
         │             │             │
         ▼             ▼             ▼
      WAITING        BLOCKED     TRUST ENGINE
                                      │
                                      ▼
                              Trust State Machine

⸻

55. The Canonical Distinction

Noema should preserve this chain:

Interpretation
"What might the user mean?"
        ↓
Resolution
"What does the user mean?"
        ↓
Validation
"Is that Intent well-formed and applicable?"
        ↓
Trust
"May that Intent proceed?"
        ↓
Execution
"Perform it."
        ↓
Outcome
"What happened?"

⸻

56. Final Definition

Validation is Noema’s deterministic verification layer for establishing that an Intent is structurally complete, semantically applicable, and consistent with the rules and information required for its next lifecycle transition.

The core invariant is:

Noema does not validate an Intent by believing the Model. It validates the canonical Intent by checking explicit rules, references, constraints, evidence, and context.