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
- Decision: the table in §1 (D1 to D4)
- Rationale and evidence: the Founder's instructions of 21 October 2026 (the amendment, then the correction and the two answers), in the words quoted in §1. No other evidence is cited
- Affected requirement IDs / SoT sections: REQ-INT-002. It cites REQ-INT-001 and INV-02 and changes neither. No SoT change. The requirement count stays 153
- Migration notes: PERD v1.12 is a new file; v1.11 stays unchanged. The `noema` model service (`providers/`, `harness/`) follows under the understanding tasks
- Supersedes: None. It adds a failover trigger and restates a rule; it loosens no invariant

---

## 1. The decision

| | Decision |
|---|---|
| D1 | The failover amendment to REQ-INT-002: a refused reply triggers failover to the next provider; the output still passes the schema gate and is never repaired. (The Founder's words: "a refused reply triggers failover to the next provider; the output still passes the schema gate and is never repaired".) |
| D2 | **A refused reply is a reply in the wrong format that fails the schema check. It is not a provider declining to answer.** (Correction by the Founder, 21 October 2026, before this record merged.) |
| D3 | A schema-failing reply triggers failover (the Founder's answer to the first open question of the first draft). |
| D4 | `PROVIDER_FAILOVER` carries the reason (the Founder's answer to the second open question). |

## 2. Agent decisions

1. **"The schema check"** is read as the JSON Schema validation step of REQ-INT-001 (the Intent Object against the generated schema). The pack checks that follow it in REQ-INT-001 (the node exists, the slots match) are not part of "refused reply". The Founders may widen it.
2. **Reason values.** No value set was given. I wrote `PROVIDER_ERROR`, `TIMEOUT` and `REFUSED_REPLY`, one per failover trigger. This is a default for the Founders to confirm; the Record event type list is unchanged (`PROVIDER_FAILOVER` already exists), only the carried reason is added, as `GRANT_VOIDED{reason}` already does.
3. **Every provider fails.** The sentence for "every provider fails" now lists the three triggers, and the result stays REJECTED_AT_GATE (`PROVIDER_UNAVAILABLE`), never a heuristic guess. When every provider returned a wrong-format reply, `PROVIDER_UNAVAILABLE` reads oddly; the code was not changed because no other was given.
4. **Never repaired** is written as: no Noema code edits, completes, re-types or infers a field of a provider's output.
5. **Tests.** The failover chaos test gains a case where a provider returns a reply that fails the schema check; a property test shows that no field of any provider's output changes between receipt and the schema gate.

## 3. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted by the requesting Founder (one Founder) | 21 October 2026 | Instruction in a working session, written here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
