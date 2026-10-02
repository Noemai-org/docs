> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

ADR-018 — Canonical Repository Authority

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational
Domain: Governance / Repository / Architecture
Canonical Path: decisions/ADR/ADR-018-canonical-repository-authority.md

⸻

1. Decision

The Noema canonical repository SHALL be the authoritative repository for the currently accepted definitions, principles, specifications, architectural boundaries, contracts, and invariants that constitute Noema.

The repository is the canonical representation of the current Noema system.

However, not every file in the repository has equal authority.

Authority SHALL be determined by the repository’s canonical document hierarchy and the status of each artifact.

The canonical hierarchy is:

Canon
   ↓
Specification
   ↓
Architecture
   ↓
Decision Records
   ↓
Reference Workflows
   ↓
Research
   ↓
Strategy

This hierarchy describes semantic authority, not implementation dependency or document importance.

⸻

2. Context

Noema is a system composed of multiple conceptual and implementation layers.

As the repository grows, it will contain:

* foundational principles
* terminology
* ontology
* lifecycle definitions
* state machines
* technical specifications
* architectural descriptions
* contracts
* implementation decisions
* workflows
* experiments
* research
* commercial strategy

Without an explicit authority model, these artifacts can begin to conflict.

For example:

Research document:
"Trust could be probabilistic."
Canon:
"Trust is deterministic."

The research document may contain a valuable hypothesis, but it does not silently modify the Canon.

Likewise:

Architecture:
"Component X currently implements Trust as..."

does not automatically redefine the canonical meaning of Trust.

Noema therefore requires an explicit repository authority model.

⸻

3. Problem

A repository containing many documents can develop semantic drift when contributors cannot determine which document governs a disputed concept.

Typical sources of conflict include:

* research findings
* implementation behavior
* outdated specifications
* architectural shortcuts
* experimental workflows
* product requirements
* historical ADRs
* informal documentation
* generated documentation

Without a canonical authority boundary, the repository can become internally inconsistent.

The system then risks having multiple definitions of the same concept.

For example:

Document A:
Intent = user request
Document B:
Intent = structured objective
Document C:
Intent = executable action
Document D:
Intent = conversation state

Noema cannot maintain reliable architecture if foundational terminology is allowed to drift in this manner.

⸻

4. Repository Authority

The canonical repository SHALL establish the current authoritative model of Noema.

This means that accepted canonical documents define:

* what Noema is
* what Noema owns
* what Noema does not own
* what core concepts mean
* what boundaries exist
* what invariants must hold
* what contracts are normative
* what lifecycle semantics apply

Implementation code does not automatically override canonical definitions.

If implementation and Canon disagree, the discrepancy must be treated as an architectural or implementation defect unless the Canon is deliberately changed through the appropriate governance process.

⸻

5. Canonical Document Classes

Noema SHALL distinguish repository artifacts by authority class.

5.1 Canon

Canon defines foundational truths and principles.

Canon answers:

What does Noema fundamentally mean and stand for?

Examples:

