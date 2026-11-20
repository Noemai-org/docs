# DEC-2026-11-19 · Founder decision: the full confirmation path ships before G1

| | |
|---|---|
| **Status** | **Founder decision**, given to the Repo Steward on 19 Nov 2026 and committed here by the Steward. It counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 19 November 2026 |
| **Owner** | Founders |
| **Decides** | The full confirmation path ships before G1, not in G2. |
| **Closes** | When the full confirmation path ships. |
| **Supersedes** | Any schedule that puts the full confirmation path in G2. The Steward found no committed document that says so (the plan's G1 and G2 definitions do not list it); the Founder's wording says "not in G2", so any such schedule, written or held by a lane, is replaced. |
| **Amends** | Nothing in the SoT or the PERD (the requirements are unchanged). The plan's gate assignment of the confirmation tasks, if the Founders or the Architect want it changed, goes through a change request (§2). |
| **Authority order applied** | Latest recorded founder decision (SoT §0.4, item 1) → SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Founder decision; counts on merge by a non-author Founder (A111)
- Date: 19 November 2026
- Owner: Founders
- Decides: the confirmation path before G1
- Decision: §1
- Rationale and evidence: the Founder's instruction to the Steward of 19 Nov 2026. The Founder gave no rationale in the instruction; none is invented here.
- Affected requirement IDs / SoT sections: REQ-TRU-009; SoT §43.2a; PERD §23; plan TRU-07 (the confirmation contract), UI-02 (the confirmation cards), OUT-03 (confirmation expiry)
- Supersedes: see the Supersedes row above
- Migration notes: none from this record; the confirmation store is migration 0032 (noema#756) and the lookup key may add 0034 (A366)

## 1. The decision, as the Founder worded it

The full confirmation path (Given, Declined, Expired, BindingChanged, PolicyChanged, NotEligible, WrongRequest, approver route) ships before G1, not in G2.

## 2. What the Steward notes (the record does not decide these)

- **The eight cases are the Founder's list.** The Steward does not define them. The PERD says where they come from: REQ-TRU-009 and SoT §43.2a (the confirmation contract, the binding, the 10-minute expiry and the approver requirement), and the reason codes of §23.3 (`DECLINED_BY_APPROVER`, `POLICY_VERSION_MISMATCH`, and the others).
- **G1 as the plan defines it** (plan §3.1) is "one clean case (US-01) and one timeout-after-write case (US-06) run end to end on text". It does not list the confirmation path. This decision widens what must be built before G1 reviews; it does not edit the gate. If the Founders want the gate's wording or the confirmation tasks' gate column changed, that is a change request (plan §19) and a new plan version; the Steward opens it when told which tasks and which gate wording.
- **Tasks that carry the path today** (tasks.csv, 19 Nov): TRU-07 (the confirmation contract), UI-02 (the confirmation cards), OUT-03 (confirmation expiry), and the confirmation store and route pull requests (noema#756, noema#754, noema#759). The Steward does not know whether other rows belong, and does not change any row.
- **Ruling A369** says `CONFIRMATION_EXPIRED` is written by the Recorder in the same transaction as the new CONFIRM decision for the superseding request, with no sweeper in G1. That stays as ruled; OUT-03's sweeper-based expiry is later.
- **The safer reading applies meanwhile** (AGENT-20): the path is built to the PERD as it stands; nothing here relaxes a Tier 0 gate or an invariant.
