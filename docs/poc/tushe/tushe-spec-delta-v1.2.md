# Changes to the Noema × Tushe specification (v1.0 → v1.2)

> **Status: records the exchange of 13 October 2026.** This file lists what Noema asked of Tushe, and what Noema agreed, in its response of 13 October 2026 and the acceptance worksheet sent with it. It adds nothing that those documents do not record. **The record is the PDF** ([`responses/2026-10-13-noema-response.pdf`](responses/2026-10-13-noema-response.pdf), SHA-256 `c1f1e33a7295a1b16998c5aff26d06a92bea5dbefd30613712f673f71f2c3e6a`) and the worksheet PDF ([`acceptance/G0-worksheet-2026-10-13-SENT.pdf`](acceptance/G0-worksheet-2026-10-13-SENT.pdf)); if this file disagrees with either, the PDF is right.
>
> Delta v1.1 ([`tushe-spec-delta-v1.1.md`](tushe-spec-delta-v1.1.md)) was never sent to Tushe and is superseded by this file. Nothing in v1.1 is requested of Tushe unless this file or the 13 October response says so. The issued v1.0 ([`Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md`](Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md)) stays unchanged.

Requirement and test IDs refer to v1.0. The three amended acceptance conditions below are proposals until both sides sign the worksheet in the joint session, whose date Tushe has not yet confirmed (DEC-2026-10-16 E4).

## 1. Amended acceptance conditions

### AT-01 · Deterministic replay: what "the same material fault sequence" means

Two runs count as **the same run** when all four of these match: the scenario key, the scenario version, the definition checksum (SHA-256) and the seed. Each run happens in its own freshly reset tenant.

The test passes when these six are identical in both runs. Any difference, even one transition or one kobo, fails it.

| # | What | In plain words | How it is checked |
|---|---|---|---|
| M1 | The objects | The scenario creates the same customers, accounts, beneficiaries and payouts, with the same IDs | Compare the ID lists; they must match exactly |
| M2 | The faults | The same faults, applied to the same objects, in the same order relative to each other | Compare the ordered list of (fault, target object) |
| M3 | Each object's path | For every object, the same sequence of state changes: from which state, to which state, and caused by what (`api`, `provider_webhook`, `watchdog`, `operator`, `backfill`) | Compare each object's ordered list of (from, to, source) |
| M4 | Where everything ends | Every object finishes in the same final state, on every lifecycle (`status`, `settlementStatus`, `arrivalStatus`) and in the ledger | Compare the final states and ledger balances |
| M5 | The money | Every amount, fee and balance is the same, to the kobo | Compare the integer kobo values |
| M6 | The events | The same events are emitted, each for the same object, in the same order for that object | Compare each object's ordered list of event types |

**May differ:** wall-clock timestamps (`occurredAt`, `observedAt`, `deliveredAt`); how long things took and the gaps between requests; global sequence numbers in the event feed; the order between different objects that have no causal link; row order where no sort applies.

The labels M1 to M6 are the worksheet's (section 1.1). The 13 October response lists the same six items in prose, without labels.

### AT-02 and AT-03 · Where "what actually happened" is read from

Noema accepts Tushe's counter-proposal (Tushe's §5.2) instead of a separate privileged-oracle endpoint, on two conditions:

- a programmatic, read-only partner-administrator credential that Noema's test harness can use without a browser, issued to one named person on Noema's side and never to the system under test;
- a refusal test: an ordinary API key calling any `/partner/...` route is refused.

"What actually happened" is then read from three places: the checksummed scenario definition; `GET /partner/events`; and the transition log, once its read endpoint ships (request R2).

### AT-15 · Time control

Noema accepts per-object time instead of an environment-wide clock. The amended pass condition: a transition scheduled through the `MMMM` delay fires at its scheduled time, and fires immediately when `POST …/simulate/advance` is called. No global freeze is required. In the response's words: "a scheduled transition fires at its scheduled time, and fires immediately on manual advance."

## 2. Requests R1 to R13, with dates

Dates are as sent on 13 October 2026. They are commitments Noema asked for and are not moved by Noema's own re-planning.

| # | Request | Date |
|---|---|---|
| R1 | **Tenants and credentials, in two batches.** Batch 1: 3 to 5 test-mode tenants, a read-only API key for each, one programmatic read-only administrator credential, and one test-mode payout-creating credential for building scenario histories (held by one named person on Noema's side, never by the system under test). Batch 2: the rest, to about 10 | Batch 1: Thu 15 Oct. Batch 2: Tue 20 Oct |
| R2 | **The read surfaces (E1):** transition history (STM-03), transaction history (REC-01), the correlated timeline (REC-02), causation on events (EVT-01, AUD-04), audit query by transaction, account, customer and correlation ID (AUD-05), and actor on the transition record (AUD-02, AT-19) | No later than Fri 23 Oct |
| R3 | **Seeded transaction histories:** past payouts with set beneficiary names, amounts, outcomes and `occurredAt` dates, including near-duplicates | No later than Fri 23 Oct |
| R4 | **Switch state as its own queryable dimension:** raw code, normalised status, and whether it is final | No later than Fri 23 Oct |
| R5 | No behaviour change on the sandbox from 13 Oct to 6 Nov without 48 hours' notice, and the sandbox version on every response | From now |
| R6 | Written confirmation that the status query can never move money or change balances | Fri 16 Oct |
| R7 | Test-mode rate limits and quotas, and the sandbox's hosting region | Fri 16 Oct |
| R8 | Answers to the questions in the response | Fri 16 Oct |
| R9 | **Ambiguous name enquiry (E6, AT-09).** Some lookups return a single exact name; some return several possible matches; some return a name that does not match the account. Set by the scenario and repeatable on replay | Fri 30 Oct |
| R10 | **Payout approval states (E6, AUTH-02):** pending, approved, rejected and expired, settable by scenario | Fri 30 Oct |
| R11 | **Scenario-definition richness (the rest of E4):** adversarial fixtures, faults and event schedules declared in the definition, ordered composition of several faults, and medium and large data tiers | Fri 30 Oct |
| R12 | **The diagnostics view (E5, AT-20):** what was injected, when, against which target, the configured behaviour and the actual outcome, plus a clear injected-versus-genuine-error flag. Tushe's existing markers serve as an interim until then | Fri 30 Oct |
| R13 | **Webhooks kept active on Noema's tenants,** delivering to a public HTTPS endpoint Noema registers, alongside the event feed | With batch 1 (Thu 15 Oct) |

## 3. Withdrawn

These were asked for in the v1.0 specification or proposed in the draft v1.1 (never sent). They are not asked of Tushe.

| Item | What it was | What replaces it |
|---|---|---|
| A global clock (TIM-01, TIM-02) | An environment-wide fast-forward clock | Per-object scheduling with on-demand advance (AT-15 above). Noema handles the rest of its time-sensitive testing on its own side |
| A GT-02 endpoint | A privileged answer-key endpoint | Tushe's partner-administrator surface, on the conditions in AT-02 and AT-03 above |
| Case-API items (CON-01, IDP-07) | Version tokens on cases, and lookup of a case by client idempotency key | Not needed: Noema writes to its own case system |
| Proposed AT-21 to AT-25 | Five additional acceptance tests proposed in the draft v1.1 | Withdrawn. AT-25 (simulated time reported consistently) fell with the global clock |
| A case or dispute domain | Cases and disputes hosted on Tushe | Out of scope for Tushe. Noema runs its own small synthetic case system. Disputes are not part of the POC |
