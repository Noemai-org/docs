> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

ADR-001: Intent as a First-Class Object

Status: Accepted
Version: 0.1
Decision Type: Foundational
Domain: Intent
Canonical Path: decisions/ADRs/ADR-001-intent-as-first-class-object.md

⸻

1. Context

Noema exists to establish a reliable boundary between human intent and executable actions across existing software systems.

Human intent is initially expressed through natural language or another human-facing interface. That expression is not, by itself, an executable representation.

If intent remains embedded in conversational text, application-specific workflows, or transient model output, Noema cannot reliably:

* represent what the Actor is trying to accomplish
* distinguish resolved meaning from unresolved ambiguity
* validate the resulting semantics
* attach evidence and context
* evaluate Trust deterministically
* apply constraints and policy
* establish authorization
* select an executable capability
* construct an Execution Contract
* maintain lifecycle state
* preserve provenance
* audit decisions
* re-evaluate the Intent when relevant conditions change

The Noema Canon therefore requires a canonical representation of Intent that exists independently of the interface through which the Actor expressed it.

⸻

2. Decision

Intent is a first-class canonical object in Noema.

An Intent represents the Actor’s desired objective together with the semantic information required to reason about that objective throughout its lifecycle.

Conceptually, an Intent may contain:

Intent
├── actor
├── objective
├── subject
├── context
├── constraints
├── desired outcome
├── required capabilities
├── provenance
└── state

The precise representation is defined by the canonical Intent and Ontology specifications.

Natural-language expression is therefore treated as an input to Intent interpretation and resolution, rather than as the canonical representation itself.

The canonical progression is:

Human Expression
       ↓
Interpretation
       ↓
Intent Resolution
       ↓
Canonical Intent
       ↓
Validation
       ↓
Trust
       ↓
Action
       ↓
Outcome

⸻

3. Rationale

Making Intent a first-class object establishes a stable semantic layer between human expression and software execution.

It allows Noema to preserve the distinction between:

What the Actor said
        ↓
What Noema believes the Actor means
        ↓
What has been validated
        ↓
What Noema trusts
        ↓
What may be executed
        ↓
What actually happened

This distinction is foundational to Noema’s architecture.

A canonical Intent can persist across clarification, validation, Trust evaluation, execution, re-evaluation, and outcome recording.

It can therefore serve as the stable referent for the Noema lifecycle rather than requiring every subsystem to reinterpret the original human expression.

⸻

4. Alternatives Considered

4.1 Treat natural-language expression as the Intent

Rejected.

Natural language is an input representation and may contain ambiguity, omissions, contextual references, or unresolved entities.

It is not sufficiently structured to serve as the canonical object governing execution.

⸻

4.2 Treat the LLM’s output as the Intent

Rejected.

Model output is probabilistic and may change between evaluations.

LLM output may be used to propose or construct a candidate Intent, but it cannot itself constitute the authoritative canonical Intent representation.

The canonical boundary remains:

LLM
 ↓
Candidate Intent
 ↓
Deterministic Validation
 ↓
Trust

⸻

4.3 Encode Intent separately inside each application

Rejected.

Application-specific representations would prevent Noema from establishing a consistent intent-to-action abstraction across systems.

They would also cause intent semantics to become coupled to individual application interfaces.

Noema instead requires a canonical semantic representation that can be mapped to capabilities exposed by different systems.

⸻

4.4 Treat Intent as temporary execution metadata

Rejected.

Intent persists beyond the immediate execution decision.

It may require:

* clarification
* additional evidence
* approval
* authorization changes
* policy re-evaluation
* capability changes
* execution
* outcome recording
* audit
* historical reconstruction

Therefore Intent must exist as a durable semantic object rather than transient execution metadata.

⸻

5. Consequences

5.1 Positive Consequences

Making Intent first-class provides a common semantic object for:

* interpretation
* resolution
* validation
* Trust evaluation
* action selection
* execution planning
* execution contracts
* provenance
* state management
* re-evaluation
* outcome correlation

It also allows Noema to remain independent of the presentation layer.

The same canonical Intent model can originate from:

Chat
Voice
API
Embedded UI
Workflow
Agent
Automation

without changing the fundamental Noema abstraction.

⸻

5.2 Negative Consequences

A first-class Intent introduces additional modeling requirements.

Noema must define and maintain:

* Intent schemas
* semantic fields
* lifecycle states
* provenance
* versioning
* validation rules
* state transitions
* relationships between Intent and Actions
* relationships between Intent and execution records

