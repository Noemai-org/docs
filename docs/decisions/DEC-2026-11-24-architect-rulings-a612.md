# DEC-2026-11-24 · Architect ruling A612 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 24 Nov 2026, who commits it. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 24 November 2026 |
| **Owner** | Principal Architect (the ruling); Founder and Technical Co-Founder (the merge) |
| **Decides** | Ruling A612 (§1), Interim. |
| **Supersedes** | **A612 makes binding**, with owners, the four conditions Security Reviewer gave on docs#238 for rulings A606 to A609. It adds to those rulings; it contradicts none. |
| **Amends** | Nothing in the SoT, the PERD or the plan, as written. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 24 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A612
- Decision: §1
- Rationale and evidence: the Architect's message of 24 Nov 2026, relayed to the Steward; the Security Reviewer's conditions on docs#238
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-12; AGENT-16; REQ-TRU-009; `trust-limits.v2`; AGENTS §5, §8
- Supersedes: see the Supersedes row above
- Migration notes: none from this record.

## 1. The ruling

### A612 (interim, SR's four conditions on A606 to A609, binding with owners).

The conditions Security Reviewer gave on docs#238 for A606 to A609 are binding, owned as follows:

- **A606 (C2, #932):** exact decimal parse, no float; a plain decimal in [0,1]; integer basis points; abstain on a missing or malformed value.
- **A607 (C1, #914):** a request exactly at expiry counts as expired; a boundary test.
- **A608 (Voice, #824):** no partial audio left in the store after a budget stop.
- **A609 (C2 and EL, #910):** the loader refuses the malformed limits file at start-up; composition fails closed.

docs#238 and noema#933 merge as they are once a non-author Founder reviews.

## 2. What the Steward did, and where the rulings are silent

- **Where A606 to A609 are recorded.** A606 to A611 are in `DEC-2026-11-24-architect-rulings-a606-a611`, in docs#238, which is open at this writing; this record is written from `main` and does not link to that file. When docs#238 merges, the Steward merges `main` into this branch and keeps both rows of the decisions README.
- **A606's detail.** The Architect's text is the binding one. Security Reviewer's fuller wording on docs#238 (no exponent, NaN, sign or extra text; 0.9 meets 9000 and 0.8999 does not; the threshold is pack data with no default in code; no golden or input edited, A533) is how SR will read the code PR; it states the same conditions in more detail and adds no new rule to A612. OD-P-101 stays Open: the 9000 basis-point value is still the Architect's interim value for the Founders to confirm.
- **A607.** The database's expiry check is authoritative (A607): the boundary case is "exactly at expiry is expired".
- **A608 and A587.** A587 (a run that fails before any session removes the zero-byte report file it created, never a non-empty report) stays as it is; A612 adds that no partial audio is left in the store after a budget stop.
- **A609 and A596.** A596 and A609 make packcheck validate the shipped limits file against `trust-limits.v2` with a negative test; A612 adds the runtime side: the loader refuses the same malformed file at start-up, and composition fails closed (a pack that does not load starts nothing).
- **Merge direction.** The direction that docs#238 and noema#933 "merge as they are once a non-author Founder reviews" is recorded. The Steward does not merge or approve either (AGENTS §11); both have Security Reviewer READY and Codex with no findings at their current heads.
- **Task status (`tasks.csv`)** and the **migration ledger** are unchanged (0037 #922, 0038 #923, 0039 #925, 0040 reserved, next free 0041).
- **Next free ruling: A613.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` and `DEC-2026-11-21-*` records | A358 to A362, A380 to A485 (A467: no text), A489 to A492, A502 to A517 | |
| `DEC-2026-11-22-architect-rulings-a518-a524` and the `DEC-2026-11-23-*` records | A518 to A605 (A541 noted; A590 to A592 in full) | |
| `DEC-2026-11-24-architect-rulings-a606-a611` (docs#238, open) | A606 to A611 | |
| This record | A612 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank, by ruling A592) | **A613** |
