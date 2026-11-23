# DEC-2026-11-23 · Architect rulings A525 to A538 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 22 and 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A525 to A538 (§1), every one Interim. |
| **Supersedes** | **A536 amends A527** (two holders of the migration password, not one). **A531** settles what the Planner returns for an empty runnable set (noema#896). **A534** settles the A503 path (the ESCALATE record) and rescopes noema#733. **A535** removes a refusal gate for a missing time slot from Understanding. Otherwise per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A525 to A538
- Decision: §1
- Rationale and evidence: the Architect's messages of 22 and 23 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-07, INV-12, INV-21; AGENT-11, AGENT-15, AGENT-16, AGENT-25; REQ-RCV-001, REQ-RCV-003, REQ-TRU-010; PERD §23; AGENTS §8
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. A532 and A534 may need additive contract changes with the AGENT-15 steps (a version bump and a migration note), in the same PR as the change.

## 1. The rulings

A525 to A529 are the texts already recorded in `DEC-2026-11-22-architect-rulings-a518-a524` (merged in docs#226), repeated here so the set A525 to A538 sits in one record. A536 amends A527.

### A525 (interim, STM-05 and REQ-RCV-001).

STM-05 keeps REQ-RCV-001. STM-05 only resumes work that was already decided. A step that needs a new dispatch ends `NEEDS_PERSON`, or becomes a `RecoveryRequest` that Trust evaluates fresh. STM-05 carries no budget: it reports its counts (not-resumed, refused, failed) and the caller escalates. The recovery budget in REQ-RCV-003 stays with the RCV tasks.

### A526 (interim, SR's Trust double).

The recovery package has no Trust port to double. The structural guard (the `no_trust_test.go` import test, with its mutation proof) is the accepted done-when. SR's other test, a voided grant that ends `NEEDS_PERSON`, stays.

### A527 (interim, migrate password; amended by A536).

The password comes only from the checked file (mode 0400, owner, no link). It must never appear in argv, the environment, a log or an error. The one-shot is its only holder, and IL pins that in netcheck.

### A528 (interim).

C2 moves `cmd/migrate` to the shared reader before migration 0037.

### A529 (interim).

A522 fix-forward on `core-keys-init` must never loosen a file mode or the capability set. The A519 end-to-end test runs through the real Recorder adapter, after EL's `DeclinedRequestID` mapping PR.

### A530 (interim).

The DB image's libsodium download fails on a transient HTTP error with no retry. IL adds `--retry 5 --retry-all-errors` to that curl, keeping the SHA-256 check. It is a small PR. A flaky job gets an owner within 24 hours, and no test is ever skipped.

### A531 (interim, noema#896).

An empty runnable set is not PLAN_INVALID, which is reserved for a malformed plan from a verified pack. It is also not a silent WAIT. The Planner returns an explicit "no runnable capability" result. Trust maps it per REQ-TRU-010: the disposition stays ESCALATE, the delivery becomes a handoff plus an ops alert, and if no handoff is possible the outcome is UNKNOWN. No grant is ever issued.

### A532 (interim).

The compile service must accept every locale in BO's g1_inputs.json. If its contract lists locales, extend it additively with the AGENT-15 steps in the same PR as the fix. Never silently map a locale to English.

### A533 (interim).

A golden is never edited to turn the run green. If a recording shows the customer did ask for a remedy, C2 changes the golden only with that evidence quoted in the PR. Otherwise the schema and prompt change.

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

- **A525 to A529 appear twice on `main` once this merges** (here and in the A518 to A529 record), with identical texts. Where they differ, the A518 to A529 record's text is the one the Architect gave first; A527 is amended by A536 in both readings.
- **A530.** The `curl` line is IL's (the DB image build); a `.github` or `deploy` change needs SR's read and a Founder's approval. The Steward changes no workflow.
- **A531 and PERD §23.** The Steward changes no PERD text. If the new "no runnable capability" result needs a place in §23.3 or a contract, it is C1's change with the AGENT-15 steps (noema#896).
- **A534.** The task ID the allowlist extension applies to is not named in the ruling ("this task", the A503 path); the Steward does not guess it. The Steward adds no new field or contract: `DispositionDecisionID` is C1's change with the AGENT-15 steps. #733 is rescoped by C1, not by the Steward.
- **A535.** "Unresolved" for the time slot and the CLARIFY mapping are C2's and C1's; no PERD text is changed here. The goldens G-B and G-E are untouched.
- **A536 and A521/A527.** Changes no setting value; Compose values are IL's. SR reads the one-shot.
- **A537 is incomplete as relayed.** It points to "Section 3" for the four lanes, and Section 3 did not arrive; the 19 components and their lanes are not listed here. The Steward does not infer them. The Architect (or the author of that section) sends the section, or it is committed on its own, and a follow-up adds the lanes to this record.
- **A538.** Pack data; the Founders review it as data and nobody waits on that review. SYNTHETIC labels are required (AGENT-25).
- **The status pass continues** (the same pull request): `UND-17` is marked **Done** (session note `2026-11-23-0700-OPS-24-status-pass-2`).
- **Next free ruling: A539.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` records | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-*` and `DEC-2026-11-22-architect-rulings-a518-a524` | A489 to A492, A502 to A517, A518 to A529 | |
| This record | A525 to A538 (A525 to A529 repeated) | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank), A474 follow-up, A537 lanes (Section 3) | **A539** |
