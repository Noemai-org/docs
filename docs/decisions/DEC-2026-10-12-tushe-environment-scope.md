# DEC-2026-10-12 · How the POC uses Tushe: scope, ground truth, time, faults and the G0 gate

| | |
|---|---|
| **Status** | Proposed. Founder approval required before merge |
| **Date** | 12 October 2026 |
| **Owner** | Founders (TODO: name). Reviewer: engineering lead (TODO: name) |
| **Prepared by** | Engineering lead, with the integration lead |
| **Amends** | SoT §36 "The synthetic enterprise environment" [DECISION] and its Phase A exit line; SoT §35.6 rule 4 [DECISION] (the time-source sentence only); SoT §40.1 (Phase A row); SoT §41 (Phase 0 exit gate) |
| **Closes** | The OD-P entries mirroring PERD OQ-03 (Tushe case API semantics) and OQ-10 (CI access to Tushe): OD-P-16 and OD-P-23. Amendment 1 opens OD-P-43 (PERD OQ-15, webhook receiver hosting), to be closed by plan task GOV-20 |
| **Supersedes** | None. Withdraws the proposed AT-25 (simulated-time reporting) in `docs/poc/tushe/tushe-spec-delta-v1.1.md`, because Tushe will not run a global clock |
| **Evidence** | *Tushe × Noema: Response to the Synthetic Enterprise Environment requirements*, Tushe engineering, 7 October 2026 (received 8 October 2026). To be committed unchanged as `docs/poc/tushe/responses/2026-10-07-tushe-draft-response.pdf` |

**Record fields (decisions README template).** The table above already gives Status, Date, Owner, Closes and Supersedes; the template headings it lacks point to the sections below.

- Status: Proposed (see the table above)
- Date: 12 October 2026 (see the table above)
- Closes: OD-P-16, OD-P-23 (see the table above)
- Owner: see the table above
- Decision: see section 2
- Rationale and evidence: see sections 1, 5 and 6, and the Evidence row above
- Affected requirement IDs / SoT sections: see sections 3 and 9
- Migration notes: see section 7
- Supersedes: see the table above

---

## 1. The short version

Tushe has already built the hardest things we asked for, and they are running today:

- a payment whose own record, the rail and the beneficiary are allowed to disagree;
- "unknown" that is never quietly turned into "failed";
- commit-then-no-answer on demand;
- seeded, resettable scenarios with predictable IDs;
- a replayable event feed;
- read-only credentials.

Four things are different from what SoT §36 assumed:

1. **Tushe has no case or dispute system, and doesn't plan one.** Every write Noema makes in the POC goes to a case system, so we build a small synthetic one ourselves.
2. **Tushe will not put a privileged "answer key" endpoint on the platform.** It offers an equivalent we can use: an administrator-only read surface that ordinary API keys cannot reach, plus checksummed scenario definitions.
3. **Tushe will not run one global clock.** It schedules time per object and lets us fire scheduled changes on demand.
4. **Some fault types are not in Tushe and won't arrive in time.** These are transport faults, stale reads, and dropped or reordered events. SoT §36 already tells us what to do in that case: run a thin hostility proxy ourselves.

None of this weakens a safety rule. No money moves, the oracle stays out of the runtime's reach, and every fault stays reproducible. What changes is **who provides which piece**. That needs a recorded decision, because SoT §36 is a [DECISION].

## 2. What we are deciding

### D1. Noema runs its own synthetic case service for the POC

- **What.** A small service, called `mock-case` in SoT §36, that acts as the bank's case system. It provides:
  - create a case with an idempotency key; find a case by that key;
  - a version token on every read; route a case with an expected version;
  - append-only evidence attachments;
  - a complaint reference.

  It implements exactly the case, complaint and evidence rows of PERD §34.4, and nothing more. It offers **no** operation to close or resolve a case, downgrade priority, change an SLA or clock, or edit or delete evidence: those capabilities are prohibited in the POC, so they don't exist on the target either. There are no disputes, because no POC capability touches a dispute.
- **Faults.** The service can be told by the benchmark runner to:
  - commit, then drop the response;
  - return a 5xx;
  - return a 429 with `Retry-After`;
  - reject a stale version;
  - split results across pages.
- **Ground truth.** Its own truth endpoint is reachable only from the benchmark network.
- **Independence**, because we are now building a system Noema writes to:
  - the integration lead builds it, never the core engineers (C1, C2);
  - it is built only from the PERD §34.4 contract;
  - the benchmark owner owns its fault plans and its truth endpoint;
  - its code sits outside `services/core`;
  - its contract tests run in CI;
  - Noema reaches it only through a normal adapter, so a partner's real case system can replace it later with no core change (REQ-NFR-006).
