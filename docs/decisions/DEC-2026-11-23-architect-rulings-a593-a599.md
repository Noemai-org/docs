# DEC-2026-11-23 · Architect rulings A593 to A599 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A593 to A599 (§1), every one Interim. |
| **Supersedes** | **A599 clarifies A585** (how long an agent stays subscribed). **A593 completes A582** (what SLOT mode does not require). **A598 fixes the meaning of "turn"** in A581 and A590 and reserves a migration for the key. **A596 changes the version** of `trust-limits` that A561 and A579 rely on (v1 to v2). **A597 narrows** A542's rule for `#912` to a DECLINED_BY_APPROVER reject. Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan, as written. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A593 to A599
- Decision: §1
- Rationale and evidence: the Architect's message of 23 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-12; AGENT-15, AGENT-16; REQ-AMB-004, REQ-TRU-009; `clarification.v1`, `trust-limits`; AGENTS §5, §8, §11
- Supersedes: see the Supersedes row above
- Migration notes: A596 is a contract change (`trust-limits.v1` to `trust-limits.v2`, with a migration note and regenerated models; both Founders, AGENT-15). A598 adds a database migration for C1's early-decision key: **0040** (reserved on noema#183; author C1, so the independent read comes from EL or C2 and SR reads as SR, A463). A593 is an addition to the contract change of #926 (C1).

## 1. The rulings

### A593 (interim, SLOT mode).

`allow_none` and `none_option_id` are not required in SLOT mode, and a "None of these" option is never shown. C1 adds this to #926.

### A594 (interim).

The execution and outcome key `MAX_ACTIVE` settings are 2, mirroring the edge and orchestrator keys. #921 stands.

### A595 (interim, #638).

The audit panel shows one "Record verified" line only when the response carries the backend's chain verdict. If the verdict is absent it shows nothing, and it never fabricates one. The panel's current behaviour is the safe side.

### A596 (interim, #910, the one real Codex finding).

Adding a required member to `trust-limits.v1` breaks AGENT-15. C2 bumps to `trust-limits.v2` with a migration note and regenerated models, and moves the pack file and the loader to v2. #910 follows #916.

### A597 (interim).

C1 follows up on #912's note: the Writer refuses an empty id for a DECLINED_BY_APPROVER reject only. Other reject reasons keep mapping empty.

### A598 (interim, the turn of A590).

The turn is the request id the Gateway mints for each POST. C1's key migration takes the next free number after 0039, which the Steward reserves on #183.

### A599 (interim, A585 clarified).

After pushing, stay subscribed until the PR's current head CI has been read and READY posted, or a failure is fixed. Then unsubscribe.

## 2. What the Steward did, and where the rulings are silent

