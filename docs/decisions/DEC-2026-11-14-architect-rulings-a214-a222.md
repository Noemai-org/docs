# DEC-2026-11-14 · Architect rulings A214 to A222 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect on 14 Nov 2026, relayed to the Repo Steward, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 14 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Nine rulings, A214 to A222 (§1). Each states what it supersedes. |
| **Closes** | The masking gap and the second push on noema#521 (A214); the place of the real-stack RunWrite tests (A215); the review questions on noema#576 (A216) and the Executor adapters of noema#593 (A217); the Trust intake questions (A218); C2's design questions on noema#580, #583 and #579 (A219); the review of noema#591 (A220); the response limit of the model service (A221); the reader rule (A222). |
| **Supersedes** | Per ruling, in §1. In short: **A215 amends A210** (the Architect says A210 was wrong); A214 allows a second push that A211 ("one push") did not. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 14 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A214 to A222
- Decision: §1
- Rationale and evidence: the Architect's message of 14 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-07, INV-12, INV-22; AGENT-14, AGENT-16, AGENT-29; REQ-SEC-003, REQ-STM-001, REQ-TRU-001, REQ-API-001; SoT §0.4; PERD §13
- Migration notes: none by this record
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A214** (interim) | **noema#521.** Cap `policy_version` at 4 digits in total. EL pushes once now. The re-reads are cheap, and it closes a real masking gap. | The "one push" limit of **A211** for noema#521: one further push is allowed, now. Nothing else. |
| **A215** (interim) | **A210 amended.** My A210 was wrong. The lint refuses an `execution/` test that reaches `outcome/`. The real-stack RunWrite tests stay in `adapters/outcome_e2e`. No lint change. | **A210** (recorded in the A209 to A213 record): its statement that the tests live in `services/core/execution/e2e`. The Architect says A210 was wrong. |
| **A216** (interim) | **noema#576.**<br>• The recovery count is derived from the Record (the recovery events for that investigation), never from a caller argument. Its limit is data, cited from the PERD default.<br>• An exhausted run ends in `HANDED_TO_TEAM` through the existing arrow. If no such arrow exists, EL files a change request and doesn't invent one. An unspent grant expires by TTL.<br>• `PARTIALLY_ACHIEVED` stays as built. A new grant needs a fresh Trust evaluation, never an automatic retry. A test proves the new evaluation sees the partial state.<br>• A spent budget becomes its own receipt class that stops and escalates. C1 adds it as a follow-up. | Nothing committed. It settles the review of the write path of **A204** (RunWrite). |
| **A217** (interim) | **Executor (noema#593).** EL's adapters in noema#576 stand. C1 reviews them as owner of the package behind the port, then adds the budget class as a follow-up PR. | Nothing committed. It accepts EL's Executor adapters as built; **A188** says each port is implemented by the owner of the package behind it, and this ruling is the exception for these adapters, with C1 as reviewer. |
| **A218** (interim) | **Trust.**<br>• The T10 split is accepted provisionally: seven settled classifications pass, and five fail closed (contradiction, unknown outcome, possible duplicate, uncertain order, insufficient evidence).<br>• The freeze check on the plan lands at T14 with noema#572.<br>• TRU-14 stays in the G2 Needs. | Nothing committed. It answers the T10 and T14 questions of the Trust assembly (**A205**) and Voice's question on docs#177 (TRU-14 in the G2 Needs): plan v1.20 stands. |
| **A219** (interim) | **C2's design questions.**<br>• **noema#580:** `intent_id` is derived from a hash of tenant, correlation and request ID. `created_at` is `received_at`. `raw_ref` is the unset marker that the core overwrites.<br>• **noema#583:** lexicon shape accepted. `PipelineInput` gets `received_at`.<br>• **noema#579:** closed lookup for enumerations. Derived states use `internal/predicate`. The pack's names are authoritative, and C2 corrects the G-B example in the runner's data file. | Nothing committed. |
| **A220** (interim) | **noema#591.**<br>• A foreign-tenant token gets 401 `SESSION_INVALID`, and a wrong-role session gets 404. SR's criterion 9 wording is amended to say so.<br>• The seed, cost and latency integer fields are exempt as number-typed fields under A154. | The wording of **the Security Reviewer's criterion 9** (of the G1 evidence criteria): amended as stated. |
| **A221** (interim) | `NOEMA_MODEL_MAX_RESPONSE_BYTES` is 65536 in the bench profile. IL adds it to the core service in noema#568, with the drift test. | Nothing committed. It supplies a limit (AGENT-16: agents set no limit; this ruling does). |
| **A222** (interim) | **Reader rule.** Reads under the shared account count. The reader assignments are in §6. | Nothing. It confirms how **A208** reads "Codex READY" and extends it to reads in general. |

## 2. What the Steward did where the rulings are silent

- **A222 points to "§6" of the Architect's message, and A213 pointed to "§5". Neither section was given to the Steward.** This record carries no reader table. The Steward searched noema#183 and the pull requests for it and found none. **The Architect is asked to post §5 and §6 on noema#183 (or give them to the Steward)**; the Steward commits them in a note on this record or the next one. The Steward invents no assignment.
- **A215 and the record of A210.** A210 is recorded in `DEC-2026-11-14-architect-rulings-a209-a213` (docs#178, open when this record was written); this record names A210 by text and amends it by A215. If docs#178 merges first, A215 reads against it; if not, A210 is committed with its amendment already on record.
- **A220 and the SR criterion.** The Steward does not edit the Security Reviewer's criteria or the G1 evidence template (noema#566); the owners (SR, BO) amend the wording on their pull requests. The Steward records the ruling.
- **A216, last bullet, and A217.** The budget receipt class is a follow-up of C1; no task row is added by this record (a follow-up PR under STM-01 and EXE tasks). If the Architect wants a row, plan v1.22 carries it.
- **A218.** TRU-14 stays in the G2 Needs as plan v1.20 has it; no plan change.
- **Next free ruling: A223.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A208 (A199 to A208 in docs#176, merged); A209 to A213 in docs#178 (open) | |
| This record | A214 to A222 | **A223** |
