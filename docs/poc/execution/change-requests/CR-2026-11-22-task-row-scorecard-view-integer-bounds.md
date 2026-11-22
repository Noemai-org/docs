# Change request: CR-2026-11-22-task-row-scorecard-view-integer-bounds

**Status: DRAFT.** Drafted by the Repo Steward at the Founder's instruction of 22 Nov 2026, from the body of noema#831. No plan version is written until the Architect confirms the row (the owner, Needs and done-when are the Steward's smallest defaults).

- Change ID: CR-2026-11-22-task-row-scorecard-view-integer-bounds
- Requester: Founder (the instruction); C1 (the author of noema#831)
- REQ IDs affected: REQ-UI-004, REQ-BEN-004 (the task's trace, as noema#831 cites them). One new plan task (below). No requirement is added or removed.
- Behaviour before: noema#831, merged, is titled "CON-08: every integer of scorecard-view.v1 is bounded to what a browser holds exactly" (A446). The plan's CON-08 is `ParseIntentRef` (A337, owner C1). The plan has **no row** whose "done when" matches the scorecard-view integer bounds. The title ID is therefore a collision, and the merged work has no task.
- Behaviour after (proposed): one new task, **CON-09** (workstream CON, owner C1, Needs CON-03, REQ-UI-004 and REQ-BEN-004): **the integers of `scorecard-view.v1` are bounded to what a browser holds exactly** (A298, A311, A446: counts exact, rates as supplied). **Done when:** every integer of `scorecard-view.v1` has a maximum of 2^53 - 1; five invalid fixtures (latency `n`, latency `p95`, severity count, slice gate trips, slice `n`) fail first and are refused by the generated parsers; the generated models and the README match; the change is in-place and additive in effect (A446), with the new major `scorecard-view.v2` (rates as integer basis points, A462) a separate, later task. noema#831's merged evidence meets the bound half; the row would be marked Done from it once adopted, by the Steward, on a check-run link at the merged head.
- The merged pull request is **not retitled**, as the Founder said; the status file of noema#831 (`status/CON-08-scorecard-bounds.md`) carries the old ID and is the author's to note.
- Safety and security impact: none of the Tier 0 gates, thresholds or TTLs change. The row describes work already merged; it keeps a displayed count exact (AGENT-13) and adds no new rule.
- Tests added or changed: the owner's, already merged (`tools/contracts/test_scorecard_integer_bounds.py` and the five fixtures). None here.
- Schedule and dependency impact: one task added (plan count at that time + 1). Whether it joins a gate's Needs is the Architect's.
- SoT or PERD text changes: no.
- Decision owner: Principal Architect
- Decision record: none yet.
- Migration and rollback: none. Would be applied in a later plan version; roll back by deleting that version.
