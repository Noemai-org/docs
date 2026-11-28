# DEC-2026-11-27 · Architect rulings A753 to A769 and SR-APP (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 27 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves, from a personal account, and merges it (A111, A638; AGENTS §2, item 3). |
| **Date** | 27 November 2026 |
| **Owner** | Principal Architect (the rulings); the Founders (the merge) |
| **Decides** | Rulings A753 to A769 and SR-APP (§1), every one Interim. |
| **Supersedes** | **A769 replaces** A753, A766 and A767, and so A749: one stacking rule (§1, A769). **A755 accepts** C1's reading of WAIT. **A758 answers** four findings. **A760 applies** A752 to #1034. **A762 confirms** the stand-in under A750 and A751. **A765 restates** the G1 critical path (A684, A696, A736, A747). **A768 rules** on A755 against INV-30 and closes SOT-C-36. **SR-APP resolves** SR's conditions 3, 4 and 6 to 9 as the Steward recommended them. Otherwise nothing; per ruling in §1. |
| **Amends** | `AGENTS.md` §11 (A769: stacking). Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder's personal approval (A111, A638)
- Date: 27 November 2026
- Owner: Principal Architect; Founders
- Decides: A753 to A769 and SR-APP
- Decision: §1
- Rationale and evidence: the Architect's message of 27 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-12, INV-16, INV-17, INV-20, INV-21, INV-29, INV-30; BD-08; AGENT-11, AGENT-12, AGENT-15, AGENT-16; REQ-RES-005, REQ-VER-004, REQ-TRU-009, REQ-STM-001, REQ-INP-004, REQ-OPS-003; SoT §51
- Supersedes: see the Supersedes row above
- Migration notes: A757 adds an optional `question_key` to the slot declaration in `intent-node.v1.json` (additive, v1, A698; one contract and pack PR for both Founders). A761: #1021's early outcome set is ESCALATE and REJECT (a widened CHECK). A764: the migration read of #1021 (A463) is Voice's. No migration is added by this record.

## 1. The rulings

### A753. Stacking PRs (replaced by A769)

Replaced by A769 (§1). It carries no rule of its own.

### A754. Evidence record timeout

`NOEMA_EVIDENCE_RECORD_TIMEOUT_MS` is required, with no code default. The bench value is 5000 ms. IL adds it to the compose.

### A755. WAIT is not recorded in the POC

- C1's reading is accepted: WAIT is returned to the caller and re-evaluated when the window ends. At expiry the contradiction becomes an ESCALATE Decision Record.
- Recording a WAIT is OPEN until after G1.
- **Scope:** A768 rules on what "not recorded" means.
- C1's wiring (T10 carries the wait, T11 ends it) is accepted.

### A756. Freeze events (#1035)

- The clearing decision carries the target reference in its payload, so the link is checkable against the freeze row.
- If the append fails, the target stays frozen. That is fail-closed and accepted.
- The by-target read function is DEBT-60.
- The emitter is `core-trust`, confirmed.

### A757. AMB-04 SLOT question template (C2)

- Add an optional `question_key` to the slot declaration in `intent-node.v1.json` (additive, v1, A698).
- A template file may hold a key that is not `<outcome>/<classification>` only when it names a declared question key.
- Add the `fin.clarify.when` text to `en-NG.json` with a native-speaker review flag.
- Packcheck requires text for every declared question key in every required locale.
- EL builds the resolver that turns a `question_key` into text, server-side in core. FE only displays it.
- It is one contract and pack PR for both Founders.

### A758. Four of the Codex and SR findings, answered

| PR | Answer |
|---|---|
| #1032 (P1 overflow) | Compare the expiry as integer seconds against `ceiling_ms/1000` before any conversion to `time.Duration`, and clamp to the 600000 ms platform bound. Add a regression test with an expiry far in the future (year 2400). |
| #1029 | The webhook message id is `<run_id>:<case id>:<kind>`, and the replay URL quotes it. Idempotency holds within a run. |
| #1014 | A digit run over 4300 characters makes the amount unread, never an exception, and gets a regression case. |
| #1036 | Drop the duplicate `NOEMA_PLAN_TEXT_MAX_BYTES` line (#1005 merged it) and give it an upper limit of 4096. |

### A759. A741 and A744 text (for BO)

- **A741:** the repeated-option fixture is one recording of a gate reply that lists the same option twice (for example `yes 0.10` and then `yes 0.95`). #932 refuses that reply as a whole. It must be served as a usable fixture (`usable_as_fixture: true`) so the offline A604 check covers it.
- **A744:** no code reads webhook payloads, so nothing is written until Tushe states the shape.

Both are in the Steward's record (A741 and A744 of `DEC-2026-11-27-architect-rulings-a738-a747` are read with this text).

### A760. Rename PR (#1034)

