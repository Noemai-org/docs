# DEC-2026-11-24 · Architect rulings A624 to A643 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 24 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 24 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A624 to A643 (§1), every one Interim. A626 is withdrawn by its own text. A638 amends A624. |
| **Supersedes** | **A624 replaces** the Architect's earlier head-by-head merge lists; **A638 amends A624** (drops its "approve as noemai-systems" clause). **A639 amends the A504 guard** narrowly for A625's typed data. **A640 splits** TRU-06 and A544 routing ownership. **A641 amends A627** (declared window, checked). **A642 sets** the safer reading for T10 against REQ-RES-005. **A643 orders** the composition PR after #907. **A625 extends** EL's TRU-10 allowlist (A615) by one handoff. **A631 changes the contract** `capability-descriptor` to v2 (both Founders, AGENT-15). **A634 sets** an interim tenant time zone (the Founder may overrule). Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan, as written. **A624 touches AGENTS §11 and A111; see §2.** |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 24 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A624 to A643
- Decision: §1
- Rationale and evidence: the Architect's message of 24 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: BD-05, INV-03, INV-12, INV-29; AGENT-14, AGENT-15, AGENT-16, AGENT-27; REQ-TRU-012, REQ-CAP-*; SR-09; PERD §22, §27; AGENTS §2.3, §5, §11
- Supersedes: see the Supersedes row above
- Migration notes: A630 (TRU-11) and A633 (EXE-06) each add a database migration (Tier 1; independent read, A463); numbers are reserved provisionally on noema#183 and checked at merge. A631 is a contract change (`capability-descriptor.v2`: a version bump, a migration note, regenerated models; both Founders).

## 1. The rulings

### A624. Merge rule (replaces all the Architect's head-by-head lists). **Amended by A638 below: the clause "approve as noemai-systems" is dropped. The Steward's hold under AGENT-20 (the first version of this record) is lifted by A638.**

- Merge any open PR that has CI green at its head, a READY comment at that same head, and a non-author approval.
- Approve as OladiranOlatunde, unless GitHub shows OladiranOlatunde as the author. Then approve as noemai-systems.
- These need both Founders: #910, #943 (`tools/ci`), #934 (CODEOWNERS), #923 (contracts and migration).

### A625 (EL, RouteScopes reader).

- The orchestrator reads the investigation, using its own login (`orchestrator_rw`). Trust never reads the investigation, so the power separation holds (BD-05).
- Add a by-correlation read to `investigations.Store`. The orchestrator hands the result to Trust as typed data on the request (TRU-12).
- If a correlation has several snapshots, the newest by database clock wins, with the id as tie-break. Trust's own basis binding rejects a hash mismatch. If there is none, there is no scope and no grant.
- `CreateGrantID`: the caller is the orchestrator's ESCALATING handoff. EL's allowlist now includes that handoff in `orchestrator/`, for this change only.

### A626 (EL, TRU-13 and SEC-04). Withdrawn.

Both are Done. EL's G2 work is #945 and its follow-ups, the composition PR, and PCK-05.

### A627 (EL, PCK-05).

- Each reconciled fact pair's window is the smaller of the two sources' freshness limits already in the pack. It is SYNTHETIC pack data.
- A missing window fails packcheck.
- No new number is invented.

### A628 (EL, PLT-09).

Fix the 20 existing `services/core` findings. No waivers. It goes in its own refactor PR with no behaviour change, and SR reads it.

### A629 (EL, #943).

- Both Founders approve it at merge.
- Do not require the word "blast radius".
- Accepted limit: a conflict an agent never raises can't be caught mechanically.
- The second founder-run trial is not blocking.
- IL opens the `safeguards.yml` step as its own `.github` PR, and SR reads it.

### A630 (C1, TRU-11).

- Approved as proposed: count the principal's decisions for that capability over the last hour on the database clock, through a read function for the Trust login.
- It is a migration (next free number, checked at merge) and Tier 1, so it needs an independent migration read (A463).

### A631 (C1, CAP-02).

