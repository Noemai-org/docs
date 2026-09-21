ADR-003 — Probabilistic / Deterministic Boundary

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational
Domain: AI / Trust / Architecture
Canonical Path: decisions/ADRs/ADR-003-probabilistic-deterministic-boundary.md

⸻

1. Decision

Noema will establish an explicit architectural boundary between probabilistic AI inference and deterministic system authority.

Probabilistic models may interpret, infer, retrieve, propose, classify, plan, and generate candidate representations of human intent.

They must not, by their own confidence or output, establish authorization to execute consequential Actions.

The canonical boundary is:

Human Expression
       ↓
AI / Probabilistic Processing
       ↓
Candidate Intent
       ↓
Canonical Intent
       ↓
Deterministic Validation
       ↓
Deterministic Trust Evaluation
       ↓
Execution Eligibility
       ↓
Action Contract
       ↓
Execution

The fundamental rule is:

Probabilistic inference may propose what should happen; deterministic Noema mechanisms establish whether it may happen.

⸻

2. Context

Noema is designed to convert human intent expressed through natural language and other interfaces into executable Actions across existing software systems.

AI models are useful because human intent is frequently:

* expressed in natural language
* incomplete
* contextual
* ambiguous
* implicit
* distributed across multiple turns
* dependent on external information

These characteristics make probabilistic models valuable for interpretation and reasoning.

However, the same characteristics make model output unsuitable as the sole authority for consequential execution.

A model can produce a highly plausible interpretation that is nevertheless incorrect.

A model can also produce different outputs for materially equivalent inputs because of:

* model version changes
* sampling
* prompt changes
* retrieved context
* tool results
* conversation history
* model uncertainty
* implementation differences

Noema therefore requires a boundary at which probabilistic output becomes subject to deterministic system rules.

Without such a boundary, the system risks allowing model judgment to become implicit authority.

⸻

3. Problem

A conventional agentic architecture can collapse the following concepts:

Model believes X
        ↓
Model proposes X
        ↓
System accepts X
        ↓
Action occurs

This makes the model’s probabilistic inference functionally equivalent to authorization.

That is incompatible with Noema’s intended authority model.

In particular, the following must remain distinct:

* model confidence
* intent interpretation
* intent validity
* authorization
* policy compliance
* capability
* trust
* execution eligibility
* execution outcome

A model saying:

“The user probably wants this.”

must never be equivalent to:

“Noema has established that this Action is authorized and executable.”

⸻

4. Architectural Principle

Noema adopts the following principle:

Probability may inform.
Determinism must govern.

More precisely:

Probabilistic mechanisms may

* interpret natural language
* extract candidate entities
* identify candidate Actions
* resolve references provisionally
* retrieve potentially relevant information
* propose contextual relationships
* generate clarification questions
* propose execution plans
* rank candidate capabilities
* generate candidate Action Contracts
* assist human operators

Deterministic mechanisms must establish

* canonical Intent validity
* required-field satisfaction
* explicit constraints
* applicable policy
* authorization
* capability requirements
* mandatory approvals
* execution eligibility
* Trust state
* execution boundary conditions

The model may participate throughout the lifecycle, but its output does not become authority merely because it is highly confident.

⸻

5. The Boundary

The canonical architecture is:

                    PROBABILISTIC DOMAIN
┌─────────────────────────────────────────────────┐
│                                                 │
│  Natural Language / Other Human Expression      │
│                     ↓                           │
│              AI Interpretation                  │
│                     ↓                           │
│             Candidate Intent                    │
│                     ↓                           │
│             Context Retrieval                   │
│                     ↓                           │
│             Candidate Planning                  │
│                                                 │
└─────────────────────┬───────────────────────────┘
                      │
                      │ canonicalization /
                      │ deterministic evaluation
                      ▼
═══════════════════════════════════════════════════
        PROBABILISTIC / DETERMINISTIC BOUNDARY
═══════════════════════════════════════════════════
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│              DETERMINISTIC DOMAIN               │
│                                                 │
│  Canonical Intent                               │
│       ↓                                         │
│  Validation                                     │
│       ↓                                         │
│  Authorization                                  │
│       ↓                                         │
│  Policy                                         │
│       ↓                                         │
│  Constraints                                    │
│       ↓                                         │
│  Capability                                     │
│       ↓                                         │
│  Trust Evaluation                               │
│       ↓                                         │
│  Execution Eligibility                          │
│       ↓                                         │
│  Action Contract                                │
│       ↓                                         │
│  Execution Boundary                             │
│                                                 │
└─────────────────────┬───────────────────────────┘
                      │
                      ▼
              Existing Systems

