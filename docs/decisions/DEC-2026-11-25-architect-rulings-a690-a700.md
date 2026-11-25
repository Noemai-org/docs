# DEC-2026-11-25 · Architect rulings A689 to A703 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 25 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves, from a personal account, and merges it (A111, A638; AGENTS §2, item 3). |
| **Date** | 25 November 2026 |
| **Owner** | Principal Architect (the rulings); the Founders (the merge) |
| **Decides** | Rulings A689 to A703 (§1 and §1A), every one Interim. A689 is the stop order, recorded in full in §1A (A703). |
| **Supersedes** | **A690 redraws** the review tiers of AGENTS §11 and **A701 and A702 settle them by path** (the highest tier wins; `deploy`, keys and secrets are named Tier 1). **A703 records A689**, the stop order. **A691 replaces** A674's removal of the reversal pair. **A692 settles** lane 5 slice 4 (option (b)). **A693 confirms** A543 and A681. **A694 confirms** OD-P-116's members. **A696 adds** four gaps to A684's list. **A698 settles** the pack version rule until the contracts-v1.0.0 tag. Otherwise nothing; per ruling in §1. |
| **Amends** | `AGENTS.md` §11 "Reviews" (A690: the review load). OD-P-113 and OD-P-116 (update lines). Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder's personal approval (A111, A638)
- Date: 25 November 2026
- Owner: Principal Architect; Founders
- Decides: A689 to A703
- Decision: §1
- Rationale and evidence: the Architect's message of 25 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-05, INV-07, INV-17, INV-22, INV-29; BD-08; AGENT-14, AGENT-15, AGENT-16; REQ-RES-005, REQ-VER-001, REQ-VER-002, REQ-CTX-007, REQ-EXE-003; SoT §51
- Supersedes: see the Supersedes row above
- Migration notes: A692's `step_params` is an additive member of the receipt contract, with a migration note and regenerated models (AGENT-15), for both Founders, owned by C1. A694's `SLA_EVALUATED` contract file follows A681. A695's matcher manifest kind is a pack-contract addition. A698 keeps additive optional members in `pack.v1` (no `pack.v2`). No migration is added by this record.

## 1. The rulings

### A690. Review load

- SR is the bottleneck. SR now reads **Tier 1 only**: trust, execution, outcome, record, contracts, packs, security, identity and `.github`.
- **Tier 2** is tests, docs, benchmark, voice, UI and refactors. It needs Codex READY, or none if Codex hasn't posted, plus green CI and the Founder's approval.
- SR's order: #989, #990, #986, #956, #981, #985, #987, #976, #930, #980, #984, #974, #960, #972, #932, then the rest.

### A691. #988, the reversal pair (replaces A674's removal)

- Keep the pair. Do not weaken the set-730 corpus test.
- Declare its `convergence_window_seconds` as **0**, meaning no window and an immediate ESCALATE. That is the safest value, packcheck passes, and no number is invented.
- When Tushe states the `reversal_posted` shape, the window becomes the smaller of its sources' freshness limits.

### A692. Slice 4, option (b)

- Add `step_params` to the signed execution receipt, as an additive member in the receipt contract. It holds only the params named by the outcome definition's PLAN_PARAM bindings.
- It is a contract change (AGENT-15) with a migration note and both Founders. C1 owns it, because Execution produces the receipt.
- EL builds the slice 4 reader after that lands.
- The A665 version token in `evidence/portread` is a separate small PR. The allowlist for it is extended to that package.

### A693. EL's three questions

- A pack with no `write_when` answers "no write" (A543). It is not a gap. If #990 reports a gap, change it.
- Choosing the limits file by content, through the manifest kind, is accepted if the manifest pin covers it.
- The two bench execution timeouts stay required with no code default, as in A681.

### A694. C1's OD-P-116 and the Runnable adapter

- The `SLA_EVALUATED` members and the two conditional rules in #984 are confirmed.
- An unevaluable later step means "not runnable", and an unevaluable root is `ErrNotEvaluable`. Confirmed.
- EL builds the `FactsSource`. C1 adds the one optional `EvidencePacket` field to `RunnableQuery`, in its own change.
- SR's two findings on #977 are fixed red first: an unlisted phase must not default to NORMAL (A660), and the Recorder re-checks the owner-queue shape and a negative elapsed.

### A695. C2's open decisions

- Approved: `golang.org/x/text` for the Go recipient matcher, and one manifest kind for the matcher data file. The Steward adds an OPEN entry, and both Founders approve at the #960 merge.
- #972: the three safer readings are accepted (dev and ci refuse replay, live plus a fixtures directory is refused, "absent refuses" applies where the transport is chosen).
- #964: there is no built-in pattern minimum. The packs carry the patterns. With no pattern data there is no Detector, and the composition names a gap for the screen.
- IL adds the `NOEMA_MODEL_PROVIDER_PROFILE` lines to the compose files, `.env.example` and netcheck, in one small PR.

### A696. Stack-check gaps to add to A684's list

The latest `/readyz` also names: the input gateway write path; the recovery reader; the recovery write path; the events route.

EL owns the input gateway write path. C1 owns the recovery reader and write path. They all join EL's one-PR-per-gap burn-down.

### A697. FE

