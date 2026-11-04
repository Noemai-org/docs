# DEC-2026-11-04 · BEN-05 reports a named open exclusion as non-full coverage; G1 needs one US-01 and one US-06 case

| | |
|---|---|
| **Status** | Proposed for the Founders. The Founder gave this ruling in a work-order reply of 3 to 4 November 2026 (after the benchmark owner agent put both options to the founders); an instruction given in a session is not authoritative until committed (AGENTS §2, item 3), and Codex has said so on noema#102. It counts once both Founders approve and merge this pull request. |
| **Date** | 4 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None |
| **Amends** | None. No SoT, PERD or plan text changes. It records how the BEN-05 comparison reports a case that no producer can yet drive, and what the plan §3.1 G1 text requires |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Proposed; counts once both Founders approve and merge this pull request (see the table above)
- Date: 4 November 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: REQ-BEN-002, REQ-NFR-001 (replay), INV-21 (determinism); plan v1.10 §3.1 (G1) and task BEN-05; AGENT-20. No requirement is added or changed
- Migration notes: none. `benchmark/replay` in `Noemai-org/noema` (noema#102) already behaves as D2 to D5 say; its README and `status/BEN-05.md` cite this record once it is merged
- Supersedes: None

---

## 1. The decision

| | Decision |
|---|---|
| D1 | **G1's text is met by one case of each kind.** Plan v1.10 §3.1 and `gates/G1.md` require "one clean case (US-01) and one timeout-after-write case (US-06) run end to end on text through the public API", the unknown outcome verified by key and never retried, the Record reconstructing both, and the property tests green. They do not require every generated case that covers US-01 or US-06. BEN-05's identical-results check compares every case that covers the two stories and that the runner can drive. |
| D2 | **A case that no producer can yet drive may be a named open exclusion.** It is named, with a reason, the party that holds the blocking fault, and the date opened, in `benchmark/replay/open_exclusions.json`. Today there is one: `BEN-CLEAN-1007` (US-01 with `INJECTION_IN_NAME`), which needs `mock-customer INJECTION_PAYLOAD`, a fault held by Tushe. Only a named case is excluded; the flag removes no case by kind. |
| D3 | **A named exclusion is reported as non-full coverage, never as a pass.** The comparison says "IDENTICAL on 5 of 6 cases (1 open exclusion, so not full coverage)", carries `full_coverage: false`, and lists the exclusion with what each run showed for it. It does not report NOT_COMPARABLE for the named case, because that case is errored or missing by construction until the fault is wired. |
| D4 | **Every other errored or missing story-covering case makes the verdict NOT_COMPARABLE.** A difference in any compared case, including a named case that can now run, makes it DIFFERENT. A named case that can run is compared and counted, so a registry entry cannot hide a difference and closes itself. |
| D5 | **An exclusion is closed by wiring, never accepted.** If a founder decides that G1 needs all six cases, the exclusion is closed by wiring the fault. The case stays in the G2 and G3 runs whatever G1's reading. The registry changes only by a reviewed pull request. |

## 2. Rationale and evidence

**D1.** The G1 text is one clean case and one timeout-after-write case, end to end. The default suite has six cases covering US-01 or US-06: `BEN-CLEAN-0001`, `-0014`, `-0027` (US-01), `BEN-TMO-0001`, `-0018` (US-06), and `BEN-CLEAN-1007`, an injection mutation of US-01. Five can be driven today. Requiring the sixth would make G1 wait on a Tushe-held fault the gate text does not name.

**D2 and D3.** The alternative was to force NOT_COMPARABLE for the named case. That is the strict reading Codex asked for, and it is the right rule for every case the team could drive. For a case blocked by construction it would make the comparison unreachable until the Tushe fault exists, and would hide the five comparable results behind a label that says nothing about them. The chosen rule keeps the information (five identical results, one named gap) and prevents the misreading Codex raised: the headline and the `full_coverage` flag both say the coverage is partial.

**D4 and D5.** They keep the no-false-identical rule for everything else and keep the gap open as a debt that is visible in the report, not an accepted risk.

**Evidence.** noema#102 (`benchmark/replay`, tests for each rule: `test_a_named_exclusion_that_is_missing_or_errored_stays_open_with_its_observed_state_and_full_coverage_is_false`, `test_a_named_exclusion_cannot_hide_a_difference`, `test_an_unnamed_mutated_case_is_never_excluded_and_an_error_in_it_makes_the_verdict_not_comparable`); the Codex reviews of 1 to 3 November on that pull request; plan v1.10 §3.1; `gates/G1.md`.

## 3. What is not decided here

Whether the dates move (DEC-2026-11-03 sets G1's target and evidence dates). Whether the G1 evidence also needs the Record reconstruction compared (the replay tool compares the recorded case result, which does not hold the Record events; stated in its report). The Tushe-held fault itself.