The exact implementation may distribute these responsibilities across services, but the semantic boundary must remain intact.

⸻

6. Candidate Intent vs Canonical Intent

AI-generated output should initially be treated as a candidate representation.

For example:

User:
"Send John the usual amount."

A model may propose:

Action:
TRANSFER
Recipient:
John
Amount:
UNKNOWN

This is useful model output.

It is not yet an executable Intent.

Noema must establish the canonical representation through deterministic processing and, where necessary, clarification.

If multiple Johns exist, Noema must not select one merely because the model considers one more probable.

The resulting state may instead be:

WAITING_FOR_CLARIFICATION

The canonical Intent is therefore the object that has passed through the required semantic and structural controls, not simply the first structured object emitted by a model.

⸻

7. Model Confidence Is Not Authority

Noema must not use a model confidence score as a substitute for Trust.

For example:

Model confidence = 0.99

does not imply:

Trust = READY

Likewise:

Model confidence = 0.70

does not necessarily imply:

Trust = BLOCKED

Confidence can be relevant evidence for deciding whether clarification or additional processing may be useful, but it cannot independently determine execution eligibility.

The Trust Engine evaluates explicit conditions.

⸻

8. Deterministic Validation

Before Trust evaluation, the canonical Intent must be validated.

Validation establishes properties such as:

* required fields
* types
* references
* domain constraints
* cross-field relationships
* contextual applicability
* temporal validity
* freshness requirements

Conceptually:

Candidate Intent
       ↓
Canonical Intent
       ↓
Validation
       ↓
VALID / INCOMPLETE / INVALID / UNKNOWN

Validation does not authorize execution.

A valid Intent may still be:

VALID
   ↓
Trust
   ↓
WAITING_FOR_APPROVAL

or:

VALID
   ↓
Trust
   ↓
BLOCKED

⸻

9. Deterministic Trust

Trust is the principal control boundary between understanding and execution.

The Trust Engine evaluates explicit conditions such as:

Intent validity
+
Evidence
+
Authorization
+
Policy
+
Risk controls
+
Capability
+
Constraints
+
Context
+
Freshness

and produces a defined Trust state.

For example:

UNRESOLVED
EVALUATING
WAITING
BLOCKED
READY

The exact state semantics are defined by the Trust State Machine.

The critical invariant is:

Noema must not transition an Intent to READY merely because an AI model considers the Action safe, likely, or appropriate.

⸻

10. Action Contracts

Even after Trust establishes execution eligibility, execution must occur through an explicit Action Contract.

The model does not directly invoke an arbitrary external operation.

The canonical sequence is:

Trusted Intent
      ↓
Action Selection
      ↓
Action Contract
      ↓
Consumer Acceptance
      ↓
Execution

The Action Contract establishes the executable boundary.

Depending on the Action, it may define:

* Action identity
* target
* inputs
* capability
* authorization requirements
* preconditions
* constraints
* expected effects
* postconditions
* failure semantics
* idempotency
* audit requirements

This prevents free-form model output from becoming an implicit execution API.

⸻

11. Planning Is Not Authorization

AI planning may produce a proposed sequence of Actions.

For example:

1. Retrieve customer
2. Check card status
3. Create replacement
4. Notify customer

The plan itself does not authorize those operations.

Each consequential Action remains subject to the applicable deterministic controls.

Therefore:

Plan
  ≠
Trust

and:

Plan
  ≠
Authorization

Planning may propose the route.

Noema’s deterministic control layer establishes whether the proposed route may be executed.

⸻

12. Capability Is Not Permission

The probabilistic/deterministic boundary also preserves the distinction between capability and authority.

A model may discover that a system exposes:

refund_payment()

That establishes neither:

the actor is authorized

nor:

the current Intent is trusted

The distinctions remain:

Capability
"Can the system perform this operation?"
Authorization
"May this actor cause this operation?"
Trust
"Has Noema established sufficient grounds for this Intent to cross the execution boundary?"

⸻

13. External Systems Remain Authoritative

The deterministic boundary does not make Noema the owner of every business rule or business state.

Existing systems remain authoritative for their domains.

For example:

Payment System
    → payment state
CRM
    → customer state
Identity Provider
    → identity state
Banking System
    → account state

