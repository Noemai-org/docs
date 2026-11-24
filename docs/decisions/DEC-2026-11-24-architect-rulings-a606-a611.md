# DEC-2026-11-24 · Architect rulings A606 to A611 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 24 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 24 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A606 to A611 (§1), every one Interim. |
| **Supersedes** | **A611 replaces** the "one extra attempt is allowed" part of the first fix of noema#915 (the Steward's own fix, recorded in the PR) with a count of client-issued statements. **A610 changes who pushes** the gateway writer of A592's PR A (it goes on #925 as a commit by EL). Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan, as written. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 24 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A606 to A611
- Decision: §1
- Rationale and evidence: the Architect's message of 24 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-07, INV-12; AGENT-12, AGENT-15, AGENT-16; REQ-TRU-009; `trust-limits.v2`; AGENTS §5, §8, §11
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. Migration 0039 stays in noema#925 (ledger unchanged).

## 1. The rulings

### A606 (interim, #932 gate). Confirmed.

A "yes" below the threshold counts as doubt and the slot stays absent. A "no" stays a no. The probability is compared as the decimal the provider wrote. This is deliberately stricter than the existing `asserted()` path, because a false remedy is the harmful error. 9000 basis points remains the Architect's interim value for the Founders to confirm.

### A607 (interim, #914).

Lookup keeps full timestamp precision. The database's own expiry check is authoritative, and the route never rounds the application clock up against it.

### A608 (interim, #824 budget).

Codex is right that charging after buffering is only a post-hoc check. Voice charges TTS audio chunk by chunk as it streams, before accepting the next chunk. When the next chunk would exceed the budget, the run stops with `budget_exhausted`. Nothing is buffered and then charged.

### A609 (interim, #910).

packcheck validates the shipped limits file against `trust-limits.v2`, so a re-pinned malformed file cannot pass. C2 adds this with a negative test.

### A610 (interim, verified issuer).

EL pushes the gateway writer for the verified issuer as a commit on #925. C2 consents here, so there is no wait (A508). PR B, the recovery refusal, follows after #925 merges.

### A611 (interim, #915).

SR's proposal is accepted: the deadline test counts client-issued statements instead of allowing one extra attempt. The Steward fixes it.

## 2. What the Steward did, and where the rulings are silent

- **A606 and OD-P-101.** The threshold stays the Architect's interim 9000 basis points; the Founders have not confirmed it, so OD-P-101 stays Open. A606 says the gate compares the probability **as the decimal the provider wrote**, with no rounding to a float first (the same spirit as A566's exact comparison). The Steward changes no value (AGENT-16).
- **A607.** The expiry decision belongs to the database clock (the A368 rule, already in the confirmation store); the route does not round the application time up. The Steward changes no code.
- **A608 and A568.** A568 already said every second of audio, sent and received, counts against the budget. A608 says how: TTS audio is charged chunk by chunk before the next chunk is accepted, and the run stops with `budget_exhausted` at the chunk that would exceed it. Voice's, noema#824.
- **A609 and A596.** A596 moved the contract to `trust-limits.v2`; A609 makes packcheck validate the shipped limits file against v2, so a malformed file with a re-pinned digest cannot pass. C2's, noema#910.
- **A610 and A592.** A592 put the gateway writer in PR A; A610 says EL pushes it as a commit on #925, with C2's consent (A508), so PR A is #925 with EL's commit. PR B still waits for #925 to merge. The migration ledger is unchanged (0039 is #925).
- **A611 and noema#915.** The first fix of #915 allowed one extra attempt after `Spend` returned (the one statement a single connection can have in flight). A611 replaces that with a count of client-issued statements: the test fails if the client issues any statement after `Spend` returned, and no server-side timing is involved. The Steward made the change in noema#915 in the same session (the PR body and its status file say what changed).
- **A605 in the compile-run record.** A605 is already in `DEC-2026-11-23-architect-rulings-a602-a605`. At the Founder's instruction the Steward also recorded its stop rule in the compile-run record in `noema`, `status/UND-16.md` (the series that holds the live compile runs, `UND-16-run6.md` being the latest): at most two more live compile runs (8, and 9 only if run 8's readable evidence shows a threshold problem); no run 10 without a Founder decision between an asymmetric pass rule and a delay; no golden edited (A533).
- **Task status (`tasks.csv`)** is unchanged here. **Migration ledger on noema#183** is unchanged: 0037 #922, 0038 #923, 0039 #925, 0040 reserved, next free 0041.
- **Next free ruling: A612.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` and `DEC-2026-11-21-*` records | A358 to A362, A380 to A485 (A467: no text), A489 to A492, A502 to A517 | |
| `DEC-2026-11-22-architect-rulings-a518-a524` | A518 to A529 | |
| `DEC-2026-11-23-*` records, `a530-a533` to `a602-a605` | A530 to A605 (A541 noted; A590 to A592 in full) | |
| This record | A606 to A611 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank, by ruling A592) | **A612** |
