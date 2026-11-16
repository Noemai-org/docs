# Tushe specification delta v1.3: the routes of Tushe's addendum of 15 Nov 2026

Date: 16 November 2026 · Status: **interim; drafted by the Repo Steward at the Architect's ruling A248; counts once a Founder who did not author the pull request approves and merges it (A111).** It adopts the routes of [Tushe's addendum of 15 Nov 2026](responses/2026-11-15-tushe-addendum-to-reply-of-10-nov.pdf) **exactly as the addendum states them** and adds nothing. It is a delta beside the frozen specification v1.0 and delta v1.2; it edits no frozen file. It is Noema's internal record of what to build against; sending anything to Tushe is for the Founders.

**Two cautions that stay true.** (1) Every row below is **Tushe's statement, not yet observed by Noema** (AGENTS §2, item 4): the joint session and the AT report decide acceptance, and a route that behaves differently is reported as a Tushe discrepancy (plan §18). (2) The earlier internal file [`tushe-spec-delta-v1.3-draft.md`](tushe-spec-delta-v1.3-draft.md) (request R14, an account-state read surface, never sent) is a different matter: this delta does not adopt, withdraw or renumber it; R14 stays open.

## 1. Faults (addendum §1 and §2; A240, A247)

| Fault | Where it lives | How (the addendum's words) | Noema's side |
|---|---|---|---|
| duplicate | Tushe | `POST /partners/webhooks/messages/{id}/replay` re-delivers the same message; the receiver sees the same `webhook-id`, which is also its idempotency key, and both attempts appear in the delivery log | use the replay route (A240) |
| timeout | Tushe | hold the response past Tushe's **12-second** delivery timeout; it is recorded as a distinct `timeout` outcome, separate from `connection_error` and `http_error`, and the retry ladder follows | our receiver holds the response; **the bench hold is 15 s** (A247) |
| stale, reordered, drift | Noema's harness proxy | ordering and timing faults sit in the proxy, under Noema's control; Tushe builds none into the platform | IL adds them to the hostility proxy (AT-07, A240) |

## 2. The read-only credential (addendum §3)

| Route | What the addendum says |
|---|---|
| `POST /partners/api-keys` | body `{ "environment": "test", "description": "noema-harness-readonly", "scopes": ["events:read", "audit:read", "accounts:read", "customers:read", "cards:read", "bills:read", "compliance:read", "group_savings:read"] }` creates a partner API key with read-only scopes |
| `GET /partners/api-keys/scopes` | lists everything grantable |
| `POST /partners/api-keys/{keyId}/rotate`, `POST /partners/api-keys/{keyId}/renew`, `DELETE /partners/api-keys/{keyId}` | rotation, renewal and revocation, independent of the runtime and fixture keys (the addendum names them as `/{keyId}/rotate`, `/renew` and `DELETE`) |
| rule | an empty scope list is refused rather than meaning "everything" |

The Founder creates the key (A240); its value goes in the bench Environment only (INV-22). Administration stays on the dashboard session; no machine credential is issued into the privileged surface (addendum §3).

## 3. Reads (addendum §3, §4, §7)

| Route | What the addendum says |
|---|---|
| `GET /v1/events?after={sequence}&limit=50` | read forward from a cursor; **paginate on `sequence`, never on a timestamp** (two events in the same millisecond have no defined order) |
| `GET /v1/events/{id}` | one event |
| `GET /v1/audit-events` | the audit trail |
| `GET /v1/accounts/{accountId}/payouts/{payoutId}/transitions` | the transition log, oldest first, per transition: `seq`, `lifecycle`, `fromState`, `toState`, `source`, `sourceRef`, `inferred`, `injected`, `reason`, `occurredAt`, `observedAt`, `actor`, `request.{id, idempotencyKey}` |
| point in time | there is no "state as at T" endpoint and none is added: fold the transitions up to a timestamp and take `toState` |
| correlation and causation | not on the transition row; join to `/v1/events` on `traceId` (a two-call join) |
| retention | 30 days is the only figure Tushe commits to |

## 4. Webhook endpoints (addendum §5, §6)

| Route | What the addendum says |
|---|---|
| `POST /partners/webhooks/endpoints` | register the address |
| `PUT /partners/webhooks/endpoints/{id}/subscriptions` | choose the events |
| `POST /partners/webhooks/endpoints/{id}/send-test` | verify the path end to end |
| `POST /partners/webhooks/endpoints/{id}/rotate-secret` | the signing secret, "yours to rotate" |
| `POST /partners/webhooks/endpoints/{id}/recover` | with the endpoint disabled, recover a missed window (AT-05); or read the event feed forward |

The relay's address is registered by the Founder and lives only in a GitHub Environment (A240; DEC-2026-11-05 D5): **no address, key or secret value is written in any repository file.**

## 5. What this delta does not do

- It does not change any AT, requirement or date of the specification or delta v1.2. Tushe says its claimed ATs are unchanged except M-13's contribution to AT-07, which Tushe declines (addendum §9).
- It does not make a request of Tushe. Tushe's four outstanding items (M-06, M-07, M-16, M-17, "by Wednesday 18 November") are Tushe's.
- **Governing list.** `docs/poc/tushe/README.md` lists what governs endpoint semantics (DEC-2026-10-16 E10). This pull request adds this delta to that list there. `AGENTS.md` §2, item 4 carries the same list and is vendored in `noema`; adding the delta there is a one-line change the Steward proposes separately, because it needs a re-point of the copies (REQ-OPS-005).
- What it unblocks (A248): BO's reader (the read-only key and the feed) and IL's proxy entries (the faults of §1).
