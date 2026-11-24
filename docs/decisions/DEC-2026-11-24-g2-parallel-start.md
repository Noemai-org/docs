# DEC-2026-11-24 · G2 build work starts now, in parallel with G1 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect (ruling A613, relayed 24 Nov 2026), recorded by the Repo Steward at the Architect's instruction ("the Steward records a decision for it today"). **It counts only once a Founder who did not author this pull request approves and merges it** (A111; AGENTS §2, item 3). Until then plan §9 stands as written. |
| **Date** | 24 November 2026 |
| **Owner** | Principal Architect (the decision); Founder and Technical Co-Founder (the merge) |
| **Decides** | Build work for a G2 task may start before G1 passes, when the task's "Needs" tasks are all Done. The G2 gate itself is not moved. |
| **Supersedes** | **The sequencing in plan §9 ("Entry condition. G1 passed. If it did not, Monday is spent on the slice and the ambiguity work starts on Tuesday. Nothing else in this week is allowed to start before the slice is green")**, for build work only, and only from the moment this record merges. **Exception kept:** the G1-failure hold of plan §3.1 and AGENTS §3 step 3 is preserved (§1, item 6). The plan file is **not edited** (AGENTS §11); a plan version carries the change only by change request (plan §19). |
| **Amends** | Nothing in the SoT or the PERD. |
| **Authority order applied** | SoT §0.4: an approved POC decision ranks above the plan. |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 24 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: the parallel start of G2 build work (A613)
- Decision: §1
- Rationale and evidence: the Architect's ruling A613, relayed to the Steward on 24 Nov 2026; plan §9 (v1.27); `docs/poc/execution/tasks.csv` at `dac483f`
- Affected requirement IDs / SoT sections: SoT §40.2 (if the time box and the safety gates conflict, the gates win and the date moves); plan §3, §3.1, §9; AGENTS §2.3, §3 (step 3), §4
- Supersedes: see the Supersedes row above
- Migration notes: none. No contract, schema or migration changes.

## 1. The decision

1. **G2 build work starts now, in parallel with G1.** Any G2 task whose "Needs" tasks are Done may be built now.
2. **The gates do not move.** The G2 gate itself still counts only after G0 and G1 pass (plan §3; G0 passes only when both G0-T and G0-N pass). Nothing a G2 task builds counts as G2 evidence before then.
3. **Nothing G2 touches the G1 path.** A G2 task that would change something G1 depends on does not start under this decision.
4. **G1 PRs keep priority in review.**
5. **Tasks already in flight are unchanged.** A task that is already under way for G1 (for example the TRU-10 disposition path, or any task on the G1 critical path) is not made a "G2 start" by this record, and its priority does not change. The decision adds permission to start a G2 task; it takes none away.
6. **If G1 fails, the hold of plan §3.1 and AGENTS §3 step 3 still applies, and ambiguity work waits.** *The Steward's reading, the safer one (AGENT-20); A613 does not say.* A613 does not permit ambiguity (AMB) tasks to start after a G1 FAIL, and does not override plan §3.1 ("if G1 failed, week 2 starts with the slice and ambiguity work waits"). Meanwhile G2 work in flight yields review and CI capacity to G1 repair, and no G2 PR merges while a G1 failure is open. **The Architect confirms or corrects this.**
7. **"May be built now" includes merging, on the same gates.** *The Steward's reading, not stated in A613.* A G2 PR may merge only if it passes the same checks and reviews as any PR and touches nothing on the G1 path; nothing it adds counts as G2 gate evidence before G0 and G1 pass (item 2); and item 6's hold applies. **The Architect confirms or corrects this.**
8. **Why it takes the safe path.** Plan §9 says G2 work waits for G1, and a chat instruction does not override it until it is committed (AGENTS §2.3). This record is that commitment.

## 2. What the Steward did, and where the record is silent

- **Binding only on merge.** Until a non-author Founder merges this record, plan §9's entry condition stands, and no agent starts a G2 task on the strength of the chat instruction alone. The Steward does not treat this as already in force.
- **The plan is not edited.** Plan §9 and its entry condition are unchanged on `main`. If the Architect wants the plan text to carry the change, that is a change request and a new plan version file (plan §19); the Steward drafts it on request.
- **No list of buildable tasks is in this record.** The first version carried a snapshot of "25 buildable" tasks. Two reviewers (the Benchmark Owner and Codex) showed it overstated: it counted tasks flagged `blocked` in `tasks.csv` and tasks already in flight under G1, and it goes stale as tasks reach Done. The rule is the Architect's; any list is not. The Steward's snapshot, with the blocked flags applied, is in the session note `2026-11-24-0545-OPS-36-a613-a620.md`, as information and not as authority, and it says that each owner checks that the task does not touch the G1 path.
- **Which tasks are "G2 tasks".** The Steward used the Needs of the G2 review row GOV-11 as the working definition; the plan's §9 table and the rows added later by change request are in it. If the Architect means a narrower or wider set, the Steward re-derives the list.
- **"Nothing G2 touches the G1 path" is a check each owner makes, and a reviewer confirms.** The record names no task that fails the check; an owner who is unsure stops and asks (AGENTS §14).
- **The work-in-progress cap** stays suspended until G1 passes (A558); this decision does not change that.
- **Migration ledger** and **`tasks.csv`** are unchanged by this record.