- `BENCH_MAX_BODY_BYTES` is 32768 and `BENCH_TOKEN_TTL` is 900 (A653, A683). The README forwards both to Make.
- FE reads the token directory that `make bench-journey-tokens` writes (#983).
- #957 stays draft.

### A698. Pack version (closes Codex's P1 on #932 and EL's note on #963)

- Additive optional members stay in `pack.v1`. There is no `pack.v2`.
- That holds until the `contracts-v1.0.0` tag is cut, which is a G0-N item for the Founders. After the tag, any shape change needs a version bump (AGENT-15).
- All consumers in the repo regenerate their models from `/contracts`, so none holds its own copy of the shape.

### A699. Kill switch (#980)

- Confirmed: only the ops listener, behind operator mTLS certificates, may hold a tenant's admin emitter login.
- No runtime identity and no core runtime process receives it.
- SR reads the ops listener PR as a keys and identity path before the control plane is mounted.

### A700. #963 data, #972 and #974

- #963: confirmed: NONE_REQUIRED for `create_escalation_case` and `route_to_internal_owner`. `log_complaint_reference` and `record_investigation_evidence` stay ESCALATE_ONLY (A647).
- #972 holds until IL's compose PR is in. Agreed with SR.
- #974: C1 explains or reverts the one re-encoded line.

## 1A. Rulings A701 to A703, and A689 (the Architect's answers to the review of this pull request)

### A701. Tier follows paths (SR's finding 2, adopted)

- A PR's tier follows the paths it touches, and the highest tier wins. A "refactor", "test" or "docs" label never lowers it.
- **Tier 1 paths** are:
  - `trust/`, `execution/`, `outcome/`, `record/`, `contracts/`, `packs/`;
  - security, identity, keys and secrets;
  - `.github/`, `deploy/` and `tools/ci/`;
  - the oracle and held-out paths;
  - `AGENTS.md`, `CLAUDE.md` and `docs/decisions/`.
- Everything else is Tier 2. It needs green CI, Codex READY if Codex has posted, and the Founder's approval.

### A702. `deploy`, keys and secrets

`deploy` stays Tier 1. Keys and secrets are named explicitly as Tier 1. They are not left to "security" and "identity".

### A703. A689 goes into the record in full

The text is the stop order the Architect gave, reproduced below. SR may then clear docs#246.

### A689 (the stop order, in full)

- No output on a wake that needs no action.
- No sub-agent batches to review PRs. Independent reads are for migrations only (A463), or when SR names one.
- One agent per assigned task. Nothing new starts without a ruling that names it.
- No re-reading CI unless the head moved.
- Reports are a table only: PR, head, CI result, READY or the named blocker. If nothing changed, say nothing.
- When nothing is left, end the turn. No summaries or recaps.

## 2. What the Steward did, and where the rulings are silent

- **A689** is recorded in full in §1A (A703). The Steward follows it from now on.
- **[OPEN] entries, as asked:**
  - **OD-P-117**: `golang.org/x/text` and the matcher manifest kind (A695). The new dependency is approved by the Architect; both Founders approve at the #960 merge (AGENT-14). The module is not in PERD §36.1's list; the manifest kind's name and shape are C2's to state in the pull request.
  - **OD-P-118**: the reversal pair's `convergence_window_seconds` of 0 (A691).
  - **OD-P-119**: the `step_params` member of the signed execution receipt (A692). Its shape is C1's to state in the contract pull request.
  - **OD-P-116** (`SLA_EVALUATED`) is updated in place: A694 confirms the members and the two conditional rules in #984; it stays Open until the contract file merges with both Founders' approval.
  - **OD-P-113** is updated in place: A691 keeps the reversal pair with a window of 0, replacing A674's removal; the entry stays Open for the `reversal_posted` shape.
- **A690, A701, A702 and AGENTS.md.** `AGENTS.md` §11 carries the tier rule by path and the Tier 1 path list as ruled (with `deploy`, keys and secrets named). **Plan §4 and §13.1 (v1.29) state the older tier split;** `AGENTS.md` §11 governs until a plan version restates it (A671). A small plan version for that is available on request.
- **SR's second finding and the `deploy` question (reviewers' findings on this pull request)** are settled by A701 and A702.
- **Notes from SR's read, for the owners (not decisions).** A698 is not a precedent for breaking changes: #963 changes the `compensation` vocabulary in place and is covered by A647 and A700. For A699, SR asks for a netcheck assertion that no service other than the ops listener mounts the admin emitter DSN. For A692, the `step_params` member may hold only the params named by the PLAN_PARAM bindings, and a personal identifier is held masked or as a hash (AGENT-13). For A693, SR accepts "no write" on the condition that #963 is on `main` first so packcheck refuses a pack whose write-capable node has no `write_when`, and #990 tests the shipped fintech pack.
- **The noema copy of AGENTS.md** takes the change in a re-point PR after this merges (as noema#967 and noema#991 did).
- **A692 and A665.** The Steward notes that A665's version token in `evidence/portread` goes in its own small PR, with its allowlist extended to that package (EL's PR body states it). No `docs` change.
- **A696.** The four gaps join A684's list for EL's burn-down; the Steward does not move `tasks.csv`.
- **A698 and the G0-N tag.** The `contracts-v1.0.0` tag is a G0-N item (ENV-14 in the plan); nothing for the Steward to cut.
- **A690's order, A693, A694, A697, A699, A700:** other owners' work; nothing for the Steward beyond this record.
- **Next free ruling: A704.**