- The PERD vocabulary wins. Make `capability-descriptor.v2` with compensation as the enum `NONE_REQUIRED`, `INVERSE_CAPABILITY`, `ESCALATE_ONLY`.
- Add an `inverse_mapping` of capability id plus parameter map, required when `INVERSE_CAPABILITY`.
- Add only what the PERD packcheck rules need.
- Use AGENT-15: version bump, migration note, regenerated models, both Founders.
- The Steward adds an [OPEN] entry. C1 owns the packcheck rules, and PCK-05 stays separate.

### A632 (C1, TRU-06).

- EL supplies the routing data as pack data. SYNTHETIC values.
- C1 builds the evaluator and `SLA_EVALUATED`.

### A633 (C1, EXE-06 control-plane slice).

- A297 is satisfied by this ruling: the migration is allowed, and it is Tier 1 with an independent read.
- C1's third task is TST-03.
- STM-02: IL's #941 stays as it is. After it merges, C1 adds the three extra tests in a small PR.

### A634 (DATA-02).

- The time half: the interim tenant time zone is Africa/Lagos. Everything is stored in UTC and converted only for display and local-day rules. The Founder may overrule.
- The money half waits for the UND-05 lexicon. C2 finishes UND-05 first, then DATA-02 follows. Nobody invents conversion code.

### A635 (C2).

- The G2 batch lifts the 4-open-PR limit for this window. Do not hold a PR open past READY.
- Approved: the profile switch and the demo-profile refusal, in `services/model` only.
- A604: hand-written SYNTHETIC replies for the boundary cases, plus run 8's live evidence for the model.
- A620: slice 3 is C2's.
- The OTel exporter and the Temporal memo wait until after G1. `trace_id` stays out of logs, and `correlation_id` carries the trace.

### A636 (Voice, #947).

- Yoruba, Hausa and Igbo are measured only, with no lexicon written without a native speaker. That matches SR-09.
- Demo languages: `pcm` and `en-NG`.
- Intron host: `infer.voice.intron.io`. It goes in the bench copy of `allowed_hosts` only.

### A637 (IL, FE, BO).

- **IL:** ENV-05 is IL's own task, so IL finishes it. Then ENV-16, plus TST-02's smoke CI job as a `.github` PR (SR reads, Founder approves).
- **FE (UI-01):** EL mounts the conversation-events route in the composition PR, first. FE builds the J1 to J8 tests against the real-core compose profile now, so they run the moment it lands.
- **BO:** the Steward marks BEN-06 to BEN-09 Done on the merged evidence. MEM-02 is Ready, not blocked, so BO takes it. BO also writes the SYNTHETIC replay recordings for the boundary cases. The thin-identifier strengthening should be executed now.

### A638 (approving account; amends A624).

- Drop the "approve as noemai-systems" clause. The Steward is right: an approval from the agents' account is not a human read.
- Merge only on a Founder's personal approval, with READY and green CI at the head.
- A PR a Founder authored gets the other Founder's approval.
- The agents keep their own account for comments and READYs only.
- If #921 carries a `noemai-systems` approval, ignore it. Don't count it as the approval.

### A639 (RouteRequest guard).

- Yes, amend the five-field test narrowly, for A625's named typed data only.
- The guard test changes in the same PR as the field, and SR reads that change.
- The guard stays exact: no other field is allowed.

### A640 (TRU-06 routing ownership).

- One owner per member.
- C2 keeps the Reconciler and clocks/phase routing that A544 names.
- EL supplies only the priority routing, as a separate pack member (SYNTHETIC values).
- C1 builds the evaluator and `SLA_EVALUATED`.

### A641 (PCK-05 windows; amends A627).

- The window is declared as pack data, as REQ-RES-005 says.
- Packcheck checks that each declared window equals the smaller of the two sources' freshness limits.
- A missing or different window fails packcheck.

### A642 (WAIT versus ESCALATE: §23.3 T10 against REQ-RES-005).

