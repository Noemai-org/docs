# DEC-2026-11-06 · Model qualification: the pass^k floor

| | |
|---|---|
| **Status** | **Draft, not for merge until the Founder sets the number.** Proposed for the Founders once the bracketed fields are filled. Counts once both Founders approve and merge. The text was supplied for the Repo Steward on docs#117 (6 Nov 2026) with the number left open; the Repo Steward has not chosen one (AGENT-16, REQ-AGT-005, AGENT-18). |
| **Date** | 6 November 2026 |
| **Owner** | Founder (benchmark owner) and Technical Co-Founder |
| **Closes** | The open value in A17 of DEC-2026-11-06-architect-rulings: the pass^k floor for a first qualification. |
| **Amends** | None. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Draft; proposed for the Founders once the bracketed fields are filled; counts once both Founders approve and merge
- Date: 6 November 2026
- Closes: the open value in A17 of DEC-2026-11-06-architect-rulings (the pass^k floor for a first qualification)
- Owner: Founder (benchmark owner) and Technical Co-Founder
- Decision: the Decision paragraph below
- Rationale and evidence: [FOUNDER TO WRITE], see below
- Affected requirement IDs / SoT sections: REQ-INT-006, REQ-BEN-009; AGENT-28; INV-22
- Migration notes: none; see below
- Supersedes: None

---

**Decision.** A first qualification of a model or speech provider version, which has no pinned baseline of its own, is QUALIFIED only if its pass^k (k = 5, over the Understanding-dependent cases of the qualification subset) is **at least [FOUNDER TO SET: a number between 0 and 1, with its source]**. A later version is QUALIFIED if its pass^k is not below the higher of the pinned baseline's own pass^k and this floor. All other conditions of A17 apply unchanged: the run is complete, every Tier 0 gate is zero, and the drift check result is PASS.

**Rationale.** [FOUNDER TO WRITE. The number needs a source (AGENT-18): for example a run of the pinned model on the development suite, cited by run ID, or a stated target.]

**Affected requirement IDs.** REQ-INT-006, REQ-BEN-009; AGENT-28; INV-22 (the qualification subset is generated-layer only).

**Where it lives.** The floor is pack data, not code. `qualification-record.v1` carries it as `bar.floor` with the id of this record in `bar.floor_source`. The benchmark tool takes it as `--floor` and `--floor-source`. **Open:** the current pack schema (`pack.v1`) has no field for it, so adding one is a contract change with its own AGENT-15 steps (version, migration note, regenerated models), or the floor is read from a file in the pack folder. The Engineering Lead decides which; until then the value is passed on the command line and written into every record.

**Migration notes.** None. No record exists yet; the first QUALIFIED record can be written only after this record is merged. Until then every first qualification is NOT_QUALIFIED with the reason "a first qualification waits for a Founder-set floor".

**Supersedes.** None.

Related: noema#199 (the formats and the lookup); DEBT-17 (docs#121: records are unsigned JSON in git).
