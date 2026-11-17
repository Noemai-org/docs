# DEC-2026-11-17 · Reason codes of A254 (interim; count corrected by the Architect)

| | |
|---|---|
| **Status** | **Interim.** The count question of §3 is answered: the enum goes 17 to 20 (the Architect's correction of 17 Nov 2026, recorded in `DEC-2026-11-17-architect-rulings-a270-a277`). Decided by the Principal Architect on 17 Nov 2026 (A254), relayed to the Repo Steward, who wrote this record as the ruling asks. Counts once a Founder who did not author this pull request approves and merges it (A111). |
| **Date** | 17 November 2026 |
| **Owner** | Principal Architect (the ruling); C1 (the contract change); Founders (the SoT edit) |
| **Decides** | The Decision Record's core reason codes `TARGET_FROZEN`, `CLOCK_BREACHED_UNROUTED` and `DISPATCH_BUDGET_EXHAUSTED` are added to the closed enum, which goes from 17 to **20**. `DECLINED_BY_APPROVER` was already one of the 17 (SoT §43.2a, since v1.2) and is not new. |
| **Closes** | The reason-code part of C1's questions (A244, first bullet). |
| **Supersedes** | **A244**'s first bullet (it proposed the three codes and left them as a proposal); this record adopts them. A244's other bullets are unchanged. |
| **Amends** | Nothing in the SoT or the PERD yet. The SoT's value list (§43.2, `docs/engineering/state-registry.md`, the row "Decision Record · `reason_codes`") changes in the next SoT version, made by the Founders with an Appendix D entry. |
| **Authority order applied** | SoT → decision records → PERD → plan |

## 1. The ruling

A254: "The four codes (`TARGET_FROZEN`, `CLOCK_BREACHED_UNROUTED`, `DISPATCH_BUDGET_EXHAUSTED`, `DECLINED_BY_APPROVER`) are adopted. The enum goes 17 to 21. The Steward writes the decision record. C1's contract PR goes now. TRU-14 waits until after G1."

## 2. What this means

- **The enum.** Three codes are new to the closed core list: `TARGET_FROZEN`, `CLOCK_BREACHED_UNROUTED`, `DISPATCH_BUDGET_EXHAUSTED`. An additive minor bump of the contract with a migration note (AGENT-15); the migration is C1's. Pack codes and the namespace rule are unchanged.
- **C1's contract pull request goes now.** It is not held for G1.
- **TRU-14** (the `TRUST_REFUSED` Record event) waits until after the G1 run, as the plan row already says; it is not on the US-01 or US-06 path.
- **No `CONFIRMATION_SPENT` event type** (A244, unchanged).

## 3. The count (answered)

A254 as first given said "four codes" and "17 to 21". The registry's closed list of core reason codes already held 17 codes, and `DECLINED_BY_APPROVER` is one of them (SoT §43.2a, since v1.2), so three new codes give 20. The Steward put the question to the Architect. The Architect's correction of 17 Nov 2026: "the enum goes 17 to 20. `DECLINED_BY_APPROVER` was already one of the 17, so only three codes are new. That was my error. C1 and the Steward were right." The count is **20**.

The registry (`docs/engineering/state-registry.md`) and the SoT value list keep the old list until the Founders' next SoT version adds the three codes; no edit is made here (a SoT change is a new version with an Appendix D entry). C1's contract pull request adds exactly the three codes and the enum count is 20.

## 4. Record fields

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 17 November 2026
- Closes: the reason-code bullet of A244
- Owner: Principal Architect; C1; Founders
- Decides: A254's codes
- Decision: §2 and §3 (count 20)
- Rationale and evidence: A254; `docs/engineering/state-registry.md` (the 17 core codes); SoT §43.2a
- Affected requirement IDs / SoT sections: REQ-TRU-001, REQ-TRU-002, REQ-API-001; INV-03, INV-07; SoT §43.2, §43.2a
- Migration notes: C1's contract change is an additive minor version with a migration note and regenerated models (AGENT-15)
- Supersedes: A244, first bullet
