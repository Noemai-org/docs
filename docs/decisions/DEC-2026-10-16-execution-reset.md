# DEC-2026-10-16 · Execution reset: canonical organisation, lean team, schedule, G0, test-environment components

| | |
|---|---|
| **Status** | Accepted by the Founder on 16 October 2026, with schedule option A. The Technical Co-Founder confirms by approving the pull request that adds this record |
| **Date** | 16 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Amends** | SoT §35.6 (deployables), §40.3 (environment wording) and §51 (tree); DEC-2026-10-11 (PERD adoption) and DEC-2026-10-11 (plan adoption), by re-pointing them; DEC-2026-10-12 (Amendment 2); DEC-2026-10-13 (Amendment 1) |
| **Closes** | GOV-20 and OD-P-43 (webhook receiver hosting, PERD OQ-15) |
| **Evidence** | Pre-execution audit of `docs` and `brain` (14 Oct 2026), its fact-check (16 Oct 2026), and the agent's read-only review with git bundles of the retired organisation (16 Oct 2026); our response to Tushe, sent 13 Oct 2026 (PDF record, SHA-256 `c1f1e33a…`) |


**Record fields (decisions README template).** The table above already gives Status, Date, Owner, Amends, Closes and Evidence; the template headings it lacks point to the sections below.

- Status: Accepted (see the table above)
- Date: 16 October 2026 (see the table above)
- Closes: plan task GOV-20 and provisional entry OD-P-43 (PERD OQ-15), by E6. It also confirms the answer to PERD OQ-05 (purpose of `brain`) in E8. No entry of SoT §46 is decided here
- Owner: Founder and Technical Co-Founder
- Decision: see section 2 (E1 to E13)
- Rationale and evidence: see section 1, section 5 and the Evidence row above
- Affected requirement IDs / SoT sections: SoT §35.6, §40.3 and §51 (section 3); the requirement count (153) and every invariant are unchanged (section 4)
- Migration notes: E7 (what leaves `docs`), E8 (what moves out of `brain`), E11 (the four earlier records re-pointed) and E12 (the port to `noema`)
- Supersedes: None as a record. It re-points DEC-2026-10-11 (PERD adoption) and DEC-2026-10-11 (plan adoption), and amends DEC-2026-10-12 (Amendment 2) and DEC-2026-10-13 (Amendment 1)

---

## 1. Why this record exists

Between 12 and 16 October:

- the repositories moved to a new GitHub organisation;
- the team was confirmed as two people working with coding agents;
- G0 did not hold, and Tushe has not yet confirmed a joint-session date;
- the `noema` and `benchmark-heldout` repositories were created;
- an audit found contradictions to settle before execution;
- real build work (CON-04, PCK-01, PCK-02) was pushed straight to `main` of the retired organisation's `docs`, without review.

This record settles all of it.

## 2. Decisions

### E1. `Noemai-org` is the only organisation

- All work happens in `Noemai-org`. Its repositories are `docs`, `brain`, `noema` and `benchmark-heldout`.
  - The `noema` repository was first created as `noema-` and has been renamed `noema`.
- **The old organisation, `noema-org`, is retired.** Nobody writes to it again.
- **It is archived read-only only after E12's port has merged.** The 15 Oct commit may exist only there. Archiving is a settings action, not an edit.
- **Every link** in every repository points to `Noemai-org`.
- **Links to pull requests that exist only in `noema-org`** become links to the matching merge commits in `Noemai-org`, with the text "(originally PR #N)".

### E2. The team is two people working with coding agents

**Who does what.** The Founder and the Technical Co-Founder together hold every role:

- EL (engineering lead);
- C1 and C2 (core engineers);
- IL (integration lead);
- B (benchmark owner);
- SR (security reviewer);
- V (voice lead);
- FE (front end).

**How tasks are assigned.** Tasks keep their role titles; either founder picks up any task. No personal names appear on tasks.

**Four safeguards stay, because the proof depends on them:**

1. **Held-out custody.**
   - Only the **Founder** holds `benchmark-heldout`, the Tushe administrator credential and the Tushe fixture credential.
   - The Technical Co-Founder and every coding agent never read them, and no held-out case is pasted into an agent session (OD-16, REQ-AGT-004).
2. **Review.**
   - Every change reaches `main` through a pull request approved by the founder who did not drive it (E13).
   - P0 paths (trust, execution, outcome, record, contracts, packs, safety thresholds) need that approval through CODEOWNERS.
   - An agent's report is never the approval.