Noema consumes authoritative information through explicit interfaces and uses it in validation and Trust evaluation.

The model must not be permitted to substitute an inferred fact for an authoritative external fact when the latter is required.

⸻

14. Unknown Must Remain Unknown

The boundary requires explicit treatment of unavailable information.

For example:

Authorization Service
        ↓
     unavailable

Noema must not transform:

UNKNOWN

into:

AUTHORIZED

because the model believes authorization is likely.

Likewise:

Recipient lookup unavailable

must not become:

Recipient exists

through probabilistic inference.

Where the information is mandatory for execution, the Intent must remain non-executable until the condition is established.

⸻

15. Fail-Closed Behavior

For consequential Actions, uncertainty at the deterministic boundary must fail closed.

Conceptually:

Required deterministic condition
          ↓
       UNKNOWN
          ↓
     EVALUATING
          ↓
 WAITING / BLOCKED

Never:

UNKNOWN
   ↓
READY

This applies particularly to:

* authorization
* mandatory policy checks
* identity
* required evidence
* critical constraints
* required capabilities
* execution preconditions

⸻

16. Re-Evaluation

Deterministic authority must remain sensitive to material changes.

A model may have correctly interpreted an Intent at time T1, while the conditions governing execution change at T2.

Examples:

T1: Authorization valid
T2: Authorization revoked

or:

T1: Policy permits execution
T2: Policy changes

or:

T1: Evidence fresh
T2: Evidence expires

Therefore:

READY
  ↓
material change
  ↓
EVALUATING
  ↓
WAITING / BLOCKED / READY

A previous model output does not preserve Trust indefinitely.

⸻

17. Model Version Changes

A model version change must not silently redefine deterministic authority.

For example:

Model v1 → Candidate Intent A
Model v2 → Candidate Intent B

Noema may legitimately obtain different interpretations.

However, each resulting Intent must pass through the same applicable deterministic controls.

The architecture therefore separates:

Model behavior

from:

Trust authority

This permits AI components to evolve without making model-version changes equivalent to changes in execution authority.

⸻

18. Prompt Changes

Prompt modifications must likewise not bypass deterministic controls.

A changed prompt may alter:

* interpretation
* extraction
* planning
* clarification behavior
* candidate Action selection

But it must not alter the fundamental requirement that consequential Actions pass through validation, Trust, and the execution boundary.

Therefore:

Prompt change
     ↓
Potentially different candidate
     ↓
Same canonical controls

⸻

19. AI May Assist Deterministic Systems

The decision does not prohibit AI from assisting deterministic mechanisms.

AI may be used to:

* identify potentially relevant policies
* propose evidence
* identify candidate constraints
* suggest validation rules for human review
* classify context
* propose clarification questions
* summarize evidence
* identify possible dependencies
* propose candidate Action Contracts

However, where a condition is consequential, the authoritative determination must come from an explicit deterministic rule, authoritative external fact, approved policy, or other defined control.

The distinction is:

AI-assisted determination

versus:

AI-authoritative determination

Noema permits the former where appropriate and prohibits the latter as the basis for consequential execution.

⸻

20. Auditability

The boundary must be reconstructible after execution.

Noema should be able to determine:

* which model produced the candidate Intent
* which model/version was used
* what canonical Intent was established
* which validation rules were applied
* which evidence was used
* which policies were applicable
* which authorization state was established
* which Trust evaluation occurred
* which Action Contract was produced
* which execution consumer accepted it
* what outcome was reported

This does not require storing hidden chain-of-thought.

The requirement is decision and execution provenance.

⸻

21. Security Implications

The boundary reduces the risk that probabilistic model behavior becomes an implicit privilege-escalation mechanism.

A model should not be able to establish authority by:

* asserting that authorization exists
* inventing missing evidence
* overriding policy
* interpreting capability as permission
* converting ambiguity into certainty
* modifying constraints
* declaring an Action safe
* declaring itself authorized
* bypassing required approvals

The deterministic layer must remain authoritative over these conditions.

⸻

22. Consequences

Positive consequences

This decision provides:

* separation of AI interpretation from execution authority
* deterministic Trust evaluation
* explicit execution boundaries
* model-provider and model-version flexibility
* improved auditability
* clearer security boundaries
* safer handling of uncertainty
* explicit treatment of ambiguity
* easier policy enforcement
* clearer responsibility between Noema and external systems
* compatibility with bounded autonomy

Costs

This decision also introduces:

