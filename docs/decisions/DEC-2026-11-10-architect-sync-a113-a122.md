# DEC-2026-11-10 · Architect sync of 10 Nov 2026: rulings A113 to A122

| | |
|---|---|
| **Status** | **Decided by the Principal Architect on 10 Nov 2026 (the Architect sync), relayed to the Repo Steward by the Founder; recorded by the Repo Steward.** Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 10 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Ten rulings, A113 to A122 (§1). Each states what it supersedes. |
| **Closes** | The questions on noema#393 (migration order), noema#384 (kill-switch event kinds), noema#383 (`outputs_digest`), noema#346 (`permit_case_writes`). Closing each issue is the issue owner's step. |
| **Supersedes** | Per ruling, in §1: A113 supersedes A34 and A72 and the D12 numbers where they differ; A120 supersedes the 11 Nov freeze lines; A122 completes A68; the others supersede nothing. |
| **Amends** | New PERD version `docs/poc/perd/NOEMA_POC_PERD_v1.22.md` (A114; v1.21 stays unchanged, draft for EL review); new plan version `docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v1.15.md` (A120; v1.14 stays unchanged); `AGENTS.md` line 73 (A120); the vendored copies in `noema` (REQ-OPS-005). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 10 Nov 2026; counts once a Founder who did not author this pull request approves and merges
- Date: 10 November 2026
- Closes: the questions on noema#393, noema#384, noema#383, noema#346
- Owner: Principal Architect; Founder and Technical Co-Founder
- Decides: rulings A113 to A122
- Decision: §1
- Rationale and evidence: the Architect sync of 10 Nov 2026, relayed by the Founder; the verified behaviour of `db.Migrate` (applies by file name in name order, no gap check)
- Affected requirement IDs / SoT sections: REQ-REC-001, REQ-EXE-008, REQ-EVD-002, REQ-OPS-005; INV-03, INV-17, INV-21; SoT §38.5, §0.4
- Migration notes: A113 and A119 concern migrations (see §1); no migration is added by this record
- Supersedes: see the Supersedes row above

---

## 1. The rulings

| ID | Ruling | Supersedes |
|---|---|---|
| **A113** | **The migration-number gap is accepted.** Migrations merge in strict ascending number order: noema#181 (0011), #168 (0012), #229 (0013), #233 (0014), #259 (0015), #234 (0016), #261 (0018), #263 (0019), #268 (0020), #272 (0021). The first of them to merge carries an **upgrade-path catalog test**, including function bodies. The noema#183 ledger header is corrected to say this. | **A34 and A72** (a later PR renumbers) and the sentence "no number below one already on `main` may merge"; the **D12 numbers** where they differ. |
| **A114** | `KILL_SWITCH_CLEARED` and `KILL_SWITCH_CLEAR_REFUSED` are `SECURITY_EVENT` kinds in PERD §32.2. A refused clear is recorded **only for an authenticated caller**. The `record-event` contract bump happens in TRU-08 slice 2 (AGENT-15). Draft PERD v1.22 with EL. | Nothing. PERD v1.22 (draft) carries the text. |
| **A115** | `outputs_digest = sha256(JCS(["noema/record-export/v1", event_id, payload_hash]))`. Two tests accompany it. | Nothing. |
| **A116** | `permit_case_writes` is a **slot resolved to exactly one transaction**. No pack change. BO's R3 and R4 test accompanies it. | Nothing. |
| **A117** | `DISPATCH_ATTEMPTED` keeps its `capability` key. Readers map it. There is no second key. | Nothing. |
| **A118** | **No comparison-arm run before G3** (SoT §38.5). Arms A and B use native provider tool-calling. The contracts `arm-turn.v1` and `arm-turn-result.v1` are approved as **Drafts**. | Nothing. |
| **A119** | The evidence-set hash is bound **at grant issue by a database trigger**. One forward migration, bundled with EVD-02. | Nothing. |
| **A120** | **The code freeze is Wed 9 Dec 12:00 WAT** (plan §3). The stale 11 Nov lines in plan §11 and in `AGENTS.md` (and the `noema` copy) are fixed. | The lines "From Wed 11 Nov 12:00 WAT" (plan v1.14 §11) and "(Wed 11 Nov 12:00 WAT)" (`AGENTS.md` §3). |
| **A121** | **A14 is unchanged.** A Codex review at the current head, from the Founder sweep or the Codex bot, counts. An unresolved P1 from either blocks. | Nothing. |
| **A122** | **A CLARIFY or CONFIRM on a recovery escalates.** | Completes the second clause of **A68**. |

## 2. What the Steward did where the rulings are silent

- **A113 numbers.** Taken from the Architect's list unchanged. The ledger on noema#183 is rebuilt in that order. No migration file is renamed by this record.
- **A114 version.** The change is a new PERD version file (v1.22), not an edit of v1.21 (AGENTS §11). It stays a draft until EL reviews it and a Founder who did not author the pull request approves it.
- **A120 scope.** Only the freeze lines the ruling names are changed. `AGENTS.md` §0 ("Dates ... Fri 13 Nov 2026") and the execution README ("Mon 19 Oct to Fri 13 Nov 2026") also read as the old build window; they are **not** changed here and are flagged to the Founder.
- **Contract bumps (A114, A118, A119).** Made by the owning tasks, not by this record.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| DEC-2026-11-08-rulings-a41-onward | A41 to A108 | |
| A109, A110, A111 | REC-09, control-plane callers, one non-author Founder approval | |
| A112 | DEBT-13 does not block noema#181 | |
| This record | A113 to A122 | **A123** |
