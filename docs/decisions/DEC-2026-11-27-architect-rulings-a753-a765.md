# DEC-2026-11-27 · Architect rulings A753 to A768 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 27 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves, from a personal account, and merges it (A111, A638; AGENTS §2, item 3). |
| **Date** | 27 November 2026 |
| **Owner** | Principal Architect (the rulings); the Founders (the merge) |
| **Decides** | Rulings A753 to A768 (§1), every one Interim. |
| **Supersedes** | **A753 replaces** A749 (stacking is allowed again, up to 4 child PRs on one parent). **A755 accepts** C1's reading of WAIT. **A758 answers** four findings. **A760 applies** A752 to #1034. **A762 confirms** the stand-in under A750 and A751. **A765 restates** the G1 critical path (A684, A696, A736, A747). **A766 states** who merges a child into its parent's branch. **A767 conditions** A753: no stacked child until IL's guard PR merges (A765's "stacks on that PR" is read subject to it). **A768 rules** on A755 against INV-30 and closes SOT-C-36. Otherwise nothing; per ruling in §1. |
| **Amends** | `AGENTS.md` §11 (A753: stacking). Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder's personal approval (A111, A638)
- Date: 27 November 2026
- Owner: Principal Architect; Founders
- Decides: A753 to A768
- Decision: §1
- Rationale and evidence: the Architect's message of 27 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-12, INV-16, INV-17, INV-20, INV-21, INV-29, INV-30; BD-08; AGENT-11, AGENT-12, AGENT-15, AGENT-16; REQ-RES-005, REQ-VER-004, REQ-TRU-009, REQ-STM-001, REQ-INP-004, REQ-OPS-003; SoT §51
- Supersedes: see the Supersedes row above
- Migration notes: A757 adds an optional `question_key` to the slot declaration in `intent-node.v1.json` (additive, v1, A698; one contract and pack PR for both Founders). A761: #1021's early outcome set is ESCALATE and REJECT (a widened CHECK). A764: the migration read of #1021 (A463) is Voice's. No migration is added by this record.

## 1. The rulings

### A753. Stacking PRs (replaces A749)

Stacking PRs is allowed (not more than 4). This replaces A749. In practice (the Founder's instruction): up to 4 child PRs on one parent; children base on the parent's branch; only the parent merges to `main`; readers read the parent's final head. The `pr-base-guard` change is its own `.github` PR (IL).

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

The newest stack-check (run 16, at `6d6b566`) still listed 18 components as unconfigured. That was before #1018 and about a dozen other merges. The next run is the authority. The remaining gaps, by owner, are in the table below, and owners are expected to execute on them right now and deliver reports on them. If an owner is waiting for a PR to merge, it stacks on that PR (A753), names the stack in its title and notes it in the PR body.

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

### A766. Who merges a child into its parent (SR 1)

- Agents never merge. A non-author Founder merges a child into its parent's branch.
- The conditions are green CI at the child's head and the child owner's READY.
- SR and Codex read only the parent's final head, as in A753.
- The parent's driving Founder is the default merger. Either Founder may do it.

### A767. Stacking before the guard PR (SR 2)

No stacked child until IL's guard PR merges. Until then, dependent work is one PR with commits.

### A768. A755 against INV-30 (what "not recorded" means)

- A WAIT is a stateless evaluation result. The turn ends with no write, no grant and no verdict.
- Nothing about the wait is held in Temporal, because Temporal is never authoritative (INV-30).
- The window is derived from the timestamps of facts already on the Record, so it is deterministic and replayable (INV-21).
- Re-evaluation happens either on the customer's next turn or in a Postgres-based sweep. The sweep reads the Record, and it is the fallback of REQ-VER-004.
- At window expiry the contradiction becomes an ESCALATE Decision Record.
- OD-P-136's safeguards (SR 5) apply: no write, no grant and no verdict while waiting, and an expiry that always escalates.
- Recording the WAIT as a Decision Record stays OPEN until after G1, and a Founder decides it.
- SOT-C-36 is filed as the conflict block, with A768 as the ruling.

## 2. What the Steward did, and where the rulings are silent

| Item | What was done |
|---|---|
| **`AGENTS.md` §11 (A753)** | Stacking is allowed again, replacing A749 (A766 and A767 apply: no stacked child until IL's guard PR merges; a non-author Founder merges a child into its parent's branch): up to 4 child PRs on one parent; children base on the parent's branch; only the parent merges to `main`; SR, Codex and the Founder read the parent's final head; a child names its stack in its title and body. The `pr-base-guard` change is its own `.github` PR (IL). Per A767 no stacked child is opened until that guard PR has merged, so none is red on `pr-base-guard`. The Steward does not change the guard. |
| **A741 and A744 (A759)** | Recorded with the text as given in §1 (A759). |
| **[OPEN] entries (provisional, NON-CANONICAL)** | **OD-P-136** recording a WAIT (A755, OPEN until after G1); **OD-P-137** the evidence record timeout (A754); **OD-P-138** the `question_key` design (A757). |
| **DEBT-60** | Added to the debt register: the by-target read function for freeze rows (A756). Owner C1 (the Steward's default: #1035 is C1's); Tier 3 proposed (the ruling gives none). |
| **BEN-06 to BEN-09** | Already Done in `tasks.csv` on `main`; no change. |
| **A758 and A761** | Other owners' work; the Steward records the assignments as ruled. |
| **A762** | Recorded; nothing for the Steward. |
| **A765's table** | Recorded as ruled; `tasks.csv` is not moved for it. |
| **A765's table: #1004** | Corrected by the Steward: #1004 is open and unmerged (Codex finding on docs#252). Only #1016 is merged. |
| **Points still open (SR and Codex on docs#252; A766, A767 and A768 answered SR 1, SR 2 and the INV-30 finding)** | (3) A764 gives Voice the independent read of #1021's migration, while §11 and A685 name EL, C1 or C2 (not the author): **Architect**, unless §11 is amended. (4) #1021's CHECK is widened in place in migration 0043, with no 0044 (A761), with a test inserting a REJECT keyed by turn and principal: **C1**. (5) DEBT-60's tier (SR: Tier 2, with a test that a read error reads as frozen) and what exactly it adds: **Architect**, with **C1**. (6) #1032 compares integer seconds against `ceiling_ms/1000`, which truncates the ceiling safely, and its regression covers the subtraction for a year-2400 expiry: **the #1032 owner**. (7) `NOEMA_EVIDENCE_RECORD_TIMEOUT_MS` needs an upper bound with the other required timeouts (A754, OD-P-137): **IL** with **EL**. (8) A762 holds only while #733 does not change or newly reach the start site: **EL** and **SR**. (Numbers are SR's; no committed ruling answers these yet.) |
| **A766 to A768** | Recorded as ruled. AGENTS §11 states A766 and A767. SOT-C-36 is closed with A768. OD-P-136's default is restated per A768; whether to record the WAIT as a Decision Record stays OPEN, and a Founder decides it. |
| **Next free ruling** | **A769** |
