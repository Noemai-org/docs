# DEC-2026-11-21 · Architect rulings A507 to A517 (interim), the texts of A475, A476, A486 and A487, and the withdrawal of A493 to A501

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 21 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 21 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A507 to A517 (§1); the texts of A486, A487, A475's conditions and A476's wording (§2); the withdrawal of A493 to A501 (§3). |
| **Supersedes** | **A509 changes the line of A506** "The loader checks no mode or owner for DSN files" (`DEC-2026-11-21-architect-rulings-a502-a506`): DSN files get the key-file checks. **A511 builds on A454.** **A514 completes A490 and A505** for the gateway start. **A513 accepts the design of DEBT-54** (the epoch path). **A507 orders** noema#840 before noema#833. **A493 to A501 are withdrawn** (§3). Otherwise per ruling, in §1 and §2. |
| **Amends** | The debt register (DEBT-54 notes A513); nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 21 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A507 to A517; the late texts; the withdrawal
- Decision: §1, §2, §3
- Rationale and evidence: the Architect's message of 21 Nov 2026 and the Founder's instruction to the Steward, relayed
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-12, INV-19, INV-21, INV-22, INV-29; AGENT-11, AGENT-13, AGENT-15, AGENT-16; REQ-TRU-009, REQ-STM-001, REQ-SEC-009, REQ-UI-001; PERD §23, §36.1, §40.1; SoT §43.2a
- Supersedes: see the Supersedes row above
- Migration notes: migration 0037 is DEBT-54's epoch path (A513); an `action_graph` kind in the pack manifest is a possible contract change (A510: the AGENT-15 steps apply if the manifest schema is a contract)

## 1. The rulings, as given

### A507 (interim).

Merge #840 before #833, because #840 fixes the plan-hash refusal Codex found. SR's two open items on #840 (declined-request ownership check, A503 pass-through) are accepted follow-ups, owned by C1, with a test each.

### A508 (interim).

A lane owner may push to another lane's PR branch when the owner asks, announced in the PR. Your "C1 pushed to EL's #785" is confirmed as intended.

### A509 (interim).

DSN files get the same key-file checks as key files: regular, owned by the effective user, no group or other bits, no link, read through one open descriptor. IL writes them 0400, owner 65532. EL's #810 applies the shared reader.

*Supersedes or changes:* changes the line of **A506** "The loader checks no mode or owner for DSN files".

### A510 (interim).

Action graphs must be hash-pinned: add an action_graph kind to the manifest, with new hashes in packs/, as its own PR. C2 owns it, with the AGENT-15 steps if the manifest schema is a contract. No unverified graph is ever served.

### A511 (interim): The Planner.

- The slot kind comes from the intent node's slot list (A454), not the graph file.
- C1 extends intake.PlanRequest with Runnable, PolicyParams, Facts and EvidencePacket, filled from Trust's own steps.
- The applies_when evaluator reuses the Trust policy expression evaluator, with no new language. If the grammar differs, C1 raises a CONFLICT block.
- EL builds plangraphs.Intents and PlanContexts after #785 merges.

### A512 (interim).

EL may add a second read-only pack accessor, for the Recorder's policy id and escalation set. Nothing is hard-coded.

### A513 (interim, DEBT-54).

C2's design is accepted: the epoch trigger is an explicit signal from the sealed snapshot passed into Save, with a typed subject_ref column and a CHECK against the JSON target_ref, and the increment at Save with the epoch on INTENT_ADMITTED. It is migration 0037, red first, with an independent migration read from EL or C1. It is not on the G1 critical path, so nobody waits for it.

### A514 (interim).

