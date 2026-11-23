# DEC-2026-11-23 · Architect rulings A593 to A601 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A593 to A601 (§1), every one Interim, and the Architect's confirmations of A599 and of the order in A596. |
| **Supersedes** | **The Architect confirms A599 and retires the earlier practice** of posting READY right after a push and then unsubscribing (§1). **A600 makes SR's five conditions binding** with owners. **A601 states the migration ledger.** **A599 clarifies A585** (how long an agent stays subscribed). **A593 completes A582** (what SLOT mode does not require). **A598 fixes the meaning of "turn"** in A581 and A590 and reserves a migration for the key. **A596 changes the version** of `trust-limits` that A561 and A579 rely on (v1 to v2). **A597 narrows** A542's rule for `#912` to a DECLINED_BY_APPROVER reject. Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan, as written. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A593 to A601
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

### A599 (interim, A585 clarified), confirmed by the Architect (stated with A600).

A599 stands, and the Architect confirms the reading:

- **What the earlier "stop watchers" instruction covers:** polling loops, scheduled check-ins and background watchers that sit and wait. That still stands. Nobody polls, and nobody schedules waits.
- **What A599 adds:** a PR's own event feed. It wakes an agent when CI finishes or a review lands, so it is event-driven and not a watcher. An agent stays subscribed to a PR until the current head's CI has been read and READY is posted, or a failure is fixed. Then it unsubscribes.
- **Why it replaces the old practice:** "Post READY right after a push, then unsubscribe" has repeatedly left READY posted on heads whose CI nobody read, and has led agents to ask "tell me when to read". The old practice is retired.

### A596's order (#916 before #910), confirmed by the Architect.

Confirmed, for the Steward's reason. #916 and #910 both edit `manifest.v1.json` and the packcheck files, and #916 changes the pack file and so its pin. Merging #916 first means #910, the larger change, recomputes the pin once. It is not a logic dependency. #910 stays what the record says: schema, generated models, limits document and loader all move to v2 together. The loader refuses a v1 file and a v2 file missing the ceiling, with no default filled in, and both Founders approve.

### A600 (interim, SR's five conditions).

All five are accepted as binding conditions on the code PRs, owned as follows:

