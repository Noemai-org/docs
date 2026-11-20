# DEC-2026-11-20 · Architect rulings A469 to A485 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 20 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 20 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A469 to A485 (§1). **A468 has no text** (§2). |
| **Supersedes** | **A472 replaces** the worker start deadline as a code constant with a required setting. **A474 settles** `policypublish`'s identity (no `--published-by` flag). **A477 adds** the bench settings of the worker, gateway and recovery (the settings table of A356 stands for its own names). **A481 answers** SR's open Q5 on docs#212 and docs#213 (the oracle credential, A444). **A482 assigns** migration numbers 0036 and 0037. **A483 settles** how noema#658 merges. **A470 restates** A456 for Decide (§2). Otherwise per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 20 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A469 to A485
- Decision: §1
- Rationale and evidence: the Architect's message of 20 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-03, INV-12, INV-21, INV-22, INV-30; AGENT-11, AGENT-13, AGENT-16, AGENT-22; REQ-TRU-009, REQ-STM-001, REQ-AUD-001, REQ-BEN-004, REQ-SEC-004; PERD §23, §39.2, §39.4, §64.2, §65.1; SoT §38.4
- Supersedes: see the Supersedes row above
- Migration notes: migration 0036 is noema#841 (the investigation row, A441); migration 0037 is reserved for DEBT-54's epoch path (A482)

## 1. The rulings, as given

### A469 (EL, interim ratified).

A configured Trust, worker or route whose adapters are not yet built does not stop the process. The process starts, and /readyz answers 503 naming each missing component in fixed text. A present but invalid setting stays fatal: a bad number, an unreadable key directory, a pack that fails verification, or a route with no logger. A442 stands: a worker that dies exits the process non-zero. This is what A445 asked for.

### A470 (Decide, noema#839, noema#840, noema#833).

- Decide returns the decision id for every recorded outcome.
- A plan hash and steps are required only for ALLOW.
- A non-ALLOW with no steps and no hash is recorded as is.
- A grant on a non-ALLOW is refused before any transaction.
- ConfirmationBindingEvidenceHash has one source, noema#833, computed from the sealed snapshot. noema#840 does not map it.
- C1 adds an optional DeclinedRequestID to intake.RecordRequest, plus EL's doc line.

*Supersedes or changes:* restates **A456** for Decide.

### A471 (noema#822).

An over-long upstream answer is 502 with the existing public upstream code, and no new code. 500 is for our own faults. The cap is 65,536 bytes (A457).

### A472 (noema#823, noema#838).

The worker start deadline is not a code constant. It is the required setting NOEMA_INVESTIGATION_START_TIMEOUT_MS, with the bench value in A477. No code default.

### A473 (portread).

An unusable or unavailable case list gives an explicit UNKNOWN, which blocks ALLOW. An empty list from a source that answered is "no cases".

### A474 (policypublish).

There is no --published-by flag, because identity comes only from the authenticated session (INV-12). The record carries the authenticated DB role, the pack document hash and the commit SHA.

### A475 (noema#838 gaps).

- noema#838 merges as it is, with /readyz honestly 503 for Planner, Recorder and Pack. The final main.go PR comes after noema#773 merges.
- EL builds plangraphs.Intents and PlanContexts from the verified pack store. The A454 slot declarations come from the intent node, and the graph is picked by applies_when.
- EL may add one read-only registry accessor to trustpack.Pack, and tells C1.
- The Recorder takes its policy id and escalation set from the pack, and its lifetimes from settings.
- The grant and record lifetimes and the transaction timeout are required settings. If the PERD or trust_limits.json names a value, use it. If neither does, use 60 s for the grant, 60 s for the record and 10 s for the transaction as bench-only values. Write the gap in the PR for the Founder.

### A476 (recovery and replay in a Compose run).

- The recovery trigger is a restart of the core container. The core runs one recovery sweep at startup, and a ticker repeats it.
- after_recovery: after the cases finish, the stack job restarts the core and waits for /readyz 200. It then reads each case's reconstruction through the audit-only route (noema#783).
- after_replay: the runner reads again through the same route and compares the bytes with the first read. A reconstruction depends on the Record alone (INV-21), so replay is re-reading.
- The reader is an audit principal, seeded in the stack's tenant init. The oracle is never used.

