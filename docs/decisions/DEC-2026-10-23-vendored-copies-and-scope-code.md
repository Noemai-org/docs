# DEC-2026-10-23 · Vendored copies are re-pointed in the same change set, and §39.3 names `TENANT_SCOPE_MISMATCH`

| | |
|---|---|
| **Status** | Accepted by the requesting Founder on 23 October 2026 (instructions given in a working session, in the words quoted in §1; they count once this record is merged). The other Founder confirms by approving the pull request that adds it |
| **Date** | 23 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None. Answers question (3) of OD-P-68 (whether a PERD requirement should govern vendored copies); the automation OD-P-68 proposes stays open |
| **Amends** | PERD §39.3 and §65.2 (PERD v1.15); plan v1.9 adds one task |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the requesting Founder (see the table above)
- Date: 23 October 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: new REQ-OPS-005; PERD §39.3; cites REQ-OPS-004, PERD §64.2, SoT §51. No SoT change. The requirement count becomes 154 (P0 130, P1 21, P2 3)
- Migration notes: PERD v1.15 and plan v1.9 are new files; v1.14 and v1.8 stay unchanged. `noema` re-points its five vendored copies to the docs commit that merges this record (noema#56). The security event code in `contracts/errors.v1.json` is already `TENANT_SCOPE_MISMATCH`; no contract change
- Supersedes: None

---

## 1. The decisions

| | Decision |
|---|---|
| D1 | **REQ-OPS-005.** A docs change that touches vendored text requires a matching re-point in `noema` in the same change set, and the drift check fails when a copy differs. One PERD version carries both D1 and D2, so there is one re-point per docs merge |
| D2 | **§39.3 names `TENANT_SCOPE_MISMATCH`**, the code in `contracts/errors.v1.json`, in place of `SCOPE_VIOLATION`, which the contract does not define |

## 2. Rationale and evidence

**D1.** `noema` keeps five copies of docs text (`AGENTS.md`, `CLAUDE.md`, `contracts/state-registry.md`, `contracts/perd-32-2-event-types.md`, `services/core/orchestrator/perd-28-2-state-machine.md`). After almost every docs merge the daily `docs-drift` check went red until someone re-pointed them (noema#39, #55, #56). No requirement governed this (OD-P-68). The check and its tests exist (`tools/vendor/test_drift_guard.py`, `tools/vendor/test_repoint_bodies.py`); the requirement makes the practice binding.

**D2.** `errors.v1.json` lists `TENANT_SCOPE_MISMATCH` and no `SCOPE_VIOLATION`; the PERD named the latter. The contract is the code that exists, and an error code needs one name (AGENT-15).

## 3. Agent decisions

1. The plan gains task OPS-07 (owner EL, Fri 23 Oct) because `plan_index.py --check` requires every PERD requirement to have a plan task. The owner, date and done-when are agent defaults for the Founders to change.
2. REQ-OPS-005 is P1, as REQ-OPS-004 is. The Founders may raise it.
3. "Merged with it" is read as: the `noema` re-point pull request is opened with the docs pull request, names it, and is merged straight after it. A merge to docs `main` cannot be atomic with a merge in another repository.
4. Whether the re-point is automated (OD-P-68) is not decided here.

## 4. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted by the requesting Founder (one Founder) | 23 October 2026 | Instructions in a working session, written here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
