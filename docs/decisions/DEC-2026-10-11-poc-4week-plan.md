# DEC-2026-10-11-poc-4week-plan

- Status: Accepted. The Founder approved it on 16 Oct 2026 (written instruction); the Technical Co-Founder confirms by approving the pull request that applies DEC-2026-10-16
- Date: 2026-10-11
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision:
  1. Adopt the current plan, named in [`docs/poc/execution/README.md`](../poc/execution/README.md) (v1.5), as the execution plan for the POC build, from 12 October to 13 November 2026, below the SoT and the current PERD. This record first adopted v1.1; DEC-2026-10-16 E11 re-pointed it to the current plan and to the E3 schedule.
  2. Record the schedule change (plan §3; task GOV-04).
     - SoT §40.2 plans four build weeks *after* Phase A exits.
     - This plan runs Phase A in parallel with week 1.
     - G0 has two halves (DEC-2026-10-16 E4): G0-N on Thu 22 Oct 2026, 17:00, and G0-T on the date Tushe confirms. Both must pass.
     - The schedule is the one in DEC-2026-10-16 E3, with the demo on Fri 13 Nov 2026.
     - This changes a [TARGET] time box only. Every SoT gate stays intact.
     - G0 must pass before any Phase B result counts.
     - If the time box and the gates conflict, the gates win and the date moves (SoT §40.2).
- Rationale and evidence:
  - The PERD defines what to build.
  - The plan turns it into owned tasks with dependencies (the count is in the plan's task index).
  - It covers all 153 PERD requirements, all 105 edge cases and all 22 user stories.
  - `tools/plan_index.py --check` enforces this coverage in CI.
- Affected requirement IDs / SoT sections: SoT §40.1, §40.2 and §40.3; PERD §61 and §69; REQ-AGT-001 to REQ-AGT-005; REQ-OPS-004. No SoT or PERD text changes in this record or its pull request.
- Migration notes:
  - None for code; no code exists yet.
  - Plan changes follow [`docs/poc/execution/README.md`](../poc/execution/README.md): a change request, a new version file, the regenerated `tasks.csv` and a note in that day's daily note, in one pull request.
  - Tracked as provisional entry [OD-P-42](../open-decisions.md#od-p-42) until accepted.
- Supersedes: none.
- Links: [DEC-2026-10-11-poc-perd-v1.1](DEC-2026-10-11-poc-perd-v1.1.md); [DEC-2026-10-16](DEC-2026-10-16-execution-reset.md) E3, E4 and E11.

## Sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Founder | — | Approved, 16 Oct 2026 (written instruction) | 16 Oct 2026 |
| Technical Co-Founder | — | Confirms by approving this PR | Date of the approving review |

## SoT §52 questions

- **Which requirement ID does this serve?** SoT §0.4, §40.2, AGENT-01, AGENT-02, AGENT-23, AGENT-29; PERD REQ-AGT-001 to REQ-AGT-005, REQ-OPS-004, REQ-BEN-008.
- **What breaks without it?** The PERD has no dated, owned task list, so work on Mon 12 Oct would start without agreed order, owners or gate dates.
- **Which benchmark case proves it works?** None directly; it is a plan. Its gates (plan §3.1) are decided on benchmark evidence.
- **What business value does it create?** A dated path to the SoT §40.3 evidence by Fri 13 Nov 2026, with the gates unchanged.
- **Core, pack, adapter or nowhere?** Nowhere in code. It is documentation in the docs repository.
- **Which failure mode does it prevent?** Unowned or out-of-order work, uncovered requirements, and gates being treated as status updates.
- **Why are existing products or components not good enough?** PERD §61 gives build steps and a day plan, but not every task with an owner, dependencies and a completion test.
- **Which phase does it belong to?** Phases A to F (SoT §40.1), within the four-week [TARGET] time box (SoT §40.2).
- **What vertical, country, model or interface assumptions does it make?** Those of the POC fence only (SoT Part VII). None enters core.
- **What is the simplest viable implementation?** Commit the plan unchanged, generate the board import from it, and check it against the PERD index in CI.
- **Can its result be independently verified and tested adversarially?** Yes: `tools/plan_index.py --check` fails on stale output, duplicate or forward dependencies, unknown REQ IDs and missing coverage.
- **Does it preserve the separation of Understanding, Trust, Execution and Outcome?** Yes. Its tasks follow the PERD and SoT §13.
- **Does it work across models and interfaces?** Yes. It keeps all six providers (BD-16) and text as the canonical contract (BD-14).
- **Does it create reusable infrastructure and a measurable enterprise metric?** It creates a reusable task index and records, not runtime infrastructure. Its metrics are the SoT §38 benchmark metrics.
- **What evidence would make us reverse it?** G0 failing in a way that makes week-1 results unusable, or a SoT revision that changes Phase A.
- **Does it increase or decrease the unsafe autonomy surface?** **Neither directly.** It adds no capability, and it adds explicit gates, stop rules and checks.
