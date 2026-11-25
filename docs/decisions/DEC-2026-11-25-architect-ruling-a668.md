# DEC-2026-11-25 · Architect ruling A668 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 25 Nov 2026, who commits it. Counts once a Founder who did not author this pull request approves, from a personal account, and merges it (A111, A638; AGENTS §2, item 3). |
| **Date** | 25 November 2026 |
| **Owner** | Principal Architect (the ruling); the Founders (the merge) |
| **Decides** | A668 (§1). |
| **Supersedes** | **A668 restates and closes A661** for noema#954. It changes nothing else; it relies on A657 (SR's READY stands in for an unread Codex, A656) and on Trust's basis binding. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Affected IDs** | INV-03, INV-17, INV-21; AGENT-16; REQ-OPS-004; noema#954 |
| **Migration notes** | None. No migration is added. The later database-defaulted `sealed_at` column is tracked as DEBT-58 and needs its own migration and approval then. |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder's personal approval (A111, A638)
- Date: 25 November 2026
- Owner: Principal Architect; Founders
- Decides: A668
- Decision: §1
- Rationale and evidence: the Architect's message of 25 Nov 2026, relayed to the Steward; Codex stand-in's and C1's reads of noema#954 (finding 1)
- Affected requirement IDs / SoT sections: INV-03, INV-17, INV-21; AGENT-16; REQ-OPS-004
- Supersedes: A668 restates and closes A661 for noema#954; nothing else
- Migration notes: none; the later database-defaulted `sealed_at` column is DEBT-58

## 1. The ruling

### A668 (restates and closes A661, for noema#954)

1. **`sealed_at` is the ordering authority for the POC.**
   - The POC runs one core process on one clock interface, so no migration is needed.
   - The Steward adds the debt entry (owner C1): **DEBT-58**. A database-defaulted column is required before any multi-sealer or Phase 2 deployment.
   - The alternative migration is taken only if multi-sealer enters the POC, which it does not.
2. **Intent versus snapshot.**
   - The fail-closed check is required. If the newest snapshot predates the admitted intent, `ScopeFor` returns `ErrNoRouteScope`, so there is no scope and no grant.
   - EL adds it red first, as one small follow-up commit. It does not block merging #954, because Trust's basis binding already refuses a hash that does not match.
   - It must land before the composition wires the route handoff. The `selectIntent` read is not dropped.
3. **#954's READY.**
   - The Codex stand-in's NOT READY and C1's NOT READY were both on finding 1, which this ruling settles. That is a ruling, not a code change, so the earlier SR READY at `8969f679` stands under A657.
   - EL undrafts #954 and posts a comment citing A668 and the debt entry.
   - The follow-up commit is a code push, so it gets a fresh SR READY at its own head.

## 2. What the Steward did, and where the ruling is silent

- **DEBT-58 added** to `docs/poc/execution/debt.md`: owner C1; removal condition, a database-defaulted `sealed_at` column before any multi-sealer or Phase 2 deployment; expiry the same point; Status Open. **Tier 3 is the Steward's default**; the ruling gives no tier, and the Architect or the Founders may change it. The guarding test column names EL's follow-up check (item 2), because the ruling names no test for the ordering itself.
- **Rulings A657 to A667 are not in this record.** The Steward was given A668 alone and found no record of A657 to A667 in `docs` `main` or in an open `docs` pull request. A668 cites A657 and A661, so the Steward has not invented their text. If they exist, send them and the Steward records them in their own record. Until then **the next free ruling is not asserted** beyond "A669 or later"; the Steward's ledger still reads A657 as the next free after A656.
- **Review gate for #954.** A668 item 3 rests on A657 and A656 (SR's READY stands in for an unread Codex; independent role reads for migrations only). Neither is committed in `docs` yet (A644 to A656 is docs#242, merged). The Steward notes it and does not act on #954 here.
- **No code or plan change.** `tasks.csv`, the plan and the PERD are untouched.