- **Why not wait for Tushe?** Tushe has asked whether cases are in their scope and has no plan to build them. Its version tokens (CON-01) are dated 12 December. Our timeout-after-write slice (G1) is due Friday 16 October and needs a case system that day.

### D2. Ground truth comes from Tushe's administrator surface, held only by the benchmark owner

- **What.** For Tushe-held state, "what actually happened" is established from three sources:
  1. the checksummed scenario definition and the fault each object was given;
  2. Tushe's partner-administrator event feed (`GET /partner/events`), which ordinary API keys cannot reach;
  3. Tushe's transition log, once its read endpoint ships.
- **Conditions.** All of these must hold, or D2 falls back to asking Tushe to build GT-02 as written:
  - Tushe issues a **programmatic, read-only** administrator credential, not a browser session;
  - only the benchmark owner holds it, and only the benchmark runner uses it;
  - it never appears in any runtime configuration;
  - an API-key refusal test proves ordinary credentials cannot reach those routes (AT-02).
- **Why.** Tushe's objection is fair. An answer key on the platform the agent drives is one credential mistake away from leaking. Their administrator surface gives the same isolation the SoT requires (INV-22, REQ-ENV-002), enforced by credential.

### D3. Time: per-object schedules on Tushe; our own clock for everything else

- **What.**
  - Tushe schedules each object's outcome in minutes (the `MMMM` field of its test account numbers) and fires it on demand (`POST …/simulate/advance`). There is no environment-wide freeze or fast-forward.
  - In runs against Tushe, Noema's clock interface uses the real wall clock.
  - Noema's simulated clock is used in tests that don't touch Tushe live: unit and integration tests, and cases replayed from recorded Tushe responses through our proxy.
  - Cases whose result depends on a time boundary (freshness limits, SLA phases, expiry) run on the simulated clock against recorded responses.
- **Pass condition AT-15** changes from "freeze, then advance the clock" to: "a scheduled transition fires at its scheduled time, and immediately on manual advance."
- **Why.** A global clock contradicts our own requirement that parallel runs must not disturb each other (Tushe spec DATA-05). Tushe also can't honestly provide one, because their database stamps rows with its own time. The SoT allows "a controllable simulated clock or an equivalent deterministic time mechanism" (Tushe spec TIM-01); per-object time is that mechanism.
- **Cost, stated plainly.** Replay near a time boundary can't be guaranteed against live Tushe. Running those cases on recorded responses keeps replay determinism (INV-21) intact.

### D4. Faults: two sources, one owner

| Fault family | Produced by |
|---|---|
| Decline before commit; commit then no answer; fail after accept; reverse after completion; never resolves; delayed outcome | Tushe test account numbers `9999SSMMMM` |
| Duplicate notification | Tushe replay (same delivery ID) |
| Timeout, disconnect, reset, 502/503/504, slow response, 429 | **Noema hostility proxy** in front of Tushe |
| Stale read (old version returned after a write) | **Noema hostility proxy** |
| Event lost, delayed, reordered, malformed or stale | **Noema hostility proxy**, on the event-feed poller path (D5) |
| Case-system faults | **Noema `mock-case`** (D1) |
| Impossible data (for example, a credit with no debit) | **Noema hostility proxy**, labelled synthetic. This replaces Tushe scenario 19, which Tushe has rightly refused to fake |

- **Proxy behaviour.** The proxy also rewrites Tushe's test account numbers to stable synthetic numbers before any system under test sees them. Otherwise a system could learn that `999904…` means "will be reversed", and the environment would no longer force a real investigation.
- **Ownership.** The benchmark owner owns every fault plan, whichever side produces the fault, and every fault plan records which side produced it.
- **Status change.** The proxy (PERD REQ-ENV-005) stops being a contingency and becomes the primary source for the families marked above. That is the contingency route SoT §36 already allows.
- **Not buying a proxy.** We are not buying WireMock Cloud, Hoverfly or Microcks. A thin proxy of our own avoids a new vendor (AGENT-14), runs in Docker Compose and CI, and reads our own fault plans.

### D5. Inbound events come from polling Tushe's feed