3. **Comparison arms (week 4).**
   - The arm builder and the arm reviewer must be people outside the build (SoT §38.5).
   - One external engineer is engaged, under NDA, before Mon 9 Nov.
4. **Separation of duties for test-environment components.** The founder who drives `mock-case` or the hostility proxy does not approve its fault plans (DEC-2026-10-12, SR-19).

**CODEOWNERS** lists both founders on every protected path, with "require review from code owners" switched on.

### E3. The schedule moves one week (option A, approved)

**Why.**

- G0 did not hold on 15 or 16 October.
- Tushe's committed dates (R2 to R4 by Fri 23 Oct; R9 to R12 by Fri 30 Oct) then each land just before the work that needs them.

**The rule.** Every date in plan v1.4 moves forward exactly seven days. There are three exceptions:

1. **Work already done** keeps its actual date, taken from git history.
2. **Tushe's R-dates do not move.** They are commitments made to us.
3. **G0 is split** (E4):
   - G0-N on Thu 22 Oct, 17:00;
   - G0-T on the date Tushe confirms. Our request goes to Tushe by Thu 22 Oct.

**What results:**

| Event | Plan v1.4 | Plan v1.5 |
|---|---|---|
| G0 | Fri 16 Oct, 18:00 (joint) | **G0-N** Thu 22 Oct, 17:00 · **G0-T** to be confirmed by Tushe |
| G1 evidence (BEN-05) / review (GOV-07) | Fri 16 Oct / Mon 19 Oct, 10:00 | Fri 23 Oct / **Mon 26 Oct, 10:00** |
| G2 | Fri 23 Oct, 16:00 | **Fri 30 Oct, 16:00** |
| G3 | Fri 30 Oct, 16:00 | **Fri 6 Nov, 16:00** |
| Code freeze | Wed 4 Nov, 12:00 | **Wed 11 Nov, 12:00** |
| G4 and G5 | Wed 4 Nov, 16:00 | **Wed 11 Nov, 16:00** |
| G6 | Thu 5 Nov, 18:00 | **Thu 12 Nov, 18:00** |
| G7 dry run / demo | Fri 6 Nov, 09:00 / 14:00 | **Fri 13 Nov, 09:00 / 14:00** |
| Reserve Saturdays | 17, 24, 31 Oct | 24, 31 Oct and 7 Nov |

- The window closes Sun 15 Nov.
- Tushe is told two things: their no-change window (R5) runs to Fri 13 Nov, and we need their confirmed joint-session date.
- Nothing else changes: not the gate contents, not the requirements, not the Tushe dates.

**Option B (rejected)** kept the demo on Fri 6 Nov and compressed the plan. It left US-02 and D1 without their Tushe inputs until the hardening week.

### E4. G0 has two halves, and both must pass

| Half | What | When |
|---|---|---|
| **G0-T (Tushe)** | AT-01 to AT-20, run against the signed worksheet in the joint session (ENV-12, ENV-07) | The date Tushe confirms |
| **G0-N (Noema)** | TEN-01 to TEN-08 (Noema-side checks against Tushe; internal, not in the worksheet); `/contracts` v1 tagged; ≥ 50 reproducible fixtures; the isolation tests, including runtime refusal on Tushe `/partner/...` routes and on the `mock-case` truth endpoint | Thu 22 Oct, 17:00 |

- **G0 passes when both halves pass.**
- **G1 may run before G0-T.** Its evidence is recorded, but it counts only once G0 passes (no Phase B result counts before G0).

### E5. Test-environment components are not Noema services

| Component | Path in `noema` | What it is |
|---|---|---|
| `mock-case` | `synthetic/mock_case/` | Emulates the bank's case system (DEC-2026-10-12 D1, REQ-ENV-008); task ENV-08 |
| Hostility proxy | `benchmark/hostility_proxy/` | Injects faults; benchmark and test profiles only; task ENV-09 |
| Webhook relay | `synthetic/webhook_relay/` | Receives Tushe's webhooks from the internet (E6); task ENV-13 |

- These three are test-environment components, not Noema deployables. The two deployables stay the Go core and the Python model service (SoT §35.6).
- None of them holds a decision, grant, Record, provider or core-database credential.
- None of them runs in a production profile.

### E6. The webhook relay (decides GOV-20)

