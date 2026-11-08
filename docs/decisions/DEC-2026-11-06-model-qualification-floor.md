# DEC-2026-11-06 · Model qualification: the pass^k floor

| | |
|---|---|
| **Status** | **Decided by the Founders on 8 Nov 2026 (the number and the wording); counts once both Founders approve and merge this pull request.** The text was supplied for the Repo Steward on docs#117 (6 Nov 2026) with the number left open; the Founders set it on 8 Nov 2026 (noema#312). The Repo Steward chose no value (AGENT-16, REQ-AGT-005, AGENT-18). |
| **Date** | 6 November 2026 |
| **Owner** | Founder (benchmark owner) and Technical Co-Founder |
| **Closes** | The open value in A17 of DEC-2026-11-06-architect-rulings: the pass^k floor for a first qualification. |
| **Amends** | None. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided by the Founders on 8 Nov 2026; counts once both Founders approve and merge
- Date: 6 November 2026
- Closes: the open value in A17 of DEC-2026-11-06-architect-rulings (the pass^k floor for a first qualification)
- Owner: Founder (benchmark owner) and Technical Co-Founder
- Decision: the Decision paragraph below
- Rationale and evidence: the Founders' message of 8 Nov 2026 (noema#312), see below
- Affected requirement IDs / SoT sections: REQ-INT-006, REQ-BEN-009; AGENT-28; INV-22
- Migration notes: none; see below
- Supersedes: None

---

**Decision.** A first qualification of a model or speech provider version, which has no pinned baseline of its own, is QUALIFIED only if its pass^k (k = 5, over the Understanding-dependent cases of the qualification subset) is **at least 0.90, measured on at least 40 cases, with Tier 0 at zero** (Founders, 8 Nov 2026). A later version is QUALIFIED if its pass^k is not below the pinned baseline's own pass^k (the wording of A17); the "higher of" wording of the first draft is dropped. The two are equivalent in effect, because a baseline that qualified is already at least 0.90. All other conditions of A17 apply unchanged: the run is complete, every Tier 0 gate is zero, and the drift check result is PASS. After the first measured baseline run, the Repo Steward records that run's ID as the pinned baseline.

**Rationale.** The Founders' message of 8 Nov 2026 (noema#312): the first-qualification floor is a target set by the Founders, not a measured value, and it is stated as a floor so that no agent can lower it (AGENT-16, REQ-AGT-005). The source of the number is that decision. Once a baseline run exists its run ID replaces the floor as the bar for every later version.

**Affected requirement IDs.** REQ-INT-006, REQ-BEN-009; AGENT-28; INV-22 (the qualification subset is generated-layer only).

**Where it lives.** The floor is pack data, not code. `qualification-record.v1` carries it as `bar.floor` with the id of this record in `bar.floor_source`. The benchmark tool takes it as `--floor` and `--floor-source`. **Open:** the current pack schema (`pack.v1`) has no field for it, so adding one is a contract change with its own AGENT-15 steps (version, migration note, regenerated models), or the floor is read from a file in the pack folder. The Engineering Lead decides which; until then the value is passed on the command line and written into every record.

**Migration notes.** None. No record exists yet; the first QUALIFIED record can be written only after this record is merged. The floor now exists, so a first qualification can be QUALIFIED when it meets the Decision; the pinned baseline run ID is recorded after the first measured run.

**Supersedes.** None.

Related: noema#199 (the formats and the lookup); DEBT-17 (docs#121: records are unsigned JSON in git).
