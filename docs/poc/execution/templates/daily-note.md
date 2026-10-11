# Daily note: <YYYY-MM-DD>

<!-- Save as docs/poc/execution/daily/<YYYY-MM-DD>.md. Fill from today's evidence only (plan §15). Never write a note in advance. -->

> **A non-empty "Scope or safety deviations" field blocks release.** It must read NONE.

- DATE: <!-- The working day, YYYY-MM-DD. -->
- GATE STATUS (G0–G7): <!-- Each gate: not yet due, PASS, FAIL or BLOCKED, with the link to gates/G<n>.md once recorded. -->
- ACCEPTED TODAY (task IDs, evidence links, SHAs): <!-- Only tasks that reached Done today against plan §13.1, each with its merged PR and commit SHA. -->
- BLOCKED (task, blocker, owner, age, decision needed, deadline): <!-- One line per blocked task; every field filled. -->
- TESTS by layer (pass / fail): <!-- Counts per layer from CI (plan §12). -->
- BENCHMARK: run ID, n, held-out n (no labels), Tier 0 counters <!-- From the run report; never include held-out labels or case content. -->
- NEW FAILURES: regression case IDs and owners <!-- Every new failure has its regression case ID before its fix merges (REQ-MEM-002). -->
- RECORD / RECONSTRUCTION: pass or fail <!-- Result of today's reconstruction and chain checks. -->
- LATENCY: P50 / P95 / P99 by stage, where instrumented <!-- Measured values only; leave "not instrumented" where there is no measurement. -->
- DECISIONS NEEDED (from whom, by when): <!-- Include any decision past its date in plan §17 and the default that took effect. -->
- TOMORROW'S CRITICAL PATH (one outcome per owner): <!-- One observable outcome per owner. -->
- SCOPE OR SAFETY DEVIATIONS: must be NONE <!-- Anything other than NONE blocks release; name it and link the change request. -->

**Plan changes today:** <!-- Name any plan change made today and link its change request (plan §19), or write "none". -->

**Debt register changes:** <!-- Entries added, changed or closed in ../debt.md today (plan §5), or "none". -->
