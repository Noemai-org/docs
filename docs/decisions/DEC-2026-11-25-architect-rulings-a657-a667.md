# DEC-2026-11-25 · Architect rulings A657 to A667, and A669 to A672 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 25 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves, from a personal account, and merges it (A111, A638; AGENTS §2, item 3). |
| **Date** | 25 November 2026 |
| **Owner** | Principal Architect (the rulings); the Founders (the merge) |
| **Decides** | Rulings A657 to A667 and A669 to A672 (§1 and §1A), every one Interim. A668 is `DEC-2026-11-25-architect-ruling-a668` (docs#243). |
| **Supersedes** | **A669 amends A657** (the re-read rule's wording) and **A670 adds an end marker to A656**; **A671 and A672** are applied by plan v1.29 (§2). **A657 confirms A656** and ends the re-read loop; it amends AGENTS §11 "Reviews" (this pull request edits it). **A659 changes** A641's use of `window_seconds` (A647) to the name `convergence_window_seconds` and moves the rule set to version 2. **A661 is restated and closed by A668** (`DEC-2026-11-25-architect-ruling-a668`, docs#243); it is recorded here as given. **A662 settles** noema#952 (merge as is). **A664 fixes** the landing order of the contract and pack PRs. **A666 sets** RES-02's freeze as a Record event. Otherwise nothing; per ruling in §1. |
| **Amends** | `AGENTS.md` §11 "Reviews" (A656, A657, A669, A670). **Plan v1.29** (new version: §4, §13.1, and the owner of CON-04). Nothing in the SoT or the PERD. The plan row EVD-05 is untouched (see §2, "EVD-05"). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder's personal approval (A111, A638)
- Date: 25 November 2026
- Owner: Principal Architect; Founders
- Decides: A657 to A667; A669 to A672
- Decision: §1
- Rationale and evidence: the Architect's message of 25 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-07, INV-17, INV-21, INV-22, INV-29; BD-08; AGENT-14, AGENT-15, AGENT-16; REQ-CTX-005, REQ-CTX-006, REQ-CTX-008, REQ-RES-002, REQ-RES-005, REQ-ENV-001, REQ-TRU-011; PERD §36.1
- Supersedes: see the Supersedes row above
- Migration notes: A659 moves the reconciliation rule set to version 2 (A671 and A672 add no migration) and adds a `recon-rule-set.v1.json` schema (AGENT-15 steps, in C1's #963). A666 uses migration 0042 for EXE-06. A664's `injection_patterns` member is version-gated. No migration is added by this record.

## 1. The rulings

### A657. Re-read rule (ends the re-read loop)

- A push after READY that changes only comments, docs or status files **keeps the READY**. Green CI at that head is still required. **Amended by A669 (§1A):** the exact conditions are in A669.
- A code push needs a **fresh READY at the new head**.
- SR's READY stands in for Codex on every Tier 1 PR while Codex is out of usage (A656, confirmed).
- The Steward opens a docs PR that commits A656 and A657, so they are in force before any merge relies on them. **This pull request does that** (AGENTS §11 "Reviews").

### A658. #907 event settings

Approved ranges: the table in #907's body. Approved values (resource limits only, not safety thresholds):

| Setting | Value |
|---|---|
| `NOEMA_EVENTS_POLL_MS` | 2000 |
| `NOEMA_EVENTS_MAX_STREAM_MS` | 300000 |
| `NOEMA_EVENTS_WRITE_TIMEOUT_MS` | 5000 |
| `NOEMA_EVENTS_READ_TIMEOUT_MS` | 2000 |
| `NOEMA_EVENTS_MAX_EVENT_BYTES` | 65536 |
| `NOEMA_EVENTS_MAX_STREAMS` | 100 |
| `NOEMA_EVENTS_MAX_STREAMS_PER_PRINCIPAL` | 3 |
| `NOEMA_EVENTS_MAX_BATCH` | 100 |

A missing or out-of-range setting fails the start. EL fixes the two Codex P2s, red test first:

- a stepwise saturating multiply in the recovery pass bound;
- `Stop()` that cancels and joins recovery before any pool closes, with `Close` made a `sync.Once`.

EL also checks the possible double `p.Close()`.

### A659. Reconciler and PCK-05

- The window member is **`convergence_window_seconds`**. It is declared in the rule file, and the rule set moves to **version 2**.
- C1 adds a new `recon-rule-set.v1.json` schema to #963 that requires it. EL's PCK-05 aligns to that name, and packcheck checks it equals the smaller freshness limit (A641).
- The reversal source is the inbound `reversal_posted` event from the Tushe inbound-events adapter. If the Tushe documents don't state its shape, EL stops and lists the gap.
- The `trust/reconcile` allowlist extension is approved for EL.
- A future-dated `effective_at` means **no window**, which means ESCALATE and never WAIT. Do not clamp to now. C2 fixes it in `splitByWindow`, red test first, and guards every `PermitTarget` caller.
- #949 merges before #958.
- **OD-RES05-1:** no new numbers. The windows come from A641.

### A660. #965 and priority routing

- Packcheck requires an entry for every SLA phase. The phase vocabulary is the clock statuses. A missing phase fails packcheck, so no "default queue" is needed.
- SYNTHETIC priorities and the single `PAYMENTS_OPERATIONS` queue are accepted.
- "Every queue must be in `routing_allowlist`" stays.
- #965 stays its own PR. No rebuild.

### A661. #954 (restated and closed by A668)

- `sealed_at` is the ordering authority for the POC (one core process). The Steward adds a debt entry for a database-clock column before any multi-sealer setup. No migration now.
- Route admission check: if the newest snapshot predates the intent's admission time, there is no scope and no grant. EL adds it with a red test, as a follow-up, and it doesn't block the merge.

### A662. #952

- Merge as is. Nothing rate-limited is composed, so there is no live behaviour.
- Before the Rates adapter is wired after G1, **C1 takes the rate check and the grant under one advisory lock in the Writer transaction**. That makes it a hard cap, not advisory.
- The debt entry names C1.
- A retry of an already-ALLOWed request must not be counted as `RATE_LIMITED`; this is an acceptance item in the wiring PR.

### A663. #903

C1 fixes it in a follow-up. The early-gate ESCALATE is written after the decision is judged, using the null-basis form that 0038 allows (A574, A577). It waits on #923 merging.

### A664. Contracts and packs

Landing order, so each later PR only re-pins the manifest: **#910, #964, #965, #963**.

- `injection_patterns` is version-gated, so older manifests still load (A579 pattern). The "at most one" wording in #964 is fixed.
- `FIELD_TRUNCATED` in `SecurityKind` is approved. C2 opens it as one small contracts PR for both Founders in the same pass.

### A665. Compile run

- `POOL_SIZE` 7 is confirmed for #932. It changes concurrency only; the USD 5 ceiling is unchanged.
- The ledger payload (A556): EL's reader adds a transaction-level version token and a complete marker. The candidate item is the payment-facts source.
- BEN-23 recordings regenerate on `main` after #932, #936, #931 and #938 merge. Run 8 comes after that.

### A666. Lane and G2 items

- **Slice 4** (the Record reader) starts now for EL's agent. **Slice 2** starts now for C1.
- **EXE-06**: C1's design is approved:
  - a small ops binary behind mTLS operator certificates;
  - its own login limited to set and clear;
  - runtime identities set-only (migration 0017);
  - the clear path recorded as existing `SECURITY_EVENT` kinds;
  - migration **0042**.
- Promoting **`go.temporal.io/api`** from indirect to direct for `REJECT_DUPLICATE` is approved. It is already in the module graph, so it is not a new dependency. The Steward notes it (§2).
- **RES-02**: the freeze is a Record event, and the effective state is derived from the events. No separate mutable table.
- **EVD-05**: the Steward drafts a one-page change request so C2 can build the hostility-proxy part now (the proxy is ours). The Tushe-contract part waits for ENV-03. C2 starts when that CR merges.
- **INP-01 (#684, #685)**: for each of C2's five open questions, take C2's stated safer default. It is final unless it adds a threshold, a dependency or a contract change, in which case C2 stops and says so. Correct the correlation-id statement in #684, and close #685 after #944 merges.

### A667. Identity, deploy and Tushe

- The core exits 1 because `NOEMA_MODEL_TLS_KEY_FILE` fails the 0400 owner check. IL fixes the owner and mode in the Compose init. The reader is not relaxed.
- #955: the empty-file stand-in is gated to `MODE=stack-check`, with a test that a full-mode capture with a missing file still exits 2.
- A654's token: IL issues 19 short-lived customer tokens through `bench_tokens.sh`, one per principal in BO's manifest, 15 minutes at most, never stored.
- #961 merges as a fold plus the recorded list. **ENV-05 is not counted Done.**
- The Steward turns `status/ENV-05.md`'s eight unstated items into one question list for Tushe, including R6 (a status query never moves money). The Founder sends it with the OpenAPI request on #690.
- BO builds the runner timeline drivers for `webhook:settlement_updated`, `webhook:reversal_posted` and `session_resume:same_channel`. An unsupported event is a failure, never a skip.
- FE moves the journeys spec to its own directory and config, and keeps #957 draft until #907 and #962 land.

## 1A. Rulings A669 to A672 (the Architect's answers to the review of this pull request)

### A669. Re-read rule wording (A657 amended). Adopt SR's wording.

- A push keeps READY only if one of these holds:
  - every changed file is `*.md` or under `status/`;
  - or the only changed lines in code are directive-free comments (no `//go:build`, `# noqa`, `//nolint` or similar) and the rest of the file is byte-identical.
- The pusher states which case applies.
- A merge-main commit voids no earlier read unless its conflict resolution changed code.
- Anything else is a code push and needs a fresh READY at the new head.

### A670. End marker for A656

- The Steward records the day Codex returns.
- From that day the old Tier 1 text applies again: Codex, or SR standing in, plus SR READY at the same head.
- Key and identity paths stay SR paths regardless (A541). No extra role reads are kept for them.

### A671. Plan and AGENTS.md. Yes to both.

- A small plan version restates §4 and §13.1, with its change request, so the plan, AGENTS.md and the rulings agree. The plan file is never edited in place.
- The noema copy of AGENTS.md goes in a pull request once docs#244 merges. The copy states the `docs` commit it was taken from.

### A672. CON-04

- It goes back to **In progress**. The schema-valid `intent_hash` and `plan_hash` vectors are what a grant binds to (INV-17), so the Architect will not mark it Done without them.
- C1 owns it. C1 adds the shared Go and Python golden vectors for both hashes, red first, as a small pull request that touches `/contracts` fixtures only, with no schema change.
- The Architect does not rule those vectors outside its done-when. The earlier instruction to mark CON-04 Done is withdrawn.

## 2. What the Steward did, and where the rulings are silent

- **AGENTS.md §11 "Reviews" amended** (A656, A657): SR's READY at the same head stands in for an unread Codex on every Tier 1 pull request while Codex is out of usage; independent role reads apply to migrations only (A463); the re-read rule above. Plan §4 and §13.1 keep their older Tier text (a plan is not edited in place); A656 and A657 rank above the plan (SoT §0.4, approved POC decisions). **The copy of AGENTS.md in `noema` carries the old text** and takes this change by its own pull request after this one merges; the `docs` original wins until then (AGENTS §16).
- **[OPEN] entries opened (provisional, NON-CANONICAL)**, from the rulings' own words and the owners' status files, none with an invented number:
  - **OD-P-107** (named `OD-RES05-1` in the rulings): the convergence window of each compared fact pair. A659 settles it: no new number; the windows come from A641. Kept Open until packcheck's equality check lands.
  - **OD-P-108** (named `OD-A544`): pack limit values the SoT and the PERD do not state (A544).
  - **OD-P-109** and **OD-P-110** (named `OD-EVD02-1` and `OD-EVD02-2`, from `status/EVD-02.md`): the per-source freshness override, and the read budget of REQ-CTX-003.
  - **OD-P-111**: the `EVENT_ORDER` clock-skew tolerance.
  - **OD-P-112**: the EVD-05 retry budget.
  - **Already open, not duplicated:** OD-P-101 (the 9000 basis-point gate threshold; the rulings call it `OD-A603`), OD-P-104 (tenant-wide rate limit), OD-P-105 (outcome pack mapping and `Pending`), OD-P-106 (`REGRESSION_LINK` writer); all four are in `main`.
  - **Wording of OD-P-111 and OD-P-112 is the Steward's.** The message named them without text. The missing decision and the default are drawn from REQ-CTX-008, OD-P-56 and the safe-default rule; the Architect confirms or corrects them.
- **Debt.** **DEBT-58** (`sealed_at` as the ordering authority, A661 and A668, owner C1) is in docs#243; this pull request does not repeat it. **DEBT-59** (the rate check and the grant under one advisory lock, A662, owner C1) is added here. Tier 2 is the Steward's proposal; the ruling gives no tier.
- **Tasks marked Done in `tasks.csv`, on merged evidence** (PLT-08 and EVD-06; **CON-04 is not Done**, A672) (status columns only; the plan is not edited):

  | Task | Evidence (merged pull request, merge commit; checks at the pull request's last head) |
  |---|---|
  | **BEN-06 to BEN-09** | Already Done in `tasks.csv` on `main`; no change. |
  | **PLT-08** | noema#693 (`196b452`; 25 check runs succeeded at the merge commit). Done-when: an event commits with its state change or not at all, shown by a crash test. |
  | **EVD-06** | noema#674 (`f043976`, the permutation property) and noema#688 (`af1e9fd`, the advisory injection detector). Done-when: permutation property test passes; injection fixture records a security event. For #674, all 24 check runs succeeded at the last head (`6d773ad`); the merge commit on `main` shows one red `checks` job in "Vendored-copy script tests (the current PERD is resolved, not hardcoded)", a tool test the test-only change does not touch. For #688, 25 succeeded at the merge commit. |
  | **CON-04** | **Not Done (A672).** Set back to In progress, owner C1. noema#652 (`cddaab2`; 25 succeeded) and noema#1 and #2 delivered the Go tests for every family and the `evidence_set_hash` vectors, but the schema-valid `intent_hash` and `plan_hash` vectors (INV-17) are still to do (C1's small contracts-fixtures PR). |

- **`go.temporal.io/api`**: promoted from an indirect to a direct dependency in `services/core` for `REJECT_DUPLICATE` (A666). It is already in the module graph, so no new module is added; AGENT-14's approval is A666. Recorded here; the change itself is C1's.
- **EVD-05 change request**: drafted as `CR-2026-11-25-evd-05-hostility-proxy-split` (Draft). The plan row is not changed until a plan version applies it (plan §19); A666 says C2 starts when the CR merges.
- **Tushe question list**: `docs/poc/tushe/questions-2026-11-25-env05.md` (a draft for the Founder to send with the OpenAPI request; the Steward does not send it). It carries the eight unstated items of `status/ENV-05.md` (noema#961's branch), with R6.
- **A659, #949 and #958; A664's order; A665's runs; A667's journeys:** other owners' work; nothing for the Steward beyond this record. A663 waits on #923.
- **A669 to A672 applied here:** the AGENTS.md §11 paragraph carries A669's wording and A670's end marker; **plan v1.29** (`NOEMA_POC_4WEEK_PLAN_v1.29.md`, a new version; v1.28 is not edited) restates §4 and §13.1 and moves CON-04's owner to C1, with `CR-2026-11-25-a671-review-standing` and `CR-2026-11-25-a672-con-04`; `tasks.csv` is regenerated by `plan_index.py` (only the CON-04 row differs), CON-04 In progress. **The noema copy of AGENTS.md** goes in a pull request once this one merges (A671). **A670's marker:** the Steward records the day Codex returns in that day's daily note (`docs/poc/execution/daily/`); no date is set now.
- **Next free ruling: A673** (A668 is `DEC-2026-11-25-architect-ruling-a668`; A669 to A672 are in §1A).
