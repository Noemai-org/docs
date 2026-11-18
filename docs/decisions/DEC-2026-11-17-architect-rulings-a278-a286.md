# DEC-2026-11-17 · Architect rulings A278 to A286 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 17 Nov 2026, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 17 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Nine rulings, A278 to A286 (§1). |
| **Closes** | The fact-value rule and noema#615 (A278), the money text (A279), noema#658 and the tenant row-security gap (A280), the part list (A281), the worker's task ID (A282), the YAML checks of noema#622 and #629 (A283), noema#653 (A284), noema#654 (A285) and the wiring of C2's adapters (A286). |
| **Supersedes** | **A278** replaces the key-list sentence of **A272**; **A279** restates **A270** as its final text. Otherwise per ruling, in §1. |
| **Amends** | Nothing in the SoT or the PERD. The plan gains one task (STM-04, plan v1.22, A282). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 17 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A278 to A286
- Decision: §1
- Rationale and evidence: the Architect's message of 17 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-12, INV-22, INV-30; AGENT-13, AGENT-14, AGENT-15, AGENT-29; REQ-API-001, REQ-SEC-004, REQ-EXP-002, REQ-EXE-005, REQ-EXE-006, REQ-RCV-002, REQ-OPS-003; SoT §0.4
- Migration notes: A278's in-place change and A284's enum change are minor contract changes in place while no tag exists (AGENT-15), C1's; A280's migration is 0030, C1's, numbered on C1's ledger; A282 is plan v1.22
- Supersedes: see the Supersedes row above

## 1. The rulings, exactly as given

| Ruling | Text | Supersedes or changes |
|---|---|---|
| **A278** (interim) | **Facts by value, replacing A272's key list.** SR's rule is better. Every fact value must be one of: an ID that is exactly `<prefix>_<ULID>`, or a typed ID with a letter in its body; a resource reference whose body contains a letter; a string that passes the digit-run pattern. `request_id` is served masked, so it passes the pattern. A digits-only reference such as `fin.account:0123456789012345` is refused. `recev_1005` and `TX88213` stay valid. Merge noema#615 now as it stands (the core's serve-time mask covers the gap). The change follows as one small in-place pull request after #615 merges and before the `contracts-v1.0.0` tag. The tag waits for it. C1 uses the fixtures C1 listed. SR's 36-key list is the checking inventory. | **Replaces** the key-list sentence of **A272** ("only the free-text keys get the digit pattern; references and IDs do not"). The rest of A272 stands. Adds a condition to the tag (**A203**, A272). |
| **A279** (interim) | **A270 text (money).** Money is rendered by the core from integer minor units only. It is exempt from the digit-run rule if and only if the whole string matches `^[A-Z]{3} [0-9]{1,3}(,[0-9]{3})*(\.[0-9]{2})?$` with at most 9 integer digits. Ungrouped digit strings, more than 9 integer digits, and a wrong prefix or decimals stay refused. Negative vectors cover each. It goes in as named vectors in the A259 shared file. It is Tier 1 (Codex, SR, EL, Founder). SR challenges that no 9-digit grouped string can carry an identifier. The core never renders an identifier through the money renderer. | **Restates A270** as its final text (adds the "if and only if the whole string" rule and the negative vectors). |
| **A280** (interim) | **noema#658 and tenant row security.** Keep #658 as a catalog guard. Its two exception lines are the tracked gap, closed by the migration pull request (0030). A273 stands. Codex's P2 is accepted as tracked under DEBT-43 (owner C1). REQ-SEC-004 is not Done until 0030 merges. The G0-N checklist says so. Codex marks the P2 as "accepted by ruling", so #658 does not hold up G1. | Confirms **A273**. Opens DEBT-43. |
| **A281** (interim) | **Part list.** EL derives the seven parts mechanically from the answer contract's text-bearing members. A test fails if the list and the contract differ. If the contract has a summary member, EL adds it. No sentences until the Founder and a native speaker supply wording (REQ-EXP-002). | Follows **A271**. Note: A250 waived native-speaker review for the POC (DEBT-39); A281 holds wording back until the Founder and a native speaker supply it. The two are read together: no sentence is written by an agent. |
| **A282** (interim) | **Worker task ID.** The Steward registers the worker as the next free ID in the STM family. EL's noema#660 cites that ID, replacing the WRK-01 that the trace check refuses. | Nothing committed. Registered as **STM-04** in plan v1.22 (change request CR-2026-11-17-A282-worker-task-row). |
| **A283** (interim) | **YAML checks (noema#622, #629).** Stop line-scanning YAML; each round finds a new bypass. SR checks whether a YAML parser is already a dependency in `tools/ci`. If so, use it and refuse any file it cannot load. If not, SR files an [OPEN] entry under AGENT-14 proposing PyYAML. The Architect approves the proposal in principle, and the Founder approves the entry. #629 also has a merge conflict, so SR merges main in the same push. | Nothing committed. No dependency is added by this record (AGENT-14). |
| **A284** (interim) | **noema#653.** The explicit AGENT-15 OK: while no tag exists, additive enum members go in place as a minor. The enum is 20. The test's "21" wording is wrong and C1 fixes it. | Applies the corrected count of **A254** (20) and the no-tag rule for in-place minors (as A258 and A275). |
| **A285** (interim) | **noema#654.** The code follows the documented exit meanings. If the doc is silent on `--dry-run`, it exits 0 and the doc says so. | Nothing committed. |
| **A286** (interim) | **Wiring.** EL is the bottleneck for wiring, so C2 wires its own adapters (noema#661 and #663) into the core in a separate file, `cmd/core/wire_understanding.go`. EL reviews that pull request and keeps the Trust adapter, worker, route and SSE. This amends C2's allowlist for that one file only. | Amends C2's allowlist for `cmd/core/wire_understanding.go` only (REQ-AGT-002). Nothing else. |

## 2. What the Steward did where the rulings are silent

- **A282.** The worker is registered as **STM-04** in plan v1.22 with a change request. The ruling gave the family, not the date, Needs or done-when: the Steward's defaults are the day of EXE-06 (2026-11-18), Needs STM-01 and EXE-06 (a Need must appear earlier in the plan, so the row sits after EXE-06), the owner EL and the card's own acceptance criteria. It joins the G2 review row GOV-11 Needs. Whether it must land before the G1 run is the Architect's to say. EL is told on noema#660.
- **A280 and REQ-SEC-004.** REQ-SEC-004 is not Done until migration 0030 merges. DEBT-43 records it. G0-N checklist row 11 (docs#196, not yet merged) already reads "partly shown"; its text is to be amended to name DEBT-43 and 0030 in the next pull request that touches that file, after docs#196 merges, so that Codex's read of docs#196 is not disturbed.
- **A283.** The Steward adds no dependency. If SR files the PyYAML [OPEN] entry, the Founder approves it there.
- **A277's readers and A286.** Not read by the Steward.
- **Next free ruling: A287.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A277 (A253 to A277 in docs#196) | |
| This record | A278 to A286 | **A287** |
