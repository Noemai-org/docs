# Task card: ENV-09

Plan v1.2 task ENV-09. Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-12](../../../decisions/DEC-2026-10-12-tushe-environment-scope.md).

```
TASK-P2-009  ENV-09 · Hostility proxy: transport faults, stale-read profile, event-feed faults, impossible-data fixtures, test-number rewriting, fault-plan control API on `bench_net`
Priority: P0
Requirement IDs: REQ-ENV-005, REQ-ENV-004, REQ-ENV-006; SoT IDs: POC-NFR-08, AGENT-25; SoT §36 (contingency)
Rationale: Tushe does not produce transport faults, stale reads or event-delivery faults, and refuses to fake impossible state; the proxy becomes the primary source for those families. It also rewrites Tushe test account numbers so the environment still forces a real investigation. DEC-2026-10-12, D4.
Modules touched (allowlist; all paths in the `noema` repository, DEC-2026-10-13): benchmark/hostility_proxy/ (PERD §64.2); benchmark/fault_plans/ (proxy fault plans, owned by the benchmark owner)   ← nothing else may change
Contracts: FaultPlan contract (PERD §37.1, `source: PROXY`); bump required? N
Inputs/outputs: Tushe responses and the event feed in → responses with injected faults and rewritten test numbers out; fault-plan control API on bench_net
Acceptance criteria:
  REQ-ENV-005:
  - Each proxied fault SHALL have a test proving it is observed by the adapter exactly as specified.
  - Every proxy fault family SHALL reproduce from a scenario and seed; the same Tushe number SHALL always map to the same synthetic number; no `9999` test-number pattern SHALL appear in any response delivered to a system under test.
  REQ-ENV-004:
  - Running the same case with the same seed twice SHALL produce identical fault traces and identical authoritative outcomes.
  REQ-ENV-006:
  - A CI grep SHALL find no unlabelled code-table fixture.
  Task "Done when" (plan v1.2): each proxy fault family reproduces from a seed; rewritten numbers stable across runs; no `9999` pattern reaches a system under test
Tests to write FIRST (AGENT-11): one reproducibility test per proxy fault family; number-rewriting stability across runs; a scan proving no `9999` pattern reaches a system under test; EC-S12, EC-S13, EC-S14, EC-S20
Faults to exercise (AGENT-12): timeout, disconnect, reset, 502/503/504, slow response, 429; stale read after a write; event lost, delayed, reordered, malformed or stale on the feed-reading path; impossible-data fixtures (labelled synthetic); timestamp shifts for time cases (labelled synthetic)
Dependencies: PLT-01, PLT-04; REQ-ENV-005, REQ-ENV-004, REQ-ENV-006
Out of scope: buying a service-virtualisation product (AGENT-14); any change in services/core; faults Tushe produces natively (test account values, replay)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

**Builder.** The builder must not be C1 or C2 (REQ-ENV-008 separation of duties; plan SR-19). Owner: EL, with a coding agent.
