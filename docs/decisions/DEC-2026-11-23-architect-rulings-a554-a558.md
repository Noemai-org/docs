# DEC-2026-11-23 · Architect rulings A554 to A558 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A554 to A558 (§1), every one Interim. |
| **Supersedes** | **A555 changes** where the candidate ranker lives (a Go port in Trust, with parity vectors); it amends PERD §22.1's [REC] note, which stays unedited until a new PERD version is made by change request (§2). **A557 widens** #912 (the intake refuses an empty or malformed decline id as well as the adapter). **A556 splits** A550 (§1). Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan, as written. A555's PERD change goes through `CR-2026-11-23-A555-perd-22-1-ranker-placement` (draft). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A554 to A558
- Decision: §1
- Rationale and evidence: the Architect's message of 23 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-01, INV-06, INV-14, INV-21, INV-29; AGENT-15, AGENT-16, AGENT-25; REQ-AMB-003, REQ-TRU-010; PERD §22.1, §32; AGENTS §5, §8
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. A554 reads key announcements from existing migrations and adds none. A555's pack members are a separate pack PR with the AGENT-15 steps (a version bump and a migration note).

## 1. The rulings

### A554 (interim, lane 5).

C1 writes the task card and builds it. The settings mirror the orchestrator and edge pattern, required together, with absence being a named gap:

- **Settings:** `NOEMA_EXECUTION_DSN_DIR` (the per-tenant `execution_rw__<tenant>` login), `NOEMA_OUTCOME_DSN_DIR` (`outcome_rw__<tenant>`), and `NOEMA_EXECUTION_KEY_DIR` with `NOEMA_EXECUTION_KEY_MAX_ACTIVE` for the receipt signer.
- **Files:** mode 0400, owner 65532, with identity names taken from the migrations' key announcements.
- If the code differs, C1 raises a CONFLICT block. IL adds the mounts.

### A555 (interim, candidate ranker).

C2's recommendation (a) is accepted. A Go port of the ranker lives in Trust, with shared golden vectors proving parity with the Python ranker. This keeps Trust independent of the model deployable's availability. It amends PERD §22.1's [REC] note, so the Steward drafts the change request. C2 adds the pack members in a separate pack PR with the AGENT-15 steps.

### A556 (interim, A550 split).

- **Payment kinds:** C2 builds the explainer's facts source now. Case kinds return UNKNOWN until C1's lane 5 provides a Record reader for receipt, plan and SLA.
- **Version tokens:** the target version token becomes a mapped field in the pack mapping, owned by C2.
- **`--base-url`:** Voice pins it to a Founder-supplied allowlist host in the settings file, as SR asked.

### A557 (interim, noema#912).

Widening into the intake is approved: the intake refuses an empty or malformed decline id, and so does the adapter. The `rnaRequest` change to `NOT_AUTHORIZED` is confirmed. The stale comment at `ports_t13_t15.go:144` is fixed after #903 merges. Agents read the red CI job and push the green in the same turn, without waiting for the Architect.

### A558 (interim).

The work-in-progress cap stays suspended until G1 passes (A317).

## 2. What the Steward did, and where the rulings are silent

- **noema#892 and A542.** noema#892 is already merged (11:43 UTC, 23 Nov 2026), as `DEC-2026-11-23-architect-rulings-a542-a553` records. The empty-`DeclinedRequestID` fix is noema#912 (open at last check), which A557 widens into the intake. **A542 closes when #912 merges** with its test, not before.
- **A554.** The Steward changes no Compose value and no setting; IL adds the mounts. New key directories and logins are secrets paths, so SR reads them. The identity names come from the migrations' key announcements, which the Steward does not restate. If the code differs, C1's CONFLICT block governs (AGENT-27); the Steward raises none here.
- **A555 and PERD §22.1.** The PERD text says "**Ranking is deterministic code in the model service, not a model call [REC]**", and the lifecycle table gives the Rank stage to "Understanding (deterministic code, no model)". A555 places a Go port in Trust. The merged PERD is not edited. The Steward drafted `CR-2026-11-23-A555-perd-22-1-ranker-placement` (Draft, status Proposed, owner the Architect), which asks for a new PERD version file with the §22.1 note and the Rank row changed. Until that version exists, A555 governs (A448 pattern). The change request raises one question the ruling does not answer: whether the Python ranker stays, and which implementation is authoritative if the two differ.
- **A555 and A546.** A546 told C2 to build the ranker "where the PERD places it"; A555 now places a Go port in Trust. Read together: C2 builds the Python ranker (model deployable) and the Go port with shared golden vectors; EL builds the Reader and Labeller (A546) unchanged. The pack members are a separate pack PR with the AGENT-15 steps, and all entries stay SYNTHETIC (AGENT-25).
- **A556.** Payment kinds, version tokens and `--base-url` are C2's, C1's lane 5 and Voice's. "Case kinds return UNKNOWN" is the safe default until lane 5's Record reader exists. The Founder supplies the `--base-url` allowlist host; no host is recorded here.
- **A557.** noema#912's widening is C1's and EL's. The "agents push the green in the same turn" rule is the Architect's instruction to agents; the Steward reads it as covering a red CI job on the agent's own PR, never a skipped or weakened test (AGENTS §8).
- **A558.** The WIP cap of AGENTS §3 (4 open PRs per driving founder, 2 of them P0) stays suspended until G1 passes, as A317 set; no cap is enforced in the interim.
- **Task status (`tasks.csv`).** Unchanged: it moves only on merged evidence, and nothing new has merged against a done-when since UND-17.
- **Migration ledger on noema#183** is unchanged: 0037 stays reserved.
- **Next free ruling: A559.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` records | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-*` and `DEC-2026-11-22-architect-rulings-a518-a524` | A489 to A492, A502 to A517, A518 to A529 | |
| `DEC-2026-11-23-architect-rulings-a530-a533`, `-a534-a540`, `-a542-a553` | A530 to A533; A534 to A540 (A541 noted in the third); A542 to A553 | |
| This record | A554 to A558 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank); A537 lane contents beyond lane 5 | **A559** |
