# DEC-2026-11-26 · Architect rulings A704 to A720 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 26 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves, from a personal account, and merges it (A111, A638; AGENTS §2, item 3). |
| **Date** | 26 November 2026 |
| **Owner** | Principal Architect (the rulings); the Founders (the merge) |
| **Decides** | Rulings A704 to A720 (§1), every one Interim. |
| **Supersedes** | **A708 refines** A691 (window 0 for the reversal pair): the schema and loader allow 0. **A712 rejects** design 8 of the INP-01 note. **A717 waives** ENV-03 for EVD-05's hostility-proxy part only (the draft `CR-2026-11-25-evd-05-hostility-proxy-split` is approved by it). **A718 narrows** Codex's reading to the current open list. **A719 restates** the plan's G0 rule without changing it. Otherwise nothing; per ruling in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. `tasks.csv`: EVD-05 `blocked` false (§2). OD-P-118 updated in place. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder's personal approval (A111, A638)
- Date: 26 November 2026
- Owner: Principal Architect; Founders
- Decides: A704 to A720
- Decision: §1
- Rationale and evidence: the Architect's message of 26 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-12, INV-14, INV-16, INV-22, INV-29; BD-08; AGENT-14, AGENT-15, AGENT-16; REQ-CTX-007, REQ-CTX-008, REQ-RES-005, REQ-INT-004, REQ-INP-004, REQ-STM-001, REQ-EXE-003, REQ-ENV-003, REQ-OPS-003; SoT §51
- Supersedes: see the Supersedes row above
- Migration notes: A708 changes the pack schema and loader to allow a window of 0 (C1, a small contracts PR for both Founders; AGENT-15 steps). A709: the next migration also tightens migration 0040's CHECK to `outcome = 'ESCALATE'`. A706 extends the allowlist to `evidence/portread`. No migration is added by this record.

## 1. The rulings

### A704. Injection screen inputs (unblocks Reconciler, Evidence, Policies, Recorder)

The five Limits are settings with no code default (AGENT-16):

| Limit | Value |
|---|---|
| max patterns | 64 |
| max pattern length | 1024 characters |
| max document size | 65536 bytes |
| max nesting depth | 8 |
| field cap | 256 characters, as the README already says |

- Values go in the bench compose only. EL maps them to the real field names and adds the required `NOEMA_INJECTION_*` settings.
- Alert writes a structured log line through the redactor and increments `noema_injection_record_failures_total`.
- `CorrelationOf` reads the correlation id from the request context through `platform/telemetry`.
- IL provisions the evidence login and the `core-evidence` key as the A536 two-holder design, with `MAX_ACTIVE` 2 (A594).

### A705. Planner text bound

`NOEMA_PLAN_TEXT_MAX_BYTES` is required with no default. The bench compose sets 256.

### A706. Version token (A665)

- `version_token` is the maximum entry version, as a string.
- `complete` means the read answered and was not unavailable.
- The allowlist is extended to `evidence/portread`, in its own PR.

### A707. Dispatcher and Revalidator build site

Approved: a small port in `execution/bridge` that `cmd/core` implements over a client from the composition.

### A708. #988

- The schema and loader allow a window of 0. C1 changes them in a small contracts PR for both Founders.
- The reversal pair stays with window 0 (A691).
- The four single-valued windows use the smaller freshness limit of their sources (300 s for credit and switch).
- EL reworks #988 after that PR.

### A709. Controller PR conditions (SR)

- `step_params` carries only bound params.
- Personal identifiers are masked or hashed.
- The schema sets `maxProperties` and `maxLength`.
- These are conditions of the Controller PR, not follow-ups.
- The next migration also tightens migration 0040's CHECK to `outcome = 'ESCALATE'`.

### A710. Owners for the gaps nobody owned

| Gap | Owner |
|---|---|
| RequestEvents appender (confirmation route) | C1 |
| StepFactSource (Recorder) | C2 |
| Explainer row reader for `explanation.FactsSource` | C2 |
| Go recipient matcher (`x/text`, manifest kind) | C2 |
| Ownership and Candidates builders | EL, after C2's matcher |
| Runnable FactsSource | EL, after #977 |
| Ops listener | EL (G2 work, not on the G1 path) |
| `confirmation-answer.v1` TypeScript entry point | C1 |
| Conversation POST success schema and parser | C1 |

### A711. #970

- `payment.counterparty` is removed from the candidate-sourced kinds. The facts inventory and any template naming it are updated.
- C2 finishes #970 with amount, account and time.
- The recipient label loses the name. That is the intended privacy result (A676).

### A712. INP-01

