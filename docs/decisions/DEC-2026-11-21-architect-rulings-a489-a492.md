# DEC-2026-11-21 · Architect rulings A489 to A492 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 21 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 21 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A489 to A492 (§1). A486, A487 and A488 have no text for the Steward as rulings (§2). |
| **Supersedes** | **A489 amends A484** (`DEC-2026-11-20-architect-rulings-a469-a485`): `cmd/tenantinit` registers the core-trust public key only, and tenant rows keep one creator, `create-tenants.sh`; A484 "wrongly had both". **A490 settles** the order of noema#843 and noema#789. **A492 confirms** Codex's P1 on noema#855 (the hostility proxy). Otherwise per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 21 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A489 to A492
- Decision: §1
- Rationale and evidence: the Architect's message of 21 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-12, INV-19, INV-22; AGENT-12, AGENT-13; REQ-TRU-009, REQ-STM-001, REQ-UI-001; PERD §40.1; plan EXE-08, STM-05, UI-01, UI-02
- Supersedes: see the Supersedes row above
- Migration notes: none from this record (migration 0036 is noema#843, which replaces noema#841; see §2)

## 1. The rulings, as given

### A489 (interim, noema#852).

tenantinit registers the core-trust public key only. Tenant rows keep one creator, create-tenants.sh. This amends A484, which wrongly had both. I chose C1's option 1.

*Supersedes or changes:* amends **A484**.

### A490 (interim, noema#789 and noema#843).

noema#843 merges first. Recovery reads the stored principal_role and authn_ref from the row. A row without both is never resumed and never given an invented role. The sweep names it and counts it, so it stays visible.

### A491 (interim, UI).

- The UI shows "Verified" only when the backend verdict says so, never because a reconstruction parses.
- policy_version stays hidden unless PERD §40.1 allows it.
- A card's request id is made once, the button locks after the first click, and any retry reuses the same id.

### A492 (interim, noema#855 follow-up).

Codex's P1 on the proxy stands. Randomness is injected through a struct field, no package-global is mutated, and the test sets nothing globally. IL fixes it in a small PR.

## 2. What the Steward did, and where the rulings are silent

- **A486, A487 and A488 have no text** as rulings for the Steward. **A488** is described in `OD-P-100` (docs#218), which C1 opened "under ruling A488 (relayed by the Founder in session, interim, not yet committed)": it replaces the commit-SHA line of A474 with an optional typed `build_revision` member of the POLICY_PUBLISHED payload. The Steward does not restate A488 from that entry; the Architect sends the text, or says OD-P-100 carries it. **Next free ruling: A493.**
- **A489 and the Steward's earlier record.** A484 in `DEC-2026-11-20-architect-rulings-a469-a485` says "C2 builds cmd/migrate", "C1 builds cmd/tenantinit, which registers the core-trust public key and the tenant rows". A489 removes "and the tenant rows" from tenantinit: the tenant rows have one creator, `create-tenants.sh`. The merged record is not edited; this record says it is amended.
- **Migration numbers (A482, A490).** A482 gave 0036 to noema#841. **noema#843 replaces #841** (and #836) and keeps the number, as C2's independent read says; A490 says #843 merges first. The ledger on noema#183 is repointed: **0036 is noema#843**. 0037 stays reserved for DEBT-54. Next free: 0038. The Steward adds no other change.
- **A491 and plan rows.** The three UI rules are recorded as given; no plan row, debt entry or task is changed (A491 names none). "Unless PERD §40.1 allows it" is the PERD's own rule; the Steward adds no list.
- **A492:** IL's small PR; the Steward only records it.
- **The independent reads of A463, with their heads** (also posted on noema#183): noema#843 (C2, migration 0036), noema#849 and noema#850 (C2, Tier 1 role reads). The links and heads are on noema#183; under A468 a merge-main commit voids no read, and a head that moved after a read is noted there.
- **Task status follows merged evidence only** (the Architect's instruction): none of noema#843, #849, #850, #852 or #789 has merged, so no `tasks.csv` status changes.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-architect-rulings-a358-a453` | A358 to A362, A380 to A453 | |
| `DEC-2026-11-20-architect-rulings-a454-a467` | A454 to A466 | |
| `DEC-2026-11-20-architect-rulings-a469-a485` and `DEC-2026-11-20-architect-a468-and-a480-corrected` | A468; A469 to A485 | |
| This record | A489 to A492 | |
| Named without text | A467, A474 follow-up, A475 conditions, A476 wording, A486, A487, A488 (see OD-P-100) | **A493** |
