# Demo pre-flight: Fri 6 Nov 2026

<!-- Source: plan §14 (NOEMA_POC_4WEEK_PLAN_v1.1.md). Fill on the day; never in advance. -->

**Rules.** Every scenario runs live from the release build against Tushe, with the evidence panel open. Nothing is scripted, edited or replayed from video. If a scenario fails in the dry run, it is dropped and the drop is said out loud.

## Pre-flight at 13:00 WAT

- Release run ID: <!-- From the G6 record. -->
- Person holding the stop decision: <!-- TODO(FND): one named person (plan §14). -->

- [ ] `make reset` to the release seed <!-- Tick only once checked on the demo host. -->
- [ ] Run IDs recorded <!-- Tick only once checked on the demo host. -->
- [ ] Kill switch confirmed off for the demo tenant <!-- Tick only once checked on the demo host. -->
- [ ] Masking spot-checked <!-- Tick only once checked on the demo host. -->
- [ ] Device, audio and network checked <!-- Tick only once checked on the demo host. -->
- [ ] Consent forms in hand for any live voice <!-- Tick only once checked on the demo host. -->
- [ ] Evidence panel and scorecard open <!-- Tick only once checked on the demo host. -->
- [ ] One named person holds the stop decision <!-- Tick only once checked on the demo host. -->

## Stop rule

**Stop rule.** If a safety anomaly appears during the demo, stop, say so, and preserve the run. It becomes a regression case that afternoon.

## Run order (plan §14, verbatim)

| Order | Scenario | Case | Driver | Shows | Fallback if it fails at 09:00 |
|---|---|---|---|---|---|
| 1 | D4 Timeout after a safe write | US-06 | C1 | OUTCOME_UNKNOWN, verify by key, ACHIEVED, dispatch count 1 | None. This is the core proof; if it fails, the demo opens by saying so |
| 2 | D1 Ambiguous transaction, clarified in Pidgin | US-02 (voice) | V | Two options, no write before the answer, Intent Object v2 | Text in Pidgin if G5 did not pass |
| 3 | D2 Cross-system conflict | US-03 | C2 | Honest "unknown", do-not-resend, one case | Drop |
| 4 | D5 Duplicate submission | US-05 | C1 | Same key, one case | Drop |
| 5 | D6 Policy mutation mid-flight | US-08 / US-20 | C1 | Grant voided, both versions in the Record | Drop |
| 6 | D3 SLA clock near breach | EC-T05 | C2 | Clock fields labelled SYNTHETIC, prioritised routing | Drop |
| 7 | D7 Injection in a narration | US-09 | SR | Treated as data, security event | Drop |
| 8 | D9 Prohibited monetary attempt, customer and evil provider | US-10, ADV-08 | SR | REJECT at Trust; no reads before it; no code path | Drop |
| 9 | D10 "Close the complaint" | US-22 | C2 | REJECT; the case stays open | Drop |
| 10 | D8 Full reconstruction | US-12 | EL | Causal chain with Record IDs; chain verified | Drop |
| Close | Scoreboard and comparison | Release run ID | B | Tier 0 first; curve; arms, including where they win | — |

Scenarios dropped at the 09:00 dry run: <!-- List each dropped scenario; the drop is said out loud at the demo (plan §14). -->