### A477 (bench settings).

These go in Compose only, with no code default, bench-only. Values:

| Setting | Bench value |
|---|---|
| NOEMA_INPUT_DEDUP_WINDOW | 5 min |
| NOEMA_INPUT_RECORD_TIMEOUT | 5 s |
| NOEMA_INVESTIGATION_QUEUE | 64 |
| NOEMA_INVESTIGATION_WORKERS | 1 |
| NOEMA_INVESTIGATION_RUN_TIMEOUT_MS | 180000 |
| NOEMA_INVESTIGATION_START_TIMEOUT_MS | 30000 |
| NOEMA_EDGE_KEY_MAX_ACTIVE | 2 |
| NOEMA_TEMPORAL_ACTIVITY_TIMEOUT_MS | 240000 |
| NOEMA_TEMPORAL_SHUTDOWN_DRAIN_MS | 30000 |
| NOEMA_STM_RECOVERY_IDLE_MS | 240000 |
| NOEMA_STM_RECOVERY_BATCH_SIZE | 50 |

Workers = 1: the model-service pool is 6 and one pipeline uses 5 in flight. A second concurrent pipeline would be refused locally.

Ordering constraints: the loader refuses ACTIVITY_TIMEOUT ≤ RUN_TIMEOUT and RECOVERY_IDLE ≤ RUN_TIMEOUT, if the settings mean what their names say. Otherwise a live run could be picked up twice.

### A478 (A460 fixture).

CI proves the fixture equals fresh output through a step in the core tests job. SR approves the step and you approve the .github change. No lint exemption.

### A479 (noema#815).

JSON Schema cannot compare ids across members. noema#815 merges with EL's README, which names the three consumer checks, and the test that pins that the schema does not state them. Three follow-ups, each with an owner:

- C1: a cross-member check in validate.py with fixtures.
- C1: the same refusal in the core's writer.
- FE: the UI refuses an inconsistent response before polling.

### A480 (flow).

- Codex outage: a Tier 1 independent read comes from SR or another role. Tier 2 and 3 need no read. A455 stands (local red output recorded once, flagged).
- noema#832: IL's follow-up PR makes the reader sum all gathers, not take the widest. The sum is 5, against a pool of 6.
- noema#821: BO's follow-up PR makes the full-run path call the two writers, before noema#730's full mode runs.
- noema#786: IL fixes the proxy panic, then it merges.

### A481 (oracle credential, A444).

The oracle credential lives only in the bench-live Environment, which needs 2 reviewers. No agent session holds, requests or reads it (INV-22). Each agent confirms this in its next hand-off.

### A482 (DEBT-54 and migrations).

- 0036 is noema#841. DEBT-54's migration takes 0037.
- Later migrations take the next free number at merge time. The Steward keeps the list on docs#183.
- The epoch lives in Postgres, on the row it governs, written in the same transaction as the Record event. Code never derives it from a clock.
- C2 quotes the DEBT-54 rule text in the PR if it conflicts with this.

### A483 (noema#658).

It merges as a slice. SEC-08 stays In progress, and the author names the remainder in a follow-up card.

### A484 (two one-shots).

- C2 builds cmd/migrate --dsn-file … --migrations-dir …, a one-shot that calls db.Migrate, under EXE-08.
- C1 builds cmd/tenantinit, which registers the core-trust public key and the tenant rows.
- IL writes the Compose one-shots against those names.

### A485 (benchmark data).

- The operating point is null with a stated reason until you supply the two limits. G1 does not need it, because it serves the comparison arms.
- The arm manifest default is benchmark/arms/arms.v1.json. BO may propose another path in the noema#799 PR.
- Units: rates are _bp integers, durations _ms, counts integers.
- noema#826: the zero-unsafe test uses integer counts, not a rounded rate.

## 2. What the Steward did, and where the rulings are silent

