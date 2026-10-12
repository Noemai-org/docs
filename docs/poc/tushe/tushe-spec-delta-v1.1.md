# Requested changes to the Noema × Tushe specification (v1.0 → v1.1)

> **12 Oct 2026:** the proposed AT-25 (simulated-time reporting) is withdrawn; Tushe will not run a global clock (DEC-2026-10-12, D3).

> **Status: draft, not yet sent to Tushe.** This delta is shared with the Tushe team only after the founder approves it. Once agreed and re-issued, it becomes specification v1.1; the issued v1.0 ([`Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md`](Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md)) stays unchanged.

These are the changes we would like to make to the *Noema × Tushe Synthetic Enterprise Environment: Technical Requirements & Acceptance Specification v1.0*. Requirement and test IDs refer to v1.0. IDs marked "proposed" are new and are confirmed only when v1.1 is issued.

## 1. Concurrency control on cases and disputes (CON-01, raised from P1 to P0)

For case and dispute resources, CON-01 becomes **P0**:

- every read returns a version token (for example an ETag or a version number);
- every update, and create-with-deduplication, accepts an expected version (for example `If-Match` or an `expected_version` field);
- if the stored version differs from the expected version, the service rejects the request with a distinct error, separate from validation and authorisation errors, and applies no change.

## 2. Lookup by client idempotency key (new, P0)

**IDP-07 (proposed), P0 — Idempotency-key lookup.** Case creation accepts a client-supplied idempotency key, and the case service supports looking up a case by that key with ordinary integration credentials, so a client can find out whether a request whose response was lost actually created a case.

## 3. Extended fault classes (§7)

The following are added to the failure classes in §7. Each must be reproducible from a scenario ID and seed (CHA-01, CHA-02) and visible in privileged diagnostics (CHA-05, CHA-06):

- HTTP 429 with and without a `Retry-After` header, and burst throttling;
- schema drift: added, renamed or missing fields, and unknown enum values, switchable by scenario;
- responses timed around the client timeout: just before it and just after it;
- clock skew between sources (for example ledger, switch and settlement reporting different times for the same event).

## 4. Pagination (API-05, raised from P1 to P0)

API-05 becomes **P0**, and the scenario engine can produce:

- partial pages;
- histories that change between page requests (records added or updated while a client is paging).

## 5. Delayed settlement under the virtual clock (TIM-04, confirmation requested)

Please confirm that TIM-04 covers settlement that arrives hours of simulated time after the transfer, with the corresponding settlement events emitted at the scheduled simulated time, so that tests can advance the clock and observe a pending settlement become settled, failed or reversed.

## 6. Simulated time on ordinary responses (new, P0)

**TIM-05 (proposed), P0 — Simulated time visible to ordinary clients.**

- Every ordinary API response carries the current simulated time (for example in a response header).
- A read-only endpoint returns the current simulated time.
- Both are reachable with ordinary integration credentials, so the integrating system can follow the virtual clock without control-plane access.

## 7. Additional acceptance tests (proposed)

| ID | Test | How we check | Pass condition |
|---|---|---|---|
| AT-21 | Conditional update after a concurrent change | Read a case, change it through another principal, then update it with the first version token. | Update rejected with the distinct version-mismatch error; no change applied. |
| AT-22 | Idempotency-key lookup after commit-then-timeout | Run commit-then-timeout on case creation, then look the case up by the client key. | The committed case is returned; no second case exists. |
| AT-23 | Seeded 429 with `Retry-After` | Run a scenario that returns 429 with `Retry-After` on a configured request. | The 429 and its `Retry-After` value reproduce with the same seed. |
| AT-24 | Schema-drift profile switched by scenario | Run the same request under two scenarios, one with a schema-drift profile. | Responses differ only as the drift profile specifies, and diagnostics show the profile. |
| AT-25 | Simulated time reported consistently | Read the simulated time from ordinary responses and the read-only endpoint, then advance the clock through the control plane. | Simulated time is reported consistently on every ordinary response and advances only when the control plane advances it. |