- **Migration ledger (A598).** The Steward reserved **0040** on noema#183 for C1's early-decision key (A581, A590, A598). On 23 Nov 2026 the open pull requests claim 0037 (noema#922) and 0038 (noema#923); no pull request claims 0039 or 0040. **Next free: 0041.** The author is C1, so the independent migration read comes from EL or C2 (not C1, not SR), and SR reads as SR (A463).
- **A598 and A590.** "The turn" in A581 and A590 means the request id the Gateway mints for each POST, so a replay of the same POST returns the stored record and a new POST evaluates fresh. The key shape stays as A590 gives it (tenant, verified principal, turn, intent hash, pack version, outcome, reason), with both identity values from the authenticated session.
- **A593 and A582.** A582 made `candidate_set_id`, its version and `options` not required in SLOT mode; A593 adds `allow_none` and `none_option_id`, and says a "None of these" option is never shown. The conditional required rule and negative fixture for the non-SLOT case (SR's condition) stand. The contract change is #926 (C1; both Founders).
- **A594.** The values are the Architect's (2, mirroring the edge and orchestrator keys); the Steward changes no setting (AGENT-16). The setting names are `NOEMA_EXECUTION_KEY_MAX_ACTIVE` (A554) and `NOEMA_OUTCOME_KEY_MAX_ACTIVE` (A564).
- **A595.** A570 already rules that the audit panel shows "Record verified" once, only from the backend's chain verdict; A595 states what the panel does when the verdict is absent (shows nothing; never fabricates one). FE's.
- **A596 and the limits change requests.** A561 made the confirmation TTL ceiling a required member of `trust_limits.json`, and A579 made `trust_limits.json` the single freeze-list authority. A596 makes the version bump (v1 to v2) a condition of adding that required member, so AGENT-15 holds. `CR-2026-11-23-A567-perd-res-002-freeze-allow-list` names `trust_limits.json` and is unchanged; the PERD text, when the version file is made, names the file, and C2's PR names the contract version. #910 follows #916 (the pack candidate labels).
- **A597 and A542.** A542 closed when #912 merges. A597 is C1's follow-up to a note on #912: only a DECLINED_BY_APPROVER reject needs a non-empty id; other reject reasons keep mapping an empty one. The Steward changes no code.
- **A599 and my own flow (a change for you to know about).** A599 clarifies A585: after pushing, an agent stays subscribed until the PR's current head CI has been read and READY posted (or a failure is fixed), then unsubscribes. Until now the Steward posted "READY FOR CODEX" right after each push and unsubscribed at once, as the Founder asked earlier. **Once this record merges, the Steward follows A599** on its own pull requests: it stays subscribed until the head's CI is read, then posts READY and unsubscribes. The Founder's earlier instruction to stop unnecessary watchers is read as superseded by the Architect's later flow rule only after this record binds. **This reading is the Founder's to confirm on the merge** (Security Reviewer's point): an earlier Founder instruction is being narrowed by a later Architect rule, and the Steward does not narrow it alone.
- **Task status (`tasks.csv`)** is unchanged here; it moves only on merged evidence.
- **Next free ruling: A600.**

## 3. Reviewer conditions for the code pull requests

Security Reviewer read this record READY at `d6e44e1`. The conditions are **reviewers' conditions, not rulings**; each owner meets them in the code PR.

1. **A598 and the 0040 migration.** The Gateway's request id is minted by the Gateway on the authenticated path and is never taken from a client header or body. The key's tenant and principal come from the session. A client retry is a new POST and so a new evaluation; only a replay of the same POST returns the stored record. The migration follows A463 (independent read from EL or C2; SR reads as SR).
2. **A597.** The Writer refuses an empty id for a DECLINED_BY_APPROVER reject **before opening a transaction**, and a test says so. A reject for another reason with an empty id still maps empty; any other outcome that names an id stays refused (A542).
3. **A595 and noema#638.** At `5b16a740` the audit panel shows no "Record verified" line even when the chain is verified: the safe side, but not what A595 asks. The verdict is the contract's `chain.verified` (fixed to `true` once the body parses); it must not be the outcome verdict item or the timeline's VERDICT entry. FE adds that one line and a test that it never appears when the body is refused.
4. **A596 (`trust-limits.v2`).** The loader and the pack file move to v2 together. The loader refuses a v1 file, and a v2 file missing the required confirmation-ceiling member, with no default filled in (AGENT-16). The consumers (intake and the Writer, A561) fail closed when the limit is absent. The migration note and regenerated models follow AGENT-15; both Founders approve the contract change.
5. **A593 (SLOT mode).** `allow_none` and `none_option_id` are not required in SLOT mode, and the contract keeps them required outside SLOT, with a negative fixture for a non-SLOT card that omits them (SR's condition 3 on docs#234 stands). The card never shows "None of these" in SLOT mode.

SR also answered from the earlier points: A594 closes the question on #921; A598 (a server-minted request id) answers the worry on A581; A597 answers the note on #892.

## 4. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` records | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-*` and `DEC-2026-11-22-architect-rulings-a518-a524` | A489 to A492, A502 to A517, A518 to A529 | |
| `DEC-2026-11-23-*` records: `a530-a533`, `a534-a540`, `a542-a553`, `a554-a560`, `a561-a580`, `a581-a592`, `a590-a592-confirmed` | A530 to A592 (A541 noted; A590 to A592 in full) | |
| This record | A593 to A599 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank, by ruling A592) | **A600** |
