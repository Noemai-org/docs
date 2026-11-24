# DEC-2026-11-24 · Founder decisions: WAIT in the T10 row (SOT-C-34), and the approval on noema#921

| | |
|---|---|
| **Status** | **Decided by the Founder in session on 24 Nov 2026; committed by this record.** It counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). A Founder decision ranks first in the order of authority (SoT §0.4, item 1). |
| **Date** | 24 November 2026 |
| **Owner** | The Founder who gave the decisions in session (the Steward records them; the Steward does not decide) |
| **Decides** | **D1:** SOT-C-34 is resolved by alternative 1 (WAIT is added to the §23.3 T10 row). **D2:** the Founder accepts the `noemai-systems` approval on noema#921. |
| **Supersedes** | **D1 replaces** the interim safer reading of ruling A642 for this point (same behaviour; now a decision, not a holding position). **D2 overrides ruling A638's "ignore" for noema#921 only**; A638 stands for every other pull request. |
| **Amends** | The PERD: a new version file, `NOEMA_POC_PERD_v1.29.md` (Proposed), carries D1. The merged PERD v1.28 is not edited. No SoT edit. |
| **Authority order applied** | SoT §0.4: the latest recorded founder decision first |

**Record fields (decisions README template).**

- Status: decided in session by the Founder; counts on merge by a non-author Founder (A111)
- Date: 24 November 2026
- Owner: the Founder
- Decides: D1, D2
- Decision: §1
- Rationale and evidence: the Founder's words of 24 Nov 2026 in session ("The approval is accepted ... I approve your recommendation on WAIT. Implement now"); the Steward's recommendation, given the same day, which the Founder approved
- Affected requirement IDs / SoT sections: PERD §23.1 (WAIT), §23.3 (step T10), REQ-RES-005, REQ-RES-002, INV-20, INV-25; plan tasks RES-02 and RES-05; conflicts register SOT-C-34
- Supersedes: see the Supersedes row above
- Migration notes: none (no contract, schema or database change).

## 1. The decisions

### D1. SOT-C-34 resolved: WAIT is added to the §23.3 T10 row.

- The PERD §23.3 row for step T10 (reconciliation; freeze check) gains **WAIT inside a convergence window**: a watch and a deadline at the window's end, and no write. **ESCALATE** stays the result on contradiction (outside the window) or an unknown outcome, per pack mapping.
- REQ-RES-005 stands as written. The two texts now agree.
- Why alternative 1 (the Steward's reasons, approved by the Founder): WAIT is already one of the seven outcomes (§23.1: nothing may be done yet because a bounded, known condition must first change); a recorded WAIT with its deadline can be audited and survives a crash, because the deadline is a database row; a hold with no recorded decision cannot be seen in the Record; and WAIT can never allow a write (grants come only from ALLOW, INV-25), so inside the window nothing is written either way.
- RES-02 and RES-05 build on this reading; they were never blocked.

### D2. The `noemai-systems` approval on noema#921 is accepted.

The Founder accepts the approval that `noemai-systems` gave to noema#921. No after-the-fact read by the other Founder is required for #921. This applies to noema#921 only. Ruling A638 stands for every other pull request: an approval from the agents' account is not a human read, and a merge needs a Founder's personal approval.

## 2. What the Steward did

- **PERD v1.29 (Proposed).** `docs/poc/perd/NOEMA_POC_PERD_v1.29.md` is v1.28 with exactly three differences: its header (version, date, and the reference to this record), a "Changes in v1.29" section, and the T10 row. A line-by-line comparison against v1.28 shows nothing else changed. `requirements-index.csv` is regenerated and is unchanged (173 requirements). The PERD README gains its row. Like v1.24 to v1.28, v1.29 is Proposed and takes effect only with the SoT versions those name; until then this decision governs (A448).
- **SOT-C-34** in the conflicts register is now **Resolved** by this record.
- **The plan is not edited.** Nothing in the plan changes: RES-05's row already says "inside the window WAIT with a watch and deadline".
- **Ruling A642** (in `DEC-2026-11-24-architect-rulings-a624-a643`) gave the same behaviour as an interim safer reading; D1 makes it a decision. Its CONFLICT block is kept as the audit record of what was raised.
- **noema#921 (D2).** The facts are in `DEC-2026-11-24-architect-rulings-a624-a643` (§2): the pull request's author is `OladiranOlatunde`; it was approved at 13:17:04Z and merged at 13:17:13Z on 24 Nov 2026, both by `noemai-systems`; the Steward did neither. D2 accepts the approval for that pull request only.
- **Migration ledger on noema#183** and **`tasks.csv`** are unchanged.
