# DEBT-02: a human is alerted when a signature fails (design for the founders)

Date: 2026-11-03. Owner of the alert rule and its fixture: SR. Owner of the channel decision and the PERD text: EL (DEBT-02). Status: **Design adopted by the Architect on 3 Nov 2026 (recipients: both founders); it counts as a decision once the Engineering Lead records it. Nothing is built.** It answers OD-P-71 (a)–(f) and extends it to the new failure classes that the signing design (docs#80) and anchoring (REQ-AUD-007) create. Source of the requirement: the Founders, 29 Oct 2026 ("a human must be alerted when a receipt signature fails"); [`DEC-2026-10-29-receipt-signature-alert`](../decisions/DEC-2026-10-29-receipt-signature-alert.md). Non-normative until a decision record adopts it.

## 1. What must alert a person (the classes)

Today only one event exists, `SECURITY_EVENT SIGNATURE_INVALID` from the Controller, and nothing reads it. Under the signing design there are more ways a signature or the Record can fail, and **some of them leave no Record event at all**, which is why a Record-only alert cannot be enough.

| # | Failure | Where it is first seen | Record event? | Class |
|---|---|---|---|---|
| A1 | The Controller finds a receipt signature invalid | core (`noema#90`) | `SECURITY_EVENT SIGNATURE_INVALID` (own transaction) | page |
| A2 | The database trigger refuses an insert whose signature does not verify (`NS001`), e.g. a stolen credential forging a receipt | Postgres | **none** (the transaction aborts; nothing can be appended in it) | page |
| A3 | Verification is unavailable (extension or library missing, function raising): inserts fail closed | Postgres and core | **none** (no append succeeds while verification is down) | page |
| A4 | The chain verifier finds a break, a bad signature, or an event under a revoked key | core (nightly or on demand) | `SECURITY_EVENT` | page |
| A5 | An anchor does not match the live chain, or an anchor is missed after its retries | core (REQ-AUD-007) | `SECURITY_EVENT` for a mismatch; none if the store is unreachable | page (mismatch), notify (a single miss) |
| A6 | The core or the database is down or silent | nothing reports it | none | page (dead-man's switch) |

A2, A3 and A6 are the reason for the design below: they produce **no Record event**, so an alerter that only reads the Record misses exactly the attacks that bypass the core.

## 2. Requirements for the path

1. **Independent of the failing component.** It must work when Postgres, the core or the signing extension is the thing that failed (OD-P-71 b).
2. **No new egress for the core.** The core has no route out (INV-29, PERD §65.1, REQ-SEC-002). The channel must not give it one.
3. **No customer data in an alert.** An alert carries the class, key id, counts, the correlation id and a time. It is scanned by SEC-07.
4. **A person receives it, and acknowledges it.** A log line or a Record event is not an alert. Closure needs a drill in which a founder receives and acknowledges a live page.
5. **Rate-limited, not silent.** One page per (class, key id, source) per 15 minutes with a count, so a repeating fault is one page that updates (OD-P-71 d).
6. **Its own failure is visible.** A failed delivery is retried, then written locally and counted; a daily test page that no one acknowledges is itself an alert (OD-P-71 c).

## 3. Options

| | Option | Meets 1 | Meets 2 | Meets A2/A3/A6 | Cost | Verdict |
|---|---|---|---|---|---|---|
| O1 | The core sends the alert itself (HTTP or SMTP) | no: dies with the core | **no**: needs core egress | no | low | rejected |
| O2 | An **alerter service** on its own network with the only route out. It reads three things: the core's metrics endpoint, a **read-only** database role over `SECURITY_EVENT` rows, and the Postgres log (a mounted read-only volume). It pages through one pluggable outbound channel | yes | yes | yes (log for A2, silence for A6, metrics for A3) | one new service, one network, one read-only role | **recommended** |
| O3 | A watcher on a **second owner's host** that polls the stack's metrics and the anchor store | yes, strongest | yes | A6 and A5 only; A2 needs the database log, which is not exposed | needs a published metrics endpoint | compatible later; not enough alone |
| O4 | Status quo: record and log only | n/a | n/a | no | none | fails the Founders' requirement |

## 4. Recommended design (O2)

- **Service.** `alerter`, in the `ci`, `bench` and `demo` profiles and in production. It joins `edge_net` (the core's metrics, health and the ops inspector) and a new network `alert_egress`, the **only** non-internal network it holds besides none other. It does **not** join `data_net`; it reaches Postgres through a read-only role over a connection that the core's network policy already allows for readers. (If the founders prefer, `data_net` membership is the alternative, and the profile check `deploy/compose/netcheck/profiles.py` gets the matching rule.)
- **Credentials.** A database role `alert_ro` with `SELECT` on `record_event` (and `ops_alert`) only; no write; not a member of any runtime role; not the migrator. The channel secret is a file-mounted secret that the core never mounts. An egress allowlist of one host (the channel).
- **Triggers.** A1, A4, A5-mismatch: a new `SECURITY_EVENT` row. A2: an `NS001` line in the Postgres log (`log_min_error_statement = error`; the log volume is read-only in the alerter and absent from the core). A3: the core's `noema_verification_unavailable` gauge, and the Postgres `could not access file` / missing-function errors in the same log. A5-miss and A6: the absence of a heartbeat metric for 2 minutes, or the metrics endpoint refusing connections (dead-man's switch).
- **Payload.** `{class, severity, key_id, source, count, first_seen, last_seen, correlation_id, runbook}`. Nothing else.
- **Record of the alert.** When the database is up the alerter does **not** write to it. The core appends `OPS_ALERT_RAISED` and sets `ops_alert` (PERD §32.2, §38.2) when it can; the alert's authority is the page, not the row. The gauge `noema_ops_alert_open` (§44.1) counts open alerts.
- **Channel (recommended).** Two independent deliveries to **both founders**, who hold the Security Reviewer role (DEC-2026-10-16 E2): a **push notification with acknowledgement** and an **email**, each with a retry of three attempts at 10 s, 30 s and 90 s. If neither delivers, the alerter writes the alert to a local file, raises `noema_alert_delivery_failed_total`, and the ops inspector shows it. An unacknowledged page escalates to the second founder after 10 minutes. The vendor of the push service is not chosen here (nothing in this repository names one, and I have not verified any vendor's documentation).
- **Canary.** A synthetic test page every day at a fixed time; two missed acknowledgements in a row is an alert of its own.

## 5. Test plan (SR owns; fixtures use a local HTTP sink in CI, not a real person)

| ID | Test | Passes when |
|---|---|---|
| D2-1 | Forge a receipt signature through the Controller (A1) | the sink receives one page within 30 s, with class, key id and no customer data |
| D2-2 | As `execution_rw`, insert a forged receipt directly, with no core involved (A2) | the sink receives a page from the log within 30 s, though no Record event exists |
| D2-3 | Drop the extension or remove its library file (A3) | a page within 30 s; inserts still fail closed |
| D2-4 | Corrupt one Record row offline and run the verifier (A4); rewrite the chain against an anchor (A5) | a page for each |
| D2-5 | Stop the core, then stop Postgres (A6) | a page within 3 minutes for each, from silence alone |
| D2-6 | Fifty failures in one minute | one page with a count, then one update per 15 minutes |
| D2-7 | The sink refuses delivery | three retries, the local file written, the failure counter incremented, the inspector shows it |
| D2-8 | Every payload is scanned (SEC-07) | no personal identifier, account number or secret |
| D2-9 | **The drill:** a live page to both founders | both receive it, one acknowledges, the other is not paged again; recorded as evidence for DEBT-02 closure criterion (2) |

D2-1 to D2-8 run in CI. D2-9 is a drill by people and is the only test that proves a human is alerted.

## 6. What this needs, and when

- **Decisions (founders):** recipient and channel (4 above); approval of a new service and network under AGENT-14; the PERD v1.20 text (§44.1 rows for `noema_signature_invalid_total`, `noema_verification_unavailable`, `noema_alert_delivery_failed_total`; `ops_alert` kinds for these classes); how the alerter reads the Postgres log. The core engineers build the metrics; SR builds the fixtures and the drill.
- **Schedule (proposed, no scope cut):** decision by Fri 6 Nov; alerter and metrics built by G2 (Fri 20 Nov); D2-1 to D2-8 green by G3 (Fri 4 Dec); the live drill D2-9 before the code freeze (Wed 9 Dec).
- **Consequence of not deciding:** DEBT-02 stays open, a stolen-credential forgery (A2) is refused by the database but **no one is told**, and the demo would have to say so.

## 7. Escalation (charter §6 format)

**Decision required (§6 items 3 and 6: a security boundary; a new service).** How is a human alerted when a signature fails, given that three of the six failure classes leave no Record event and the core may not have egress?

**Options:** O1 rejected (core egress); **O2 recommended** (alerter service, read-only role, one outbound channel); O3 complementary (second owner's watcher, strongest separation, covers only A5/A6); O4 does not meet the requirement.

**Effort / risk / impact / maintenance of O2:** about 4 days of core-engineer work (metrics) plus 3 days of mine (fixtures, drill); the alerter is a bridge between the database and the outside, which is why it holds a read-only role, a one-host allowlist and a fixed payload; it adds one service to maintain.

**Recommendation:** O2, to both founders, push with acknowledgement plus email, daily canary.

**Questions:** (1) Are both founders the recipients, and who is the escalation after 10 minutes? (2) May the alerter read the Postgres log through a read-only volume? (3) Is a hosted push service acceptable, and which may I verify? (4) May the service be added now (AGENT-14)?


## 8. Decisions of 3 Nov 2026, and what the implementation PR must name

Relayed by the Architect.

1. **The design of sections 3 and 4 is adopted, with both founders as recipients.** Escalation after 10 minutes unacknowledged goes to the founder who was not paged first.
2. **The alerter service is approved under AGENT-14 on one condition:** the implementation PR names every dependency with its **exact name, licence and pinned version**. My intention, so that the list can be short: the alerter is written in Go using only the standard library (`net/http` for the push call, `net/smtp` or an HTTPS mail API for email, `log/slog`), so the only third-party item is the push service itself, which is a service and not a library. The Go toolchain is the version already pinned in `go.mod`. If the implementation needs any module, the PR lists it and its licence; I will not add one silently.
3. **Postgres log access is a least-privilege read-only role.** Concretely: a role `alert_log_ro` with `EXECUTE` on one function, `alert.read_log(from_offset bigint, max_bytes int)`, owned by the migration role, `SECURITY DEFINER`, `SET search_path = pg_catalog, pg_temp`, which reads only the files in the log directory (it refuses any other path) and returns lines. The role is **not** a member of `pg_read_server_files` or `pg_monitor`, which would read far more. To keep the log free of statement text (a failed insert's statement could carry receipt content), the log is configured with `log_destination = jsonlog`, `log_min_error_statement = panic` and `log_error_verbosity = terse`; `NS001` is recognised by its SQLSTATE and message alone. A test (D2-10) pins all of this: the role can call the function and nothing else; the function refuses a path outside the log directory; the log of a forced `NS001` contains no statement text.
4. **The hosted push service: I name Pushover, and nothing is verified yet.** The requirement is a push that is repeated until a person acknowledges it, with a way for the alerter to learn the acknowledgement. From memory, Pushover's emergency priority does this (repeat interval and expiry parameters, and a receipt that reports acknowledgement), for a small one-time fee per person per platform and a free monthly message allowance far above what an alert path sends. **That is NOT VERIFIED: its documentation host is unreachable from my session.** To close it by Thu 5 Nov I need the Founder to attach three pages: Pushover's API documentation (priority and receipts), its pricing page, and its terms and privacy page (to confirm it stores only the fixed payload). The fallback if any of that fails is ntfy (open-source; hosted or self-hosted), which has no acknowledgement tracking, so the email channel would carry the acknowledgement and the 10-minute escalation would run from the alerter's own state. The mail channel needs a sending account: I propose each founder's own mailbox with an app-specific password in a file-mounted secret, and I ask the Founder to confirm that or name another.
5. **Schedule unchanged:** the alerter and the core metrics by G2 (Fri 20 Nov); D2-1 to D2-10 green by G3 (Fri 4 Dec); the live drill D2-9 before the code freeze (Wed 9 Dec).

**Open for the Founder:** (a) attach the three Pushover pages by Thu 5 Nov; (b) confirm the mail channel; (c) confirm that the alerter may be a new Compose service on its own network (`alert_egress`), which also needs a rule in `deploy/compose/netcheck/profiles.py` (I will add it with the service).
