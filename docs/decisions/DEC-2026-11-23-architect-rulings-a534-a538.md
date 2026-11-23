# DEC-2026-11-23 · Architect rulings A534 to A538 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A534 to A538 (§1), every one Interim. A525 to A533 are in two merged records (§1, first paragraph); they are not repeated. |
| **Supersedes** | **A536 amends A527** (two holders of the migration password, not one; A527 is in `DEC-2026-11-22-architect-rulings-a518-a524`, which is merged and not edited, so a reader of that record must read A536). **A534** settles the A503 path (the ESCALATE record) and rescopes noema#733. **A535** removes a refusal gate for a missing time slot from Understanding. Otherwise per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A534 to A538
- Decision: §1
- Rationale and evidence: the Architect's message of 23 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-07, INV-12, INV-21; AGENT-11, AGENT-15, AGENT-16, AGENT-25; REQ-RCV-001, REQ-RCV-003, REQ-TRU-010; PERD §23; AGENTS §8
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. A532 and A534 may need additive contract changes with the AGENT-15 steps (a version bump and a migration note), in the same PR as the change.

## 1. The rulings

The Architect's rulings A525 to A538 were relayed together. Their texts are recorded as follows, and no text is repeated:

- **A525 to A529:** `DEC-2026-11-22-architect-rulings-a518-a524` (merged, docs#226).
- **A530 to A533:** `DEC-2026-11-23-architect-rulings-a530-a533` (merged, docs#228).
- **A534 to A538:** below.

**A536 amends A527:** where A527 says the one-shot is the password's only holder, read A536 (two holders).

### A534 (interim, the A503 path).

EL's agent was right to stop, and each of its four points is answered.

- **Where it is recorded.** An ESCALATE disposition is a Decision Record and the Record comes first, so it must be recorded. C1 changes the intake so an ESCALATE outcome goes through the existing Recorder port (no steps, no grant, a decision id returned per A456).
- **How the id reaches each step.** The id goes into the investigation's start arguments, then `ContinuationRequest.DispositionDecisionID` (one new optional field, C1's), then `RouteDecider` forwards it, and #883's pass-through carries it into the record. EL's allowlist extends to `orchestrator/portadapters/trust` and the `cmd/core` worker files for this task.
- **Replay.** No new rule. The disposition has the normal A186 decision key, so a replay returns the stored record, and the action decisions' keys include its id. C1 proves it with a test.
- **The complaint write.** `log_complaint_reference` is not in the escalation set (A346 corrected the A335 text). The Writer rule applies only to a decision whose steps include a capability in the injected escalation set. A complaint write is a normal ALLOW with no disposition. #733's title ("iff it carries steps") is too broad, so C1 rescopes it and adds a test that a complaint write is accepted.
- **Order:** C1's intake change, EL's path, then #733.

### A535 (interim, a request with no time reference).

There is no default window and no refusal. AGENT-16 forbids inventing one. The compile proposal carries the time slot as unresolved, and Trust asks the customer when (CLARIFY). A refusal gate in Understanding for a missing slot is wrong and moves out. The goldens G-B and G-E stay as they are.

### A536 (interim, tenants-provision; amends A527).

A527 is amended: migrate and tenants-provision are the two holders of the migration password. Each runs as its own one-shot with a read-only root, a tmpfs, no capabilities and no network except postgres. The password never appears in argv, the environment, a log or an error, and netcheck pins both. SR reads it.

### A537 (interim, composition).

`/readyz` names 19 components that are not built, and that is now the G1 critical path. Section 3 splits it into four lanes.

### A538 (interim).

The Pidgin lexicon is pack data. C2 adds only the phrases the G1 inputs use plus obvious ones. Entries are labelled SYNTHETIC and reviewed by the Founders as data, and nobody waits on that review.

## 2. What the Steward did, and where the rulings are silent

- **Why this record exists.** docs#228 merged (06:40, `27ea8fd`) with A530 to A533 only. The Steward pushed a combined A525 to A538 record to that branch afterwards, which never reached `main`; SR and EL both found it. That commit is abandoned. This record carries A534 to A538 only, the merged A530 to A533 record stays as merged, and A525 to A529 are not repeated, so no ruling has two texts.
- **A534.** The ruling does not name the task ID the allowlist extension applies to ("this task"), and the Steward does not guess it. EL asks which start arguments carry the decision id: the workflow's input, or the investigation row, which has no column for it (INV-30 allows an id in workflow input but no I/O in workflow code). The ruling says only "the investigation's start arguments"; the Architect names which. The Steward adds no field or contract: `DispositionDecisionID` is C1's change with the AGENT-15 steps, and #733 is rescoped by C1.
- **A535.** "Unresolved" for the time slot and the CLARIFY mapping are C2's and C1's; no PERD text is changed. The goldens G-B and G-E are untouched.
- **A536.** SR asks why `tenants-provision` holds the migration password and not a narrower role, and whether the answer is that it needs the DDL role. The ruling does not say; it is a question for the Architect. SR reads both one-shots when IL pins them (the pin, the read-only root, tmpfs, no capabilities, postgres-only network). Compose values are IL's.
- **A537 is incomplete as relayed.** It points to "Section 3" for the four lanes, and Section 3 did not arrive; the 19 components and the lanes are not listed here, and the Steward does not infer them. A follow-up adds them once the section is committed.
- **A538.** Pack data; the Founders review it as data and nobody waits on that review. SYNTHETIC labels are required (AGENT-25).
- **Next free ruling: A539.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` records | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-*` and `DEC-2026-11-22-architect-rulings-a518-a524` | A489 to A492, A502 to A517, A518 to A529 | |
| `DEC-2026-11-23-architect-rulings-a530-a533` | A530 to A533 | |
| This record | A534 to A538 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank), A474 follow-up, A537 lanes (Section 3), A534 start-arguments location, A536 reason for the second holder | **A539** |
