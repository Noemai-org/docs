# DEC-2026-10-11-poc-4week-plan

- Status: Proposed (founder approval required)
- Date: 2026-10-11
- Closes: none
- Owner: Founders (TODO: name), with the technical co-founder as reviewer
- Decision:
  1. Adopt [`docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v1.1.md`](../poc/execution/NOEMA_POC_4WEEK_PLAN_v1.1.md) as the execution plan for the POC build, from 12 October to 6 November 2026, below SoT v1.3 and PERD v1.1.
  2. Record the schedule change (plan §3; task GOV-04).
     - SoT §40.2 plans four build weeks *after* Phase A exits.
     - This plan runs Phase A in parallel with week 1, with G0 due Thu 15 Oct.
     - This changes a [TARGET] time box only. Every SoT gate stays intact.
     - G0 must pass before any Phase B result counts.
     - If the time box and the gates conflict, the gates win and the date moves (SoT §40.2).
- Rationale and evidence:
  - The PERD defines what to build.
  - The plan turns it into 201 owned tasks with dependencies.
  - It covers all 152 PERD requirements, all 105 edge cases and all 22 user stories.
  - `tools/plan_index.py --check` enforces this coverage in CI.
- Affected requirement IDs / SoT sections: SoT §40.1, §40.2 and §40.3; PERD §61 and §69; REQ-AGT-001 to REQ-AGT-005; REQ-OPS-004. No SoT or PERD text changes in this record or its pull request.
- Migration notes:
  - None for code; no code exists yet.
  - Plan changes follow [`docs/poc/execution/README.md`](../poc/execution/README.md): a change request, a new version file, the regenerated `tasks.csv` and a note in that day's daily note, in one pull request.
  - Tracked as provisional entry [OD-P-42](../open-decisions.md#od-p-42) until accepted.
- Supersedes: none.
- Links: [DEC-2026-10-11-poc-perd-v1.1](DEC-2026-10-11-poc-perd-v1.1.md).

## SoT §52 questions

- **Which requirement ID does this serve?** SoT §0.4, §40.2, AGENT-01, AGENT-02, AGENT-23, AGENT-29; PERD REQ-AGT-001 to REQ-AGT-005, REQ-OPS-004, REQ-BEN-008.
- **What breaks without it?** The PERD has no dated, owned task list, so work on Mon 12 Oct would start without agreed order, owners or gate dates.
- **Which benchmark case proves it works?** None directly; it is a plan. Its gates (plan §3.1) are decided on benchmark evidence.
- **What business value does it create?** A dated path to the SoT §40.3 evidence by Fri 6 Nov 2026, with the gates unchanged.
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