- Until a Founder decides, take the safer reading. Inside the window there is no write and no verdict.
- At window expiry the case goes to ESCALATE.
- The Steward writes the CONFLICT DETECTED block with the two alternatives.
- RES-02 and RES-05 build on the safer reading and are not blocked.

### A643 (composition PR and #907).

- Yes, it waits for #907 to merge, because a PR is never based on another PR.
- The Founder merges #907 as soon as it has green CI at its head, READY at that same head, and a non-author approval.
- EL then branches the composition PR off `main`.
- EL builds everything that doesn't need the route first.

### BEN-32 target (the Architect's message of 24 Nov 2026; no ruling number was given).

Two cases per identifier is approved as the target. It runs after G1.

## 2. What the Steward did, and where the rulings are silent

- **A638 resolves the A624 conflict below (alternative 1 of the block).** A638 is the Architect's own amendment: the merge needs a Founder's personal approval, READY and green CI at the head; a PR a Founder authored gets the other Founder's approval; the agents' account is for comments and READYs only. It matches AGENTS §11 (the agents never approve or merge) and A111 (a Founder who did not author), so **no change to AGENTS.md is needed**. The Steward neither approves nor merges. The CONFLICT block is kept below as the audit record of what was raised.
- **noema#921 (A638's last line), the facts.** noema#921's author is `OladiranOlatunde`. Its only review at the merged head `05d045a8` is an approval by `noemai-systems` at 13:17:04Z on 24 Nov, and it was merged by `noemai-systems` at 13:17:13Z. **The Steward did not approve or merge it**; the Steward's only action on #921 was the merge-main commit `05d045a8` that cleared a conflict. Under A638 that approval is not counted, so #921 merged with no counted Founder approval at its head. Its earlier reads stand (A468): SR's READY and the Founder's READY comment at `ea7eab22`. **The Founder has decided (D2 of `DEC-2026-11-24-founder-decisions-t10-wait-and-921`):** the `noemai-systems` approval on #921 is accepted, for #921 only; no after-the-fact read is required. Who may act under `noemai-systems` from now on is still for the Founders.
- **A624: CONFLICT DETECTED (REQ-AGT-003; AGENT-26, AGENT-27). Resolved by A638.** Not listed in the conflicts register (SOT-C-01 to SOT-C-33) or PERD §72.

```
CONFLICT DETECTED
Affected IDs: A624; AGENTS §11 ("You never: approve or merge any PR"); A111 / DEC-2026-11-09-one-founder-approval (one approval from a Founder who did not author or drive the pull request); AGENTS §2, item 3; AGENT-27
Statements in conflict: "Approve as OladiranOlatunde, unless GitHub shows OladiranOlatunde as the author. Then approve as noemai-systems." and "Merge any open PR that has CI green at its head, a READY comment at that same head, and a non-author approval." (A624, interim) vs "never approve or merge any PR" (AGENTS §11) and "One approval from a Founder who did not author or drive the pull request is enough to merge" (A111)
Evidence: noemai-systems is the account the Steward and the other agents author and comment under (the Steward's own token resolves to it), so an approval from it does not show that a person who did not write the change has read it; EL's review of docs#241 (head 0f3a47f) reaches the same reading
Proposed alternatives: (1) keep the approval human: the Founder approves from a personal account that no agent can use, and the merge follows a READY at the head and CI green; blast radius: none on AGENTS §11 or A111 (the merge stays a Founder's act). (2) amend AGENTS §11 and A111 in a committed record, naming which accounts count as a Founder and who may act under each; blast radius: AGENTS.md and its copy in noema, the review gates of plan §4, branch protection. (3) give the agents their own account and keep noemai-systems for a Founder only; blast radius: tokens, CODEOWNERS and review requests
Safer reading applied meanwhile (AGENT-20): A624 is held. The Steward neither approves nor merges; an approval counts as a Founder's only when GitHub shows a Founder's personal account, not the author, as the approver
Decision required from: founders (and the Architect, who made the ruling)
```

