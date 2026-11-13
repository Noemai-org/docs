# DEC-2026-11-13 · Architect rulings A183 to A192 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect on 13 Nov 2026, relayed to the Repo Steward, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 13 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Ten rulings, A183 to A192 (§1). Each states what it supersedes. |
| **Closes** | The questions on noema#505 (A183), noema#515, #457, #468 and #492 (A184), noema#522 (A185), noema#511 (A192). |
| **Supersedes** | Per ruling, in §1. In short: A186 replaces the index specification of A172; A184 overrules two proposals (C1's limit of 10, C2's masking when served). |
| **Amends** | Founder decision D14 (route spelling, A183; its own record: [DEC-2026-11-13-d14-route-spelling](DEC-2026-11-13-d14-route-spelling.md)). Nothing else in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 13 November 2026
- Closes: noema#505, #515, #457, #468, #492, #522, #511 (the questions)
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A183 to A192
- Decision: §1
- Rationale and evidence: the Architect's message of 13 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-07, INV-12, INV-29; AGENT-14, AGENT-15, AGENT-29; REQ-SEC-003, REQ-AUD-001, REQ-VOI-003, REQ-API-001; SoT §7, §0.4
- Migration notes: none by this record. Migration 0027 stays reserved (A186). A187 bumps `errors` to v2 and A190 bumps the scorecard to v3 (the owners' pull requests, AGENT-15)
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A183** (interim) | **D14 route spelling (#505).** Use the segment form `/versions/{v}/publish`, with the D14 amendment recorded in a decision record. SR, C1 and I agree. | The spelling `/versions/{v}:publish` in Founder decision D14 (OD-P-79), SEC-04's control-plane matrix row 5 and PERD §39.4. See [DEC-2026-11-13-d14-route-spelling](DEC-2026-11-13-d14-route-spelling.md). |
| **A184** (interim) | **Masking and the Record (#515, #457, #468, #492).**<br>• Masking belongs to the write path. Producers mask before the append. The Record appender refuses any payload string holding a digit run longer than 4, except by type: typed IDs by contract shape, RFC 3339 timestamps, and number-typed fields (A154).<br>• C1's proposed limit of 10 is rejected. The limit is 4.<br>• An `object_ref` is always core-minted, never built from a client value.<br>• The hashed `events` array is served as stored, only after the append guard lands. Until then it is audit and ops only, and no UI or arm reads it.<br>• One masking definition lives in `masking-limits.v1`: all Unicode digits and the wider separator set from #492. #457 and #468 adopt it.<br>• Stored history is never rewritten. A CI scan covers every test Record.<br>• C2 proposed masking when served. I overrule it, because the Record is hashed and cannot be edited later. | Nothing committed. It refines A154 (4 on every outward surface) and A162. It overrules C1's limit of 10 and C2's masking when served (proposals on noema#515 and #492). |
| **A185** (interim) | **Complaint creation (#522).**<br>• `log_complaint_reference` stays undispatchable until the target creates conditionally and atomically.<br>• mock-case is our own component, so IL adds an atomic conditional create (unique on case and epoch), which keeps scope. C1 then restores the mapping with a concurrent "exactly one" test.<br>• US-06 (silent success, PERD line 1656) is about the case create, not the complaint, so this costs G1 nothing.<br>• A human escalation never counts as a pass of anything. | Nothing committed. It decides the question on noema#522 and replaces C1's proposed default there (the capability stays undispatchable and US-06 ends with a human escalation). |
| **A186** (interim) | **Trust decision idempotency, replacing A172's index spec.**<br>• Decide is a pure function of its inputs. The lookup key is the full deterministic tuple: tenant, `intent_id`, `intent_hash`, context snapshot and policy version. Same inputs return the stored decision and append nothing.<br>• A re-evaluation with new evidence has a new key, so WAIT and CLARIFY re-decisions stay legal.<br>• EL maps the key onto the real columns. If the key cannot be formed from existing columns, EL stops and asks. Migration 0027 stays reserved. | **The index specification of A172** (the lookup on `(tenant_id, intent_id, intent_hash)` and its unique index). The rest of A172 stands. It also fixes the lookup that A168 asks C1 to check. |
| **A187** (interim) | **Public API contracts (#521).**<br>• The client receives a small public stage enum (6 values or fewer), never the 21 internal states.<br>• FE owns the plain-language strings.<br>• There is one not-found shape. `TENANT_SCOPE_MISMATCH` is never shown next to `NOT_FOUND_OR_NOT_AUTHORIZED`.<br>• `case_ref_masked` shows 4 digits only.<br>• `errors.v2` gets a version bump for `details[].field` (AGENT-15).<br>• FE's UI treats "verified" as true only with at least one verdict and all ACHIEVED. | Nothing committed. |
| **A188** (interim) | **How G1 is proven.**<br>• Ownership. EL owns the US-01 and US-06 path through the core: composition and the orchestrator write path (EXECUTING, RECOVERING, OUTCOME_UNKNOWN). Each port is implemented by the owner of the package behind it.<br>• Understanding in the G1 run is a recorded-replay provider under `providers/`. It is selected by configuration in bench and test profiles only, and refused in the demo profile.<br>• Its recordings come from a real live compile run, stored as synthetic fixtures with provenance.<br>• The evidence is labelled "Understanding: recorded replay of live output".<br>• It needs an [OPEN] entry and your approval (AGENT-14).<br>• I chose replay because live model output differs between runs, and G1 requires two runs with identical decisions. | Nothing committed. It decides how Understanding is supplied in the G1 run; it does not change what G1 must show (plan §3.1). |
| **A189** (interim) | **Intent signature.**<br>• Trust checks that the recomputed `intent_hash` equals the hash in the signed `INTENT_ADMITTED` event, read through the admission reader (tenant, principal and correlation bound).<br>• This differs from SoT §7, which says the Intent Object is "signed by Understanding". A177 therefore stays interim.<br>• The SoT edit goes into v1.13 as its own PR, after the Intron change in v1.12. Until then the conflict (OD-P-85) stays open and G1 evidence says "signatures verified: no". | Nothing committed. It refines **A177** and **A166** item (1). |
| **A190** (interim) | **Scorecard.** Approve `exact_upper95` in scorecard v3 (AGENT-15 steps, thresholds unchanged). | Nothing. |
| **A191** (interim) | **Voice.**<br>• Cap STT frames at 32,000 bytes, 16 kHz mono PCM16 only, as configuration data.<br>• A missing per-token confidence is not a disqualification. It counts as low (VOI-03), is measured, and triggers the second-provider decision (OD-P-88) if G5 fails. | Nothing committed. It refines **A181** (a missing confidence counts as low). |
| **A192** (interim) | **#511.** A model repeating identity fields gets a metric and a log now. A Record event only if an existing kind fits. No contract bump before G1. | Nothing committed. It decides the point raised on noema#511 about **A166** item (3). |

## 2. What the Steward did where the rulings are silent

- **A171 to A175 are in the merged docs#159.** Confirmed: `DEC-2026-11-12-architect-rulings-a171-a175` is on `main`.
- **OD-P-85 and OD-P-86 reconciled.** A189 says the signature conflict is "OD-P-85". In the register OD-P-85 is the stranded-run resume (A168, A172) and **the signature conflict is OD-P-86** (the numbers moved when BO and FE took 83 and 84). The Steward applied A189 to OD-P-86 and A186 to OD-P-85, and changed no other entry's number.
- **A184 and the number 4.** "Longer than 4" is read as A154's maximum unmasked digit run of 4: a run of 5 or more is refused. The Steward did not restate which characters count beyond what A184 names (all Unicode digits and the separator set from noema#492).
- **A186 and A172.** A172's lookup key and unique index are replaced by A186. OD-P-85 now says so. No migration number is taken; 0027 stays reserved.
- **A188 and OD-P-92: approved by the Founder.** A188 says the replay provider "needs an [OPEN] entry and your approval (AGENT-14)". The Steward filed **OD-P-92** and does not approve a new component. **The Founder approved it in session on 13 Nov 2026** (the Founder's statement to the Steward, recorded here and in OD-P-92; it counts as committed once a non-author Founder merges this pull request, A111). The approval covers exactly the default in OD-P-92.
- **The task rows (A188 and the Architect's list).** [CR-2026-11-13-A188-task-rows](../poc/execution/change-requests/CR-2026-11-13-A188-task-rows.md) proposes six rows and records that EDG-02 stays with EL and is marked Done on the merge evidence of noema#496 (merged 13 Nov). The rows enter the plan in a new version after plan v1.18 (docs#166) merges; plan v1.18 carries EDG-02. The Steward writes no plan version in this pull request.
- **G1.** Recorded **BLOCKED, no date yet**, in `docs/poc/execution/gates/G1.md`, with a re-baseline template that has no date ([templates/gate-rebaseline.md](../poc/execution/templates/gate-rebaseline.md)). The gate did not run; nothing is pre-filled except the outcome the ruling names.
- **docs#168 (now merged).** The Architect's instruction was that the Founder commits the v1.12 SoT edit on that branch before any review; docs#168 merged with the SoT unchanged (SoT v1.11 on `main`), so A179 to A182 are still not in effect and the Founders decide when the v1.12 edit lands. The Steward pushed once to it, at the Founder's request, only to clear a README conflict. OD-P-88, 89, 90 and 91 are **adopted as written**. Their register entries are in docs#168; the Steward changes their Status line only after docs#168 merges, in a pull request that touches nothing else.
- **UND-05 and EXE-05 task notes: dropped.** `tasks.csv` is unchanged; the notes were never given in text and the CSV has no note column.
- **A189 and the SoT.** The Steward drafts the SoT v1.13 change for A189 in a separate pull request and edits nothing in the SoT.
- **Not done here (waiting on others).** The device holder (the Founder names it; noema#514). Closing noema#391 and #423 (after Codex's note). The retro reads on the governance issues (the Security Reviewer).
- **Numbering.** Next free ruling: **A193**. Next free OD-P: 93 (87 to 91 are in the merged docs#168, 92 is here; 83 and 84 stay with BO and FE).

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records (merged) | A41 to A178 | |
| docs#168 (merged) | A179 to A182 | |
| This record | A183 to A192 | **A193** |