- Design 8 (slot inheritance) is rejected. N+1 is compiled alone, and missing slots are asked through SLOT clarification, which is on `main` since #926.
- The other safer defaults stand.
- #684 merges after EL's re-read.
- The Steward drafts the REQ-INT-004 rewording (A680).

### A713. Compile run 8

- #931, #932, #929, #910, #936 and #938 are merged.
- C2 runs the offline A604 check against BO's regenerated recordings, with no spend.
- When it passes, C2 states the exact workflow inputs and the Founder dispatches.
- Stop rule A605 stands: runs 8 and 9 at most.
- The 9000 basis-point threshold stays as the Interim value, to be reviewed on run 8's evidence.

### A714. Bench compose values (IL)

| Setting group | Value |
|---|---|
| Events settings | A658's table |
| Execution timeouts | execute 10000, rollback 5000 |
| Plan text | 256 |
| Injection limits | A704 |

- Relay: in the bench and test profiles only, with one shared SYNTHETIC secret file for mock-case and the relay. It trusts mock-case's key only there.
- Netcheck asserts that only the ops listener mounts the admin emitter DSN (A699).

### A715. Frontend

- Maximum push-to-talk recording: 30 s, as a UI setting, and Voice enforces the same limit host-side. It is OPEN for the Founders.
- SSE frame bound: 65536 bytes, equal to the server's `NOEMA_EVENTS_MAX_EVENT_BYTES`. On a disconnect FE falls back to its 2 s polling.
- `none_option_id` comes from the parsers regenerated after #926.
- Tokens never appear in an artifact, log or screenshot.
- The token directory is whatever #983's README documents. FE reads it from there.

### A716. Voice and devices

Recording devices are confirmed (the Founder's statement of 26 Nov). Voice records it in `status/VOI-05.md`. It will not be asked again. The private store still needs `store.sh init|check` on the bench host.

### A717. EVD-05

The ENV-03 waiver is ruled for the hostility-proxy part only (the proxy is ours). The Steward records it. C2 starts now.

### A718. Codex

The sweep read stale heads, including merged PRs. From now Codex reads only the current open list, at the heads named below.

### A719. G1 and G0-N

- Everything for G1 proceeds now.
- The plan says Phase B results count only after G0 passes, and G0-N needs Tushe.
- So the run is executed and the evidence kept, and the gate record is written when G0-N closes. That is the existing plan, not a new rule, and it blocks no work.
- The Tushe URL and Environment #620 is the open G0-N item.

### A720. G2 start

G2 work in parallel stands (A613, A622). The tasks are in the prompts.

## 2. What the Steward did, and where the rulings are silent

| Item | What was done |
|---|---|
| **EVD-05 waiver (A717)** | Recorded: ENV-03 is waived for the **hostility-proxy part only**; the Tushe-contract part keeps ENV-03 as its Need and waits for ENV-05's list of unstated behaviours. `tasks.csv`: EVD-05 `blocked` set to false (status Backlog; C2's pull request moves it). The draft `CR-2026-11-25-evd-05-hostility-proxy-split` is applied by this waiver; the plan row text follows in plan v1.30 (its own pull request). |
| **BEN-06 to BEN-09** | Already Done in `tasks.csv` on `main`; no change. |
| **[OPEN] entries (provisional, NON-CANONICAL)** | **OD-P-120** the injection limits values (A704); **OD-P-121** the planner text bound (A705); **OD-P-122** the 30 s push-to-talk maximum (A715, OPEN for the Founders); **OD-P-123** the version token (A706); **OD-P-124** window 0 in the schema and loader (A708; OD-P-118 updated in place); **OD-P-125** INP-01 design 8 rejected (A712); **OD-P-126** the REQ-INT-004 rewording (A712, A680: PERD v1.30, Proposed, in `main`). |
| **Plan version (A701, A671)** | Opened as its own pull request: plan v1.30 restates §4 and §13.1 (the tier by path and the review standing) with its change request. |
| **AGENTS §15 lessons** | Opened as its own small pull request (AGENTS §15: a correction goes in a small PR reviewed by EL). |
| **A707, A709, A710, A711, A714, A715 (other items)** | Other owners' work; nothing for the Steward beyond this record. A709's conditions bind the Controller PR (#994 and its follow-up). |
| **A713** | The Steward notes the stop rule (runs 8 and 9 at most) and the Interim 9000 bp (OD-P-101 stays Open). The Founder dispatches run 8 when C2 states the inputs. |
| **A716** | Voice's `status/VOI-05.md` (in `noema`) carries the devices statement; the Steward writes nothing there. |
| **A718** | Recorded; nothing for the Steward. |
| **A719** | The gate record for G0-N is written when G0-N closes; nothing is dated now. |
| **Next free ruling** | **A721** |
