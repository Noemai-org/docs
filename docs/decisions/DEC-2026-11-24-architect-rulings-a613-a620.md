# DEC-2026-11-24 · Architect rulings A613 to A620 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 24 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 24 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A613 to A620 (§1), every one Interim. A613 has its own decision record, `DEC-2026-11-24-g2-parallel-start`. |
| **Supersedes** | **A613** changes the sequencing of plan §9 for build work (see that record). **A615 extends** the TRU-10 allowlist (A534, A539). **A618 and A619 refine** earlier rulings on #800 and UND-15. **A620 splits** the build of lane 5 (A547). **A614 is a reporting rule** that keeps A585 and A599. Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan, as written. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 24 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A613 to A620
- Decision: §1
- Rationale and evidence: the Architect's message of 24 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-03, INV-14, INV-29; AGENT-14, AGENT-16; REQ-TRU-010; plan §3, §9; AGENTS §2.3, §5, §11
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. A615 adds a field to `EscalateInput` and `RouteGrantRequest` (EL; the AGENT-15 steps apply to any contract change).

## 1. The rulings

### A613. G2 starts now, in parallel with G1.

- Plan §9 says G2 work waits for G1. A chat instruction doesn't override that until it is committed (AGENTS §2.3).
- So the Architect takes the safe path. Any G2 task whose "Needs" tasks are Done may be built now, and the Steward records a decision for it today (`DEC-2026-11-24-g2-parallel-start`).
- The G2 gate itself still counts only after G0 and G1 pass. Nothing G2 touches the G1 path. G1 PRs keep priority in review.

### A614. Stop the loops.

- An agent reports only when a PR is READY at a head, merged, or blocked with a named blocker.
- No status-only reports and no recaps.
- A585 and A599 stay: read the red, push the green, read the green's CI, post READY, unsubscribe.

### A615 (EL, TRU-10 escalation path).

- Approved: the allowlist grows to `trustpg`, the `trustport` interface, and `workflows/` for the single field `DispositionDecisionID` on `EscalateInput` and `RouteGrantRequest`.
- EL builds, in one PR: the by-correlation read port and its Postgres reader, the production `RouteScopes` reader, and the start site.
- C1 gives the independent read on the `workflows/` change. C1 does not build any of it.

### A616 (EL, #935).

An empty required slot and an out-of-vocabulary value are errors. That is the fail-closed reading.

### A617 (EL, #934).

- Add the CODEOWNERS line for `evidence/` in the same PR. It uses the same owner as its parent path.
- Treat "the live case system never reports CLOSED" as safe: nothing increments.

### A618 (C2, #800).

- Charge 0 only for a call that provably sent nothing (`local=True`). Every other failure keeps its projection.
- Add a test for each case. The USD 5 ceiling is unchanged.

### A619 (C2, UND-15).

- Wait for a passing run. Do not hand over run 7's recordings.
- Approved: the provider class under `providers/` in the model service. That directory and its tests only, with no new dependency.

### A620 (lane 5).

Slices 2 to 4 are split so C1 is not the only builder:

- Slice 2 goes to C1.
- Slice 3 (Outcome request builder) goes to C2.
- Slice 4 (Record reader) goes to an EL agent.
- All three start from a fresh branch off `main` once #917 has merged.

## 2. What the Steward did, and where the rulings are silent

- **A613.** Recorded in its own decision record, `DEC-2026-11-24-g2-parallel-start` (Interim; binding on merge; the plan is not edited). Until that record merges, plan §9 stands.
- **A614.** The Steward adopts it: it reports only when a PR is READY at a head, merged, or blocked with a named blocker, and sends no status-only report or recap. A585 and A599 are unchanged (the Steward stays subscribed until the head's CI is read, then posts READY and unsubscribes).
- **A615.** The task is TRU-10 (A539). The allowlist is the Architect's to widen; the Steward changes no task card. `DispositionDecisionID` is a contract field on two workflow inputs: the AGENT-15 steps (a version bump where a contract changes, a migration note, regenerated models) apply, and C1's independent read covers `workflows/` (INV-30: workflow code does no I/O).
- **A616 and A617.** A616 is EL's (#935). A617 is EL's (#934): the CODEOWNERS line for a new top-level owned path in the same PR is AGENTS §11's rule. "Nothing increments" refers to the epoch (A513, A520).
- **A618 and noema#800.** noema#800 shows **merged** on GitHub (it records a call refused by the full pool as `POOL_REFUSED`, A372). A618's change (charge 0 only for a call that provably sent nothing) is therefore a **follow-up PR by C2**, not a change to #800, unless the Architect meant a different number. The Steward does not guess; C2 names the PR. The USD 5 ceiling is unchanged (AGENT-16: no agent changes a threshold).
- **A619 and AGENT-14.** The provider class under `providers/` in the model service is where provider code lives (INV-29). "No new dependency" keeps AGENT-14 satisfied. "Wait for a passing run" ties to the stop rule of A605: run 7's recordings are not handed over, and no run is started by this ruling.
- **A620 and #917.** A547 gave lane 5 to C1 with EL integrating the ports; A620 splits slices 2 to 4 among C1, C2 and an EL agent, all from a fresh branch off `main` after #917 merges. noema#917 (slice 1) is open at this writing. Lane 5 traces to STM-01 (A589).
- **Migration ledger on noema#183** and **`tasks.csv`** are unchanged: 0037 #922, 0038 #923, 0039 #925, 0040 reserved, next free 0041.
- **Next free ruling: A621.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` and `DEC-2026-11-21-*` records | A358 to A362, A380 to A485 (A467: no text), A489 to A492, A502 to A517 | |
| `DEC-2026-11-22-*` to `DEC-2026-11-24-architect-rulings-a612` | A518 to A612 (A541 noted; A590 to A592 in full) | |
| This record | A613 to A620 (A613 also in `DEC-2026-11-24-g2-parallel-start`) | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank, by ruling A592) | **A621** |