- **Where it runs.** On one small public HTTPS host that runs nothing else. EL picks the provider at setup and records it in the `local-setup` runbook.
- **What it does on receipt.**
  - Verifies the Standard Webhooks signature and the five-minute tolerance.
  - Rejects and counts anything unverified.
  - Appends each verified delivery, unchanged, to its own local store, keyed by delivery ID.
- **What it holds.** Only the webhook signing secret. No database, Tushe, grant or provider credential.
- **How the core gets deliveries.** The core pulls verified deliveries from the relay:
  - over an authenticated, outbound connection to an allowlisted host;
  - into its inbox, which deduplicates by delivery ID (REQ-API-008).

  Nothing on the internet can reach the core.
- **Where faults are injected.** In the benchmark profile, the core's pull runs through the hostility proxy. The proxy never runs on the public host.

### E7. `contracts/` and `packs/` leave `docs`

- **What gets archived.** The draft OpenAPI `contracts/schema.yaml` (including its 15 Oct additions) and `contracts/fixtures/intent_valid.json`. They move to `docs/archive/2026-10-pre-poc-drafts/`, with a README listing their mismatches with the SoT:
  - FactStatus `CONFLICTED`/`VERIFIED`/`UNVERIFIED` instead of `CONTRADICTORY`/`AMBIGUOUS`/`UNAVAILABLE`;
  - `TrustReasonCode` `NONE`;
  - a grant without its binding fields;
  - OpenAPI 3.0.3 with `/dummy`.

  CON-01 builds the JSON Schemas in `noema` from the SoT and PERD, failing test first.
- **What moves.** The golden vectors, the packs, the bad-pack fixtures and `packcheck` go to `noema` under E12.
- **Afterwards.** `docs` holds no `contracts/`, `packs/` or product code.
- **Packs.** The POC packs are fixed by the SoT (§15.4): fintech (populated) plus three conformance packs (telecom, insurance and healthcare administration), each capped at three intent nodes, one trust profile and one outcome definition. All four exist in the 15 Oct work. The other industries the SoT names are the company's direction, not the POC (AGENT-03).

### E8. `brain` keeps founder knowledge only

This confirms DEC-2026-10-13 R7.

- **What `brain` holds.** Strategy, research, partner context, notes.
- **What it never holds.** Specifications, build records or technology decisions.
- **Where build records live:**

  | Record | Lives in |
  |---|---|
  | Gates, daily notes, sessions | `docs/poc/execution/` |
  | Tushe observations and correspondence | `docs/poc/tushe/` |
  | Incidents and as-built notes | `noema/docs/` |

- **`integrations/providers/tushe-integration-plan.md`.** It moves to `history/superseded/`. A short, non-authoritative summary that agrees with DEC-2026-10-12 replaces it.
- **The duplicate ADR-002:**
  - `ADR-002-openapi-schema-generation.md` keeps 002 and is marked **Superseded**: it conflicts with PERD §36.1 and AGENT-14, and technology decisions live in `docs/decisions/`.
  - `ADR-002-align-brain-with-sot-v1.3.md` becomes **ADR-003** and stays current.
  - Numbers are never reused.

### E9. The record of what we sent Tushe is the PDF

- The 13 October response is recorded only as the PDF Tushe received (SHA-256 `c1f1e33a…`).
- The hand-edited Markdown copy, with 16 truncation markers, is removed.
- The PDF goes on the frozen-files list.
- Frozen records keep their original wording, including quoted old spellings. Every other file uses "Tushe".

### E10. The Tushe delta is reissued as v1.2

- **The old delta.** `tushe-spec-delta-v1.1.md` was never sent and is marked superseded.
- **The new delta, `tushe-spec-delta-v1.2.md`, records:**
  - what we asked for and agreed on 13 October (R1 to R13 with their dates; the amended AT-01, AT-03 and AT-15; the six "material" items);
  - what we withdrew: a global clock (TIM-01, TIM-02), a GT-02 endpoint, case-API items (CON-01, IDP-07), proposed AT-21 to AT-25, and a case/dispute domain.
- **What governs Tushe semantics:**
  - Tushe specification v1.0;
  - Tushe's response of 7 October;
  - DEC-2026-10-12;
  - delta v1.2;
  - the signed worksheet.

### E11. The four earlier decision records are re-pointed and accepted

