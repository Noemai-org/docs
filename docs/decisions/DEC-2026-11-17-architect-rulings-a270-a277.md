# DEC-2026-11-17 · Architect rulings A270 to A277 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 17 Nov 2026, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 17 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Eight rulings, A270 to A277 (§1), and a correction to A254 (§2). |
| **Closes** | The money wording of EL's explanation (A270), the answer parts (A271), C1's contract questions (A272), tenant row security (A273), the duplicate TEN-05 pull requests (A274), the "None of these" option (A275), IL's probe facts (A276) and the reader assignments (A277). Closes the open question of `DEC-2026-11-17-reason-codes-a254`. |
| **Supersedes** | **A254**'s count ("17 to 21") is replaced by 20 (§2). Otherwise per ruling, in §1: A270 adds to **A231** and **A259**; A272 adds to **A203** and opens DEBT-42. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 17 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A270 to A277
- Decision: §1 and §2
- Rationale and evidence: the Architect's message of 17 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-12, INV-22; AGENT-13, AGENT-15, AGENT-29; REQ-API-001, REQ-SEC-004, REQ-EXP-001, REQ-ENV-007, REQ-TRU-001; PERD §39.2; SoT §0.4, §43.2a
- Migration notes: A272's enum and `TransactionClassification` list and A275's `none_option_id` are minor contract changes in place, C1's, with a migration note and regenerated models (AGENT-15); A273's migrations are numbered by C1 on C1's ledger
- Supersedes: see the Supersedes row above

## 1. The rulings, exactly as given

| Ruling | Text | Supersedes or changes |
|---|---|---|
| **A270** (interim) | **Money wording.** EL's "NGN 1,234 and 50 kobo" does not work, because any amount of 10,000 or more still has five digits. Money is rendered by the core from integer minor units only. The shape is `^[A-Z]{3} [0-9]{1,3}(,[0-9]{3})*(\.[0-9]{2})?$` with at most 9 integer digits. It gets a narrow exemption, and the shape is a named vector in the A259 shared file. Ungrouped digit strings, and groups with more than 9 integer digits, stay refused. This touches the Record guard, so it is Tier 1: C1 owns the pull request, and Codex, SR, EL and the Founder review it. Until it merges, EL's explanation blocks on amounts. That is the safe behaviour. | Adds a second narrow exemption to the Record guard beside **A231**'s reason-code exemption; extends **A259**'s shared vector file by one named vector. |
| **A271** (interim) | **Answer parts.** Each part (found, not-known, summary, advice, next, and so on) has its own template key in the pack. Build assembles them from several renderer-made parts. This is a pack pull request from EL, with pack data and tests first. | Nothing committed. |
| **A272** (interim) | **C1's contract questions.** Enum = 20. Facts: only the free-text keys (`text` and `reason_codes` items) get the digit pattern; references and IDs do not. The bounds 1000/1000/100/50 stand, and any change is a minor version. Add a closed `TransactionClassification` list with the 12 PERD classes, in place before the tag (A203); red test first. The Go pattern gap becomes DEBT-42 (C1). It closes before any partner data, and the tag notes say so. | **Corrects A254** (17 to 20, not 21; `DECLINED_BY_APPROVER` was already one of the 17). Adds to **A203**'s tag conditions. Opens DEBT-42. |
| **A273** (interim) | **Tenant row security.** The tenant table is readable by every power login. Fix it with a policy bound to the login's tenant. It is a Tier 1 migration, reviewed by SR and the Architect, with a behavioural cross-tenant test. C1 assigns the numbers on the ledger: `principal_ref` first (it is on the G1 path), tenant row security next. | Nothing committed. Related: DEBT-04 (tenant binding of the Record functions), SEC-08. |
| **A274** (interim) | **Duplicate TEN-05.** noema#649 (EL) and noema#657 (C1) do the same job. #657 stays because C1 owns the task and it prints `TEN_RESULT`. EL closes #649 once the "no production code builds the simulated clock" test is moved onto #657. IL adds the CI grep for `TEN_RESULT`. | Settles the owner of the Temporal half of TEN-05 (G0-N checklist row 3: C1, with EL's test). |
| **A275** (interim) | **"None of these".** PERD §39.2's `option_id` carries it. The clarification object gets a core-minted `none_option_id`, unique per clarification, and the UI submits it as `option_id`. It is a minor in-place contract change after noema#615 merges. EL handles it as PUS-01: one narrowing question, or hand-off after the round limit. The UI never invents a sentinel. | Nothing committed. A contract change by AGENT-15 (minor, in place; nothing consumes it yet). |
| **A276** (interim) | **IL probe facts.** IL reads how the credential is presented, and a permitted read, from spec v1.0, delta v1.3 and the addendum. Only the base URL and the credential's Environment come from the Founder. | Narrows what noema#655 waits on to two facts; **A263**'s probe is unchanged. |
| **A277** (interim) | **Reader assignments.** C2 reads noema#646, #642 and #659. C1 reads #576, #457, #628 and #650. EL reads #653, #651, #652 and #657. SR reads #615's delta, #646 (security), #635 (is it the A265 wiring pull request?) and #658. IL reads docs#191. Each reader posts one line at the final head. | Nothing committed. A working assignment; the reads are the roles' own. |

## 2. The correction to A254

The Architect wrote: "Correction to A254: the enum goes 17 to 20. `DECLINED_BY_APPROVER` was already one of the 17, so only three codes are new. That was my error. C1 and the Steward were right." The three new codes are `TARGET_FROZEN`, `CLOCK_BREACHED_UNROUTED` and `DISPATCH_BUDGET_EXHAUSTED`. The earlier records (`DEC-2026-11-17-architect-rulings-a253-a269` and `DEC-2026-11-17-reason-codes-a254`) are updated in the same pull request to say 20.

## 3. What the Steward did where the rulings are silent

- **DEBT-42** (the Go pattern gap, owner C1) is in the debt register in this pull request. A272 names the gap in four words; the Steward has not seen C1's description of it, so the entry quotes the ruling and asks C1 to state the exact gap in the contract pull request.
- **A270 is Tier 1.** The Steward only records it. The review gates are those of A143: Codex, SR, one independent role review (EL), CI and a Founder.
- **A275** says the change comes "after #615 merges"; the Steward records the order and does not hold any pull request.
- **A277** names noema#576, #457, #628, #650, #646, #642, #659, #653, #651, #652, #657, #615, #635 and #658 and docs#191. The Steward did not read them for this record.
- **ENV-02 and ENV-17** are marked Done in `tasks.csv` on IL's report on noema#183; see the task audit (docs#195). The Steward re-checked ENV-02 against `main` (the 20 AT rows are byte-equal to §22 of the frozen specification) and ENV-17 against noema#537 and #594.
- **Next free ruling: A278.**

## 4. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A269 (A253 to A269 in docs#196) | |
| This record | A270 to A277 | **A278** |
