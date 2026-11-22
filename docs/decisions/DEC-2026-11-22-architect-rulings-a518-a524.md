# DEC-2026-11-22 · Architect rulings A518 to A529 (interim), and the confirmation of the task rows STM-05, EDG-03 and UND-17

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 22 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 22 November 2026 |
| **Owner** | Principal Architect (the rulings and the confirmation); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A518 to A529 (§1; A525 and A526 settle the points raised on this pull request); the confirmation of the three task rows of `CR-2026-11-21-task-rows-stm-05-edg-03-und-17` (§2). |
| **Supersedes** | **A518 settles** the scope of the key-file rule on noema#884 and amends A509's DSN reading only by naming the two TLS client private keys. **A520 accepts both recommendations** on DEBT-54 (and so completes A513). **A521 settles** how `cmd/migrate` gets its password. **A524 settles** the SR and FE disagreement on noema#638. **A525 and A526 settle** the flag on STM-05's REQ list (§3) and the done-when of STM-05. Otherwise per ruling, in §1. |
| **Amends** | Plan v1.27 (three rows added, §2); `tasks.csv` (§3); the debt register (DEBT-54 notes A520). Nothing in the SoT or the PERD. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 22 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A518 to A529; the confirmation of the rows
- Decision: §1 and §2
- Rationale and evidence: the Architect's message of 22 Nov 2026 relayed to the Steward; the Security Reviewer's read on docs#224
- Affected requirement IDs / SoT sections: INV-12, INV-29; AGENT-13, AGENT-16; REQ-SEC-009, REQ-TRU-009, REQ-STM-001, REQ-RCV-001, REQ-RCV-003, REQ-SEC-004, REQ-API-001, REQ-INP-001, REQ-INT-001, REQ-INT-002, REQ-UI-001; PERD §40.1
- Supersedes: see the Supersedes row above
- Migration notes: migration 0037 is DEBT-54's epoch path (A520); no new migration number is assigned by this record

## 1. The rulings, as given

### A518 (interim, noema#884).

The two TLS client private keys stay in scope. The public edge.Load data stays out. The rule is mode exactly 0400 and owner the core user. 0600 is refused. C2 moves cmd/migrate's own copy of the checks to the shared reader.

### A519 (interim, noema#885).

The confirmation request row is written by the Recorder in the same transaction as the CONFIRM decision, so a request exists when the answer arrives. EL adds an end-to-end test: a CONFIRM through the real adapter leaves exactly one open request, and the T13 decline references it.

### A520 (interim, DEBT-54).

Both of C2's recommendations are accepted. The subject is a pack-declared subject_slot on the intent node, and the epoch comes from asking the Evidence reader for the subject's case list at admission and passing it into Save. No new table. It is migration 0037, and it is not on the G1 path.

### A521 (interim, migrate password).

There is no new image and no third credential holder. cmd/migrate builds its DSN in process from host, port, database, user and a password file (checked by the shared reader), so there is no shell and no entrypoint script. C2 builds it, and IL's one-shot calls it.

### A522 (interim).

The first stack-check run is the acceptance for core-keys-init. Merge on green and fix forward.

### A523 (interim).

Voice's --check-key prints accepted, rejected or inconclusive (a dropped connection is not a rejection). Accepted.

### A524 (interim, UI access message).

A wrong-role session on the panel gets one plain generic message, the same text for 403 and 404, with no role names and no hint that the view exists. This settles the SR and FE disagreement on #638.

### A525 (interim, STM-05 and REQ-RCV-001).

