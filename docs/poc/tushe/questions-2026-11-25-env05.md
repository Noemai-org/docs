# Questions for Tushe from the ENV-05 build (draft for the Founder to send)

> **INTERNAL HEADER. REMOVE EVERYTHING ABOVE THE LINE "SEND FROM HERE" BEFORE SENDING.**
>
> **Date:** 25 November 2026 · **Status:** DRAFT, not sent. The Founder sends it with the OpenAPI request; the Steward does not send it.
> **Source (internal):** `status/ENV-05.md` in `noema` (the eight unstated items), and ruling A667 (`DEC-2026-11-25-architect-rulings-a657-a667`).
> **Why the split:** AGENTS §11 keeps internal strategy, benchmark detail and hidden test material out of any document meant for an external partner. Only the section below the line goes out. Do not add repository names, pull-request numbers, ruling IDs or Noema's design to it.

---

## SEND FROM HERE

**Questions on Tushe's read behaviour (25 November 2026).** We built from the specification v1.0, delta v1.2 and v1.3, and your response of 7 October 2026 only, and guessed no field, route or value. Eight things are not stated in those documents. Please answer each one, or point us to the document that does.

| # | Question |
|---|---|
| 1 | **Beneficiary and name enquiry.** Is there a route, a request and a response for a beneficiary or a name enquiry? We asked about an ambiguous name enquiry (R9) on 30 October and have no recorded answer. |
| 2 | **Settlement and destination as objects.** Is there a read of a settlement or of a destination account (a settlement reference, a batch, evidence of settlement), or only the two lifecycles in the transition log? |
| 3 | **The switch's own state** (R4: raw code, normalised status, whether it is final). Where does it live: a payout member or a log lifecycle? We asked on 23 October. |
| 4 | **The status query** `POST /v1/accounts/{accountId}/payouts/{payoutId}/status-query`: its request body, its response beyond `outcome` (`terminal`, `pending`, `unreachable`, `cooling_down`, `retryAfterSeconds`), and its credential scope. The read-only key of delta v1.3 section 2 has no scope for it. |
| 5 | **R6: please confirm in writing that a status query never moves money**, under any outcome, retry or replay. We asked on 16 October. |
| 6 | **Transition rows.** Do the `lifecycle` values and the `fromState` and `toState` strings in a row use exactly the spellings and casing in your response of 7 October (section 4.1), or others? |
| 7 | **"State at time T".** When a state is read as of a timestamp, is it `occurredAt` or `observedAt`, and does a row at exactly T count? |
| 8 | **The OpenAPI document and the event schemas**, including: credential presentation, list envelopes and field types, the event types and members beyond `id`, `sequence` and `traceId`, the webhook header names, and the payout read. |

**Order that helps most:** the OpenAPI document first, then item 5 (R6), then items 1 to 3.