- **What.** Noema reads `GET /v1/events` by sequence number and feeds its inbox (REQ-API-008). Webhooks are optional: allowed for the demo, never needed for correctness.
- **Why.**
  - Tushe treats the feed as the source of truth and webhooks as pointers to it.
  - Tushe will not deliver to private addresses, and our local and CI environments are private.
  - Polling also makes event faults deterministic, because we inject them on our own read path.

### D6. Credentials: the runtime holds nothing that can write to Tushe

| Credential | Scope | Held by | Network |
|---|---|---|---|
| Runtime API key | Tushe **reads only**, test mode | Core service | Egress allowlisted to the Tushe API host only |
| Fixture key | Test-mode payout creation, to build transaction histories for scenarios | Benchmark owner; fixture loader only | Benchmark network only |
| Administrator credential | Read-only partner-administrator surface | Benchmark owner; benchmark runner only | Benchmark network only |
| `mock-case` write | Non-monetary case operations | Core service, through its adapter | Internal |
| `mock-case` truth | Read of the case service's true state | Benchmark runner only | Benchmark network only |

Because every Noema write now goes to `mock-case`, the runtime has no Tushe write scope at all. That is a stricter money boundary than SoT §36 required.

### D7. G0 is held Thursday against a written exception list

- **What.** The joint session on Thursday 15 October at 10:00 runs AT-01 to AT-20.
- **Pass rule.** Each test passes in one of three ways, and is recorded in `docs/poc/tushe/acceptance/` as such:
  - **(a) passes as written;**
  - **(b) passes under an amended condition both sides signed:** AT-01 ("material" defined), AT-03 (truth source per D2), AT-15 (per D3);
  - **(c) is covered by an agreed exception** naming who covers it, how it will be shown, and by when.
- **Rules for (c):**
  - an exception covered by Noema must be demonstrated by Friday 16 October (G1) or by the named date;
  - an exception covered by Tushe must have a working-day delivery date;
  - an exception we don't need for the POC says so and is never quietly counted as a pass.
