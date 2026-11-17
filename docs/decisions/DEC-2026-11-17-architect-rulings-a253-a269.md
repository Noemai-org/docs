# DEC-2026-11-17 · Architect rulings A253 to A269 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 17 Nov 2026, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 17 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Seventeen rulings, A253 to A269 (§1). The message headed them "A253 to A268" and then gave A269 (Codex); all seventeen are recorded. |
| **Closes** | The WIP-limit reading (A253), the reason-code and TRU-14 questions (A254), the Role in the capability check (A255), the Temporal test environment (A256), SEC-08 authorship (A257), noema#615 (A258), masking (A259), the evidence mapping and switch record (A260), noema#580 and #583 (A261), noema#565 (A262), the Tushe key scope and probes (A263), noema#643 (A264), binding (A265), TTS playback (A266), the Benchmark Owner's items (A267), the Intron URL test (A268) and the Codex rule (A269). |
| **Supersedes** | Per ruling, in §1. In short: A254 adopts and extends **A244**; A259 extends **A231**; A260 accepts **A245**; A261 follows **A219**; A267 confirms **A235**. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 17 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A253 to A269
- Decision: §1
- Rationale and evidence: the Architect's message of 17 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-07, INV-12, INV-21, INV-22; AGENT-14, AGENT-15, AGENT-29; REQ-API-001, REQ-SEC-003, REQ-ENV-005, REQ-TRU-001, REQ-VOI-001, REQ-UI-001; SoT §0.4, §43.2a
- Migration notes: A254's reason codes are an additive minor bump with a migration note, C1's (AGENT-15); A258 changes `reconstruction.v3` in place because nothing consumes it
- Supersedes: see the Supersedes row above

## 1. The rulings, exactly as given