* additional architectural components
* additional state transitions
* validation and Trust infrastructure
* policy and authorization integration requirements
* additional latency in some workflows
* more explicit contracts between components
* greater implementation complexity than direct agentic execution

These costs are accepted because the architecture is intended for consequential intent-to-action workflows where implicit authority is unacceptable.

⸻

23. Rejected Alternatives

Alternative A — Model confidence determines execution

confidence > threshold
        ↓
execute

Rejected.

Confidence does not establish authorization, policy compliance, capability, or current business-state validity.

⸻

Alternative B — LLM decides whether an Action is safe

LLM
 ↓
"This action is safe."
 ↓
execute

Rejected.

Safety and execution eligibility must be established through explicit controls.

⸻

Alternative C — Deterministic controls only after execution

LLM
 ↓
execute
 ↓
validate

Rejected.

Consequential controls must exist before the execution boundary.

⸻

Alternative D — Treat the entire system as deterministic

Rejected.

Natural-language interpretation and many forms of context acquisition are inherently probabilistic or uncertain.

Noema should not pretend otherwise.

Instead, it should explicitly contain and control the probabilistic portions of the system.

⸻

Alternative E — Eliminate AI from the execution lifecycle

Rejected.

AI is valuable for interpretation, contextualization, planning, retrieval, and interaction.

The decision is not to remove AI.

It is to prevent AI inference from becoming implicit execution authority.

⸻

24. Relationship to Other Canonical Concepts

This ADR establishes a foundational relationship among several Noema concepts.

Intent

Defines what the Actor intends.

Validation

Determines whether the canonical Intent is structurally and semantically valid for progression.

Trust

Determines whether the Intent satisfies the conditions required to cross the execution boundary.

Capability

Defines what an external system can perform.

Authorization

Defines what the Actor or principal is permitted to cause.

Action Contract

Defines the explicit executable operation.

Execution

Occurs only after the required controls and contract boundary have been satisfied.

The resulting chain is:

Interpretation
      ↓
Resolution
      ↓
Canonical Intent
      ↓
Validation
      ↓
Trust
      ↓
Execution Eligibility
      ↓
Action Contract
      ↓
Execution
      ↓
Outcome

⸻

25. Invariants

The following invariants follow from this decision.

Invariant 1

Probabilistic model output is not execution authority.

Invariant 2

Model confidence is not Trust.

Invariant 3

A candidate Intent is not necessarily a canonical Intent.

Invariant 4

Canonical Intent must pass deterministic validation before consequential execution.

Invariant 5

Unknown mandatory conditions cannot produce READY.

Invariant 6

Authorization cannot be inferred solely from model output.

Invariant 7

Capability cannot be interpreted as permission.

Invariant 8

Planning cannot authorize execution.

Invariant 9

A model cannot override deterministic policy or authorization controls.

Invariant 10

Material changes require applicable re-evaluation.

Invariant 11

Execution must occur through an explicit Action Contract or equivalent execution boundary.

Invariant 12

Deterministic decisions must be reconstructible from their relevant inputs, rules, evidence, and versions.

Invariant 13

The probabilistic portion of Noema may evolve without silently redefining the deterministic authority model.

Invariant 14

Consequential uncertainty must fail closed.

⸻

26. Canonical Mental Model

The decision can be reduced to:

AI asks:
"What might the human mean?"
Noema establishes:
"What does the canonical Intent represent?"
Validation establishes:
"Is that Intent valid?"
Trust establishes:
"May it proceed?"
The Action Contract establishes:
"What exactly may be executed?"
The consumer establishes:
"What actually happened?"

Therefore:

             PROBABILISTIC
                  │
                  ▼
           Candidate Meaning
                  │
                  ▼
          Canonical Intent
════════════════════════════════
   PROBABILISTIC / DETERMINISTIC
          BOUNDARY
════════════════════════════════
                  │
                  ▼
             Validation
                  │
                  ▼
               Trust
                  │
                  ▼
          Action Contract
                  │
                  ▼
              Execution
                  │
                  ▼
               Outcome

⸻

27. Final Decision Statement

Noema will explicitly separate probabilistic intelligence from deterministic authority.

AI models may interpret and propose.

Deterministic Noema mechanisms must validate, establish Trust, enforce authority and policy, and control access to execution.

The foundational rule is:

Noema does not execute because a model is confident. Noema executes when the canonical Intent satisfies the deterministic conditions required to cross the execution boundary.