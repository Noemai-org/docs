# DEC-2026-11-14 · Architect rulings A199 to A208 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect on 14 Nov 2026 (A199 and A200 on the Founder's decision), relayed to the Repo Steward, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 14 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Ten rulings, A199 to A208 (§1). Each states what it supersedes. |
| **Closes** | The three questions on noema#536 (A201); the review questions on noema#535 (A202); the contract fix noema#543 (A203); the write-path design of the orchestrator (A204); the Trust plan questions (A205); the explanation facts source (A206); the public contracts of noema#521 (A207); the small calls on noema#540, #554 and #555 and the meaning of a Codex READY (A208). |
| **Supersedes** | Per ruling, in §1. In short: A199 suspends the work-in-progress limit for one day; A200 replaces the G1 wording of A188 (applied in a separate pull request, see §2); A201 drops C1's stricter local fix. |
| **Amends** | Nothing in the SoT, the PERD or the plan by this record. The G1 wording and the new task rows go through plan v1.20 (§2). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 14 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A199 to A208
- Decision: §1
- Rationale and evidence: the Architect's message of 14 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-12, INV-21, INV-29; AGENT-15, AGENT-29; REQ-SEC-003, REQ-AUD-001, REQ-STM-001, REQ-TRU-003, REQ-EXP-001; SoT §0.4; PERD §39.1
- Migration notes: A203 is a minor schema bump of `common.v1.json` with its own migration note and regenerated models, made by the owners in noema#543 (AGENT-15). None by this record
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A199** (interim; the Founder's decision) | **WIP limit.** Lifted for today for G1-lane PRs. | The limit of at most 4 open pull requests per driving founder, at most 2 of them P0 (plan §5; AGENTS §3, step 3), **for G1-lane pull requests, on 14 Nov 2026 only**. Nothing else. |
| **A200** (interim; the Founder's order) | **G1 record.** The wording below replaces "BLOCKED, no date". G0 is held today with Tushe. The wording: "G1 OPEN. Founder target 14 Nov 2026. Not yet run. Result recorded only at the review, from evidence. Counts only after G0." | The G1 wording of **A188** ("BLOCKED, no date", recorded in `DEC-2026-11-13-architect-rulings-a183-a192`, §2). |
| **A201** (interim) | **noema#536.**<br>• Application-only enforcement.<br>• No bound inside exempt IDs.<br>• No size cap.<br>• Implement A193 as written (one token of at most 64 characters, no space, at `/external_ack` and `/target_ref`). The stricter local fix is dropped, because it could refuse a real receipt and turn it into an unknown outcome.<br>• C1 pushes now. #531 is merged, so merge `main` and drop the duplicate gateway commit. | Nothing committed. It answers the three calls on noema#536 and confirms **A193**. C1's stricter local fix for `/external_ack` and `/target_ref` is dropped. |
| **A202** (interim) | **noema#535.**<br>• A first-use probe per pool: refuse a superuser or a `record_verify` member.<br>• No file-mode check, because Compose secrets are 0444.<br>• Bench profile defaults live in IL's Compose config as data: pool max 4, connect timeout 5 s, statement timeout 10 s. They are labelled bench-only, and production values go through an [OPEN] entry.<br>• Refusing `sslmode=disable` outside the bench profile is a later hardening task, tracked. | Nothing committed. It settles the review of the pool code of **A170** (OD-P-82). |
| **A203** (interim) | **Contract fix (noema#543).** Correct the two definitions in place in `common.v1.json` as a minor schema bump. It widens the key pattern and adds `ClientRequestId`, which is additive under PERD §39.1. It carries a migration note and regenerated models. No `common.v2`, because it would touch 66 schemas. | Nothing committed. It chooses the form of the contract fix that **A193** asked for. |
| **A204** (interim) | **RunWrite.** The investigation state is a projection and the Record is the truth. The runner records EXECUTING after Execute returns, reads GRANT_SPENT and DISPATCH_ATTEMPTED from the Record, and resumes from the Record after a crash. Grants keep being issued with the decision, with no planner caller in the POC. A test covers a crash between those steps. | Nothing committed. It sets the write-path design of the composition task of **A188** (STM-03). |
| **A205** (interim) | **Trust plan.**<br>• **Q1:** the values come from the PERD: AT_RISK is remaining under 25% (PERD line 2126), the auto-resolve margin is 0.35, the absolute floor is 0.70, and there are at most 4 options. They go in as pack data, provisional per GOV-06.<br>• **Q2:** follow D8.<br>• **Q3:** an empty plan with its hash.<br>• **Q5:** add Role to `orchestrator.Session`.<br>• **Q4 (TRUST_REFUSED event):** approved, but sequenced after the G1 run, because it isn't on the US-01 or US-06 path. It is a named task, not dropped. | Nothing committed. |
| **A206** (interim) | **FactsSource.** EL builds it slot by slot from the EXP-01 template slots, sourced from the Record: the admitted intent, evidence statuses, the classification, and the receipt and verdict. A slot with no source makes the explanation refuse. EL invents no mapping. | Nothing committed. |
| **A207** (interim) | **noema#521.**<br>• The public stage enum has 6 values, proposed as `understanding`, `needs_input`, `needs_confirmation`, `working`, `answered`, `unavailable`. EL may change a value with a stated reason.<br>• One not-found shape.<br>• `case_ref_masked` is the masked form with at most 4 digits. The core masks it before it reaches the client, and the raw reference never leaves.<br>• The errors bump goes in as part of the push. | Nothing committed. It fills in the shape that **A187** fixed (at most six stage values, one not-found shape, `errors.v2`). |
| **A208** (interim) | **Reviews and small calls.**<br>• Codex READY means the Codex role's comment at the head. Reviews posted under the shared account count.<br>• noema#554's limits are a hard ceiling: configuration can lower them but never raise them.<br>• noema#540 fixes `tier2.false_block` (it omits `failure=True`) and the publication check (still using 3/n) in one push.<br>• The evidence mapping from source payload to rule-set fields is versioned pack data. C2 owns it and EL reviews. Classify first, then seal (A3).<br>• The mTLS design on noema#555 is accepted. IL does Docker and Compose, and EL does the core client. It is on the G1 path, because the compile route can't be wired without it. | Nothing committed. The meaning of "Codex READY" settles how the Codex gate of **A143** is read; the limits of noema#554 are those of **A191** (32,000 bytes, 16 kHz), now a ceiling. |

## 2. What the Steward did where the rulings are silent

- **A200 is applied in a separate pull request.** The new G1 wording goes into the G1 gate record and plan v1.20 in one pull request (the Founder's order), with its own short record. This record carries A200 as given and changes no gate file.
- **A205, Q4 (TRUST_REFUSED) and the "tracked" hardening of A202 have no task row today.** Plan v1.20 gets a row for TRUST_REFUSED (proposed ID TRU-14, owner and date are Steward defaults, after the G1 run), and A202's `sslmode=disable` hardening is entered as a debt row in the next debt pull request. The Steward invents nothing else.
- **PERD line 2126.** In the current PERD (v1.23) the `AT_RISK` value sits at that line; in v1.24 (proposed) it is line 2146. The value is marked `[REC]` there and stays so until a decision record adopts it; A205 makes it provisional pack data per GOV-06, so it is tracked as an OD-P entry by task GOV-06. The margin 0.35 and the floor 0.70 are the SoT and `[ADOPTED DEC-2026-10-17]` values.
- **A202, production values.** The bench defaults are bench-only. The production values are an [OPEN] entry to be filed by IL when they are first needed (AGENT-02); nothing in this record sets one.
- **A203 and A193.** The two contract defects that A193 sent to "one contract-fix pull request" are the same two as here. noema#543 is that pull request; the Steward adds no contract.
- **Merged since the rulings were given.** noema#531 and noema#535 are merged (read on GitHub on 14 Nov 2026). A201 says "#531 is merged", which holds. A202's review of noema#535 now applies to what merged and to any follow-up.
- **A208, "Codex READY".** Where this record or a Status line says "Codex READY", it means the Codex role's comment at the head, posted under the shared account. The Steward counts it the same way.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A198 (A193 to A198 in docs#172) | |
| This record | A199 to A208 | **A209** |
