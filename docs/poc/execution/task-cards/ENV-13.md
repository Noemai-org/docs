# Task card: ENV-13

Plan v1.3 task ENV-13. Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-12](../../../decisions/DEC-2026-10-12-tushe-environment-scope.md), Amendment 1.

```
TASK-P2-013  ENV-13 · Public HTTPS webhook receiver: verifies the Standard Webhooks signature and the five-minute tolerance, rejects forged or replayed deliveries, sits behind the hostility proxy, feeds the inbox; endpoint registered with Tushe
Priority: P0
Requirement IDs: REQ-API-008, REQ-ENV-005, REQ-SEC-002; SoT IDs: INV-29
Rationale: Webhooks stay active on Noema's test tenants alongside the event feed, for replay and deduplication tests (AT-06); they are never needed for correctness. Tushe delivers only to public HTTPS endpoints. DEC-2026-10-12, Amendment 1 (D5).
Modules touched (allowlist; all paths in the `noema` repository, DEC-2026-10-13) [REC, pending engineering-lead approval]: services/core/adapters/synthetic_tushe/webhooks/; deploy/compose/ (receiver profile only); tests   ← nothing else may change
Contracts: inbound event (PERD §39.6); bump required? N
Inputs/outputs: Tushe webhook deliveries over public HTTPS → hostility proxy → receiver → inbox rows (the same inbox as the ENV-10 poller)
Acceptance criteria:
  REQ-API-008:
  - A replayed event SHALL create no second inbox row and change no state; a forged event SHALL be rejected.
  REQ-ENV-005:
  - Each proxied fault SHALL have a test proving it is observed by the adapter exactly as specified.
  - Every proxy fault family SHALL reproduce from a scenario and seed; the same Tushe number SHALL always map to the same synthetic number; no `9999` test-number pattern SHALL appear in any response delivered to a system under test.
  REQ-SEC-002:
  - Connection tests run from inside each container SHALL show that every forbidden route fails.
  Task "Done when" (plan v1.3): a replayed delivery arrives twice with the same delivery ID and is recorded once; a forged signature is rejected; reachable from Tushe before Fri 16 Oct
Tests to write FIRST (AGENT-11): EC-E07, EC-X17, and the replay test for AT-06 (same delivery ID twice, one inbox row)
Faults to exercise (AGENT-12): forged signature; timestamp outside the five-minute tolerance; replayed delivery (source TUSHE); event-delivery faults on the webhook-receiver path (source PROXY)
Dependencies: PLT-01, GOV-20, ENV-09; REQ-API-008, REQ-ENV-005, REQ-SEC-002
Out of scope: using webhooks for correctness (the feed stays the main source, ENV-10); exposing any other Noema component; deduplication and late-evidence handling beyond the inbox (OUT-04)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: EL, with a coding agent.
