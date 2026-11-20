# DEC-2026-11-20 · Architect rulings A358 to A453 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 20 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 20 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | The ledger A358 to A362 and A380 to A428 (§1), and the rulings A429 to A453 (§2). The rulings A363 to A376 are in `DEC-2026-11-19-architect-rulings-a362-a376`, A377 to A379 in `DEC-2026-11-19-founder-intron-data-terms-a377-a379`, and A384 to A388 in `DEC-2026-11-19-architect-rulings-a384-a388`; this record does not repeat them. |
| **Supersedes** | **A360 is replaced by A362** (as the ledger says). **A429 supersedes the force-push question.** **A447 corrects A345 S4** (and answers the question of `DEC-2026-11-19-architect-corrections-a371-a345s4`). **A430 corrects the earlier KILL_SWITCH instruction** (and states A400). **A410 states the correction to A371**: the reconstruction route is audit-only and ops use the panel route. **A448 answers** the PERD-version questions of the same record. **A449 confirms** the Steward's defaults. **A450:** noema#764 is closed because A363 supersedes it. Otherwise per ruling, in §1 and §2. |
| **Amends** | Plan v1.26 (the consent wording of VOI-06, VOI-08 and the demo pre-flight; the gate column of TRU-07 and TRU-12), by `CR-2026-11-20-A449-plan-v1.26`; `tasks.csv` (TST-02); the debt register (DEBT-54 to DEBT-56 confirmed). Nothing in the SoT or the PERD. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 20 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A358 to A362, A380 to A453 (less the ranges named above)
- Decision: §1 and §2
- Rationale and evidence: the Architect's message and ledger of 20 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-01, INV-02, INV-07, INV-12, INV-14, INV-20, INV-22; AGENT-09, AGENT-11, AGENT-12, AGENT-13, AGENT-15, AGENT-16, AGENT-27; REQ-TRU-002, REQ-TRU-009, REQ-TST-005, REQ-BEN-004, REQ-VOI-004, REQ-CTX-007; PERD §23, §32.2, §39.4; SoT §43.2a
- Supersedes: see the Supersedes row above
- Migration notes: A441 adds `principal_role` and `authn_ref` to the investigation row (a Tier 1 migration with a migration read; no number is assigned yet, §3); A438 bumps the evidence mapping to `fin.map.v1@2` with the manifest; A396 and A440 change the pack schema (the owners write the migration notes)

## 1. The ledger, as given

*The Architect's ledger lists most rulings in one line. They are recorded exactly as given. Where a ruling of A429 to A453 or an earlier record says the same thing, that is noted in §3, and the Steward changes no wording.*

