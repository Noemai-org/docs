# DEC-2026-11-16 · Architect rulings A242 to A252 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect on 16 Nov 2026, relayed to the Repo Steward, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 16 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Eleven rulings, A242 to A252 (§1). A251 and A252 are the texts of A237 and A238. |
| **Closes** | The questions on noema#617 and #601 (A242, A243), C1's questions (A244), the evidence mapping (A245), the redactor (A246), the relay hold (A247), the Tushe delta (A248), Intron's key and dependency (A249), the small answers (A250), and the texts of A237 and A238 (A251, A252). Closes OD-P-94 (A252). |
| **Supersedes** | Per ruling, in §1. In short: A242 changes one line of **A234** (`conversation_ref`); A251 and A252 are the content that **A237** and **A238** pointed to. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 16 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A242 to A252
- Decision: §1
- Rationale and evidence: the Architect's message of 16 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-12, INV-21, INV-22, INV-29; AGENT-14, AGENT-16, AGENT-29; REQ-API-001, REQ-SEC-003, REQ-ENV-005, REQ-VOI-001, REQ-UI-001; SoT §0.4
- Migration notes: A243's migration is C1's, numbered on C1's ledger (AGENT-15); A244's reason codes are an additive minor bump with a migration note
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A242** (interim) | **noema#617 and noema#601.** `conversation_ref` equals `investigation_id` (no new prefix, no contract change). Public routes answer with `errors.v3`. Core-minted `<prefix>_<ULID>` IDs are exempt from the digit rule (A184 and A193). Tests use `ten_` tenant IDs. | The `conversation_ref` line of **A234** ("the same ULID with its contract prefix"): it now equals `investigation_id`. |
| **A243** (interim) | **The investigation route.** The handler reads through a read-only method of the orchestrator's store. A migration adds `principal_ref` to the investigation (set at Start), so the route can refuse another principal. C1 assigns the next number on the ledger. The map from 21 states to 6 stages is EL's table with a test that every state is covered. | Nothing committed. It applies **A207** and **A211** (the six stage values). |
| **A244** (interim) | **C1's questions.**<br>• Add three reason codes, additive minor bump: `TARGET_FROZEN`, `CLOCK_BREACHED_UNROUTED`, `DISPATCH_BUDGET_EXHAUSTED`.<br>• No `CONFIRMATION_SPENT` event type in the POC. The spend is visible on `DECISION_MADE` and `GRANT_ISSUED`.<br>• noema#600's narrowed `/raw_status` exemption is confirmed.<br>• `reconstruction.v3` is for the operator and auditor UI only. | Nothing committed. The third bullet confirms a narrowing of the exemptions of **A231**. |
| **A245** (interim) | **Evidence mapping.** `required` defaults to true. `reconciliation_id` is deterministic: a hash of tenant, intent, rule-set version, mapping version and the sorted item hashes (INV-21). | Nothing committed. It answers the questions on noema#579 (**A219**). |
| **A246** (interim) | **The redactor.** The model-service redactor must adopt the wide separator set before any live provider call. C2 replaces the test that pins the narrow behavior (allowed by A231). | Nothing committed. It applies **A231** and **A194** to the model service. |
| **A247** (interim) | **Relay hold.** The bench hold is 15 s, above Tushe's 12 s. | Nothing committed. It sets the number behind **A240** ("our receiver holding the response past 12 seconds"). |
| **A248** (interim) | **Tushe delta v1.3.** The Steward drafts `tushe-spec-delta-v1.3.md` adopting the addendum's routes exactly. It unblocks BO's reader and IL's proxy entries. | Nothing committed. It is the delta that `DEC-2026-11-16-tushe-addendum-od-p-67` said adoption of the addendum needs. |
| **A249** (interim) | **Intron.** The API key comes only from a file mount (`INTRON_API_KEY_FILE`, a 0600 file), read by the model service only, with a netcheck rule. The `websockets` dependency is approved. There is no replay to a second provider (noema#630 closed): failover means degrade to text. | Nothing committed. It applies **A241** and approves one dependency under AGENT-14. |
| **A250** (interim) | **Small answers.**<br>• Native-speaker review is waived for the POC (your earlier decision), so noema#595 merges after A155. A debt note records it.<br>• The scorecard view for the UI is a new `scorecard-view.v1` that BO defines (aggregates only, no case or oracle refs). C1 adds its root.<br>• `MOCK_CASE` is accepted as criterion 6's plan source. | Nothing committed. The first bullet waives the native-speaker dependency (REQ-EXP-002) named on noema#595. |
| **A251** (interim) | **A237 text (the Steward asked).** The core sets `done.verified` true only with at least one verdict and all ACHIEVED. It sets `case_ref_masked` only after `case_opened` is ACHIEVED. The UI renders what it receives and never derives either. EL tests it in the answer builder. | The content of **A237** ("noema#611 as in §3"). |
| **A252** (interim) | **A238 text.** Approve `@axe-core/playwright` 4.14.0 (`axe-core` ~4.14.0), pinned with a lockfile, local scan only. It is a test-only dependency under MPL-2.0 (file-level terms, unmodified). The Steward records it. | The content of **A238** ("the axe approval as in §3"). It closes **OD-P-94**. |

## 2. What the Steward did where the rulings are silent

- **Reader tables.** The message says they are in its "§6"; the Steward received no §6 in it. None is recorded and none is invented.
- **G0-N table.** The message asks the Steward to update the G0-N checklist "with the table in this message"; no table came through. The G0-N lines are not changed.
- **A252 and OD-P-94.** The approval is exactly the default proposed in OD-P-94 (docs#189): `@axe-core/playwright` 4.14.0 with `axe-core` ~4.14.0. OD-P-94 is closed by this record when both merge; its entry is updated in docs#189.
- **A249's dependency.** `websockets` is approved without a version in the ruling; the exact pin and lockfile are Voice's, as D2 of the UI dependency record requires for pins, and are read by the Security Reviewer.
- **Debt to register (next debt pull request):** the native-speaker waiver of A250 (owner Voice and the Founder; removal: a native-speaker review of the changed sentences before the pilot) and the BO follow-up of A235 (a generated switch-timeout case). Numbers are assigned there.
- **A248** is a separate pull request (the delta file); it changes no frozen file.
- **Next free ruling: A253.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A241 (merged) | |
| This record | A242 to A252 | **A253** |