| Record | Action |
|---|---|
| DEC-2026-10-11 (PERD) | Re-pointed to the current PERD (v1.5 after this change; 153 requirements). Accepted |
| DEC-2026-10-11 (plan) | Re-pointed to the current plan (v1.5) and the E3 schedule. Accepted |
| DEC-2026-10-12 | Accepted, with Amendment 2 (E4 to E6, E9, E10) |
| DEC-2026-10-13 | Accepted, with Amendment 1 (E1) |

The Founder approved all four on 16 October 2026. The Technical Co-Founder confirms by approving the pull request that applies them.

### E12. The 14–15 Oct build work is ported to `noema`, through review

**The two commits.** Both were pushed straight to `noema-org/docs` `main`:

- `fd16980` (14 Oct) delivers **CON-04** golden vectors;
- `ce8897e` (15 Oct) delivers **PCK-01** and **PCK-02**.

**Where the files go.** One pull request in `noema`, with authorship and original commit IDs kept:

| Files | Destination |
|---|---|
| `golden_vectors.json` | `contracts/fixtures/` |
| `fintech_v1.json`, `conformance/*.json`, `fixtures/bad_packs/*.json` | `packs/` |
| `packcheck.py` | `tools/` |

**What was checked on 16 Oct.**

- The JCS, `intent_hash`, `plan_hash`, `binding_hash` and HMAC grant-signing vectors reproduce.
- `packcheck` accepts the four packs and rejects all eight bad packs, each for the stated reason.
- The pack's 20 `fin.cap.*` capabilities match SoT §34.3 (12 allowed, 8 prohibited).

**What review must settle before merge.** Each item is fixed or recorded as a PCK-01 follow-up:

1. Evidence sources use `fin.src.tushe_ledger`. The SoT uses `fin.src.core_ledger`, `fin.src.switch` and `fin.src.settlement`; no vendor name belongs in a pack.
2. The outcomes lack `fin.outcome.exception.status_explained`.
3. Reason code `NONE` is not in the SoT.
4. The intent classes use `TRANSFER_FUNDS`-style names. The SoT uses intent nodes such as `fin.payments.exception.investigate`.
5. The `evidence_set_hash` and idempotency-key vectors use their own constructions. CON-04 is done only when Go and Python both compute every vector.

**Task status.** CON-04 stays open until the Go and Python implementations pass. PCK-01 and PCK-02 are done once the port merges with the review items settled.

### E13. No direct pushes to `main`

- Branch protection is on for `docs`, `brain` and `noema`:
  - pull request required;
  - one approving review from the other founder;
  - CODEOWNERS review on protected paths;
  - status checks must pass;
  - no force pushes.
- **This applies to the founders as well.** The 12 Oct `brain` commits and the 14–15 Oct `docs` commits went in without review. That is how the Tushe plan contradicting DEC-2026-10-12, the duplicate ADR, and build code in the documentation repository arrived.

## 3. SoT v1.6 edits (AGENT-29)

- **§35.6.** After the two deployables, add:

  > Test-environment components (`synthetic/mock_case`, `benchmark/hostility_proxy`, `synthetic/webhook_relay`) are not Noema deployables. They hold no decision, grant, Record, provider or core-database credential, and never run in a production profile (DEC-2026-10-16 E5).

- **§40.3.** Replace "the virtual clock is controllable" with:

  > Noema's simulated clock is controllable, and Tushe time is controlled per object (§36)

- **§51 tree.** Add:
  - `/synthetic` (test-environment components: `mock_case`, `webhook_relay`);
  - `/deploy` (Docker Compose and profiles).
- **Version and change log.** Bump to v1.6, and add an Appendix D entry.

## 4. What stays the same

- Every invariant.
- Every requirement (153).
- Every gate's content.
- No money moves.
- The two deployables.
- Held-out custody.
- Every Tushe date.

## 5. SoT §52 questions

- **What breaks without it?** Execution starts against contradictory documents, the wrong organisation, an impossible G0 date and an unsafe receiver design. Delivered work is lost in a retired organisation.
- **Does it increase or decrease the unsafe autonomy surface?** It decreases it:
  - no credential sits on the internet-facing host;
  - held-out custody is named;
  - wrong draft schemas stay out of the build;
  - nothing reaches `main` without review.

## 6. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founder | Approved this record and DEC-2026-10-11 (PERD), DEC-2026-10-11 (plan), DEC-2026-10-12 and DEC-2026-10-13; schedule option A | 16 Oct 2026 | Written instruction to the coding agent |
| Technical Co-Founder | Confirms | Date of approval | Approving review on the pull request that adds this record |