The gateway start fills AuthnRef, PrincipalType and AssertedBy (empty, because the verified issuer isn't stored), and Start reads sess.AuthnRef. EL adds these as commits inside #872 (A505). C2's resolver swap follows #872.

### A515 (interim, #860).

The maximum utterance duration is a required host setting with no UI default. The bench value is 20000 ms, equal to A380's STT 20 s. The pack's session_limits.json holds only clock_skew_s.

### A516 (interim, UI merge rule).

A UI PR merges when its own tests are green and its card's slice is complete. Live integration and Android acceptance are separate cards and PRs.

### A517 (interim).

- BO's row-12 format (a stamped artifact file list plus the leak scan, with a secret-name pattern) is accepted.
- A --tokens-dir run cannot read reconstructions. The G1 stack uses the IdP provider.
- "Stamp comparison" means both: re-read equality (already in #875) and the run stamp compared across artifacts, for #717.
- OpenTelemetry is already in PERD §36.1, so #685 needs no new approval. SR's conditions (enum-only attributes, no production exporter) are accepted.

## 2. The texts received late, as given

These four were named without text in `DEC-2026-11-20-architect-rulings-a469-a485` and `DEC-2026-11-21-architect-rulings-a502-a506`. The Founder gave their texts to the Steward on 21 Nov 2026.

- **A486:** a partial worker setting is a gap, `/readyz` 503 names the missing setting; invalid stays fatal.
- **A487:** the Intron key is read from a file; the base URL is a runner argument; Voice builds `--check-key`.
- **A475 conditions:** PERD sections cited, value labelled a Founder decision, no G1 evidence states a grant lifetime as the product's.
- **A476 wording:** re-read, not replay.

*How they fit:* A486 is the rule noema#838 applies (EL's red `e338c1c9` and green `a42d8532`). A475's conditions are the ones noema#847 follows for the grant, record and transaction lifetimes. A476's wording means the runner's `after_replay` phase is a **re-read** of the reconstruction through the audit-only route, compared byte for byte with the first read, not a replay. The Steward changes no wording of the merged records.

## 3. The withdrawal of A493 to A501, and what remains without text

- **A493 to A500 and A501 are withdrawn** by the Architect (the merge queue, the compile gate, the CI lanes, the docs-only skips and the flake rule). They were relayed to the Steward on 21 Nov 2026 and **are not recorded**; docs#221, which carried them, is closed by the Founder and nothing was pushed to it. The merge queue is not turned on, and the Steward's list no longer holds "turn on up-to-date".
- **The merged record `DEC-2026-11-21-architect-rulings-a502-a506`** lists, in its ledger, a row for A493 to A500 "(docs#221, open)" and "A501 not received". That record is not edited; this paragraph supersedes those two lines: A493 to A501 do not exist as rulings.
- **A467 is left blank**, as the Founder said: the Steward has no separate text and invents none.
- **A474's follow-up (by C1)** is still named without text. (A474 itself and OD-P-100 are as recorded.)
- **DEBT-54** (the epoch path) carries a note in the debt register: A513 accepts C2's design, migration 0037, red first, independent migration read from EL or C1, not on the G1 critical path.

## 4. What the Steward did, and where the rulings are silent

- **The merge order of A507** (noema#840 before noema#833) is recorded for the Founder; nothing here changes a gate. SR's two open items on #840 are C1's follow-ups, a test each.
- **A508** confirms that a lane owner may push to another lane's PR branch when the owner asks and it is announced in the PR. The Steward's own pushes to others' branches have been merge-main commits and mechanical fixes at the Founder's request, announced in each PR.
- **A509 and the DSN files.** The Steward writes no value or path: IL writes the DSN files 0400, owner 65532, and EL's noema#810 applies the shared reader. The `deploy/` files are IL's, and a `.github` or `deploy` change needs SR's read.
- **A510 and A515** may touch the pack manifest schema or a host setting. The Steward registers no migration for them; a contract change follows AGENT-15 (a version bump and a migration note, owned by C2 and IL).
- **A513 and the migration ledger.** 0037 is DEBT-54's; the ledger on noema#183 already reserves it. Next free migration: 0038.
- **No `tasks.csv` change here.** The task rows for STM-05, EDG-03 and UND-17 are in their own change request (`CR-2026-11-21-task-rows-stm-05-edg-03-und-17`), and the G0-N checklist is refreshed in its own pull request.
- **Next free ruling: A518.**

## 5. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-architect-rulings-a358-a453` | A358 to A362, A380 to A453 | |
| `DEC-2026-11-20-architect-rulings-a454-a467` | A454 to A466 (A467: no text) | |
| `DEC-2026-11-20-architect-rulings-a469-a485` and `DEC-2026-11-20-architect-a468-and-a480-corrected` | A468; A469 to A485 | |
| `DEC-2026-11-21-architect-rulings-a489-a492` and `DEC-2026-11-21-architect-rulings-a502-a506` | A489 to A492; A502 to A506 | |
| This record | A507 to A517; the texts of A475, A476, A486, A487 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank), A474 follow-up | **A518** |
