# DEC-2026-10-21 · REQ-INT-002: a refused reply triggers failover

| | |
|---|---|
| **Status** | Accepted by the requesting Founder on 21 October 2026 (an instruction given in a working session; it counts once this record is merged). The other Founder confirms by approving the pull request that adds it |
| **Date** | 21 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None |
| **Amends** | PERD REQ-INT-002 (PERD v1.12) |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the requesting Founder (see the table above)
- Date: 21 October 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: the Founder's instruction of 21 October 2026, in the words quoted in §1. No other evidence is cited
- Affected requirement IDs / SoT sections: REQ-INT-002. It cites REQ-INT-001 and INV-02 and changes neither. No SoT change. The requirement count stays 153
- Migration notes: PERD v1.12 is a new file; v1.11 stays unchanged. The `noema` model service (`providers/`, `harness/`) follows under the understanding tasks
- Supersedes: None. It adds a failover trigger and restates a rule; it loosens no invariant

---

## 1. The decision

| | Decision |
|---|---|
| D1 | The failover amendment to REQ-INT-002: a refused reply triggers failover to the next provider; the output still passes the schema gate and is never repaired. (The Founder's words: "a refused reply triggers failover to the next provider; the output still passes the schema gate and is never repaired".) |

## 2. Agent decisions

1. **Wording in PERD v1.12.** A refused reply is defined as one in which the provider declines to answer instead of returning output. "Never repaired" is written as: no Noema code edits, completes, re-types or infers a field of a provider's output. Both are readings of the instruction, not new rules; the Founders may correct them.
2. **Every provider refuses.** The existing sentence for "every provider fails" now reads "fails or refuses", so the result is REJECTED_AT_GATE (`PROVIDER_UNAVAILABLE`), never a heuristic guess. This follows from the instruction and is the safer reading (AGENT-20).
3. **Not decided here.** (a) Whether a reply that is returned but fails the schema gate also triggers failover. REQ-INT-001 says rejected objects are never admitted; this record does not change that and does not add a trigger. (b) Whether `PROVIDER_FAILOVER` carries the reason (error, timeout, refusal): the Record event list is closed and no field is added. Both are raised as open decisions.
4. **Tests added to REQ-INT-002.** A refusal case in the failover chaos test, and a property test that no field of a provider's output changes between receipt and the schema gate.

## 3. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted by the requesting Founder (one Founder) | 21 October 2026 | Instruction in a working session, written here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