| Ruling | Text | Supersedes or changes |
|---|---|---|
| **A253** (interim) | **WIP limit.** The limit is counted per agent role. Drafts do not count. The Steward keeps the count. Merging comes before opening. This is an interpretation the Founders can overrule. | Nothing committed. It is a reading of the plan §5 limit (at most 4 open pull requests per driving founder, at most 2 of them P0); the plan is not edited (a change is a new plan version). |
| **A254** (interim) | **Reason codes.** The four codes (`TARGET_FROZEN`, `CLOCK_BREACHED_UNROUTED`, `DISPATCH_BUDGET_EXHAUSTED`, `DECLINED_BY_APPROVER`) are adopted. The enum goes 17 to 21. The Steward writes the decision record. C1's contract pull request goes now. TRU-14 waits until after G1. | Adopts what **A244** proposed (three codes) and adds the fourth name. The text as given said 17 to 21; the Architect corrected it to **20** on 17 Nov 2026 (`DEC-2026-11-17-architect-rulings-a270-a277`; record `DEC-2026-11-17-reason-codes-a254`). |
| **A255** (interim) | **Capabilities.** `Capabilities.Check` carries the Role (the safer reading). | Nothing committed. |
| **A256** (interim) | **Temporal test environment.** `go.temporal.io/sdk/testsuite` counts as the "Temporal test environment" of PERD §36.1. No [OPEN] entry is needed. | Nothing committed. It is a reading of the PERD §36.1 row "Temporal test environment" and of AGENT-14. |
| **A257** (interim) | **SEC-08.** C1 authors SEC-08 and the Security Reviewer reviews it. | Nothing committed. |
| **A258** (interim) | **noema#615.** Fix `reconstruction.v3` in place before it merges: add a digit pattern, add `maxItems`, and widen the public digit pattern. Nothing consumes it yet, so there is no v4. The bundle gets two entry points: customer (four public contracts plus `errors.v3`) and operator (adds `reconstruction.v3` and `record-event.v3`). One push, which also merges main. | Changes the shape of **A244**'s third bullet only in that the operator entry point holds `reconstruction.v3`. |
| **A259** (interim) | **Masking.** The wide separator set is the one definition for the Record guard, the model redactor and the UI scan. Identifier-shaped codes stay exempt under A231. C1 owns one shared vector file, run by Go, Python and the UI. It is a fixture, not a contract change. It goes in after noema#636. | Extends **A231** (the Record guard's separators) to the model redactor and the UI scan; keeps A231's exemption. |
| **A260** (interim) | **Evidence mapping.** A245 and the noema#589 loader are accepted as built. A missing switch record is `UNKNOWN`, never `NOT_POSTED`. | Accepts **A245**; adds the missing-record rule. |
| **A261** (interim) | **noema#580 and the replay recordings.** noema#580 follows A219. The noema#583 lexicon shape is confirmed. Replay recordings go in `services/model/tests/fixtures/replay/` with a manifest and the label "Understanding: recorded replay of live output". | Follows **A219**. |
| **A262** (interim) | **noema#565.** C2's four recommendations stand. EL confirms in one line. | Nothing committed. |
| **A263** (interim) | **Tushe.** The key scope is as in the Steward's action 4. The docs#194 line that says "eight scopes" changes to "the key's scope list as created". The `/partner` refusal probe uses the runtime integration credential. Extra probes confirm that the read-only key cannot write (TEN-08a and TEN-08b). | Changes one line of the TEN-07b row (docs#194); no frozen file. |
| **A264** (interim) | **Session and CSRF (noema#643, interim).** The UI holds the session token in memory and sends it in the Authorization header. There is no cookie. The core also checks an Origin allowlist. Replay is covered by the idempotency key and by single-use confirmations. EL confirms on noema#643 what the middleware actually reads. | Nothing committed. |
| **A265** (interim) | **Binding.** The pull request that wires the compiler must refuse to start without mTLS, including when every setting is absent. noema#536's app-only guard stays, with a DEBT entry; its closing test: a direct `record_insert_t` call with a five-digit payload is refused. The noema#576 debt items (`ErrNotResumable`, `RECOVERY_REQUESTED`, the void loop) have owners EL and C1. No new spend event in the POC. The PERD amendment comes before G3. | Nothing committed. Debt entries: DEBT-40 and DEBT-41. |
| **A266** (interim) | **TTS playback.** TTS audio plays at the declared 48 kHz with no resampling. | Nothing committed. |
| **A267** (interim) | **BO (Benchmark Owner).** The switch-timeout case comes after G1. Synthetic audio uses Intron TTS as a labelled round trip, with no second vendor. The N10 reading is yes. `scorecard-view.v1` is frozen; new members arrive as minor versions. Held-out authoring (BEN-11 and BEN-28) belongs to the GOV-03 Benchmark Owner, starting this week. | Confirms **A235** (the switch-timeout case is a follow-up, not a gate condition; DEBT-38). Fixes the contract of **A250**'s `scorecard-view.v1`. |
| **A268** (interim) | **Intron URL test.** The Intron URL test stays strict. Voice drops the URLs from noema#625. | Nothing committed. |
| **A269** (interim) | **Codex.** Codex reads only changed heads. No more full sweeps. | Nothing committed. A working rule for the reviewer role. |

## 2. The WIP reading of A253 (for the plan §5 limit)

- **Counted per agent role**, not per driving founder. A role is one of the roles of the plan §4 staffing table (EL, C1, C2, SR, IL, B, V and the others).
- **Drafts do not count.** A pull request opened as a draft is outside the count until it is marked ready.
- **The Steward keeps the count**, and posts it on the merge board (noema#183). The count is a derived record; the pull requests are the evidence.
- **Merging comes before opening:** a role at its limit merges or closes one before it opens another.
- The reading stays interim and can be overruled by the Founders. The plan text of §5 is not edited; a change to the plan is a new plan version and a change request (plan §19). Until then A199's lift for G1-lane pull requests, ruled on its day, is untouched.

## 3. What the Steward did where the rulings are silent

- **A254's count.** The message said "four codes" and "17 to 21". `DECLINED_BY_APPROVER` was already one of the registry's 17 core codes (SoT §43.2a, since v1.2), so three codes are new and the enum goes to **20**. The Steward asked; the Architect confirmed 20 and said the 21 was his error (A270 to A277 record, preface). No registry or SoT edit is made here.
- **A263.** The `eight scopes` text of the TEN-07b line in the 16 Nov session file is changed in this pull request.
- **A253.** Counted from today's open pull requests only when the Founders ask for the count; no number is invented here.
- **A265 and A250 and A235** debt entries are DEBT-38 to DEBT-41 in this pull request (the debt register). The "PERD amendment before G3" (no new spend event) is a follow-up for the PERD v1.25 change request, owner EL; it is not a debt entry.
- **Not committed by this record:** the decisions on noema pull requests (#615, #580, #583, #565, #643, #625, #636, #536, #576) are the Architect's reviews of those pull requests; the owners act on them there.
- **Next free ruling: A278** (A270 to A277 are in `DEC-2026-11-17-architect-rulings-a270-a277`).

## 4. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A252 (merged) | |
| This record | A253 to A269 | |
| Next record | A270 to A277 | **A278** |