The REQ-RCV-001 link stays on the row (SR's reading, so there is no v1.28).

- STM-05 only resumes work that was already decided.
- A step that needs a new dispatch ends `NEEDS_PERSON`, or becomes a `RecoveryRequest` that Trust evaluates fresh.
- STM-05 carries no budget. It reports its counts (not-resumed, refused, failed) and the caller escalates. The recovery budget in REQ-RCV-003 stays with the RCV tasks.

### A526 (interim, SR's Trust double).

The recovery package has no Trust port to double. The structural guard (the `no_trust_test.go` import test, with its mutation proof) is the accepted done-when. SR's other test, a voided grant that ends `NEEDS_PERSON`, stays.

### A527 (interim, migrate password).

The password comes only from the checked file (mode 0400, owner, no link). It must never appear in argv, the environment, a log or an error. The one-shot is its only holder, and IL pins that in netcheck.

### A528 (interim).

C2 moves `cmd/migrate` to the shared reader before migration 0037.

### A529 (interim).

A522 fix-forward on `core-keys-init` must never loosen a file mode or the capability set. The A519 end-to-end test runs through the real Recorder adapter, after EL's `DeclinedRequestID` mapping PR.

*Supersedes or changes:* A525 and A526 settle the flag on STM-05's REQ list and its done-when (§3). A527 completes A521. A528 orders A518's `cmd/migrate` change before migration 0037 (DEBT-54, A520). A529 bounds A522 and orders A519's test.

## 2. The task rows, confirmed

The Architect confirmed (Interim) the rows of `CR-2026-11-21-task-rows-stm-05-edg-03-und-17` (docs#224), with the Security Reviewer's three additions to STM-05 and the rewording of UND-17 (SR's read on docs#224, 22 Nov 2026). **Applied in plan v1.27** (`NOEMA_POC_4WEEK_PLAN_v1.27.md`): three tasks added, **STM-05, EDG-03 and UND-17** (owner EL for all three), each joining the G2 review row GOV-11's Needs as CON-08 did. Plan count 278 + 3 = 281; Appendix A and B and `tasks.csv` are regenerated. The merged change request is not edited; this record says it is confirmed and applied.

- **STM-05's done-when gains** (SR's three additions): (1) recovery never asks Trust for a decision, shown by a structural test that the recovery package imports no Trust package or port adapter and by a Trust double that fails the test if it is called; (2) a stored role is used only to resume work already decided and never satisfies Trust's authority step for a decision made afresh; (3) the sweep's count of rows it refused to resume (no role or no `authn_ref`) is reported without any identifier. The migration 0036 written by C1 or C2 is read independently by the other (an author cannot give the independent migration read).
- **UND-17's last clause** now reads "the port refuses an input whose INPUT_RECEIVED the Record does not confirm (A161)" (it read "refuses an unconfirmed input").

## 3. What the Steward did, and where the rulings are silent

- **The flag on STM-05's REQ list is settled (A525 and A526).** The Steward had flagged that the row cites REQ-RCV-001 ("Recovery only through Trust") while SR's first addition says recovery never asks Trust for a decision. The settlement: REQ-RCV-001 **stays** on the row (SR's reading; STM-05 only resumes work already decided, and a step that needs a new dispatch ends `NEEDS_PERSON` or becomes a `RecoveryRequest` that Trust evaluates fresh); STM-05 carries no budget and reports its counts (not resumed, refused, failed) for the caller to escalate, so **REQ-RCV-003 is removed from the row** (it stays with the RCV tasks); the structural import guard (with its mutation proof) is the accepted done-when, so the clause about a Trust double is dropped, and SR's voided-grant test (a voided grant ends `NEEDS_PERSON`) stays. Applied in plan v1.27 (the row, the header note and Appendix A); no plan v1.28.
- **A518 and A509.** A509 (`DEC-2026-11-21-architect-rulings-a507-a517`) gave DSN files the key-file checks. A518 names the two TLS client private keys as in scope, keeps the public `edge.Load` data out, and fixes the rule (mode exactly 0400, owner the core user, 0600 refused); `cmd/migrate`'s own copy of the checks moves to the shared reader (C2).
- **A520 and DEBT-54.** The debt register's DEBT-54 notes A520 (below). The migration number stays 0037 (reserved on noema#183); it is not on the G1 path.
- **A521** changes no setting value; the password file path is IL's Compose value.
- **A522.** "Merge on green and fix forward" is the Architect's rule for the `core-keys-init` pull request only; the Steward does not read it as a general rule.
- **A523 and A524** are Voice's and FE's; recorded as given. A524 means noema#638's wrong-role message is one generic text for 403 and 404 (no role names, no hint the view exists).
- **docs#221 is closed** (the Founder closed it); nothing was pushed to it.
- **Task status (`tasks.csv`), merged evidence only.**
  - **EDG-03 → Done.** noema#822 merged 21 Nov 2026 (merge commit `32fb713f`, 26 checks success), Codex READY and SR READY at its head: the cap tests, the 502 for an over-long upstream answer and the fixed-text body are its "done when".
  - **STM-05 → In progress.** noema#843 (migration 0036), #789 (`RecoverInvestigations`) and #865 are merged; the recovery package that reads the stored row is open as noema#882 (draft). **noema#882 replaced noema#872**, which was closed under A429 after a secret-scan hit (same tests and code, plus the Trust guard and the A514 commit). SR's three additions are not yet shown on `main`.
  - **UND-17 → In progress.** noema#837 is **out of draft with green commits** (26 of 26 checks at `1b3e3aba`, read 22 Nov 2026); it has not merged, so nothing is shown on `main`.
  - **STM-04, TRU-10, TRU-12: Backlog → In progress** (merged pull requests exist: noema#812, #794 and #862; #883; #756, #849 and #885). Their "done when" is **not** met, so none is marked Done.
- **The gaps (merged work, not marked Done, because the Steward did not verify the "done when" against the merged head):** CON-07 (noema#815, #873, #877), EDG-01 (#722), EDG-02 (#726), ENV-04 (#730, #790, #868), ENV-12 (#791, #869), EXE-08 (#846), PLT-09 (#786), REC-05 (#737), SEC-07 (#857), SEC-08 (#658, merged as a slice, A483: stays In progress), TRU-07 (#788, #768, #830, #833), UND-05 (#834), UND-16 (#811, #832, #845, #856), VOI-01 (#625, #806, #816), VOI-05 (#871), VOI-10 (#805), BEN-05 (#853). **CON-08 has an ID collision:** noema#831 is titled "CON-08: every integer of scorecard-view.v1 is bounded ..." while the plan's CON-08 is `ParseIntentRef` (A337); the plan's CON-08 stays Backlog and the Steward does not mark it from #831. The author or the Architect names the right ID.
- **Next free ruling: A530.**

## 4. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-architect-rulings-a358-a453`, `-a454-a467`, `-a469-a485`, `-a468-and-a480-corrected` | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-architect-rulings-a489-a492`, `-a502-a506`, `-a507-a517` | A489 to A492; A502 to A506; A507 to A517 | |
| This record | A518 to A529 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank), A474 follow-up | **A530** |
