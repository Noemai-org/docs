# DEC-2026-11-28 · Architect rulings A770 to A776 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 28 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves, from a personal account, and merges it (A111, A638; AGENTS §2, item 3). |
| **Date** | 28 November 2026 |
| **Owner** | Principal Architect (the rulings); the Founders (the merge) |
| **Decides** | Rulings A770 to A776 (§1), every one Interim. |
| **Supersedes** | **A772 amends** A605 (run 9 is allowed after the fixes and the labelled probe; run 10 still needs the Founder). **A773 confirms** A769 as in force on the Founder's order. **A770 restates** A455 (the 20-minute rule). Otherwise nothing; per ruling in §1. **Numbering:** the Steward had numbered the approval of SR's conditions 3, 4 and 6 to 9 "A770" in `DEC-2026-11-27-architect-rulings-a753-a765`; that is renamed SR-APP there, because the Architect's A770 is the CI throughput ruling below. |
| **Amends** | `AGENTS.md` §11 and the Review standing paragraph (A770, A771, A773). Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder's personal approval (A111, A638)
- Date: 28 November 2026
- Owner: Principal Architect; Founders
- Decides: A770 to A776
- Decision: §1
- Rationale and evidence: the Architect's message of 28 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-03, INV-14, AGENT-08, AGENT-11, AGENT-16, AGENT-27; REQ-TST-006, REQ-INP-004, REQ-OPS-003; BD-08; SoT §51
- Supersedes: see the Supersedes row above
- Migration notes: A774 adds a per-binding `disclosure` member to `outcome_bindings` (#1026, a draft; additive, AGENT-15, C1). A757's `question_key` (OD-P-138) is unchanged. No migration is added by this record.

## 1. The rulings

### A770. CI throughput

- Runners are saturated: 94 runs queued and 195 in progress. That is why agents have waited hours to see a red.
- A455 is the rule: 20 minutes after pushing a red, the owner pushes the green, with the local red recorded in a PR comment ("red not observed in CI: queue"). Nobody waits longer for a runner.
- IL adds concurrency groups with `cancel-in-progress: true` for pull-request runs in the workflows that lack them. Docs-only and status-only pushes skip the heavy jobs. This is a `.github` PR, with SR reading it.

### A771. One owner per branch

- Only the PR's "Authored By" agent pushes to its branch. Anyone else posts the exact fix as a comment.
- Several sessions per agent are colliding and cancelling each other's runs.
- #1043: EL pushed `agrees()` at 30b47d66 and BO has a local equivalent. BO fetches, drops its duplicate, and continues.

### A772. Compile run 8 failure, and A605 amended

The investigation is accepted: G-B treats a status check as an action (the gate wording "something to be done"), and G-E misses the payment-investigation node ("resend am for me" reads as none_or_other). Goldens, the 9000 basis-point threshold and the inputs are not changed to make a run green. Fix, red first, with no benchmark-only branches (REQ-TST-006):

1. **Gate wording:** only an explicit request to the bank to do something (resend, reverse, refund, escalate, cancel) is an action. A request to check, show, look up or explain status is not.
2. **Node description:** the payment-investigation node covers advice requests and remedy requests. The compiler captures the requested remedy even when it is prohibited, because Trust decides, not the classifier.
3. **Diagnostics:** run 8's evidence shows threshold=n/a and no yes/no answer for the gate. Log the gate's selected answer, probability and threshold in the A602 lines (ids and numbers only). Find why they were missing.
4. **Offline set:** BO's 28 labelled phrasings are run against the compiler, reporting false positives, false negatives and borderline items separately.

**Run 9 (amends A605):** allowed after fixes 1 to 4 land and the labelled probe shows no false assertion on the 14 non-explicit phrasings. The probe runs the 28 phrasings once, under the same `hard_stop_usd` 5 ceiling. C2 states what has been spent and what remains. **Run 10 still needs the Founder's decision.** C2 owns it. BO supplies the labelled set. SR reads the gate and diagnostics change.

### A773. Stacking is in force now, on the Founder's order

A769 stands. The committed AGENTS text was read as saying stacking is off, so agents declined to stack until it was committed. docs#252 (Steward, SR re-read) carries it. Stacked PRs already open (#1038 on #1021, #1039 on #1037, #1051 on #1035) stay.

### A774. `step_params` disclosure (C1's blocker)

Each bound parameter has a disclosure of VERBATIM, MASKED or HASHED, declared per binding in `outcome_bindings`. The default when absent is HASHED. Packcheck refuses VERBATIM for a parameter whose descriptor type is an identifier, account or name. MASKED keeps the last four digits. C1 adds the member to #1026 (still a draft).

### A775. Deadlock between IL and EL on the ops service

Both build now, in parallel, with fixed names:

- The service name is `ops`.
- The settings are `NOEMA_OPS_DSN_DIR`, `NOEMA_OPS_TLS_CERT_FILE`, `NOEMA_OPS_TLS_KEY_FILE` and `NOEMA_OPS_CLIENT_CA_FILE`.
- EL builds `cmd/ops` main. EL names the listen address in its PR.
- IL builds the compose service, the job that writes the admin-emitter DSN files, and the operator CA and certificate sources. IL mirrors EL's listen address name when it appears.

### A776. Other answers

| Item | Ruling |
|---|---|
| `NOEMA_TRUST_RECONCILE_TIMEOUT_MS` | The bench value is 1000. |
| EPOCH runtime source (request Source kind and NextEpoch port) | C2's, because C2 built the request package. Stacked on #1019 with "STACKED ON #1019". |
| `max_body_bytes` | 32768 (A653, A697, A714). IL dispatches with it. |
| #1044's red evidence | Accepted: the compile-red, the arch-lint failure and the local first-failing test. No re-run. |
| TST-02 smoke | Built dispatch-only now (IL's recommendation). Becomes per-merge after the first 200. The make target is `bench-smoke-30`. |
| AMB-04's SLOT template | Gets its own task ID, AMB-06, in the next plan version. The en-NG `fin.clarify.when` wording is reviewed by the Founder or a native speaker the Founder names, and is not blocking. |
| #1019's condition | One receipt per grant comes from the unique constraint on grant spend (INV-03), so a retry needs a new grant (AGENT-08). EL names the constraint in the PR. |
| `TestTheContextDeadlineStopsTheAttempts` (execution/ledger) | The flaky test is a bug (AGENTS §8). C1 fixes it with a fake clock. |
| #1021 and Voice's read | C1 states in the PR that the migration runner wraps each file in one transaction (cites the code) and that the Writer's early outcome list is ESCALATE and REJECT. |
| G2 builds | Start now for BO: the BEN-12 table generator and the G2 family case fixtures, per A637. |

## 2. What the Steward did, and where the rulings are silent

| Item | What was done |
|---|---|
| **`AGENTS.md` (A770, A771, A773)** | The Review standing paragraph gains the 20-minute rule (A455, restated by A770), one owner per branch (A771), and A773 (stacking in force on the Founder's order; A769 stands). docs#252 had already merged when A773 arrived (merge commit 1049dbc), and the noema copy was re-pointed to it by noema#1046, so the committed text already carries stacking. |
| **Numbering** | The Steward's earlier "A770" (the approval of SR's conditions 3, 4 and 6 to 9) is renamed SR-APP in `DEC-2026-11-27-architect-rulings-a753-a765`, `debt.md`, the decisions README and the session note. |
| **[OPEN] entries (provisional, NON-CANONICAL)** | **OD-P-139** the `step_params` disclosure (A774); **OD-P-140** the stray branch `c2/data02-a758` (left as it is). WAIT recording (A768) is OD-P-136, already open, and DEBT-60 is already in the register; neither is duplicated. |
| **DEBT-61** | Added: TST-02's smoke is dispatch-only, where the plan row says on every merge (A776). Owner IL (the Steward's default). |
| **BEN-06 to BEN-09** | Already Done in `tasks.csv` on `main`; no change. |
| **AMB-06** | A new task ID needs a new plan version with a change request. None is made here. It is carried to the next plan version, with the en-NG review note. |
| **A772 and A605** | Recorded as ruled. `DEC-2026-11-23-architect-rulings-a602-a605` is not edited: this record amends it. |
| **A771, A774 to A776** | Other owners' work; recorded as ruled. |
| **Next free ruling** | **A777** |
