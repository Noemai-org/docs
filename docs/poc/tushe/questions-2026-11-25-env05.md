# Questions for Tushe from the ENV-05 build (draft for the Founder to send)

**Date:** 25 November 2026 · **Status:** DRAFT, not sent. The Founder sends it with the OpenAPI request; the Steward does not send it. SYNTHETIC build; no real data. Source: `status/ENV-05.md` in `noema` (noema#961's branch), ruling A667 (`DEC-2026-11-25-architect-rulings-a657-a667`).

**Scope.** We built from the specification v1.0, delta v1.2 and v1.3, and Tushe's response of 7 October 2026 only, and guessed no field, route or value. Eight things are not stated in those documents. Please answer each one, or point us to the document that does. This list holds no internal strategy, benchmark detail or hidden test material.

| # | Question | Why we ask |
|---|---|---|
| 1 | **Beneficiary and name enquiry.** Is there a route, a request and a response for a beneficiary or a name enquiry? We asked about an ambiguous name enquiry (R9) on 30 October and have no recorded answer. | No beneficiary adapter can be built without it. |
| 2 | **Settlement and destination as objects.** Is there a read of a settlement or of a destination account (a settlement reference, a batch, evidence of settlement), or only the two lifecycles in the transition log? | We read settlement and arrival only through the lifecycles today. |
| 3 | **The switch's own state** (R4: raw code, normalised status, whether it is final). Where does it live: a payout member or a log lifecycle? We asked on 23 October. | We keep the raw code and the semantic status side by side and need to know where each comes from. |
| 4 | **The status query** `POST /v1/accounts/{accountId}/payouts/{payoutId}/status-query`: its request body, its response beyond `outcome` (`terminal`, `pending`, `unreachable`, `cooling_down`, `retryAfterSeconds`), and its credential scope. The read-only key of delta v1.3 section 2 has no scope for it. | The route is a POST. |
| 5 | **R6: please confirm in writing that a status query never moves money**, under any outcome, retry or replay. We asked on 16 October. | Noema has no callable path that can move money. Without this confirmation we do not call a POST on a target. |
| 6 | **Transition rows.** Do the `lifecycle` values and the `fromState` and `toState` strings in a row use exactly the spellings and casing in your response of 7 October (section 4.1), or others? | The response names them in prose only. |
| 7 | **"State at time T".** When a state is read as of a timestamp, is it `occurredAt` or `observedAt`, and does a row at exactly T count? | Delta v1.3 says only "fold the transitions up to a timestamp". |
| 8 | **The OpenAPI document and the event schemas**, including: credential presentation, list envelopes and field types, the event types and members beyond `id`, `sequence` and `traceId`, the webhook header names, and the payout read. | Open since 18 November. Until we have them, items 1 to 7 cannot become fields. |

**Order that helps most:** the OpenAPI document first, then R6, then items 1 to 3.
