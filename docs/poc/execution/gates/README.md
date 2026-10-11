# Gate records

One record per gate review, `gates/G<n>.md` (G0 to G7), using [`../templates/gate-record.md`](../templates/gate-record.md). The gates, what must be true, the evidence, the deciders and what happens on failure are defined in plan [§3.1](../NOEMA_POC_4WEEK_PLAN_v1.1.md#31-gate-definitions); dates and times are in [`../calendar.md`](../calendar.md).

**Gate rules (plan §3.1, quoted):**

- A gate's outcome is PASS, FAIL or BLOCKED, written in `docs/poc/execution/gates/` with evidence links. A failed gate is never relabelled "mostly done" or "pass with actions".
- A fix after a failed gate gets its regression case first, then the affected property tests and the full suite run again. The rerun is a new run with its own ID; it never silently replaces the failed one, and no case is cherry-picked.
- A curated happy path never passes a gate.

A rerun after a failure is recorded separately and links the failed record; the failed record is never edited to read as a pass. TODO(EL): name the file convention for rerun records (plan §3.1 "Gate rules").