- **A468 has no text.** The Steward's earlier record named A468 as the next free number; no ruling under that number has been received. The Steward invents none. Next free ruling: **A486**.
- **A470 and A456.** A470 restates A456 ("Decide returns the decision id for every recorded decision") for the Decide route and adds the optional `DeclinedRequestID` and the single source of `ConfirmationBindingEvidenceHash` (noema#833). Both are recorded as given; the later ruling governs where the wording differs.
- **A472 and the settings rule (A330).** The setting name `NOEMA_INVESTIGATION_START_TIMEOUT_MS` follows the rule `NOEMA_<AREA>_<WHAT>[_MS|_BYTES]` (A330). Two names in A477 carry no unit suffix (`NOEMA_INPUT_DEDUP_WINDOW`, `NOEMA_INPUT_RECORD_TIMEOUT`); the values are given with their units ("5 min", "5 s"). The Steward records them exactly as given and does not rename them. The Architect or EL says if the names should carry a suffix.
- **A475's gap.** If neither the PERD nor `trust_limits.json` names the grant, record and transaction values, EL uses 60 s, 60 s and 10 s as bench-only values and writes the gap in the PR for the Founder. The Steward adds no value anywhere else.
- **A478 and A480 need the Founder.** A478 says the `.github` change (the core tests job step) is approved by the Founder, with SR approving the step. A480 says that during a Codex outage a Tier 1 independent read comes from SR or another role, and that Tier 2 and 3 need no read. The Steward reads A480 as a rule for the duration of a Codex outage, not a standing change to the tiers of AGENTS §11 and plan §4; a non-author Founder approval is still required for every merge (A111). The Architect says if it should be read differently.
- **A481 answers SR's open Q5** (docs#212, docs#213): the oracle credential lives only in the bench-live Environment (2 reviewers); no agent session holds, requests or reads it (INV-22); each agent confirms this in its next hand-off.
- **A482.** The migration numbers: **0035 is noema#771** (merged), **0036 is noema#841** (open; the investigation row's `principal_role` and `authn_ref`, A441; the number A441 left unassigned), and **0037 is reserved for DEBT-54's epoch path.** The Steward keeps the list on noema#183 and updates it there (a comment posted with this record). The ledger now: on `main` 0030, 0031, 0033, 0034, 0035; **0032 open (noema#756)**; 0036 (noema#841, open); 0037 reserved (DEBT-54); 0022 reserved; **next free 0038.**
- **A483.** noema#658 merges as a slice. SEC-08 stays In progress (the Steward changes no status). The remainder is named by the author in a follow-up card. **REQ-SEC-004 is not Done** while SEC-08 is In progress, so the G0-N checklist row 11 stays "not done" until the remainder lands (the checklist refresh of docs#214 says "not Done until #658 merges"; the Steward corrects that sentence in the next refresh).
- **Voice's two debt entries** are already registered: **DEBT-55** (noema#640 drops the audio source's cleanup exception, owner Voice, before any baseline figure is cited as evidence) and **DEBT-56** (VOI-16 has no live runner), both confirmed by A449; the A250 native-speaker waiver is **DEBT-39**. No new entry is made, so no entry is duplicated.
- **Independent reads that satisfy A463, with their heads**, are listed on noema#183 (the comment of 20 Nov and its update with this record): noema#716 (0030), noema#769 (0033), noema#759 (0034; C2's read: no link found), noema#771 (0035), noema#756 (0032; **its head moved to `6bfd491e`, so every read at `fa97db1a` needs a re-read**) and noema#841 (0036; **no independent read yet**). The Steward adds no read that is not in a thread.
- **Merge-order and status entries follow the Founder's merges** (the Architect's instruction). The Steward changes `tasks.csv` statuses only from merged evidence, after the Founder merges.
- **A479's follow-ups** have owners (C1 twice, FE once); they are tasks for the owners and are not registered as debt by the Steward.
- **A484's one-shots** sit under EXE-08 (C2's `cmd/migrate`) and C1's `cmd/tenantinit`; no task row is added by the Steward (no new ID was given).

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-19-architect-rulings-a341-a357` | A341 to A357 | |
| `DEC-2026-11-19-architect-rulings-a362-a376` | A362 to A376 | |
| `DEC-2026-11-19-founder-intron-data-terms-a377-a379` | A377 to A379 (Founder) | |
| `DEC-2026-11-19-architect-rulings-a384-a388` | A384 to A388 | |
| `DEC-2026-11-20-architect-rulings-a358-a453` | A358 to A362, A380 to A453 | |
| `DEC-2026-11-20-architect-rulings-a454-a467` | A454 to A466 (A467 named, no text) | |
| This record | A469 to A485 (A468 named, no text) | **A486** |
