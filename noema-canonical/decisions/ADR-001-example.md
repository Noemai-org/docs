ADR-001-example.md

# ADR-001 — Example Architecture Decision Record
Status: Accepted
Date: 2026-09-21
Decision Type: Foundational
Domain: Architecture
Canonical Path: decisions/ADRs/ADR-001-example.md
---
## 1. Context
Noema requires a consistent mechanism for recording architectural decisions that establish or change foundational system behavior.
The Canon defines the principles and boundaries of Noema.
Specifications define precise semantics and contracts.
Architecture documents describe how those semantics are realized.
Architecture Decision Records (ADRs) preserve the reasoning behind significant decisions so that future changes can be evaluated against the decisions that established the current architecture.
Without explicit decision records, architectural intent can become implicit, fragmented across implementation artifacts, or reconstructed incorrectly after the fact.
The ADR system therefore needs a canonical example that establishes the expected structure and level of detail for subsequent ADRs.
---
## 2. Decision
Noema will use Architecture Decision Records as the canonical historical record for significant architectural decisions.
Each ADR should explicitly identify:
- the decision being made
- the context that required the decision
- the problem or architectural tension
- the options considered
- the selected approach
- the consequences
- the relationship to Noema's canonical principles
- affected specifications or architectural areas
- relevant follow-up work
ADRs are explanatory and historical.
They do not replace the Canon or normative specifications.
The current architecture is determined by the active Canon and applicable specifications. ADRs explain why significant architectural decisions were made and provide traceability for those decisions.
---
## 3. ADR Scope
An ADR should be created when a decision materially affects:
- a foundational architectural boundary
- the semantics of a core Noema concept
- authority or ownership boundaries
- Trust or execution behavior
- state-machine semantics
- execution contracts
- provenance or auditability
- autonomy boundaries
- interaction with authoritative external systems
- another decision whose consequences are sufficiently significant to require historical traceability
Not every implementation choice requires an ADR.
Routine implementation details should remain in the appropriate specification or implementation documentation.
---
## 4. Decision Record Structure
A canonical ADR should generally contain:
1. Title
2. Status
3. Date
4. Decision Type
5. Domain
6. Context
7. Decision
8. Alternatives Considered
9. Consequences
10. Architectural Implications
11. Related Canonical Documents
12. Follow-Up Requirements
The exact sections may evolve, but the record must preserve enough information to reconstruct the decision.
---
## 5. Alternatives Considered
### Alternative A — Record decisions only in implementation documentation
Rejected.
Implementation documentation describes how the system currently works but does not reliably preserve why a foundational architectural choice was made.
### Alternative B — Record all decisions only in the Canon
Rejected.
The Canon is normative and foundational. It should not become a chronological collection of every architectural discussion or implementation decision.
### Alternative C — Use separate ADRs for significant architectural decisions
Accepted.
This preserves a clear distinction between:
```text
Canon
  ↓
Foundational principles
Specifications
  ↓
Precise semantics and contracts
Architecture
  ↓
Current architectural realization
ADRs
  ↓
Reasoning and historical decision record

⸻

6. Consequences

Positive Consequences

ADRs provide:

* architectural traceability
* explicit decision history
* preservation of design rationale
* easier review of future changes
* clearer relationships between principles and implementation
* protection against accidental architectural drift
* a mechanism for documenting rejected alternatives
* a historical record of how Noema evolved

Negative Consequences

ADRs introduce additional documentation work.

They also create a maintenance requirement: when a foundational decision changes, affected ADRs, specifications, and architectural documents may need to be related or superseded appropriately.

This cost is accepted because architectural decisions without preserved rationale become difficult to reconstruct reliably.

⸻

7. ADRs and the Canon

The relationship between ADRs and the Canon is:

                 Canon
                   │
          defines foundational
             principles
                   │
                   ▼
             Specifications
                   │
          define precise semantics
                   │
                   ▼
             Architecture
                   │
       realizes those semantics
                   │
                   ▼
                 ADRs
                   │
       preserve decision rationale

This diagram represents document responsibility, not a strict dependency direction.

An ADR may explain a decision that established a Canon principle, changed a specification, or altered the architecture.

However, an ADR does not automatically become normative merely because it exists.

⸻

8. ADRs and Canonical Authority

The existence of an ADR does not grant the ADR authority over the current system.

Where an ADR conflicts with a later accepted Canon or specification, the current canonical document governs.

The ADR remains historically useful because it records the decision that existed at the time it was made.

A subsequent change should therefore be explicit rather than silently modifying historical reasoning.

⸻

9. Superseding Decisions

When a foundational decision changes, the existing ADR should remain historically intact.

A new ADR should document the new decision.

The relationship should be explicit:

ADR-001
   │
   │ superseded by
   ▼
ADR-XXX

The new ADR should explain:

* what changed
* why it changed
* what previous decision is affected
* which specifications are affected
* which architectural components are affected
* whether migration is required

Historical decisions should not be rewritten merely to make the repository appear internally consistent.

⸻

10. Decision Status

ADR status should communicate the current lifecycle of the decision.

Conceptual statuses include:

* Proposed
* Accepted
* Superseded
* Deprecated
* Rejected

An accepted ADR represents a decision that was adopted.

A superseded ADR remains part of the historical record but no longer represents the current architectural decision.

⸻

11. Relationship to the Noema Principles

The ADR system reinforces several foundational Noema principles.

Explicit State

Architectural decisions should be represented explicitly rather than inferred from implementation behavior.

Provenance

Significant decisions should have a traceable record.

Determinism

Current architectural behavior should be governed by explicit canonical definitions rather than undocumented historical assumptions.

Separation of Concerns

The Canon, specifications, architecture, and decision records should retain distinct responsibilities.

Controlled Evolution

The architecture must be capable of changing without destroying the history of why previous decisions existed.

⸻

12. Decision Record Invariants

The ADR system follows these invariants:

1. Significant architectural decisions should be explicitly recorded.
2. ADRs preserve decision rationale and history.
3. ADRs do not replace the Canon.
4. ADRs do not replace normative specifications.
5. Historical ADRs should not be silently rewritten when decisions change.
6. Superseding decisions should be represented explicitly.
7. Rejected alternatives should be recorded when they materially explain the decision.
8. Significant architectural consequences should be documented.
9. ADR references should remain traceable to affected canonical documents.
10. The repository should distinguish current authority from historical rationale.

⸻

13. Relationship to Existing Noema ADRs

The ADR collection establishes specific foundational decisions across Noema.

Examples include:

* ADR-003-probabilistic-deterministic-boundary.md
* ADR-004-deterministic-trust-evaluation.md
* ADR-005-explicit-execution-contracts.md
* ADR-006-capability-permission-separation.md
* ADR-007-enterprise-systems-remain-authoritative.md
* ADR-008-clarification-over-guessing.md
* ADR-009-*
* ADR-010-trust-state-machine.md
* ADR-011-intent-state-separate-from-execution-state.md
* ADR-012-provenance-and-auditability.md
* ADR-013-bounded-autonomy.md
* ADR-014-human-intervention-as-explicit-state.md
* ADR-015-fail-closed-on-unknown.md
* ADR-016-consumer-side-authoritative-validation.md
* ADR-017-outcome-separate-from-trust.md
* ADR-018-canonical-repository-authority.md

These decisions collectively establish important boundaries between:

Intent
   ↓
Resolution
   ↓
Validation
   ↓
Trust
   ↓
Execution Contract
   ↓
Execution
   ↓
Outcome

ADR-001 establishes the mechanism by which such architectural decisions are preserved and evolved.

⸻

14. Architectural Implication

The repository must treat decision records as first-class architectural artifacts.

A significant architectural change should therefore be evaluated for whether it requires:

* a new ADR
* an update to an existing specification
* an update to the Canon
* an architectural document change
* migration documentation
* implementation changes

A code change alone is insufficient when the underlying architectural decision has changed.

⸻

15. Follow-Up Requirements

The repository should maintain:

1. A consistent ADR naming convention.
2. Sequential ADR identifiers.
3. Explicit ADR status.
4. Cross-references between related ADRs.
5. References from ADRs to affected canonical specifications where appropriate.
6. Supersession relationships when decisions change.
7. Preservation of historical ADR content.

⸻

16. Final Decision

Noema will maintain Architecture Decision Records as the canonical historical mechanism for documenting significant architectural decisions.

The ADR collection exists to preserve:

Context
   ↓
Alternatives
   ↓
Decision
   ↓
Consequences
   ↓
Architectural History

The Canon defines what Noema currently holds to be foundational.

Specifications define precise normative semantics.

Architecture documents describe the current architectural realization.

ADRs preserve why significant architectural decisions were made and how those decisions evolved.

The repository must preserve these distinctions.

⸻

17. Canonical Principle

The resulting principle is:

Noema’s significant architectural decisions must be explicit, traceable, historically preserved, and distinguishable from the current normative Canon and specifications.