- **A624 and AGENTS §11, in prose.**
  - AGENTS §11 says the Steward (and every agent) "never" approves or merges a pull request, and A111 (`DEC-2026-11-09-one-founder-approval`) says one approval from **a Founder who did not author the pull request** is enough to merge.
  - A624 tells the merge to be done by approving as `OladiranOlatunde`, or as `noemai-systems` when `OladiranOlatunde` is the author. `noemai-systems` is the account the Steward and the other agents post with, and it authors most pull requests, so an approval from it is not obviously "a Founder who did not author" (A111).
  - A624 is Interim and counts only when this record merges (AGENTS §2.3); it does not amend AGENTS §11 or A111 in words. **Until a committed record or an AGENTS change says otherwise, the Steward neither approves nor merges any pull request**, and treats an approval as a Founder's only when GitHub shows a Founder account as the approver who is not the author. **The Architect and the Founders confirm** (a) whether `noemai-systems` counts as a Founder for A111, and (b) whether A624 amends AGENTS §11 for the agents. If yes, the change is a small pull request to AGENTS.md (and its copy in `noema`) with EL's review, which the Steward drafts on request. The four "both Founders" items (#910, #943, #934, #923) are recorded as given.
- **A625, A639.** TRU-12 is the typed-data hand-off the ruling names; BD-05 holds because Trust never reads the investigation. EL's allowlist includes the orchestrator's ESCALATING handoff for this change only (as A615 did for `workflows/`, `trustpg` and `trustport`). C1 gives the independent read where A615 said so. **EL's point, verified against `main`:** the ruling says the result goes to Trust "as typed data on the request", which adds fields to `RouteRequest`; the A504 guard `TestRouteRequestHoldsOnlyTheCaseTheQueueAndWhatIdentifiesTheAsk` (`services/core/orchestrator/portadapters/trust/route_request_test.go`) pins the type to exactly five fields (`CapabilityID`, `CaseID`, `CorrelationID`, `OwnerQueue`, `TenantID`) and fails on any other. A625 does not say it amends that guard. **Settled by A639:** yes, narrowly, for A625's named typed data only; the guard test changes in the same PR as the field, SR reads that change, and the guard stays exact (no other field is allowed).
- **A626.** Withdrawn by its text. `tasks.csv` agrees: TRU-13 and SEC-04 are Done.
- **A642: CONFLICT DETECTED (REQ-AGT-003; AGENT-26, AGENT-27): §23.3 T10 against REQ-RES-005. Resolved by the Founder's decision D1 (`DEC-2026-11-24-founder-decisions-t10-wait-and-921`): alternative 1, WAIT is added to the T10 row (PERD v1.29, Proposed).** Not listed in the conflicts register before this record; added as **SOT-C-34**, now Resolved. The Steward read both texts in PERD v1.28.

```
CONFLICT DETECTED
Affected IDs: PERD §23.3 (row T10), REQ-RES-005, REQ-RES-002, INV-20, SOT-C-34; plan tasks RES-02 and RES-05
Statements in conflict: "T10 | Reconciliation; freeze check | ESCALATE on contradiction or unknown outcome, per pack mapping | —" (PERD §23.3) vs "Inside the window, a disagreement yields WAIT with a watch and a deadline at the window's end; outside it, the state is CONTRADICTORY, writes on the target freeze (INV-20) and the case escalates." (PERD REQ-RES-005)
Evidence: the §23.3 row for T10 lists ESCALATE as its only outcome; REQ-RES-005 gives an inside-window WAIT that no step of the table produces (EL's review of docs#241, head 0f3a47f, raised it; RES-05 depends on it)
Proposed alternatives: (1) REQ-RES-005 governs: the T10 row gains WAIT inside the window (a watch and a deadline) and ESCALATE outside it; blast radius: PERD §23.3, the T10 tests, US-13 and US-17, RES-05's done-when. (2) §23.3 T10 governs: reconciliation never yields WAIT; an inside-window disagreement is a hold with no verdict (no write, no outcome) that ends in ESCALATE at the window's expiry; blast radius: REQ-RES-005's wording ("yields WAIT"), the audit of the watch, US-13 and US-17
Safer reading applied meanwhile (AGENT-20), as the Architect rules (A642): inside the window there is no write and no verdict; at window expiry the case goes to ESCALATE. RES-02 and RES-05 build on it and are not blocked
Decision required from: founders
```

- **A627 and AGENT-16 (amended by A641).** The window is derived from limits already in the pack; the ruling invents no number. A missing window fails packcheck. **EL's two points:** (a) REQ-RES-005 says each pair "declares" a window as pack data, so EL recommends the window be an explicit member of the pack that packcheck checks equals the smaller of the two freshness limits (a later freshness change then forces a deliberate update). That is a required pack member, so a breaking schema change (both Founders, a manifest re-pin). A627 says "derived", not "declared"; **A641 settles it: declared.** The Steward's recommendation is EL's: declared and checked, because "Windows SHALL be pack data, versioned, and never loosened without a benchmark run" (REQ-RES-005). (b) The Steward read both texts: REQ-RES-005 says a disagreement inside the window yields WAIT with a watch and a deadline, while the §23.3 row for T10 lists only "ESCALATE on contradiction or unknown outcome". Read together they are consistent only if inside-window WAIT is produced by a step the table does not show. RES-05 depends on this. **A642 settles the interim and orders the block:** until a Founder decides, inside the window there is no write and no verdict, and at window expiry the case goes to ESCALATE; RES-02 and RES-05 build on that reading and are not blocked. The block is below, and the Steward added **SOT-C-34** to the conflicts register, which the Founder resolved (D1).
- **A628, with EL's points.** `edge/session/http.go:74` is a contextcheck false positive that, with no waivers, must be rewritten and not excluded; the fixes to unchecked `fmt.Fprintln` and `Close` calls may change error paths, so "no behaviour change" needs a test per site; EL's allowlist must cover `cmd/*` and `platform/packload` for it. Plan task PLT-09. A318 had said the Go gate waits for "the 12 baseline findings" to be fixed; A628 says 20 findings now. The count changed since; EL's PR states the number it fixes. A refactor is its own PR with no behaviour change (AGENTS §4).
- **A629.** #943 needs both Founders at merge. IL's `safeguards.yml` step is a `.github` change, so it needs SR's read (AGENTS §11).
- **A630 and A633, the migrations.** Tier 1; each needs an independent migration read from a role other than the author and SR (A463). The Steward reserved provisional numbers on noema#183: **0041 for A630 (TRU-11)** and **0042 for A633 (EXE-06)**, both "checked at merge". Open pull requests hold 0038 (#923) and 0039 (#925); 0037 is merged; 0040 is reserved (A598). **Next free: 0043.**
- **A631 and the [OPEN] entry.** The Steward added **OD-P-102** (Open, provisional, NON-CANONICAL) in `docs/open-decisions.md` for `capability-descriptor.v2`. C1 owns the packcheck rules; PCK-05 stays separate (A627).
- **A632 against A544, settled by A640.** A544 says the Reconciler and Clocks routing, including phase routing and the escalation reason per classification, is pack data in `limits/trust_limits.json` owned by C2. A632 says EL supplies the TRU-06 routing data as pack data. The plan's TRU-06 row says "priority routing data". The record does not say whether these are two data sets. **A640:** one owner per member. C2 keeps what A544 names (the Reconciler and clocks/phase routing in `trust_limits.json`); EL supplies only the priority routing, as a separate pack member the manifest pins (SYNTHETIC values); C1 builds the evaluator and `SLA_EVALUATED`. The values are SYNTHETIC; the Steward fills none. The event name `SLA_EVALUATED` is the Architect's.
- **A634 and GOV-08.** The interim time zone is Africa/Lagos; the Founder may overrule. The plan's GOV-08 (confirm the tenant time zone, OQ-12) is the Founder's task and stays Backlog until the Founder records it. The money half waits for UND-05 (`tasks.csv`: In progress, blocked). Nobody invents conversion code.
- **A635 and the PR limit.** The work-in-progress cap was already suspended until G1 (A558); A635 also says not to hold a PR open past READY for the G2 batch. The OTel exporter and the Temporal memo wait until after G1, which answers the open point 7 on noema#685 (REC-02) for the Temporal half. `trace_id` stays out of logs; `correlation_id` carries the trace.
- **A636.** SR-09 and DEBT-39 (A250, the native-speaker waiver) govern the Yoruba, Hausa and Igbo point; no lexicon is written without a native speaker. The Intron host goes in the bench copy of `allowed_hosts` only (IL). The Steward records the host as given; no credential appears here (AGENTS §10).
- **A637, EL's dependency note.** "EL mounts the conversation-events route in the composition PR, first" depends on noema#907 (lane 4, which carries the events route; open at this writing); noema#905 has merged. EL cannot base a PR on an open PR (AGENTS §11), so the composition PR waits for #907 to merge, or the route moves into the composition PR itself. **A643 settles it:** the composition PR waits for #907 to merge (a PR is never based on another PR); the Founder merges #907 once it has green CI at its head, READY at that head and a non-author approval; EL then branches the composition PR off `main` and builds everything that does not need the route first.
- **A637, the status pass.**
  - **BEN-06 to BEN-09 → Done** in `tasks.csv`, on merged evidence: noema#659, merge commit `282d1d6791ddfdfdf9f5597f339cf4cc39c8201d`, containing `094e9495` (`benchmark/generator/task_coverage.py`, `test_task_coverage.py` and the four status files); the merge commit's 25 check runs all succeeded (https://github.com/Noemai-org/noema/commit/282d1d6791ddfdfdf9f5597f339cf4cc39c8201d/checks). The done-when is "Cases validate" (BEN-06 adds "each is linked to its EC or US ID"): the status files show 0 gaps across 25, 26, 14 and 19 identifiers, each carried by at least one case. They also show **4 "thin" identifiers** (carried by one case: EC-T10, EC-T11 and US-18 in BEN-08; EC-E16 in BEN-09), which the done-when does not require; the Architect says the strengthening is to be executed now (BO). **Codex's P2: it has no measurable target and no task.** The status files define "thin" as exactly one case and leave to the deciders whether more is required. **The Architect approved the target:** the minimum is **two cases per identifier**, and it **runs after G1**; the evidence is `python -m benchmark.generator.task_coverage --task BEN-06` to `--task BEN-09` reporting 0 thin identifiers, committed in the status files; and the work is a tracked BO row, **BEN-32**, added by `CR-2026-11-24-task-row-ben-32-thin-identifiers` (Draft). The completion of BEN-06 to BEN-09 stays tied to their own done-when ("Cases validate").
  - **TST-02** now has BEN-06 to BEN-09 Done in its Needs; its `blocked` flag in `tasks.csv` is unchanged.
  - **MEM-02.** `tasks.csv` shows In progress and `blocked`, with its only Need (BEN-10) Done. The Architect says it is Ready and not blocked, and BO takes it. The Steward leaves the `blocked` flag as it is until the owner or the board confirms the blocker is gone, and clears it on that word; the flag follows the board (AGENTS §9).
  - **OPS-02 (the debt register's guards).** At the Founder's instruction the Steward collects the guard names from the owners in their next status files; the register's "Guarding test" column is the place. Nothing is collected or invented here.
- **Migration ledger on noema#183:** 0037 is merged (#922); 0038 #923, 0039 #925, 0040 reserved (A598), **0041 provisional (A630), 0042 provisional (A633)**; next free 0043.
- **Next free ruling: A644.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` and `DEC-2026-11-21-*` records | A358 to A362, A380 to A485 (A467: no text), A489 to A492, A502 to A517 | |
| `DEC-2026-11-22-*` to `DEC-2026-11-24-architect-rulings-a613-a623` | A518 to A623 (A541 noted; A590 to A592 in full) | |
| This record | A624 to A643 (A626 withdrawn) | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank, by ruling A592) | **A644** |