- **A598 and migration 0040 (C1):** the request id is minted by the Gateway on the authenticated path. It never comes from a client header or body. Tenant and principal come from the session. A client retry is a new evaluation.
- **A597 (C1):** the Writer refuses an empty id for a DECLINED_BY_APPROVER reject before it opens a transaction, with a test.
- **A595 (FE, #638):** one "Record verified" line driven by the contract's `chain.verified`, never by an outcome item or the timeline's verdict entry. A test shows it never appears when the body is refused. This supersedes the Architect's earlier "safe side" note.
- **A596 (C2, #910):** as above, with consumers failing closed.
- **A593 (C1, #926):** `allow_none` and `none_option_id` stay required outside SLOT mode, with a negative fixture.

### A601 (interim, ledger).

Migrations: 0037 is #922, 0038 is #923, 0039 is #925, and 0040 is reserved for C1's key. The next free number is 0041. Open PRs hold the numbers, and nothing above 0036 is merged.

## 2. What the Steward did, and where the rulings are silent

- **Migration ledger (A598), with its evidence (Codex's point).** Read from GitHub on 23 Nov 2026 at about 22:50 WAT, `noema` `main` at `5ce8d2ec`:
  - **Merged on `main`:** migrations 0030 to 0036. **Nothing above 0036 is merged.**
  - **Held by open pull requests (not merged, not free):** 0037 by noema#922 (`0037_admitted_intent_epoch_path.sql`, DEBT-54); 0038 by noema#923 (`0038_decision_basis_by_outcome.sql`, A574); **0039 by noema#925** (`0039_investigation_verified_issuer.sql`, A584 PR A).
  - **Reserved, no pull request yet:** **0040 for C1's early-decision key (A598)**, reserved on noema#183. 0022 stays reserved.
  - **Next free: 0041.** 0039 is not free and not applied: it is held by an open pull request. (When the Steward first wrote this record, no open pull request held 0039; noema#925 has since opened. The record had said "no pull request claims 0039 or 0040"; that line is replaced by this evidence.)
  - The author of the 0040 migration is C1, so the independent read comes from EL or C2 (not C1, not SR), and SR reads as SR (A463).
- **A598 and A590.** "The turn" in A581 and A590 means the request id the Gateway mints for each POST, so a replay of the same POST returns the stored record and a new POST evaluates fresh. The key shape stays as A590 gives it (tenant, verified principal, turn, intent hash, pack version, outcome, reason), with both identity values from the authenticated session.
- **A593 and A582.** A582 made `candidate_set_id`, its version and `options` not required in SLOT mode; A593 adds `allow_none` and `none_option_id`, and says a "None of these" option is never shown. The conditional required rule and negative fixture for the non-SLOT case (SR's condition) stand. The contract change is #926 (C1; both Founders).
- **A594.** The values are the Architect's (2, mirroring the edge and orchestrator keys); the Steward changes no setting (AGENT-16). The setting names are `NOEMA_EXECUTION_KEY_MAX_ACTIVE` (A554) and `NOEMA_OUTCOME_KEY_MAX_ACTIVE` (A564).
- **A595.** A570 already rules that the audit panel shows "Record verified" once, only from the backend's chain verdict; A595 states what the panel does when the verdict is absent (shows nothing; never fabricates one). FE's.
- **A596 and the order #916, then #910 (Codex's point).** A596 says "C2 bumps to `trust-limits.v2` with a migration note and regenerated models, and moves the pack file and the loader to v2. #910 follows #916." The ruling does not say why #910 follows #916. What the Steward can read from the two pull requests (23 Nov 2026), as an observation and not a ruling:
  - **#916 (PCK-09)** adds optional members to `intent-node.v1` (`options_key`, `display_template`, `attribute_order`), edits `packs/fintech_v1.json`, **changes the pack's pin in `packs/fintech/manifest.v1.json`**, and edits `tools/packcheck/checks.py` and `test_packcheck.py`. It does not touch `trust-limits`.
  - **#910 (PCK-08)** changes `contracts/schemas/trust-limits.v1.json`, the limits pack document, the manifest and the manifest schema, the loader (`platform/packload`, `platform/trustlimits`, `platform/ceilings`), the generated models, and the same `manifest.v1.json`, `checks.py` and `test_packcheck.py`.
  - The two overlap in the manifest and the packcheck files, and #916 changes the pack file and its pin, so the Steward reads the order as: **#916 merges first, then #910 builds on the new pack file and pin.** **The Architect confirmed the reason (§1):** it is not a logic dependency; #916 merges first so that #910, the larger change, recomputes the pin once.
  - **What A596 requires of #910 (stated exactly):** the schema (`trust-limits.v2`), the generated models, the trust-limits pack document and the loader all move to v2 **together in that one change**, so no consumer is left reading v1 and v2 side by side; the loader refuses a v1 file and a v2 file missing the required confirmation-ceiling member, with no default filled in (SR); the migration note follows AGENT-15; **same-head CI** is green; and **both Founders approve** the contract change. A596 is not a rename of the contract id.
  - `CR-2026-11-23-A567-perd-res-002-freeze-allow-list` names `trust_limits.json` and is unchanged; the contract version is C2's PR's to name.
- **A597 and A542.** A542 closed when #912 merges. A597 is C1's follow-up to a note on #912: only a DECLINED_BY_APPROVER reject needs a non-empty id; other reject reasons keep mapping an empty one. The Steward changes no code.
- **A599, confirmed, and the Steward's flow.** The Architect confirms A599 and retires the earlier practice. The Steward's earlier reading (that the Founder's "stop watchers" instruction was narrowed only after this record binds, and was the Founder's to confirm) is superseded by the Architect's confirmation, which the Founder relayed to the Steward on 23 Nov 2026. From this push on, the Steward stays subscribed to its own pull request until the current head's CI has been read, then posts READY and unsubscribes (or fixes a failure first). The Steward still does not poll or schedule waits. The first text of this record said to post READY right after a push; that is dropped.
- **Task status (`tasks.csv`)** is unchanged here; it moves only on merged evidence.
- **Next free ruling: A602.**

## 3. SR's conditions, now binding (A600)

Security Reviewer read this record READY at `d6e44e1` and gave five conditions. **A600 makes them binding conditions on the code PRs**, with the owners in §1 (A598 and 0040 and A597: C1; A595: FE; A596: C2; A593: C1). The text below is SR's.

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
| This record | A593 to A601 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank, by ruling A592) | **A602** |