Re-minting the pinned assertion vector is the same change as renaming the identifier, so A752 allows it. Another agent independently reproduces the new vector with a separate HMAC before merge.

### A761. SR conditions, assigned

| PR | Condition | Owner |
|---|---|---|
| #1028 | no `:` in an approver id | C1 |
| #1025 | separate generated operator CA, and a test that the keys differ | IL |
| #1013 | revocation, ops compose service, A699 assertion, server timeouts | EL, IL |
| #1021 | early outcome set is ESCALATE and REJECT, both keyed by turn and principal | C1 (the widened CHECK) |
| #733 | A542: the start site must not consume `Result.DecisionID` until it names the disposition's own intent | EL |
| #1017 | debt entry for the unrecorded attempt count; add a clock-skew freshness test | C2 |
| #1033 | build the transport explicitly, no unchecked type assertion | EL |
| #1006 | pass `BENCH_TENANT` to `bench_tokens.sh`, with a workflow-level test | IL |

### A762. SR's A730 and A750

SR's READY on #733 already decides that Codex's finding is outside the diff (A751). The stand-in stands.

### A763. FE

- FE does not need a bench-host connection and does not run the stack. IL dispatches `bench-g1-stack` with `playwright` true, and the workflow runs the suite.
- FE merges `main` into #957 and fixes its two UI CI failures, which it has already started.

### A764. Voice

Voice takes two reads that need an independent reader: the migration read of #1021 (A463) and the independent reproduction of #1034's new vector.

### A765. G1 critical path now

The newest stack-check (run 16, at `6d6b566`) still listed 18 components as unconfigured. That was before #1018 and about a dozen other merges. The next run is the authority. The remaining gaps, by owner, are in the table below, and owners are expected to execute on them right now and deliver reports on them. If an owner is waiting for a PR to merge, it stacks on that PR under A769: the first line of its PR body says "STACKED ON #N. Do not merge until #N has merged."

