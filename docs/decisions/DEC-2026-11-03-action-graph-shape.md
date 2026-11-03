# DEC-2026-11-03-action-graph-shape

- **Status:** Decided by the Founder on 3 November 2026 in a work order given in a working session. **It counts only once this record is merged** (AGENTS.md §2.3, SoT §0.4); the Technical Co-Founder confirms by approving the pull request that adds it.
- **Date:** 3 November 2026
- **Task:** PCK-04 (Action Graph verification). Prepared by the Engineering Lead role agent.
- **Closes:** none. Settles two points a review of noema#104 found were not committed: the connectedness rule and the `roots` field. It also settles the question PCK-04 left open: whether a root may have an incoming edge.
- **Owner:** Founder and Technical Co-Founder.
- **Authority order applied:** SoT v1.10 → decision records (DEC-2026-10-31 D9) → PERD v1.19 REQ-AG-001 → plan v1.10.

## 1. The decisions

| # | Decision |
|---|---|
| D1 | **Roots are required.** A graph declares its roots in `roots`: at least one unique node ID, each naming a node of that graph (`action-graph.v2.json`; the contract change and its migration note are in noema#104, AGENT-15) |
| D2 | **Every non-root node needs at least one incoming edge** (an edge whose `node_id` is that node, with its `depends_on`) |
| D3 | **A root has no incoming edge.** (The text of D9 and REQ-AG-001 does not say; this settles it.) |
| D4 | **A graph with more than one node must be weakly connected:** every node is reachable from every other when the direction of the edges is ignored. A list of nodes without edges, or with edges that leave it in separate pieces, fails. A graph of one node is connected |
| D5 | **PCK-04's dependency on PCK-02 is narrowed, by this record, to PCK-02's graph-shape part.** PCK-04 (`Needs: PCK-02`) builds on one thing PCK-02 was still missing: rejection of a flat-list graph (DEC-2026-10-31 D9, plan v1.10 PCK-02 row), which noema#104 delivers. **PCK-02 as a whole is not satisfied and stays In progress.** Its other open item, **template coverage** (REQ-EXP-002: fallback explanation templates for every outcome × classification in all five locales, 100%, checked by `packcheck`), is a separate acceptance criterion that PCK-04 does not deliver and cannot: `packs/fintech/templates/` is empty and the templates are EXP-04's (Core Engineer 2, with native-speaker review). The Founders' work order of 3 Nov said PCK-02 is "satisfied by this same change"; the facts in §3 show it is satisfied only in the graph-shape part, so this record states the narrowing and not a completion. Everything else in PCK-02's done-when is unchanged and still gates PCK-02. `noema#104` proceeds once this record merges |

The other graph rules of DEC-2026-10-31 D9 and REQ-AG-001 stand unchanged: every node has a postcondition; every write node has a precondition; `on_unknown` and `on_failure` are set; a plan is a path in the graph (REQ-AG-003).

## 2. The PERD text (applied by the Repo Steward in PERD v1.20)

PERD v1.19 is not edited in place. REQ-AG-001 becomes, in PERD v1.20 (the same PR as the text of DEC-2026-11-01-receipt-and-record-signing §12, opened the day these records merge):

> before (Requirement, last bullet): it is a graph, never a list of endpoints [ADOPTED DEC-2026-10-31-proof-depth-and-completeness D9]: every node other than a declared root has at least one incoming edge with `depends_on`; every node has at least one postcondition; every write node has at least one precondition; and every node's `on_unknown` and `on_failure` are set.
>
> after: it is a graph, never a list of endpoints [ADOPTED DEC-2026-10-31-proof-depth-and-completeness D9, DEC-2026-11-03-action-graph-shape]: the graph declares its roots (`roots`: at least one, each a node of the graph); every node other than a root has at least one incoming edge with `depends_on`, and a root has none; a graph with more than one node is weakly connected (every node is reachable from every other when the direction of the edges is ignored), so a list of nodes without edges fails; every node has at least one postcondition; every write node has at least one precondition; and every node's `on_unknown` and `on_failure` are set.
>
> before (Acceptance criteria, second sentence): A pack whose graph is a flat list (nodes without edges, postconditions or preconditions as above) SHALL fail `packcheck` and CI.
>
> after: A pack whose graph is a flat list (nodes without edges, postconditions or preconditions as above), is not connected, or has a root with an incoming edge SHALL fail `packcheck` and CI.

## 3. Evidence and effect

- **What was checked on 3 Nov 2026 (for D5).** `tools/packcheck/checks.py` already checks that every policy template a capability names is a rule of the policy (lines 106 and 123). It has no check of explanation-template coverage, and none can pass today: `packs/fintech/templates/` holds only a README. The review of this record by Codex found the same gap and was right that it cannot be called satisfied.
- **Why connectedness is needed.** With a free `roots` list, a flat list of endpoints passes by declaring every node a root, and D2 alone would never reject it. D3 and D4 close that: every root has no incoming edge, and the pieces must join.
- **What noema#104 changes after this merges:** it adds the rule of D3 (a failing test first: a root with an incoming edge), keeps the rest, and merges `main` in. It is also waiting on Core Engineer 2's `beneficiary` and `account` evidence descriptors, so that the two read nodes with no postcondition can get one; the pack is not exempted.
- **Unsafe autonomy surface:** decreases. A pack whose graph is a list of endpoints can no longer load.

## 4. Record fields (decisions README template)

- Status: see the top of this record
- Date: 3 November 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: §1
- Rationale and evidence: §3; the review of noema#104 of 2 Nov 2026
- Affected requirement IDs / SoT sections: REQ-AG-001 (amended, text in §2), REQ-AG-003; INV-18; SoT §14
- Migration notes: §2 (PERD v1.20 by the Repo Steward); the contract and fixtures in noema#104
- Supersedes: none
