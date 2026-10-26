# DEC-2026-10-26 · Session notes in `noema` live in `status/<task-id>.md`

| | |
|---|---|
| **Status** | Accepted by the Founders on 26 October 2026 (instruction given in a working session; it counts once this record is merged). The Technical Co-Founder confirms by approving the pull request that adds it |
| **Date** | 26 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None |
| **Amends** | AGENTS.md section 9 (working practice; no SoT, PERD or plan text changes) |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the Founders (see the table above)
- Date: 26 October 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: none (working practice, AGENTS §9)
- Migration notes: in `noema`, the five files of `docs/sessions/` move to `status/` (one file per task; two tasks had two files each and are merged under dated sections, text unchanged). `noema`'s vendored `AGENTS.md` and `CLAUDE.md` are re-pointed in the same session (REQ-OPS-005)
- Supersedes: AGENTS §9's `docs/sessions/YYYY-MM-DD-HHMM-<task-id>.md` for the `noema` repository

---

## 1. The decision

| | Decision |
|---|---|
| D1 | In the `noema` repository, session notes are kept in `status/<task-id>.md`, one file per task; each session adds its own dated section. The `docs` repository keeps `docs/poc/execution/sessions/` unchanged |

## 2. Rationale and evidence

`noema` already keeps one status file per task with the task's state and its message log (`status/README.md`). Two folders for the same task split what the next agent must read. The five files that existed under `noema/docs/sessions/` (ENV-08, ENV-08b, ENV-13, ENV-13b, T5-T6.3) become `status/ENV-08.md`, `status/ENV-13.md` and `status/T5-T6.3.md`.

## 3. Agent decisions

1. Two tasks have two files each (ENV-08 and ENV-08b, ENV-13 and ENV-13b); the follow-up sections go in the task's single file, newest last, text unchanged.
2. `T5-T6.3` is a track label of Session D, not a plan task ID; its file keeps that name.
3. Paths in other files that pointed at `docs/sessions/` are updated to the new path (a link repair, nothing else).

## 4. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted | 26 October 2026 | Working session, summarised here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
