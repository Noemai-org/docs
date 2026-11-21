# DEC-2026-11-21 · Architect rulings A493 to A500 (interim): red main, the merge queue and the CI lanes

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, from EL's analysis, relayed to the Repo Steward on 21 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). The Founder's settings in A494 are the Founder's to turn on; nothing here changes a setting. |
| **Date** | 21 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder (the repository settings, and the merge of this record); IL and EL (the workflow changes) |
| **Decides** | Rulings A493 to A500 (§1), from EL's analysis **without its last item, recommendation 8 ("measure it"), which is dropped** (§2). |
| **Supersedes** | **A493 states an order of priority** for a PR that makes `main` compile again (reads follow the merge); it is not a ban on other merges. **A494 adopts a merge queue** and the settings below; its fallback is "require branches to be up to date". Otherwise per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. AGENTS.md is not edited (§2). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 21 November 2026
- Owner: Principal Architect; Founder; IL; EL
- Decides: A493 to A500
- Decision: §1
- Rationale and evidence: the Architect's message of 21 Nov 2026 from EL's analysis, relayed to the Steward; the repeated reds of `main` of 19 to 21 Nov 2026 (merged PRs that each passed CI alone and collided: noema#818 against #759 and #788; noema#780 against #842; noema#794 against #812; noema#843 against #812)
- Affected requirement IDs / SoT sections: AGENT-11, AGENT-14, AGENT-22; AGENTS §8 (testing), §11 (git and pull requests); plan §12, §13.1; A111, A302, A317, A468, A480
- Supersedes: see the Supersedes row above
- Migration notes: none (no schema or contract change); `.github` changes are IL's and EL's, with SR's read and a Founder's approval (AGENTS §11)

## 1. The rulings, as given

### A493 (interim): Red main.

A PR that makes main compile again merges first on green CI plus your approval. The reads follow after the merge. This is an order of priority, not a ban on other merges.

### A494 (interim): Merge queue, adopt.

Every PR is tested on top of main and on the PRs ahead of it, so unrelated merges can no longer break main together.

Founder's settings:

- Require one non-author approval (A111).
- Merge queue on, with max group size 5, min 1, wait 5 minutes, build concurrency 2 and a 40-minute check timeout.
- Required checks are the aggregator jobs, not the shards: core, model, contracts, checks, arch-lint, benchmark, compose, compose-scripts, regression-link, grantdrill, hostility-proxy, mock-case, standin, toolfacade, webhook-relay, ui, codegen-diff and the three images jobs. IL confirms the exact names from the latest green run. pr-base-guard is PR-only, so leave it out.

Ordering rule that prevents a stall: IL's workflow PR adding the merge_group trigger must merge before you turn the queue's required checks on. Otherwise queued PRs wait forever for checks that never run. Until then, keep merging as today.

The queue runs the full matrix. Nothing is path-skipped in the queue.

Plan check: confirm in Settings → Rules that your plan offers the queue for private repos. If it does not, tell me. The fallback is "require branches to be up to date", which costs about one update click per PR.

After the queue is on: authors no longer merge main for freshness, only to resolve real conflicts. A468 stands.

### A495 (interim): Stop the line.

If main is red for more than 10 minutes, EL opens a revert PR for the merge that broke it, unless a green fix PR already exists. You merge whichever lands first. A revert needs only your approval. The lane that caused the break fixes it within 30 minutes.

### A496 (interim): Compile gate.

A one-minute build job runs `go build ./... && go vet ./...`. static and the test shards depend on it. A tree that cannot compile no longer starts about 25 jobs.

### A497 (interim): Local database tests.

`make test-db` runs the DB-backed tests against the pinned pgsodium image CI already builds, through Testcontainers. It adds no new dependency. It is a convenience, not a gate.

### A498 (interim): Red-first lane.

A draft PR runs build, vet, the changed packages' tests, contracts and checks. Ready PRs, the transition to ready, and the queue run the full matrix. The failing job in the draft lane is still the red evidence (A302, AGENT-11). Red commits go on draft PRs, and the author undrafts when the head is green.

### A499 (interim): Docs-only pushes.

Skip the Go matrix, compose and images for docs-only changes using the existing changed job and a job-level if. Never use a workflow-level paths-ignore: a required check that never reports would stall every docs-only PR. contracts, checks, the lint and the README-pinning tests still run on .md changes. Nothing is skipped in the queue.

### A500 (interim): Flakes.

A flaky test is a bug with an owner within 24 hours, and it is never skipped or quarantined (AGENTS §8). A nightly `-race -count=5` run covers the e2e tests.

Correction to EL: noema#748 (the A339 lock) is already merged (20 Nov 05:00). EL re-checks whether `TestTheTargetIsTheGuardWhenRevalidationSeesNothing` still flakes after #748. If it does, EL finds the real cause.

## 2. What the Steward did, and where the rulings are silent

- **A489 to A492 are already recorded** (`DEC-2026-11-21-architect-rulings-a489-a492`, docs#219, merged), together with the A463 independent-reads table on noema#183 for noema#843, #849 and #850 (all C2's reads, with their heads). The message repeated them; nothing is recorded twice.
- **Recommendation 8 is dropped.** The Architect's instruction says this set is "from EL's analysis without the last item ('measure it')". The Steward received no text for it and records nothing for it.
- **The merge queue is not on.** A494 is the Founder's to turn on; the Steward does not change a setting (AGENTS §11). **The Steward observed on 21 Nov 2026 (the repository's branch-protection settings):** required checks `compose`, `contracts`, `core`, `checks`, `arch-lint`, `model` and `pr-base-guard`; "require branches to be up to date" off (`strict: false`); required approving reviews 0 (the Founder approval is a process rule, A111, not yet a setting); no merge queue. A494 changes exactly these.
- **The order of the steps** (A494), as the Steward lists them for the Founder and IL: (1) the Founder confirms the plan offers the queue for private repositories (Settings → Rules), or says it does not (the fallback is "require branches to be up to date"); (2) IL's workflow PR adding the `merge_group` trigger merges first (a `.github` change: SR's read and a Founder's approval); (3) IL confirms the exact aggregator job names from the latest green run; (4) the Founder turns on the queue and the required checks; (5) the Founder requires one non-author approval. Until step 4, "keep merging as today".
- **The CI/governance checklist.** No such checklist file exists in `docs`. The nearest records are docs#38 (GOV-22: the founder CODEOWNERS identity and review enforcement) and the G0-N checklist (a gate checklist, not a CI one). The Steward records the merge queue there **after the Founder turns it on** (the Architect's instruction), by decision record, with the date and the settings as the Founder gave them; it creates no checklist file of its own without being told which one.
- **A496 to A499 are workflow and Makefile changes** (`.github`, `make test-db`): IL's and EL's, each needing SR's read on `.github` and a Founder's approval. A499 repeats a rule worth keeping: a required check must always report, so docs-only skipping uses a job-level `if`, never a workflow-level `paths-ignore`. A497 adds no dependency (the pinned pgsodium image and Testcontainers are already in use), so no [OPEN] entry is made.
- **A495 and the Steward's standing task.** The Steward has been fixing red `main` when asked (noema#858, #859, #862, #865 this week); A495 gives EL the revert and the Steward keeps the registers. Nothing here changes the Steward's duties.
- **A493 and the review order.** A PR that makes `main` compile again merges on green CI plus the Founder's approval, with the reads after. This is an order of priority within A468 and A480, not a change to the tiers.
- **A500:** the Steward files nothing; a flake gets its owner within 24 hours and, if it is a shortcut, a debt entry by that owner. The correction to EL (noema#748 already merged on 20 Nov at 05:00) is recorded as given.
- **Next free ruling: A501.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-architect-rulings-a358-a453` | A358 to A362, A380 to A453 | |
| `DEC-2026-11-20-architect-rulings-a454-a467` | A454 to A466 | |
| `DEC-2026-11-20-architect-rulings-a469-a485` and `DEC-2026-11-20-architect-a468-and-a480-corrected` | A468; A469 to A485 | |
| `DEC-2026-11-21-architect-rulings-a489-a492` | A489 to A492 | |
| This record | A493 to A500 | |
| Named without text | A467, A474 follow-up, A475 conditions, A476 wording, A486, A487, A488 (see OD-P-100) | **A501** |
