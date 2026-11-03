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
| D5 | **PCK-04's prerequisite PCK-02 is treated as satisfied by this same change.** The part of PCK-02 that PCK-04 builds on, and that docs#77 reported missing, is rejection of a flat-list graph (DEC-2026-10-31 D9, plan v1.10 PCK-02 row); noema#104 delivers exactly that. PCK-02's other open item (a negative fixture that identifiably covers template coverage) is not about graph shape, is not touched, and stays PCK-02's. `noema#104` proceeds once this record merges |

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
