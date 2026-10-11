# DEC-2026-10-11-poc-perd-v1.1

- Status: Proposed (founder approval required)
- Date: 2026-10-11
- Closes: none
- Owner: Founders (TODO: name), with the technical co-founder as reviewer
- Decision:
  - Adopt [`docs/poc/perd/NOEMA_POC_PERD_v1.1.md`](../poc/perd/NOEMA_POC_PERD_v1.1.md) as the POC's detailed engineering specification (SoT §0.4, item 4), subordinate to SoT v1.3. Where the two disagree, the SoT wins (PERD P.1).
  - Its `[REC]` defaults apply as provisional defaults, mirrored as NON-CANONICAL entries [OD-P-14 to OD-P-41](../open-decisions.md#od-p-14), until each is accepted or replaced by its own decision record.
- Rationale and evidence:
  - The SoT defines what and why.
  - The PERD defines how, with 152 testable requirements traced to SoT IDs, an executable investigation state machine, contracts, an edge-case catalogue, a threat model and a build plan.
  - Every disagreement with the SoT is listed in PERD §72 and none is resolved silently. They are tracked in [`docs/poc/perd/conflicts-register.md`](../poc/perd/conflicts-register.md).
- Affected requirement IDs / SoT sections: SoT Part VII and Part IX (no SoT text changes in this record or its pull request).
- Migration notes:
  - None for code; no code exists yet.
  - Future PERD versions follow [`docs/poc/perd/README.md`](../poc/perd/README.md): a new version file, a decision record, the regenerated requirements index and updated conflict statuses, in one pull request (AGENT-29).
- Supersedes: none. Older POC specification files in this repository (the drafts under [`docs/archive/source-drafts-2026-09/`](../archive/README.md)) are historical. They must not be given to coding agents as specifications (PERD §72, SOT-C-27; AGENTS.md §1.4). They are not moved or deleted.

## SoT §52 questions

- **Which requirement ID does this serve?** SoT §0.4 (order of authority, item 4: the engineering specification); AGENT-01, AGENT-02, AGENT-26, AGENT-27, AGENT-29; PERD REQ-AGT-001 to REQ-AGT-005.
- **What breaks without it?** Coding agents and engineers build from the SoT alone, which leaves gaps (PERD §67, §72) that each would fill differently.
- **Which benchmark case proves it works?** None directly; this is a specification. It defines the benchmark case contract (PERD §48.2) and the coverage rule (PERD §48.1).
- **What business value does it create?** A shorter, less ambiguous path to the POC evidence the SoT asks for (SoT §40.3).
- **Core, pack, adapter or nowhere?** Nowhere in code. It is documentation in the docs repository.
- **Which failure mode does it prevent?** Silent divergence between implementation and the SoT, and invented defaults (AGENT-02, AGENT-27).
- **Why are existing products or components not good enough?** The SoT sets requirements and invariants but not every contract, threshold and state transition the build needs (PERD §67.3).
- **Which phase does it belong to?** Phase A, before the four-week clock (PERD §61.2, step P0).
- **What vertical, country, model or interface assumptions does it make?** Those of the POC fence only (SoT Part VII): Nigerian fintech, voice-fronted, Mode 1. None enters core (INV-14).
- **What is the simplest viable implementation?** Commit the PERD unchanged, index it, and mirror its open items in the register.
- **Can its result be independently verified and tested adversarially?** Yes: `tools/perd_index.py --check` verifies the index and every REQ reference; the PERD's own requirements name their tests.
- **Does it preserve the separation of Understanding, Trust, Execution and Outcome?** Yes. It follows SoT §13 and BD-05 and adds no power.
- **Does it work across models and interfaces?** Yes. It keeps BD-16 (multi-provider) and BD-14 (text as the canonical contract).
- **Does it create reusable infrastructure and a measurable enterprise metric?** It creates a reusable specification and index, not runtime infrastructure. Its metrics are the SoT §38 benchmark metrics.
- **What evidence would make us reverse it?** A SoT revision that makes the PERD obsolete, or a review finding that the PERD contradicts a SoT invariant or binding decision beyond what §72 lists.
- **Does it increase or decrease the unsafe autonomy surface?** **Decreases.** It adds explicit gates, tests and stop rules without adding any capability.