The canonical Intent representation also becomes an important compatibility boundary. Changes to it therefore require deliberate governance.

⸻

6. Architectural Boundaries

This decision establishes several boundaries.

Intent vs Expression

Expression
    ≠
Intent

Expression is how the Actor communicates.

Intent is the canonical semantic representation derived from that communication.

Intent vs Action

Intent
    ≠
Action

Intent represents the desired objective.

Action represents an executable operation selected to fulfill that objective.

Intent vs Trust

Intent
    ≠
Trust

An Intent may be valid without being trusted for execution.

Intent vs Business State

Intent State
    ≠
Business State

Noema owns Intent state.

The authoritative system owns the relevant business state.

Intent vs Outcome

Intent
    ≠
Outcome

An Intent expresses what the Actor sought to accomplish.

The Outcome records what actually happened.

⸻

7. Lifecycle Implications

Because Intent is a first-class object, its lifecycle must be independently representable.

A conceptual progression is:

Created
   ↓
Resolving
   ↓
Resolved
   ↓
Validated
   ↓
Trusted
   ↓
Planned
   ↓
Contracted
   ↓
Executing
   ↓
Completed / Failed

This does not imply that Intent lifecycle state and Trust state or Execution state must be represented by one enum.

Those concerns remain conceptually distinct.

For example:

Intent State:
RESOLVED
Trust State:
WAITING_FOR_APPROVAL

or:

Intent State:
EXECUTING
Execution State:
EXECUTING

The precise state architecture is defined by the relevant canonical specifications.

⸻

8. Clarification Implications

Because Intent is first-class, unresolved meaning must be represented explicitly.

For example:

User:
"Send the report to John."
Resolved Intent:
recipient = ?

If multiple possible recipients exist, Noema must not silently select one.

The Intent may instead remain unresolved or incomplete and transition into a clarification state.

Intent
   ↓
Ambiguity detected
   ↓
Clarification required
   ↓
Additional information
   ↓
Intent updated
   ↓
Re-validation / Trust evaluation

Clarification therefore modifies the canonical Intent rather than merely changing the conversational response.

⸻

9. Provenance Implications

A first-class Intent must preserve sufficient provenance to establish how it was formed and subsequently changed.

Relevant provenance may include:

* originating expression
* interpretation event
* resolution event
* contextual inputs
* evidence references
* Intent version
* timestamps
* Actor
* system or model involved in interpretation
* clarification events
* material changes

This does not require storing private model reasoning or chain-of-thought.

It requires enough information to reconstruct the semantic lifecycle and material decisions.

⸻

10. Re-evaluation Implications

A first-class Intent must be capable of being re-evaluated when material conditions change.

Examples include:

Intent updated
Evidence changed
Authorization changed
Policy changed
Capability changed
Context changed
Constraint changed
Time-dependent condition expired

The Intent remains the stable object against which those evaluations occur.

This supports the canonical principle that Trust is a lifecycle rather than a one-time boolean decision.

⸻

11. Canonical Impact

This decision establishes the following foundational principle:

Human language is an input to Intent resolution; Intent itself is a structured canonical object that persists independently of the presentation layer.

This principle affects the:

* Intent ontology
* Intent specification
* Validation layer
* Trust Engine
* Trust State Machine
* Execution Planner
* Action Graph
* Execution Contract
* Execution Record
* Outcome Engine
* Operational Memory
* provenance model

Any future design that treats raw model output, conversational text, or an application-specific request object as the authoritative representation of Intent should be evaluated against this decision.

⸻

12. Affected Specifications

At minimum, this decision affects:

ontology/
intent/
trust/
ai/
architecture/

The precise affected files should be maintained as the repository evolves.

⸻

13. Related Decisions

* ADR-002 — Noema Owns Intent State, Not Business State
* ADR-003 — Probabilistic / Deterministic Boundary
* ADR-008 — Clarification Over Guessing
* ADR-009 — Validation Separate From Trust
* ADR-011 — Intent State Separate From Execution State
* ADR-012 — Provenance and Auditability

⸻

14. Supersedes

None.

⸻

15. Superseded By

None.

⸻

16. Decision Invariant

The canonical invariant established by this ADR is:

Noema must represent the Actor’s resolved objective as a structured Intent object rather than treating natural-language expression or probabilistic model output as the authoritative representation of that objective.