| Gap | Owner | State and next step |
|---|---|---|
| Evidence read and seal, Policies, Clocks | EL | #1018 merged, so unblocked. Bundle 1 with A754. Verify the `parseKeyOverlap` stub first. |
| Reconciler | EL, C1 | EL's adapter. C1's FreezeReader in #1035 (green pushed). |
| Candidates and Ownership | EL | #1020 and #1012 are merged. Build the Labeller, ranker adapter and v2 retype. |
| Planner | EL | #1002 merged. #1036 adds the required setting. |
| Recorder | EL, C2, C1 | C2's StepFactSource merged (#1027). C1's FreezeReader (#1035). EL wires them. |
| Explainer | EL | #1015, #970, #1031 merged or ready. EL wires them. |
| Confirmations and the confirmation route | C1, EL | #1028 appender is READY. EL builds the per-tenant adapters. |
| Input gateway write path | EL | #1019 (READY); #1016 merged; **#1004 is open and not merged** (head 932acef2, merge state blocked, so its review gates are not complete; Steward correction of 27 Nov 2026 after Codex's finding on docs#252, the Architect to confirm its dependency and next action); the A707 port, then `outcome_bindings` (#1026). |
| Events route | IL, EL | #1005 merged. The next stack-check shows whether it flipped. |
| Worker | EL | Escalation start site (A730 condition). |
| Recovery reader | EL | Reader merged (#996), but nothing sets `SurfaceSeams.Recovery`. EL sets it. |
| Recovery write path | C1 | After EL's slice 4. |

### A766 and A767 (replaced by A769)

Replaced by A769. They carry no rule of their own.

### A768. A755 against INV-30 (what "not recorded" means)

- A WAIT is a stateless evaluation result. The turn ends with no write, no grant and no verdict.
- Nothing about the wait is held in Temporal, because Temporal is never authoritative (INV-30).
- The window is derived from the timestamps of facts already on the Record, so it is deterministic and replayable (INV-21).
- Re-evaluation happens either on the customer's next turn or in a Postgres-based sweep. The sweep reads the Record, and it is the fallback of REQ-VER-004.
- At window expiry the contradiction becomes an ESCALATE Decision Record.
- OD-P-136's safeguards (SR 5) apply: no write, no grant and no verdict while waiting, and an expiry that always escalates.
- Recording the WAIT as a Decision Record stays OPEN until after G1, and a Founder decides it.
- SOT-C-36 is filed as the conflict block, with A768 as the ruling.

### A769. Stacking (replaces A753, A766 and A767)

- An agent that is waiting on PR #N to merge works on its task now, in a branch cut from #N's branch.
- It opens its PR with #N's branch as the base. The first line of its PR body says: "STACKED ON #N. Do not merge until #N has merged."
- Up to 4 PRs may stack on one #N.
- The Founder merges #N first. Then the stacked PR retargets to `main`: GitHub does this when #N's branch is deleted, and if it does not, the Founder changes the base to `main` by hand. The Founder merges the stacked PR only after that.
- If #N changes after the stacked agent started, the agent merges #N's branch into its own. No rebase.
- `pr-base-guard` is red on a stacked PR until its base merges and it retargets to `main`. That is expected, and a red guard is never merged past. No `.github` change is needed, so there is no waiting.
- SR, Codex and the Founder read the stacked PR's own diff against its base. SR's two blocking findings on docs#252 (who merges, and stacking before the guard PR) no longer apply.

### SR-APP. SR's conditions 3, 4 and 6 to 9 (approved as the Steward recommended them; first numbered SR-APP by the Steward, renumbered by DEC-2026-11-28-architect-rulings-a770-a776 because the Architect's SR-APP is CI throughput)

Source: the Steward's recommendations of 27 Nov 2026, approved in the Founder-side message that relayed A769. The relay gave no ruling number; the Steward numbered this one. Interim.

| SR | Resolved as |
|---|---|
| 3 | EL reads #1021's migration, with C2 as backup. A764 is amended: Voice keeps the #1034 vector reproduction and does not read the migration. The pool of independent readers (A463, A685) is not widened. |
| 4 | #1021 edits migration 0043 in place, with no 0044. C1 adds three tests: a REJECT keyed by turn and principal inserts; any outcome other than ESCALATE or REJECT is refused by the CHECK; the Record event is asserted. C1's status file lists every early refusal in A680 and shows each is ESCALATE or REJECT. |
| 6 | DEBT-60 is Tier 2, and is done before G1 if the freeze read is on the dispatch path. C1 builds one tenant-scoped, indexed read function by target with a context deadline. Four tests: a read error reads as frozen; no row is not frozen; a cleared row is not frozen; another tenant's row is never visible. |
| 7 | #1032 compares integer seconds and never uses `time.Duration` or `Sub`. Truncating `ceiling_ms/1000` rounds toward rejecting, and a ceiling under 1000 ms becomes 0 s, so everything is rejected. A property test covers extreme values, including a year-2400 expiry. |
| 8 | `NOEMA_EVIDENCE_RECORD_TIMEOUT_MS` is required at startup. The core refuses to start if it is absent, zero, or not less than the enclosing turn deadline. The Architect sets any absolute upper bound. The bench value of 5000 ms stays. |
| 9 | A762 is made mechanical: SR checks at each #733 head that the diff does not touch the worker start site, and if it does the stand-in ends. EL's start-site PR carries Codex's finding as a test: a duplicate or restarted start must not create a second ESCALATE. |

## 2. What the Steward did, and where the rulings are silent

| Item | What was done |
|---|---|
| **`AGENTS.md` §11 (A769)** | One stacking rule, replacing A749, A753, A766 and A767: an agent waiting on PR #N branches from #N's branch and opens its PR with that base, with "STACKED ON #N. Do not merge until #N has merged." as the first line of the body; up to 4 PRs on one #N; the Founder merges #N, the stacked PR retargets to `main`, then the Founder merges it; if #N changes, #N's branch is merged into the stacked branch, no rebase; `pr-base-guard` is red until the retarget and is never merged past; no guard change; readers read the stacked PR's diff against its base. |
| **A741 and A744 (A759)** | Recorded with the text as given in §1 (A759). |
| **[OPEN] entries (provisional, NON-CANONICAL)** | **OD-P-136** recording a WAIT (A755, OPEN until after G1); **OD-P-137** the evidence record timeout (A754); **OD-P-138** the `question_key` design (A757). |
| **DEBT-60** | Added to the debt register: the by-target read function for freeze rows (A756). Owner C1 (the Steward's default: #1035 is C1's); Tier 3 proposed (the ruling gives none). |
| **BEN-06 to BEN-09** | Already Done in `tasks.csv` on `main`; no change. |
| **A758 and A761** | Other owners' work; the Steward records the assignments as ruled. |
| **A762** | Recorded; nothing for the Steward. |
| **A765's table** | Recorded as ruled; `tasks.csv` is not moved for it. |
| **A765's table: #1004** | Corrected by the Steward: #1004 is open and unmerged (Codex finding on docs#252). Only #1016 is merged. |
| **SR 3, 4, 6, 7, 8, 9** | Resolved by SR-APP, as the Steward recommended them. The owners (EL, C1, #1032's owner, IL with EL, SR) carry them out; none is done by this record. |
| **A768 and SR-APP** | Recorded. SOT-C-36 is closed with A768. OD-P-136's default is restated per A768; whether to record the WAIT as a Decision Record stays OPEN, and a Founder decides it. DEBT-60 is now Tier 2 (SR-APP, SR 6). |
| **A769** | Replaces A753, A766 and A767. |
| **Next free ruling** | Superseded: see `DEC-2026-11-28-architect-rulings-a770-a776` (the Architect's A770 is CI throughput) |