- **Where the list lives.** The G0 exception worksheet (prepared for Tuesday's call) is the list. Thursday's G0 record links to the signed version.

## 3. The SoT edit that lands in the same pull request (AGENT-29)

Replace these parts of SoT §36. Everything else in §36 stays as written.

**The "Ten independently observable logical domains" bullet becomes:**

> Ten independently observable logical domains: customer/identity, accounts/ledger, transaction service, payment switch, beneficiary and name enquiry, settlement, events and webhooks, case/dispute, policy/authorisation, audit. For the POC, Tushe provides all of them except case/dispute. Noema provides the case domain as a synthetic case service (`mock-case`), built from the PERD §34.4 contract by someone who does not build the core, with its faults and ground truth owned by the benchmark owner (DEC-2026-10-12-tushe-environment-scope). Disputes are not modelled in the POC.

**The privileged ground-truth bullet becomes:**

> A privileged, isolated ground-truth view that our benchmark can query and Noema's runtime credentials can never reach. For Tushe-held state this is Tushe's read-only partner-administrator surface, plus checksummed scenario definitions and the transition log, reached only through a programmatic credential held by the benchmark owner.

**The controllable-clock bullet becomes:**

> Controllable time: per-object scheduled outcomes with on-demand advance in Tushe, and Noema's own simulated clock for tests that do not touch Tushe live. Tushe does not run an environment-wide clock. Reset and replay are by scenario and seed; snapshot and restore are not required.

**The "Exit of Phase A" line becomes:**

> **Exit of Phase A:** AT-01 to AT-20 pass in a joint session, or pass under an amended condition, or are covered by an agreed exception recorded in `docs/poc/tushe/acceptance/` (DEC-2026-10-12-tushe-environment-scope). Schemas frozen at v1.

## 4. What stays exactly the same

- **No money moves.** No Noema runtime credential can create, reverse or alter a payment (BD-08). The one exception is the test-mode fixture key (D6): it can create test payouts, only to build scenario histories; it is held by the benchmark owner, used only by the fixture loader on the benchmark network, and never reaches the runtime. No Noema credential of any kind can reverse or alter a payment.
- **The oracle stays out of the runtime's reach** (INV-22).
- **The benchmark owner keeps the held-out set** (OD-16).
- **Every fault remains reproducible from a scenario and a seed.**
- **The AT-01 to AT-20 test IDs and the twenty-scenario pack keep their numbers,** so nothing that cites them breaks.
- **BD-07 is unchanged:** the POC still runs on a synthetic environment with deterministic fault injection.

## 5. Options we rejected

| Option | Why not |
|---|---|
| Wait for Tushe to build a case system | Not planned by Tushe. Their version tokens are dated 12 December. G1 needs a case system on 16 October |
| Write to Tushe payouts instead of cases | That is money movement. Forbidden (BD-08) |
| Insist on a global clock | Contradicts our own parallel-run isolation requirement; Tushe cannot provide it honestly |
| Insist on GT-02 as written | Tushe's concern is valid, and their administrator surface gives the same isolation. We keep the right to ask for GT-02 if D2's conditions are not met |
| Buy a service-virtualisation product | A new vendor (AGENT-14) for something a small in-house proxy does, and one that runs in our CI |
| Delay G0 until Tushe's later deliveries (E3 to E7) | Their dates run to 12 December. The SoT contingency (control hook or our own proxy) exists for exactly this case |

## 6. Risks this creates, and how we contain them

| Risk | Containment |
|---|---|
| We grade a system we partly built (`mock-case`, the proxy) | The builders are not core engineers; the benchmark owner owns the fault plans and the truth endpoints; contract tests run in CI; every fault plan records its source |
| Integration-lead overload in week 1 (Tushe, case service, proxy) | The engineering lead takes the proxy; a coding agent does most of the typing on both builds under a task card |
| Tushe changes behaviour mid-build (v1.32 to v1.34 shipped recently) | Ask for no behaviour change between 13 October and 6 November without 48 hours' notice, and the sandbox version on every response. Record the version in every run manifest |
| The transition-history endpoint (E1) arrives late | Ask for that endpoint alone by Monday 19 October. Until then, ground truth comes from the scenario definition plus the administrator feed |
| Transaction histories can't be seeded with names and past dates before 21 November (E4) | Ask for that subset by Friday 23 October. Fallback: the fixture key builds histories through the API, and the proxy shifts timestamps for the time-sensitive cases, labelled synthetic |
| A hosted sandbox can't sit inside our private benchmark network | Isolation by credential (D6), plus an egress allowlist for the runtime. Network isolation stays for `mock-case` and the proxy |

## 7. What this changes in the PERD and the plan

**PERD v1.2 delta (one follow-up PR, same week):**

- §34.1 and §34.2: who provides the case domain and the credential table (D1, D6).
- §34.4: mapping of PERD source families to Tushe objects:

  | PERD source | Tushe object |
  |---|---|
  | Ledger | Double-entry ledger |
  | Transaction | Payout `status` |
  | Settlement | `settlementStatus` |
  | Destination | `arrivalStatus` |
  | Switch | The status query plus transition-log entries from the provider |

- §34.5: AT pass-condition amendments (D7).
- §37.1: the FaultPlan names its source: Tushe, proxy or case service (D4).
- §65.1: `bench_net` holds the runner, `mock-case` truth, the proxy control API and the administrator credential; the runtime's egress is allowlisted to Tushe.
- Requirements: REQ-ENV-002 (isolation by credential for Tushe), REQ-ENV-003 (D3), REQ-ENV-004 (two fault sources), REQ-ENV-005 (primary, not contingency), REQ-API-008 (feed polling).
- §67.2: OQ-03 and OQ-10 answered (see section 8).

**Plan v1.2 change request (plan §19).** New tasks, all in week 1:

| ID | Task | Owner | Day | Done when |
|---|---|---|---|---|
| ENV-08 | Build `mock-case` from PERD §34.4: idempotency by key, find by key, version tokens, route with expected version, append-only evidence, complaint reference, fault hooks, truth endpoint on `bench_net` | IL+AG | Tue 13 – Thu 15 Oct | Contract tests pass; commit-then-drop works from a fault plan; truth endpoint unreachable from the runtime |
| ENV-09 | Hostility proxy: transport faults, stale-read profile, event-feed faults, test-account-number rewriting, fault-plan control on `bench_net` | EL+AG | Tue 13 – Wed 14 Oct | Every proxy fault family is reproducible from a seed; rewritten numbers are stable across runs |
| ENV-10 | Event-feed poller (cursor on sequence) into the inbox | C2+AG | Wed 14 Oct | No event lost or doubled across a restart; feed faults from ENV-09 observed |
| ENV-11 | Tushe adapter mapping to PERD §34.4 payloads; status query registered as an R0 read with its cooldown | IL | Tue 13 – Wed 14 Oct | Mapping table versioned; contract tests against live Tushe pass |
| ENV-12 | G0 exception worksheet signed with Tushe | IL, EL | Tue 13 Oct | Both sides sign; worksheet committed |

**Tasks that change:**

- ENV-05: the case adapter now targets `mock-case`.
- ENV-06: FaultPlans now apply through Tushe, the proxy or `mock-case`.
- ENV-07: run against the signed worksheet.
- PLT-07: wall clock in runs against Tushe; simulated clock elsewhere.
- BEN-02 and BEN-04: each fixture names its fault source.

## 8. Open questions this answers

- **OQ-03** (does the case API support idempotency keys, find by key and version tokens?) **Yes, because the case API is now ours (D1).** The case capabilities keep the PERD §25.1 retry-safety class QUERYABLE_BY_KEY and concurrency CONDITIONAL_WRITE.
- **OQ-10** (CI access to Tushe): pull requests use recorded Tushe responses replayed through the proxy; the nightly and release runs use live Tushe in test mode.

## 9. The SoT §52 questions

- **Which requirement does this serve?** BD-07; SoT §36; INV-21 and INV-22; PERD REQ-ENV-001 to REQ-ENV-007.
- **What breaks without it?**
  - G0 can't be held, so Phase B results can't count.
  - G1 has no write target.
  - Without the number rewriting, the environment no longer forces a real investigation.
- **Which benchmark cases prove it?**
  - Thursday's G0 worksheet;
  - US-06 and US-19 on `mock-case`;
  - EC-E01 to EC-E16 and EC-S12 to EC-S17 through the proxy.
- **What business value?** We build against a real fintech platform this week instead of waiting until December.
- **Core, pack, adapter or nowhere?** Adapters, benchmark tooling and environment. Nothing enters the core.
- **Does it increase or decrease the unsafe autonomy surface?** It decreases it: the runtime loses all write scope on Tushe, and the fault and truth controls stay with the benchmark owner.

## 10. Sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Founder | TODO | Approve / amend / reject | |
| Founder | TODO | Approve / amend / reject | |
| Engineering lead | TODO | Reviewed | |
| Benchmark owner | TODO | Accepts ownership of fault plans and truth endpoints | |

## Amendment 1 · 13 October 2026

Recorded after Noema's amended response and worksheet were sent to Tushe on 13 October 2026 (docs/poc/tushe/responses/2026-10-13-noema-response.md).

Every section above stays as written. This amendment changes the following.

- **D7.** The joint session moves to Friday 16 October, 18:00–20:30 WAT. It combines the walkthrough of the worksheet, its sign-off and the acceptance tests in one sitting; the Tuesday call and the Thursday 10:00 session no longer take place. The Noema-covered exceptions are AT-04, AT-05, AT-07, AT-14 and AT-17. Noema shows them to Tushe once each is complete, and holds itself to internal targets: AT-04, AT-05, AT-07 and AT-14 before the G1 review on Monday 19 October at 10:00, and AT-17 within two working days of Tushe delivering R2. AT-09 and AT-20 become "Tushe, by date (Fri 30 Oct)".
- **D4.** The diagnostics view (E5) is requested from Tushe by Friday 30 October. Until then, Tushe's existing fault markers serve as the interim, and Noema still records every fault it injects. Stale reads (through the proxy) and stale-write detection (in `mock-case`) stay with Noema.
- **D5.** Webhooks are kept active on Noema's test tenants alongside the event feed, so that replay and deduplication can be tested. They are never needed for correctness; the feed remains the main source. This needs a public HTTPS receiver, reachable from the internet before Friday's session, which verifies the Standard Webhooks signature with its five-minute tolerance, sits behind the hostility proxy and feeds the inbox. Where it runs is an open decision (PERD OQ-15, OD-P-43, plan task GOV-20).
- **Requests to Tushe.** Tenants and credentials (R1) now come in two batches: 3 to 5 tenants and all the credentials by Thursday 15 October, and the rest, to about 10, by Tuesday 20 October. The read surfaces (R2), seeded transaction histories (R3) and switch state (R4) are due no later than Friday 23 October. New requests: ambiguous name enquiry (R9), payout approval states (R10), the rest of the scenario richness work (R11) and the diagnostics view (R12), all by Friday 30 October; and webhooks kept active on Noema's tenants (R13), with batch 1 on Thursday 15 October. R6, R7 and R8 are due Friday 16 October.
- **G1** moves to Monday 19 October at 10:00 WAT, because G0 must pass before G1.
- **Check-ins.** The 30-minute Friday check-ins with Tushe are removed.

No SoT change is needed. The status of this record is unchanged (Proposed).
