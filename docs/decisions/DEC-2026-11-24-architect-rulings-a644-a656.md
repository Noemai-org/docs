# DEC-2026-11-24 · Architect rulings A644 to A656 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 24 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves, from a personal account, and merges it (A111, A638; AGENTS §2, item 3). |
| **Date** | 24 November 2026 |
| **Owner** | Principal Architect (the rulings); the Founders (the merge) |
| **Decides** | Rulings A644 to A656 (§1), every one Interim. |
| **Supersedes** | **A650 moves** DATA-02's owner (plan v1.28). **A648 narrows** TRU-11's scope (no tenant-wide limit in the POC; see §2). **A656 relaxes** the review gate of A143 in practice (SR's READY stands in for an unread Codex; independent role reads for migrations only). **A649 and A655 refine** A606, A612 and A593. Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT or the PERD. **Plan v1.28** (a new version, owner of DATA-02 only) carries A650. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder's personal approval (A111, A638)
- Date: 24 November 2026
- Owner: Principal Architect; Founders
- Decides: A644 to A656
- Decision: §1
- Rationale and evidence: the Architect's message of 24 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: BD-05, BD-08, INV-02, INV-20, INV-22; AGENT-14, AGENT-15, AGENT-16; REQ-CTX-006, REQ-DATA-002, REQ-MEM-002, REQ-RES-005, REQ-TRU-012; PERD §23.3; AGENTS §5, §11
- Supersedes: see the Supersedes row above
- Migration notes: A647 is one contracts PR (`capability-descriptor.v2`, the node-to-graph link, `tenant_zone`, the recon-rule `window_seconds`; AGENT-15 steps; both Founders once). A630's migration is noema#952 (0041). No other migration is added by this record.

## 1. The rulings

### A644 (EL, priority routing).

The PERD and plan give no more than the phrase "priority routing data". The smallest safe design:

- A pack member `priority_routing` maps each SLA phase to `{priority, owner_queue}`.
- `priority` is one of `HIGH`, `NORMAL`, `LOW`.
- Values are SYNTHETIC. EL writes them, and the Steward logs an [OPEN] entry.
- C1's evaluator reads it. A phase with no entry gets `NORMAL`.

### A645 (EL, composition).

- The list scope prefix `<pack id>.<entity>:` is accepted. It matches `portread`.
- The confirmation expiry comes from `trust-limits.v2`'s `confirmation_ttl_ceiling_ms` (600000), as pack data. It is never a setting.
- The capability an admitted intent confirms comes from the pack's action graph. C1 owns the node-to-graph link as one pack field, inside the contracts change in A647.
- The Candidates read (REQ-CTX-006) is C2's, as EVD-04.
- The injection-screen patterns are pinned in the manifest. C2 writes them and SR reads them.
- Until those land, Planner, Candidates, Confirmations, Evidence and Policies stay named gaps, as now.

### A646 (EL, #934 and #954).

- #934: the CODEOWNERS line is justified by AGENTS §11 (a PR that adds a top-level owned path adds its line) and by A617. EL says so in the PR body. Both Founders approve it.
- #954: SR reads the amended guard.
- PCK-05: if a pair's sources lack a freshness limit, EL stops and lists it, which is correct.

### A647 (C1, A631 pack decisions).

- `log_complaint_reference` and `record_investigation_evidence` are `ESCALATE_ONLY`.
- Prohibited capabilities are exempt. Packcheck asserts they declare no compensation and have no adapter (BD-08).
- Bump `capability-descriptor` to v2. The pack manifest gets a new version only if its own schema changes, and C1 says which in the PR.
- One contracts PR carries everything: the descriptor v2; the node-to-graph link; the `tenant_zone` member (A650); the recon-rule `window_seconds` member for EL's PCK-05.
- Both Founders approve that PR once.

### A648 (C1, TRU-11).

- Confirmed: every capability in the authorized set is checked.
- Confirmed: a voided grant still counts toward the hour.
- The tenant-wide limit is not built in the POC. The Steward logs an [OPEN] entry.
- Wiring the Rates adapter happens after the G1 run.

### A649 (C2, UND-18 gate, #932 and BO's boundary findings).

- A606 and A612 stand. A missing, null, signed, NaN, infinite, string or exponent-form probability (B14 to B20) makes that slot abstain, not the whole compile.
- The parse reads the number's text, so `9e-1` is malformed and abstains.
- A reply that isn't valid JSON at all stays `ProviderUnavailable`.
- C2 fixes this in #932 with red-first tests, and BO regenerates the recordings afterward.

### A650 (tenant zone, DATA-02).

- The tenant zone is a pack member, `tenant_zone`, as an IANA name. The synthetic tenant uses `Africa/Lagos`.
- It rides in C1's contracts PR (A647).
- DATA-02 moves to C2, and the Steward corrects the owner. Its time-zone property tests follow once the member lands.

### A651 (C2, Outcome request builder, #950).

- For G1 the caller supplies the bindings. EL's composition fills them by exact name match between predicate variable and plan param, and refuses on a missing match.
- `Pending` stays nil. A pack mapping field and a `Pending` member in the outcome-definition contract are OPEN entries, after G1.

### A652 (BO, #929 and MEM-02).

- Split #929.
  - First PR: the labelled set and its tests. It is small enough to read.
  - Second PR: the boundary recordings, regenerated on `main` after #932 merges.
- B02, B06 and B12 are generated at test time. Do not add them to `leakscan.allow`.
- MEM-02's done-when (a fix PR without a regression link fails CI) is already met by the merged check. The Steward marks it Done.
- BO adds one small `tools/ci` change: the linked case must exist in the suite or be added in the same PR. Both Founders approve it.
- The `REGRESSION_LINK` observation writer is an OPEN entry for after G1.

### A653 (IL).

- `max_body_bytes` 32768 is approved as the interim value. Use it for every stack-check.
- ENV-05: build the adapters and contract tests from the Tushe spec v1.0, its delta and the 7 Oct response. If a behaviour is not stated there, stop and list it. The live run stays pending G0-N.
- Open #955's PR with its body filled in (task, REQ and SoT IDs).
- #948's body needs a SoT ID. The compose Go-proxy failure gets one re-run (A455).

### A654 (FE).

- The eight event settings are EL's. EL names them with bounds in #907's body, and the Architect approves any value that fails closed on a missing setting.
- The polling interval is a UI setting, not a safety threshold. Interim: 2 s interval, 60 s ceiling.
- BO supplies the seeded J1 to J8 manifest. IL supplies the synthetic customer token through the tenant-init seed.

### A655 (C1, #926).

A non-SLOT clarification must still require `candidate_set_id`, enforced as a conditional in the schema validator. The generated types stay shape-only, and each language's decode test covers both modes.

### A656. Review standing (clears the Codex bottleneck).

- Where Codex has not read a head, SR's READY at that same head stands in for Codex (A480, A541).
- Independent role reads apply to migrations only (A463): #923, #925 and #952.
- C2 reads #923 at `44d420f2` and #952.
- EL reads #925.

## 2. What the Steward did, and where the rulings are silent

- **Logged as [OPEN] (provisional, NON-CANONICAL), as asked:** **OD-P-103** `priority_routing` values (A644); **OD-P-104** the tenant-wide rate limit (A648); **OD-P-105** the outcome pack-mapping field and the `Pending` member (A651); **OD-P-106** the `REGRESSION_LINK` observation writer (A652). `OD-P-102` (`capability-descriptor.v2`, A631) stays open until both Founders approve the contracts PR of A647.
- **MEM-02 → Done** in `tasks.csv`, on merged evidence: noema#452 (the check script and its tests; merge commit `9a8cbbb1c6a76a922aeb9c538e9a1446c509e30b`, 20 check runs succeeded) and noema#673 (the workflow wiring; merge commit `7cec0f0b38edef38c3f24b00c1758e1da2115be9`, 25 check runs succeeded); the tests are `tools/ci/test_check_regression_link.py` and `tools/ci/test_regression_link_workflow.py`; and on 24 Nov the check failed a pull request whose `Regression case:` line named more than a file path (noema#915, `regression-link` job 137717658384), which is the done-when observed. **One nuance, not a gap in the done-when:** branch protection on `noema` `main` requires `compose`, `contracts`, `core`, `checks`, `arch-lint`, `model` and `pr-base-guard`; `regression-link` is a separate check run, so a red `regression-link` shows on the pull request without being a listed required check. The Architect may want it required; that is a branch-protection change, which the Steward does not make (AGENTS §11).
- **DATA-02 → owner C2 (A650)** by **plan v1.28** (`NOEMA_POC_4WEEK_PLAN_v1.28.md`, a new version; v1.27 is not edited) and `CR-2026-11-24-data-02-owner`. `tasks.csv` is regenerated by `plan_index.py` (only that row changed). Its status stays Backlog. No task is added or removed.
- **A648 and the plan row TRU-11.** The plan row says "Tenant rate limits and per-principal limits inside Trust"; A648 says the tenant-wide limit is not built in the POC. That narrows the row's scope. The ruling is an approved POC decision and ranks above the plan (SoT §0.4); the plan text is unchanged; the Steward drafts the plan version that narrows the row on request. TRU-11's done-when (a limit breach gives WAIT or REJECT) holds for the per-principal limit (noema#952).
- **A656 and the review gates.** AGENTS §11 and A143 state the Tier 1 gate as Codex + SR + one independent role read + CI + one Founder approval. A656 says SR's READY at the same head stands in for an unread Codex (as A480 and A541 already said) and that **independent role reads apply to migrations only**. That relaxes the independent-read part for Tier 1 changes that are not migrations. AGENTS.md still carries the old text; it is a small pull request to AGENTS.md (and its copy in `noema`), which the Steward drafts on request. Until then the Steward reads A656 as the Architect's standing ruling and applies it only when it merges. A migration read stays independent: **#923** (C2 at `44d420f2`), **#925** (EL), **#952** (C2). The Steward updated the ledger on noema#183.
- **A645.** The confirmation expiry is `trust-limits.v2`'s `confirmation_ttl_ceiling_ms` (600000, the PERD's 10 minutes, REQ-TRU-009) read as pack data, never a setting (A561). Planner, Candidates, Confirmations, Evidence and Policies stay named gaps in `/readyz` until their pieces land.
- **A646.** #934's CODEOWNERS line is AGENTS §11's rule; both Founders approve it. #954 carries the amended `RouteRequest` guard (A639), which SR reads.
- **A647.** The contracts PR is one change for both Founders to approve once (AGENT-15: a version bump, a migration note, regenerated models). The `window_seconds` member is the declared window of A641 for REQ-RES-005 and PCK-05.
- **A649.** B14 to B20 are BO's boundary cases. The exact-decimal rule of A606 and A612 is unchanged; A649 says what a malformed value does (that slot abstains; the whole compile does not). C2's tests are red first.
- **A652 and the Founders.** The `tools/ci` change needs both Founders (the same class as #943). `leakscan.allow` is not widened (B02, B06 and B12 are generated at test time).
- **A653.** `max_body_bytes` 32768 is the Architect's interim value, not an agent's (AGENT-16). The live run waits for G0-N; no result before G0 counts.
- **A654.** The polling interval is a UI setting (2 s, ceiling 60 s, interim); the eight event settings are EL's, named with bounds in #907's body.
- **A655 and A593.** A593 said `allow_none` and `none_option_id` stay required outside SLOT mode; A655 says the same for `candidate_set_id`, as a schema-validator conditional, with generated types shape-only.
- **OPS-02's guard names.** The Steward is collecting them from the owners' next status files; none is invented.
- **Migration ledger on noema#183:** 0037 merged; 0038 #923; 0039 #925; 0040 reserved (A598); **0041 noema#952** (A630, TRU-11); 0042 provisional (A633). Next free: 0043.
- **Next free ruling: A657.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` and `DEC-2026-11-21-*` records | A358 to A362, A380 to A485 (A467: no text), A489 to A492, A502 to A517 | |
| `DEC-2026-11-22-*` to `DEC-2026-11-24-architect-rulings-a624-a643` | A518 to A643 (A541 noted; A590 to A592 in full; A626 withdrawn) | |
| This record | A644 to A656 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank, by ruling A592) | **A657** |