- **A358** Diagnose compile run 44521380842 from the recordings first: per-call table (C2+SR); no dispatch before.
- **A359** Diagnostics: for a non-2xx reply record the status plus only validated error type/code/param; failure class for every call; never the message or body.
- **A360** (replaced by A362) Model move conditions.
- **A361** Failed calls are negative fixtures only; C2 confirms G-A..G-E cover US-01/US-06 or the run records their inputs; UND-15 infrastructure starts now.
- **A362** No agent uses Terra for anything; #775 closed; bench workflows never reference the terra harness.
- **A380** Baseline-run settings (bench values, args, no code defaults): STT final 20 s, response stand-in 1 s, TTS first audio 10 s, session 40 s, read_s/close_s/hold_s 2/1/5, concurrency 1, pause = max(2 s, minimum from Intron's published limit), budget 20 audio-minutes total.
- **A381** Voice route: Voice builds the model-service half after the baseline; EL builds the core-edge relay after G1; baseline calls adapters directly.
- **A382** Tier 2 voice PRs need Codex, CI and one Founder; no independent read.
- **A383** #767 updated to A377-A379; single Founder "start" stands.
- **A384 to A388** FE: poll-based UI-01; limits from contract bounds; reconnect refetch then 3 retries 1/2/4 s; parallel PRs; CI job for Playwright against the stack (under UI-04). *(Recorded in full in `DEC-2026-11-19-architect-rulings-a384-a388`.)*
- **A389** Commit status of rulings.
- **A390** PLT-09 approved by OD-P-99.
- **A391** DEBT-46 before G3 review.
- **A392** Packcheck fails any graph with uncovered required params (g3: case_id fact).
- **A393** No plan at T13; adapter asks the Planner.
- **A394** PackVersion from the manifest.
- **A395** CorrelationOf = snapshot's own, equal to the evaluation's.
- **A396** case_reasons: UPPER_SNAKE, meaning, no digits, packcheck membership.
- **A397** Pack can't answer a param -> packcheck fails.
- **A398** Runnable = preconditions AND depends_on postconditions AND edge conditions.
- **A399** DECLINE then superseded allowed; late DECLINE refused.
- **A400** KILL_SWITCH_* are SECURITY_EVENT kinds (corrects the earlier instruction).
- **A401** Slot params declare kind.
- **A402** caseverify package for the case read-back constructor.
- **A403** RecoverInvestigations design.
- **A404** INP-01: refuse terminal follow-up; no prior_intent contract change; deterministic rule; lazy void; no cap.
- **A405** UND-15 fixture form per SR's four conditions.
- **A406** POOL_REFUSED as a follow-up PR; screener refusal fails closed separately.
- **A407** Mapping rows case/complaint_ref required:false, mapping @2.
- **A408** Session extension by EL; #773 merges as is.
- **A409** G1 inputs are a new set exported by BO.
- **A410** Reconstruction route audit-only; panel route ops+audit (G2).
- **A411** A365 content hash (mapped facts) + A366 key.
- **A412** tenant-init one-shot + DB pin.
- **A413** document_hash on the publication row.
- **A414** #745 unchanged.
- **A415** #748 lock conditions.
- **A416** At-risk single source: pack trust_limits.json via trustlimits.
- **A417** ROLE:<role> = session role of that exact name.
- **A418** #756 requirements stand.
- **A419** produced_by removed.
- **A420** SEC-07 scope after G1.
- **A421** Package row 2 computed checks (US-06 / US-01).
- **A422** No BEN case for core-internal defects.
- **A423** .gitleaksignore class conditions.
- **A424** core-trust key generation/mount;
- **A425** policy-publish one-shot;
- **A426** pack dir layout;
- **A427** DEBT-46/SEC-09/TEN-08;
- **A428** request log and pinned canary.

## 2. The rulings A429 to A453, as given

### A429 (interim): History hygiene.

A PR whose history carries something that must not merge (a 33.9 MB binary, key-shaped test strings) is closed. It is reopened from a fresh branch with the clean tree. No history is rewritten, and no ignore line is added for strings in your own commits. That applies to #721 (EL) and #802 (SR) now. It supersedes the force-push question.

### A430 (interim): Kinds.

KILL_SWITCH_CLEARED and KILL_SWITCH_CLEAR_REFUSED are SECURITY_EVENT kinds (section 0).

### A431 (interim): #748.

A348 (committed in docs#210) governs. The session lock before BEGIN is the mechanism, because a SERIALIZABLE snapshot is taken at the first statement. Merge once SR is READY at the head.

### A432 (interim): #736.

ErrNoneCombined is right: none_option_id combined with any other selection is refused. Clarification.Open stays only with its contract and tests. C1 fixes the defect FE found.

### A433 (interim): #798.

- Customer SELF confirmation uses the customer entry point. confirmation-answer.v1 (request id plus response, no approver fields) is exported there. No customer page imports the approver entry.
- The path id must equal the body request_id. The route and the UI refuse a mismatch.
- Add a transitive-import test.

### A434 (interim): #783.

- A served tenant with no Record login is a deployment defect.
- It must fail /readyz, and a request gets 503 DEPENDENCY_UNAVAILABLE with fixed text. It is never 401 and never a raw 500.
- The principal id stays in the access line (a typed id).

### A435 (interim): T13 and #759.

- The binding field keeps the SoT name evidence_set_hash. Internally it is evidenceContentHash.
- The digest covers mapped facts with status included. Duplicates count once. The partial index is fine.
- #755 owns the Declined to REJECT mapping, and #759 drops its duplicate and rebases on #755.
- The REJECT decision is recorded (every decision is the Record's unit). #755's "nothing is recorded" test changes.
- #750 returns a NEW request when the open one is stale.
- #752 and #754 carry ApproverRoles from the session role.

### A436 (interim): A370.

#801 (C2) is the A370 work. RequestedCapability comes from the requested_remedy slot, so no mapping of the seven question types is needed. They drive write_when (A364). C1 stops that item.

### A437 (interim): Small adapter rulings.

- #788: a trust profile must have at least one evidence source (minItems: 1).
- #792: the internal class is SCREEN_NOT_RUN. The public error stays PROVIDER_UNAVAILABLE, so there is no contract change.
- #800: the narrow charge-0 rule comes after the run.
- #801: keep ErrStoredIntent.

### A438 (interim): Evidence mapping.

- Add a rows_from construct for list entities.
- A payload with a completeness marker (complete) means "no case" only when marked complete. Otherwise the item is UNKNOWN, never "none".
- The stand-in's case list gets that marker.
- Bump to fin.map.v1@2 with the manifest.
- The clock anchor is complaint_ref.effective_at.

### A439 (interim): The record-only compile pass.

- BO adds the candidate world rows (inputs only, no oracle labels) to g1_inputs.json, because candidates are part of the request.
- Requests are built by the same Interpreter adapter code the core uses, with a synthetic session.
- The locale is the canonical locale only. locale_mix is not sent.

### A440 (interim): Slot-param kind (EL's blocker).

- Shape: {"slot": "<name>", "kind": "<slot type>"}.
- Packcheck requires kind to equal the node slot's type, and for Resource also its resource_kind.
- The planner refuses a resolved value of another kind.

### A441 (interim): Investigation row.

Yes: add principal_role and authn_ref (set at creation from the verified session). It is a Tier 1 migration with a migration read. It is recovery's prerequisite, so it follows the G1 critical path, not before it.

### A442 (interim): Worker death.

The process exits non-zero, Compose restarts it, and /readyz reports not ready while it is down. No silent degraded mode.

### A443 (interim): SEC-07 slice 2.

After G1. IL does the nightly collection, C1 the auditor export, EL the log fields, and SR the scanner and pass/fail rule.

### A444 (interim): BO.

- The runner's oracle client may give per-case write counts (aggregates only, via the runner's own credentials from the mock-case truth listener).
- The dispatch SHA and run id are stamped into every artifact.

### A445 (interim): IL.

- NOEMA_PACK_MAX_BYTES=1048576 and NOEMA_PACK_MAX_DEPTH=32 (bench values; the largest pack file is 64,069 bytes).
- IL writes the core-trust key generation in secrets_local.sh, and C1's tenant-init registers the public key.
- stack-check reports /readyz and netcheck now, and requires them once the final composition PR merges.
- The "no print" rule applies to services/, not to tools/ and benchmark CLI scripts, whose stdout is their interface.
- The tenant-login mapping step is C2's (EXE-08).

### A446 (interim): FE.

- UI transport limit: 65,536 bytes for any single response or frame. EL asserts the server side never exceeds it.
- Scorecard numbers (#808): counts are safe integers shown exactly (refuse otherwise). Rates are shown exactly as given, with no rounding.
- BO adds the curve and arm-comparison aggregates to scorecard-view as a minor (#799).
- The POST response shape is per A234. EL and C1 publish it through CON-07 (#807).

### A447 (interim): The at-risk value.

It is clock_at_risk_remaining_bp in packs/fintech/limits/trust_limits.json, read by platform/trustlimits. That corrects my A345 S4.

### A448 (interim): PERD versions.

A365 is PERD v1.27, because a PERD is never edited in place. "Adopt v1.26" means nothing now: Proposed versions take effect when the SoT versions land, and until then the rulings govern.

### A449 (interim): The Steward's defaults confirmed.

- DEBT-54 (C2, before G2), DEBT-55 and DEBT-56 as defaulted.
- Ownership is C2's (A344 supersedes A329's listing).
- The A388 CI job sits under UI-04.
- The "confirmation path before G1" change request changes the gate column on TRU-07 and TRU-12 only. The G1 gate's four conditions are unchanged.

### A450 (interim): #764.

SR closes it, because A363 supersedes it.

*A451, A452 and A453: the Architect's heading says "A429–A453", and the message holds rulings A429 to A450. No text came for A451, A452 or A453 (§3).*

## 3. What the Steward did, and where the rulings are silent

- **The Architect's instructions to the Steward**, in the order given: record A358 to A453 (done: §1 and §2, with the earlier records for A363 to A379 and A384 to A388); the corrections of A371, A345 S4 and the KILL_SWITCH instruction (below); drop "consent" from VOI-06, VOI-08 and the demo pre-flight; the change request for the gate column of TRU-07 and TRU-12; verify TST-02 from noema#675 and mark it.
- **A371 correction (A410).** The reconstruction route is audit-only; ops use the panel route, which serves ops and audit (G2). This is the correction asked for in `DEC-2026-11-19-architect-corrections-a371-a345s4` §3, question 1; A410 gives the reading, and A436 and A370 (the route is audit-only, PERD §39.4 and A110) are consistent with it. The merged records are not edited.
- **A345 S4 correction (A447, A416).** The at-risk value is `clock_at_risk_remaining_bp` in `packs/fintech/limits/trust_limits.json`, read by `platform/trustlimits`. `NOEMA_TRUST_AT_RISK_BPS` (A356's table) is withdrawn, as the earlier corrections record says. That answers its question 2.
- **KILL_SWITCH kinds (A430, A400).** KILL_SWITCH_CLEARED and KILL_SWITCH_CLEAR_REFUSED are `SECURITY_EVENT` kinds. The Steward does not hold the earlier KILL_SWITCH instruction the ruling corrects (it is not in any committed record), so it records the corrected rule only. `DEC-2026-11-10-architect-sync-a113-a122` (A114) already says the same, so no committed document needs changing. The Founders' `DEC-2026-11-07` D5 and the `KILL_SWITCH_CHANGED` event are not touched.
- **A448 answers two questions:** PERD v1.27 is where A365 lives (the Steward's reading was right); "adopt v1.26" means nothing now (so no adoption record is written).
- **The numbers.** The ledger repeats, in its own numbers, several rulings that earlier records hold under A363 to A376: A411 is A365 and A366; A410 is A370's route sentence; A417 is A368's `ROLE:<role>`; A419 is A363's `produced_by`; A393 and A394 are A369's Q-A and PackVersion; A400 is A430; A401 is A369's graph params with A440's kind; A416 is A447. The Steward records both as given and changes no wording; where the wording differs, **the later ruling governs** (SoT §0.4, item 1: the latest recorded decision first, once committed). The Steward found no contradiction in substance. One point **is flagged for the Architect:** A435 says the evidence digest "covers mapped facts with status included; duplicates count once", while PERD v1.27 (REQ-TRU-009, from A365) says "sorted (source, source record id, payload hash) triples, ids left out". If the A435 reading is the intended one, v1.27's wording needs a new PERD version (v1.28, with a change request). The Steward writes none until the Architect says.
- **A451, A452, A453 have no text** (§2). The Steward invents none.
- **A429** (history hygiene): noema#721 (EL) and noema#802 (SR) are closed and reopened from fresh branches by their authors. The Steward does not do that.
- **A441:** no migration number is assigned: no owner is named, and the migration follows the G1 critical path. Next free is 0035 on the ledger (noema#183); an owner claims it there first.
- **A449:** DEBT-54, DEBT-55 and DEBT-56 are marked confirmed in the debt register. The A388 CI job sits under UI-04 (no new task row). The gate column of TRU-07 and TRU-12 becomes G1, by `CR-2026-11-20-A449-plan-v1.26`; the four conditions of G1 (plan §3.1) are unchanged.
- **Plan v1.26** (`CR-2026-11-20-A449-plan-v1.26`): VOI-06's done-when loses "and consent"; VOI-08's task loses "consent"; the demo pre-flight loses "consent forms in hand for any live voice" (the effect of A379); TRU-07 and TRU-12 carry **G1**. Not changed, because the instruction does not name them: line 336 of the plan's "never" list ("keep raw audio without consent") and the G5 row.
- **TST-02 (verified, not Done).** noema#675 merged on 18 Nov 2026 (the selector `greedy_cover`, the `smoke` suite with `min_cases: 30`, its tests): 30 cases, 22 of 22 user stories, 24 of 28 fault effects, 16 of 20 capabilities. Its own description says what is not done: running the smoke on every merge and the nightly run (a workflow change), and the row's "smoke runs under 10 min on every PR" is not observed (no workflow on `main` runs the `smoke` suite; `bench-nightly` is a schedule). So TST-02 becomes **In progress** (from Backlog); `blocked` stays true (the workflow needs a Founder decision and SR, and BEN-06 to BEN-09 are listed in Needs and are not Done). BEN-12 still needs it.
- **Next free ruling: A454** (A451 to A453 are named without text).

## 4. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-19-architect-rulings-a341-a357` | A341 to A357 | |
| `DEC-2026-11-19-architect-rulings-a362-a376` | A362 (heading only; its text is in this record), A363 to A376 | |
| `DEC-2026-11-19-founder-intron-data-terms-a377-a379` | A377 to A379 (Founder) | |
| `DEC-2026-11-19-architect-rulings-a384-a388` | A384 to A388 | |
| This record | A358 to A362 (A360 replaced), A380 to A383, A389 to A428, A429 to A450 | |
| Named without text | A451 to A453 | **A454** |
