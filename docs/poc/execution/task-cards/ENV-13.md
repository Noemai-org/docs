# Task card: ENV-13

Plan v1.5 task ENV-13 (first added in plan v1.3 as a public receiver; redesigned as the webhook relay by DEC-2026-10-16 E6). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decisions: [DEC-2026-10-12](../../../decisions/DEC-2026-10-12-tushe-environment-scope.md), Amendment 1 (D5); [DEC-2026-10-16](../../../decisions/DEC-2026-10-16-execution-reset.md) E5 (a test-environment component, not a Noema deployable), E6 (the relay) and E2 (point 4).

```
TASK-P2-013  ENV-13 · Webhook relay (`synthetic/webhook_relay/`): a public HTTPS relay on one small host that runs nothing else and holds only the webhook signing secret. It verifies the Standard Webhooks signature and the five-minute tolerance, rejects and counts anything unverified, and stores each verified delivery unchanged, keyed by delivery ID. The core pulls verified deliveries over an authenticated outbound connection to an allowlisted host into its inbox, which deduplicates by delivery ID; in the benchmark profile the hostility proxy sits on the pull. Endpoint registered with Tushe
Priority: P0
Requirement IDs: REQ-API-008, REQ-ENV-005, REQ-SEC-002; SoT IDs: INV-29
Rationale: Webhooks stay active on Noema's test tenants alongside the event feed, for replay and deduplication tests (AT-06); they are never needed for correctness. Tushe delivers only to public HTTPS endpoints, so something must face the internet, and nothing on the internet may reach the core or hold a credential worth stealing. DEC-2026-10-12, Amendment 1 (D5); DEC-2026-10-16 E6.
Modules touched (allowlist; all paths in the `noema` repository): synthetic/webhook_relay/ (the relay and its host configuration); services/core/adapters/synthetic_tushe/webhooks/ (the core's pull client only); deploy/compose/ (relay profile for local runs only); tests   ← nothing else may change
Contracts: inbound event (PERD §39.6); bump required? N
Inputs/outputs: Tushe webhook deliveries over public HTTPS → relay (verified deliveries stored by delivery ID) → core pull (outbound only; through the hostility proxy in the benchmark profile) → inbox rows (the same inbox as the ENV-10 poller)
Acceptance criteria:
  REQ-API-008:
  - A replayed event SHALL create no second inbox row and change no state; a forged event SHALL be rejected.
  - The relay SHALL reject and count a delivery with a bad signature or a timestamp more than five minutes off, and such a delivery SHALL never reach the inbox.
  - The relay's environment and configuration SHALL contain no credential other than the webhook signing secret.
  - No connection from the internet to the core SHALL be possible; the core's connection to the relay SHALL be outbound only.
  REQ-ENV-005:
  - Each proxied fault SHALL have a test proving it is observed by the adapter exactly as specified.
  - Every proxy fault family SHALL reproduce from a scenario and seed; the same Tushe number SHALL always map to the same synthetic number; no `9999` test-number pattern SHALL appear in any response delivered to a system under test.
  REQ-SEC-002:
  - Connection tests run from inside each container SHALL show that every forbidden route fails.
  DEC-2026-10-16 E2 (point 4), separation of duties:
  - The founder who drives the relay SHALL NOT approve its fault plans; the benchmark owner owns them.
  Task "Done when" (plan v1.5): a replayed delivery arrives twice with the same delivery ID and the inbox records it once; a forged or stale-signature delivery is rejected and counted and never reaches the inbox; the relay's environment holds only the signing secret; the core's connection to the relay is outbound only; the endpoint is reachable from Tushe before the G0-T session. The founder who drives this does not approve its fault plans (DEC-2026-10-16 E2, point 4)
Tests to write FIRST (AGENT-11): EC-E07, EC-X17, and the replay test for AT-06 (same delivery ID twice, one inbox row); a configuration test that the relay's environment holds only the signing secret; a network test that the core accepts no inbound connection and reaches only the allowlisted relay host
Faults to exercise (AGENT-12): forged signature; timestamp outside the five-minute tolerance; replayed delivery (source TUSHE); event-delivery faults on the core's pull (source PROXY)
Dependencies: PLT-01, GOV-20, ENV-09; REQ-API-008, REQ-ENV-005, REQ-SEC-002
Out of scope: using webhooks for correctness (the feed stays the main source, ENV-10); any credential on the relay other than the signing secret; running the hostility proxy on the public host; exposing any other Noema component; deduplication and late-evidence handling beyond the inbox (OUT-04)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: EL, with a coding agent.
