# DEC-2026-11-23 · Architect rulings A530 to A533 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A530 to A533 (§1). A525 to A529 were relayed in the same instruction and are already recorded (§2). |
| **Supersedes** | **A531 settles** what the Planner returns for an empty runnable set (noema#896) and how Trust maps it. **A533 states** the rule for editing a golden. Otherwise per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A530 to A533
- Decision: §1
- Rationale and evidence: the Architect's message of 23 Nov 2026, relayed to the Steward; for A530, a transient HTTP failure of the libsodium download in the DB image build
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-07, INV-21; AGENT-11, AGENT-15, AGENT-25; REQ-TRU-010, REQ-INT-002, REQ-UND-001; PERD §23; AGENTS §8
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. A532 may need an additive contract change with the AGENT-15 steps (a version bump and a migration note), in the same PR as the fix.

## 1. The rulings, as given

### A530 (interim).

The DB image's libsodium download fails on a transient HTTP error with no retry. IL adds `--retry 5 --retry-all-errors` to that curl, keeping the SHA-256 check. It is a small PR. A flaky job gets an owner within 24 hours, and no test is ever skipped.

### A531 (interim, noema#896).

An empty runnable set is not PLAN_INVALID, which is reserved for a malformed plan from a verified pack. It is also not a silent WAIT. The Planner returns an explicit "no runnable capability" result. Trust maps it per REQ-TRU-010: the disposition stays ESCALATE, the delivery becomes a handoff plus an ops alert, and if no handoff is possible the outcome is UNKNOWN. No grant is ever issued.

### A532 (interim).

The compile service must accept every locale in BO's g1_inputs.json. If its contract lists locales, extend it additively with the AGENT-15 steps in the same PR as the fix. Never silently map a locale to English.

### A533 (interim).

A golden is never edited to turn the run green. If a recording shows the customer did ask for a remedy, C2 changes the golden only with that evidence quoted in the PR. Otherwise the schema and prompt change.

## 2. What the Steward did, and where the rulings are silent

- **A525 to A529 are not recorded a second time.** The Founder asked for "A525 to A531 ... in a new record". A525 to A529 (STM-05 and REQ-RCV-001, SR's Trust double, the migrate password, `cmd/migrate` before migration 0037, the `core-keys-init` fix-forward) are already recorded, as given, in `DEC-2026-11-22-architect-rulings-a518-a524` (§1, merged in docs#226), which carries A518 to A529. Recording the same ruling in two records would give it two texts; this record points to that one. If the Founder wants a second copy, the Steward writes it.
- **A530.** The Steward changes no workflow: the `curl` line is in the pgsodium image build (IL's), and a `.github` or `deploy` change needs SR's read and a Founder's approval. A530 repeats AGENTS §8 ("a flaky test is a bug"): the failure was a download, not a test.
- **A531 and PERD §23.** PLAN_INVALID is the Planner's existing result for a malformed plan from a verified pack; A531 adds a distinct explicit result, "no runnable capability", and says how Trust maps it under REQ-TRU-010 (the disposition stays ESCALATE; the delivery becomes a handoff plus an ops alert; UNKNOWN if no handoff is possible; never a grant). The Steward changes no PERD text: if the reason-code or the result name needs a place in §23.3 or a contract, it is the owner's change with the AGENT-15 steps (C1 for the Planner and Trust mapping, noema#896).
- **A532 and A533** are C2's and BO's; recorded as given. A532 says what to do if the compile service's contract lists locales (extend additively, same PR); A533 says a golden is changed only with the recording's evidence quoted in the PR.
- **The status pass continues** (the same pull request): `UND-17` is marked **Done** (§3 of the session note `2026-11-23-0700-OPS-24-status-pass-2`).
- **Next free ruling: A534.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` records | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-*` and `DEC-2026-11-22-architect-rulings-a518-a524` | A489 to A492, A502 to A517, A518 to A529 | |
| This record | A530 to A533 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank), A474 follow-up | **A534** |
