# DEC-2026-11-14 · Architect rulings A209 to A213 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect on 14 Nov 2026, relayed to the Repo Steward, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). **A209 needs a separate Founder approval of the pack edit it asks for (A155); this record does not give it.** |
| **Date** | 14 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge and the A155 approval) |
| **Decides** | Five rulings, A209 to A213 (§1). Each states what it supersedes. |
| **Closes** | The FactsSource blocker (A209); the question where the real-stack RunWrite tests live (A210); the review of noema#521 (A211); the body limit asked on noema#577 and the four decisions of EL's EXP/Evidence work (A212); the reader assignments (A213). |
| **Supersedes** | Per ruling, in §1. In short: A209 changes who writes what in **A206** (and keeps A155's rule that the pack edit needs one Founder approval); A211 adopts **A207**'s stage values without EL's option to change one. |
| **Amends** | Nothing in the SoT, the PERD or the plan. The task row that noema#521 lacks goes through plan v1.21 (§2). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111); A209's pack edit needs its own Founder approval (A155)
- Date: 14 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A209 to A213
- Decision: §1
- Rationale and evidence: the Architect's message of 14 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: REQ-EXP-001, REQ-STM-001, REQ-API-001, REQ-INP-002, REQ-SEC-003; INV-02, INV-12; AGENT-15, AGENT-16, AGENT-29; SoT §0.4; PERD §13, §39.1
- Migration notes: none by this record. The `errors` bump of noema#521 follows AGENT-15 (A207)
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A209** (interim) | **FactsSource.** EL cannot build it, because no template has any `{fact:<kind>}` slot and the EXP-01 pack edit needs the Founder's approval (A155).<br>• **C2 owns the slot inventory.**<br>• C2 writes the pack template edit and a table of each fact kind with its Record source (event and field), from PERD §13 and the US-01 and US-06 answers. C2 posts it within the hour.<br>• The Founder's approval (A155) unblocks it.<br>• EL builds FactsSource only from that inventory. A slot with no source makes the explanation refuse. | The division of labour of **A206** ("EL builds it slot by slot from the EXP-01 template slots"): C2 now writes the inventory and the template edit, and EL builds only from the inventory. A155's rule that the pack edit needs one Founder approval stands; A206's "a slot with no source makes the explanation refuse" and "EL invents no mapping" stand. |
| **A210** (interim) | **e2e fixture.** No lint rule or guard changes. The real-stack RunWrite tests live as test files in `services/core/execution/e2e`. C1 confirmed that this passes lint. EL writes them there. | Nothing. It places the tests of **A204** (RunWrite). |
| **A211** (interim) | **noema#521.**<br>• Adopt A207's six stage values.<br>• The Go side enforces through `record/payloadguard` (A194) on outbound edge responses. Remove the RE2 claim.<br>• Bound the digits in `option_id`.<br>• One push. | **A207**'s latitude for EL to change a stage value with a stated reason: the six values are adopted as proposed. Nothing else. |
| **A212** (interim) | **Small calls.**<br>• `NOEMA_MAX_BODY_BYTES` is 16384. The canonical input text is at most 2000 characters. Worst-case JSON escaping at 6 bytes each is 12,000, plus under 1 KiB of envelope.<br>• noema#565 (EL's four decisions): use the verified-session resolver, the text and Mode 1 defaults, and the pack's required-slot rules. EL answers C2 now. | Nothing committed. It supplies the number that noema#577 says no approved figure exists for. |
| **A213** (interim) | **Reader assignments.** The rest of the PRs are in §5. | Nothing. |

## 2. What the Steward did where the rulings are silent

- **A213 points to "§5" of the Architect's message.** That section was **not given to the Steward**: the Steward has the sentence above and nothing after it. This record therefore carries no reader table. **The Architect is asked to post §5 on noema#183 (or give it to the Steward)**; the Steward commits it in the next record, or in a note on this one.
- **A209 needs a Founder approval that is not given here.** A155 says the pack edit needs one Founder approval. The Steward records the ruling and the approval the Architect asks for; it does not treat the approval as given. The Founders approve on C2's pull request when C2 posts the template edit.
- **A212's number.** 16384 = 12,000 (2000 characters at 6 bytes each) plus an envelope of under 1 KiB (1024); 13,024 fits. The value is a Founder-held limit under AGENT-16: agents set no limit, and only this ruling gives it. noema#577 carries it as data.
- **noema#521 has no task row** (EL says so, AGENTS §14; the Architect gave the Steward this item). It goes into plan v1.21, written after plan v1.20 (docs#177) merges so two plan versions are not started from v1.19. The proposed row is in the change request that pull request carries.
- **No other task row is added.** A209's slot inventory and pack edit fall under the EXP work already planned (C2); FactsSource under STM-03 (EL); A210's tests under STM-03 and EXE.
- **Next free ruling: A214.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A198 (A193 to A198 in docs#172); A199 to A208 in docs#176 (open) | |
| This record | A209 to A213 | **A214** |