CANON.md
ontology/*
trust/*

where those documents are explicitly designated as foundational canonical definitions.

Canon has the highest semantic authority.

⸻

5.2 Specification

Specifications define precise semantics derived from the Canon.

A specification may define:

* schemas
* state machines
* contracts
* interfaces
* validation rules
* protocol semantics
* required behaviors

Specifications answer:

What precisely must the system mean or do?

A specification cannot silently contradict the Canon.

⸻

5.3 Architecture

Architecture describes how the current system realizes the specifications.

Architecture answers:

How is Noema currently organized to implement the canonical system?

Architecture may evolve without necessarily changing the foundational principles.

An architectural implementation constraint must not silently become a canonical principle.

⸻

5.4 Architecture Decision Records

ADRs document significant decisions about the architecture and system.

An ADR answers:

Why was this important decision made?

An ADR records the rationale and consequences of a decision.

A later accepted ADR may supersede an earlier ADR where explicitly stated.

Historical ADRs remain part of the decision history even after being superseded.

⸻

5.5 Reference Workflows

Reference workflows demonstrate how canonical concepts operate in concrete scenarios.

They answer:

How do the canonical concepts compose in a real use case?

A workflow is illustrative unless explicitly designated as normative.

A workflow must not redefine foundational semantics merely because a particular scenario requires an implementation-specific behavior.

⸻

5.6 Research

Research contains:

* hypotheses
* experiments
* external findings
* alternative models
* exploratory concepts
* unresolved questions

Research answers:

What might improve or challenge the current system?

Research may influence future canonical decisions.

Research does not become Canon merely by being added to the repository.

⸻

5.7 Strategy

Strategy describes commercial, organizational, or product direction.

Strategy answers:

Where should Noema go?

Strategy may influence requirements but does not redefine technical semantics by itself.

⸻

6. Authority Is Not the Same as Recency

The newest document is not automatically the most authoritative document.

For example:

Research/2026-09-18.md

does not override:

CANON.md

merely because it was written later.

Likewise:

Architecture/new-model.md

does not automatically replace an accepted specification.

Authority derives from:

1. document class
2. acceptance status
3. explicit supersession
4. canonical governance

not simply from modification timestamp.

⸻

7. Explicit Supersession

When a canonical decision changes, the repository SHALL make the change explicit.

A newer artifact may supersede an older one only when the repository records that relationship.

For example:

ADR-018
Status: Superseded by ADR-024

and:

ADR-024
Supersedes: ADR-018

Historical decisions must remain reconstructible.

The repository must not rewrite history merely to make the current architecture appear internally consistent.

⸻

8. Canon Changes Must Be Deliberate

A change to a foundational concept requires explicit governance.

A canonical change should identify:

1. the existing principle
2. the proposed change
3. the reason
4. supporting evidence
5. affected specifications
6. affected architecture
7. affected contracts
8. affected implementation
9. migration implications
10. relevant ADR

This prevents silent semantic drift.

⸻

9. Implementation Does Not Define Canon

The implementation may reveal that a canonical concept is incomplete, contradictory, or impractical.

When this occurs, the implementation should trigger review.

It should not silently redefine the concept.

The correct process is:

Implementation discrepancy
        ↓
Identify canonical conflict
        ↓
Evaluate evidence
        ↓
Decision / ADR
        ↓
Update Canon if required
        ↓
Update Specification
        ↓
Update Architecture
        ↓
Update Implementation

Not:

Implementation changed
        ↓
Canon is assumed to have changed

⸻

10. Canon and Specification Consistency

Specifications derive their authority from the Canon.

Therefore:

Canon
  ↓
Specification

is directional.

If a specification requires a behavior that violates a canonical invariant, one of two things must occur:

1. the specification is corrected, or
2. the Canon is deliberately changed.

A specification must not silently create a competing foundational principle.

⸻

11. Canon and Architecture Consistency

Architecture implements specifications.

Therefore:

Canon
  ↓
Specification
  ↓
Architecture
  ↓
Implementation

Architecture may make implementation-specific choices where the Canon and Specification leave room for them.

However, architecture cannot silently redefine foundational semantics.

For example, if the Canon states:

Trust is deterministic.

an architecture document cannot establish:

Trust = model confidence > 0.8

without explicitly challenging and changing the canonical decision.

⸻

12. ADR Authority

ADRs have a special role.

An ADR does not automatically outrank the Canon merely because it records a decision.

Rather, an ADR documents the decision by which an architectural or foundational choice was made.

When an ADR establishes a foundational principle, the corresponding canonical specification should reflect that accepted decision.

The desired relationship is:

ADR
 ↓
Accepted decision
 ↓
Canonical specification
 ↓
Architecture
 ↓
Implementation

The ADR preserves the rationale.

The canonical specification preserves the resulting rule.

⸻

13. Historical Integrity

The repository SHALL preserve historical decision integrity.

An old ADR may no longer describe the current system.

That does not make it appropriate to rewrite the old ADR to match the current system.

Instead:

Old decision
   ↓
Historical record
   ↓
New decision
   ↓
Explicit supersession

This allows future maintainers to understand how Noema evolved.

⸻

14. Status Matters

Canonical documents SHOULD carry an explicit status.

Recommended statuses include:

Draft
Proposed
Accepted
Deprecated
Superseded
Experimental
Informational

Only appropriate accepted artifacts should be treated as normative.

For example:

Status: Draft

does not establish a new canonical invariant.

Where repository conventions define a narrower status vocabulary, those conventions take precedence.

⸻

15. One Canonical Definition

A foundational concept SHOULD have one authoritative definition.

If the concept appears in multiple documents, those documents should either:

* reference the canonical definition, or
* provide an explicitly scoped refinement.

For example:

Canonical definition:
Intent
Architecture:
Implementation of Intent
Workflow:
Example use of Intent

These are not competing definitions.

The repository should avoid duplicating foundational definitions unnecessarily.

⸻

16. Terminology Authority

Canonical terminology is normative.

Terms such as:

* Intent
* Actor
* Context
* Evidence
* Validation
* Trust
* Capability
* Permission
* Policy
* Constraint
* Action
* Execution Contract
* Execution
* Outcome
* Provenance

must retain their canonical meanings.

A document may use a term differently only if the difference is explicitly scoped and justified.

Otherwise, terminology drift creates architectural ambiguity.

⸻

17. Conflict Resolution

When two repository artifacts appear to conflict, contributors SHOULD resolve the conflict in this order:

1. Determine document class
2. Determine status
3. Identify canonical authority
4. Check explicit supersession
5. Check scope
6. Check version
7. Identify the actual contradiction
8. Resolve through the appropriate governance process

The repository must not resolve foundational conflicts merely by choosing whichever document is easier to implement.

⸻

18. Research Cannot Silently Become Canon

Research is intentionally exploratory.

A research result may demonstrate:

* a better approach
* a failure mode
* an architectural limitation
* a new capability
* an alternative ontology
* a contradiction in an existing assumption

But the result must pass through an explicit decision process before becoming normative.

The canonical flow is:

Research
   ↓
Evidence
   ↓
Evaluation
   ↓
Decision
   ↓
ADR
   ↓
Canonical Change

This preserves the distinction between discovery and authority.

⸻

19. Generated Artifacts

Generated documentation, diagrams, code, schemas, or other derived artifacts do not automatically become authoritative merely because they are generated from canonical material.

Their authority derives from their source.

For example:

Canon
  ↓
Generated documentation

means the generated documentation reflects Canon.

It does not independently redefine Canon.

Where generated artifacts diverge from their source, the source remains authoritative until the source itself is deliberately changed.

⸻

20. External Sources

External documentation, standards, research papers, vendor documentation, and third-party implementations may inform Noema.

They do not automatically become canonical Noema definitions.

The repository must distinguish:

External fact

from:

Noema decision

External evidence may justify a canonical change, but the change must still be explicitly adopted by Noema.

⸻

21. Repository Structure

The canonical repository should make authority discoverable through structure.

Conceptually:

/
├── CANON.md
├── CHANGELOG.md
│
├── ontology/
├── trust/
├── ai/
├── architecture/
│
├── decisions/
│   └── ADR/
│
├── workflows/
├── research/
└── strategy/

The exact repository structure may evolve.

The authority relationships must remain explicit even if directory organization changes.

⸻

22. CANON.md as Repository-Level Anchor

CANON.md serves as the repository-level statement of foundational Noema principles and boundaries.

It establishes the high-level architectural worldview from which more specific canonical documents derive.

It should therefore answer questions such as:

* What is Noema?
* What does Noema own?
* What does Noema not own?
* What is the intent-to-action boundary?
* What is the role of Trust?
* What is the role of deterministic systems?
* What remains authoritative in external systems?
* What are Noema’s foundational invariants?

More specific canonical files should provide the detailed definitions.

CANON.md should not become a duplicate of every specification.

⸻

23. Canonical References

Documents SHOULD reference canonical definitions rather than reproduce them extensively.

For example:

Trust Engine

should reference the canonical Trust definition and Trust state model rather than creating an alternative definition.

This reduces:

* duplication
* contradiction
* terminology drift
* maintenance burden

and makes authority easier to determine.

⸻

24. Changelog and Authority

CHANGELOG.md records meaningful changes to the repository and canonical system.

A changelog entry does not itself establish authority.

Its role is historical and navigational:

What changed?
When did it change?
Why was it significant?

The authoritative definition remains in the relevant canonical artifact.

⸻

25. Versioning

Version numbers identify the evolution of canonical artifacts.

A version change should correspond to a meaningful document change.

Versioning does not by itself establish authority over another document.

For example:

Specification A
Version 0.3

does not automatically supersede:

Specification B
Version 0.1

unless they represent the same authority domain and the repository explicitly establishes the relationship.

⸻

26. Decision Records as Historical Spine

The ADR directory forms the historical decision spine of Noema.

It should allow a maintainer to reconstruct:

Why was this principle adopted?
Why was this boundary established?
What alternatives were rejected?
What consequences were accepted?
What later changed?

ADRs therefore complement Canon rather than replace it.

Canon states the current foundational model.

ADRs explain important decisions that produced that model.

⸻

27. Repository Review

Before accepting a significant architectural change, contributors SHOULD check:

Does this change contradict Canon?
Does it change a canonical definition?
Does it alter an invariant?
Does it change a Trust boundary?
Does it change an ownership boundary?
Does it alter an execution contract?
Does it require a new ADR?
Does it supersede an existing ADR?
Does it require specification changes?
Does it require migration?

This makes repository governance part of the architecture rather than an administrative afterthought.

⸻

28. Canonical Drift

Canonical drift occurs when implementation, documentation, or terminology gradually diverges from accepted canonical definitions without an explicit decision.

Examples include:

Canon:
Trust is deterministic.
Implementation:
Trust depends on model confidence.

or:

Canon:
Enterprise system owns business state.
Implementation:
Noema maintains an independent authoritative copy.

Such discrepancies must be surfaced and resolved explicitly.

Canonical drift must not be normalized simply because the implementation has existed for some time.

⸻

29. Repository Authority Invariants

Invariant 1

The canonical repository is the authoritative representation of accepted Noema principles and definitions.

Invariant 2

Not every repository artifact has equal authority.

Invariant 3

Canon has the highest foundational semantic authority.

Invariant 4

Specifications derive their semantics from the Canon.

Invariant 5

Architecture implements specifications and must not silently redefine Canon.

Invariant 6

ADRs preserve the rationale and history of significant decisions.

Invariant 7

Research may challenge Canon but does not become Canon automatically.

Invariant 8

Historical decisions must remain reconstructible.

Invariant 9

Supersession must be explicit.

Invariant 10

Repository recency does not by itself determine semantic authority.

Invariant 11

Canonical terminology must remain stable unless deliberately changed.

Invariant 12

Implementation behavior does not silently redefine canonical meaning.

Invariant 13

Generated and derived artifacts inherit authority from their authoritative sources.

Invariant 14

External sources may inform Noema but do not automatically become Noema Canon.

Invariant 15

Foundational changes require explicit governance.

⸻

30. Canonical Change Flow

The preferred governance flow is:

Observation
    ↓
Evidence / Research
    ↓
Proposed Change
    ↓
Impact Analysis
    ↓
ADR
    ↓
Decision
    ↓
Canonical Update
    ↓
Specification Update
    ↓
Architecture Update
    ↓
Implementation Update
    ↓
Validation
    ↓
Changelog

Not every change requires every stage, but foundational changes should follow this pattern where applicable.

⸻

31. Relationship to the Canon

This ADR establishes the repository authority model described by the Canon.

The Canon establishes the principle that:

Canonical knowledge has authority.

This ADR makes that principle operational by defining:

* authority classes
* document relationships
* supersession
* historical preservation
* change governance
* conflict resolution
* repository consistency

⸻

32. Consequences

Positive consequences

This decision provides:

* a clear source of truth
* reduced semantic drift
* explicit architectural governance
* reconstructible decision history
* clearer contribution rules
* separation between research and accepted architecture
* predictable conflict resolution
* stable terminology
* traceable canonical evolution

Costs

This decision also introduces process overhead.

Contributors must:

* classify documents correctly
* record significant decisions
* maintain references
* update affected artifacts
* explicitly supersede obsolete decisions
* avoid silently changing foundational meaning

This overhead is intentional.

The cost is accepted because uncontrolled semantic drift would undermine the purpose of a canonical repository.

⸻

33. Rejected Alternatives

Alternative A — Latest document wins

Rejected because document recency does not establish semantic authority.

Alternative B — Code is always the source of truth

Rejected because implementation may contain bugs, temporary constraints, or intentional deviations.

Alternative C — All repository documents have equal authority

Rejected because research, strategy, architecture, and Canon serve fundamentally different purposes.

Alternative D — ADRs alone define the entire Canon

Rejected because ADRs explain decisions but should not replace consolidated canonical definitions.

Alternative E — Research automatically becomes canonical when sufficiently convincing

Rejected because evidence and authority are different concepts.

Alternative F — Rewrite historical documents whenever the architecture changes

Rejected because doing so destroys decision history and makes architectural evolution difficult to reconstruct.

⸻

34. Final Decision

The Noema canonical repository SHALL function as the authoritative source for the accepted definition of the Noema system, while maintaining explicit distinctions between Canon, Specification, Architecture, ADRs, Reference Workflows, Research, and Strategy.

The central governance principle is:

Noema’s current canonical meaning must be explicit, authoritative, and reconstructible; research may challenge it, architecture may implement it, and ADRs may explain its evolution, but no artifact may silently redefine it.