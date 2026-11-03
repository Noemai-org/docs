# DEC-2026-11-03 · `pgregory.net/rapid` is approved as a test-only dependency of the core

| | |
|---|---|
| **Status** | Proposed for the Founders. The Architect approved the dependency in a work order of 3 November 2026 and asked for it to be recorded under AGENT-14; an instruction given in a session is not authoritative until committed (AGENTS §2, item 3). It counts once both Founders approve and merge this pull request. |
| **Date** | 3 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None. Answers the AGENT-14 approval that the Go property-testing library needed |
| **Amends** | None. No SoT, PERD or plan text changes. The `[REC]` mention of `pgregory.net/rapid` in PERD §36.1 is adopted for this library; the next PERD version drops the label |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Proposed; counts once both Founders approve and merge this pull request (see the table above)
- Date: 3 November 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: REQ-TST-002 (property tests of the invariants), REQ-AUD-001 (the Record's chain property, REC-01); AGENT-11, AGENT-14; PERD §36.1 (stack row "Hypothesis (Python) and a Go property-testing library"). No requirement is added or changed
- Migration notes: none. The first code that adds the dependency cites this record and passes `check_pins`
- Supersedes: None

---

## 1. The decision

| | Decision |
|---|---|
| D1 | **`pgregory.net/rapid` is approved** under AGENT-14 as the Go property-testing library of the core service (PERD §36.1 names a Go property-testing library and marks `pgregory.net/rapid` `[REC]`). |
| D2 | **Test-only.** It is imported from `_test.go` files only. No non-test code, no shipped binary and no image contains it. |
| D3 | **Pinned at v1.3.0**, in `services/core/go.mod` and `go.sum`. |
| D4 | **Used first** for REC-01's chain property test and for TST-01 (INV-03, INV-07, INV-08, INV-05, INV-18) and TST-03 (the deep run of all thirty invariants). |

## 2. Rationale and evidence

**D1.** Example tests cannot show an invariant: INV-03, INV-07, INV-08, INV-05, INV-11 and INV-18 are claims about every input, and the plan's G1 needs the property tests green (TST-01). PERD §36.1 rejects "example tests only" as the alternative. `rapid` generates structured inputs, shrinks a failing input to a minimal one and replays it from a seed, which AGENT-11 and the debugging protocol (AGENTS §13) need.

**D2.** A test library has no reason to reach a deployable. The image file-list check (DEC-2026-10-13 R2) and `go build` both exclude test-only imports, so this holds without a new rule.

**D3, evidence read on 3 November 2026 from the module itself.**

| | |
|---|---|
| Module | `pgregory.net/rapid` |
| Version | v1.3.0, tagged 30 March 2026 (older than two weeks). v1.2.0 (24 February 2025) was the other candidate |
| Licence | Mozilla Public License 2.0. It is file-level copyleft: a file of `rapid` that is *modified* must stay under MPL-2.0 and its source be available. We use it unmodified, as a test library, so no obligation arises. A fork or patch of `rapid` would need a new decision |
| Dependencies | none (`go.mod` requires nothing); Go directive 1.23, below the core's 1.24 |
| Effect on the repository | `go.mod` +1 line, `go.sum` +2 lines |

## 3. Agent decisions (defaults for the Founders to confirm or change)

1. v1.3.0 over v1.2.0: it is the latest release and older than two weeks, and it adds no requirement.
2. The record does not approve any other test library. A second one needs its own decision.

## 4. SoT §52

1. Is it in the POC? Yes: TST-01 is on G1's path.
2. Is it the simplest viable version? A library with no dependencies, used only in tests.
3. Is it safe? It never runs outside tests.
4. Can the Record prove it? n/a (no runtime path).
5. Is it deterministic? A failing case is replayed from its seed.

**Does it increase or decrease the unsafe autonomy surface?** It decreases it: it makes the invariants testable over all inputs.

## 5. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Architect | Approved the dependency | 3 November 2026 | Work order in a working session; recorded here |
| Founder | Approves by approving this pull request | | |
| Technical Co-Founder | Approves by approving this pull request | | |
