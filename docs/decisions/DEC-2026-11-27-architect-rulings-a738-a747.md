# DEC-2026-11-27 · Architect rulings A738 to A747 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 27 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves, from a personal account, and merges it (A111, A638; AGENTS §2, item 3). |
| **Date** | 27 November 2026 |
| **Owner** | Principal Architect (the rulings); the Founders (the merge) |
| **Decides** | Rulings A738 to A747 (§1), every one Interim. |
| **Supersedes** | **A738 amends** A669 (the re-read rule), A686 (the stand-in clock: 30 minutes, not 60) and AGENTS §11's "never base a PR on another PR's branch" (stacking up to 4 PRs), and generalises A730. **A739 sets** the key ring bound. **A740 extends** A723 with a fourth source. **A741 accepts** BO's generator run as the A604 evidence. **A742 extends** IL's allowlist for one PR. **A743 settles** INP-01's answered SLOT value. **A745 restates** A680. **A746 records** the Founder's remediation of `DOCS_READ_TOKEN`. **A747 bundles** the composition gaps. Otherwise nothing; per ruling in §1. |
| **Amends** | `AGENTS.md` §11 (A738: the speed rules, the re-read rule, the stand-in clock, stacking). Nothing in the SoT, the PERD or the plan; plan §4 (v1.31) states the 60-minute clock and the A669 rule until a plan version restates them. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder's personal approval (A111, A638)
- Date: 27 November 2026
- Owner: Principal Architect; Founders
- Decides: A738 to A747
- Decision: §1
- Rationale and evidence: the Architect's message of 27 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-12, INV-14, INV-16, INV-17, INV-29; BD-08; AGENT-11, AGENT-12, AGENT-15, AGENT-16; REQ-INP-004, REQ-INT-004, REQ-VER-002, REQ-STM-001, REQ-TRU-009, REQ-SEC-004; SoT §51
- Supersedes: see the Supersedes row above
- Migration notes: A740 adds `EPOCH` as a fourth `outcome_bindings` source (C1, in #1026; the contract is additive, AGENT-15). A745: migration 0043 (#1021) has a CHECK that must not forbid any early outcome A680 records. No migration is added by this record.

## 1. The rulings

### A738. Speed rules, effective now

| Rule | Text |
|---|---|
| Red to green | The agent pushes the red, does one background wait (up to 20 minutes, A455) for the first failing job, reads it, and pushes the green. It never holds a green for a prompt. |
| READY | A push that only adds tests, docs or status keeps READY. Only a production-code push needs a fresh READY. |
| Dependent work | Goes in one PR as separate commits (AGENTS §11). |
| PR stack | Agents are allowed to stack not more than 4 PRs on the parent PR so work can progress quickly without waiting on a PR to merge. |
| Agent dependencies | If an agent needs information, data, or any item from another agent, the first thing it does is check the repo, open PRs and the agents' committed work before asking them directly. An agent can only ask another agent for information if it does not currently exist anywhere in the repo. |
| SR | Reads a PR once, at its green head. The stand-in clock is 30 minutes after SR's READY (down from 60). |
| Codex findings outside a PR's diff | Become follow-up conditions (generalizing A730). |

QA before any report (all required):

- red seen failing in CI
- green read at every check on the head
- hand mutants run
- `git diff --stat` shows only allowlist paths
- gitleaks run locally
- PR body traced and lists what is not done
- no test weakened

### A739. Key rings

- The upper bound is 999, the Execution ring's bound, for every key ring.
- The evidence key file uses the same format as the other signers' seed files, with the 16 KiB cap.
- EL conforms its loader to IL's #1023 names: the volume and the `core_evidence_ed25519_seed_1` file. IL's #1023 is not changed.

### A740. EPOCH source

`outcome_bindings` gains a fourth source, `EPOCH`: the subject's current logical-resolution epoch, read through the same `NextEpoch` port the Interpreter uses. C1 adds it to #1026.

### A741. B16 to B20

BO's generator run (22 of 22 agreeing, five of them generator-only) is accepted as the A604 evidence. The replay provider keeps refusing malformed recordings. BO adds one serveable repeated-option fixture. C2 posts the run 8 inputs on #546 now from the current `main` SHA.

### A742. Stand-in identifiers (A728)

IL does one mechanical rename PR. It uses bare refs (`TX1`, `usr_aa`, `usr_bb`), regenerates the golden with `derive`, and edits only test fixtures across other owners' files. No production behaviour changes. SR reads it. This extends IL's allowlist for this PR only.

### A743. INP-01

An answered SLOT value joins the intent as Intent Object v(N+1) with `supersedes` (AMB-03), and the gate re-runs.

### A744. Webhook payload members

No G1 item needs them, and Tushe's event schemas are not available. BO writes SYNTHETIC placeholder payloads, labelled "not Tushe's shape", only if the inbound-event adapter requires them. Otherwise nothing is written until Tushe answers.

### A745. A680 and migration 0043

- A680: a T1 to T9 refusal becomes an early null-basis Decision Record, keyed by turn, tenant, verified principal, intent hash, pack version, outcome and reason (A574, A581, A590).
- #1021's CHECK must not forbid any early outcome that A680 records. If a conflict appears, C1 stops and lists it in the PR.

### A746. DOCS_READ_TOKEN

- It is a repository secret with no main-only restriction, which is a credential-exposure risk.
- **Founder's Done:** the GitHub Environment `docs-read` has been created, restricted to `main`, and the secret moved into it.
- SR's #1007 condition stands: the `tushe-fixture` Environment needs a Founder reviewer and a main-only rule before any secret is added.

### A747. Composition bundling

EL builds the remaining gaps as commits in a few bundled PRs (the table below), not one PR per gap. Each commit pair is red then green, and each bundle states which `/readyz` gaps it flips. The size justification goes in the PR body. All the owners on this table must complete each of their tasks on the items below and report on all without any exemption.

| # | Item | Owner | Needs |
|---|---|---|---|
| 1 | Evidence (config) | EL | #1018 (SR and Codex re-read at `a238bb3f`) and IL's #1023 |
| 2 | Candidates | EL | Labeller, CandidateRanker adapter and v2 retype (#1020 matcher and #1012 are merged) |
| 3 | Ownership | EL | The same bundle |
| 4 | Evidence read and seal | EL | #1018, #1023, per-tenant router |
| 5 | Reconciler | EL with C1 | EL's adapter (EffectiveFrozen, fail-closed allow-list). C1's FreezeReader. #958 is merged. |
| 6 | Policies | EL | #1018 (`buildPoliciesInput` is coded) |
| 7 | Clocks | EL | #1018 (the screen is the only blocker, EL's finding) |
| 8 | Confirmations | C1 with EL | #1028 appender (C1). EL builds the per-tenant adapters. |
| 9 | Planner | EL | #1002 is merged. Add and require `NOEMA_PLAN_TEXT_MAX_BYTES`. |
| 10 | Recorder | C2, C1, EL | #1027 is merged. C2 wires the permission once C1's FreezeReader exists. EL wires the Recorder. |
| 11 | Explainer | EL with C2 | #1015 is merged. #970 and #1031 (C2). EL wires. |
| 12 | Input gateway and write path | EL with C1 | #1019, #1004, #1016, #1026 (C1), and the A707 port |
| 13 | Confirmation route | EL | After C1's #1028 |
| 14 | Events route | IL then EL | #1005 merged. IL reads run 16. If the gap persists, EL finds the cause. |
| 15 | Worker | EL | Escalation start site (#945 merged) |
| 16 | Recovery reader | C1 | #996 is merged. Confirm the gap flipped. |
| 17 | Recovery write path | C1 | After EL's slice 4 reader |

## 2. What the Steward did, and where the rulings are silent

| Item | What was done |
|---|---|
| **AGENTS.md §11 (A738)** | Updated: the stand-in clock is 30 minutes (A686 amended); the re-read rule is A738's (a push that only adds tests, docs or status keeps READY; only a production-code push needs a fresh READY), replacing A669's byte-identical comment rule; the speed rules and the QA list are stated; stacking up to 4 PRs on a parent is allowed (the "never base a PR on another PR's branch" sentence is amended). Plan §4 (v1.31) states the 60-minute clock and A669; `AGENTS.md` governs until a plan version restates them (A671). The noema copy is re-pointed after this merges. |
| **Fix of docs#250 (SOT-C-35)** | Already fixed and merged: SOT-C-35 is a row of the conflicts table directly after SOT-C-34 (docs#250 at `2696958`, merged as `f94117b`). Nothing further. |
| **BEN-06 to BEN-09** | Already Done in `tasks.csv` on `main`; no change. |
| **[OPEN] entries (provisional, NON-CANONICAL)** | **OD-P-132** the `EPOCH` source of `outcome_bindings` (A740); **OD-P-133** the key ring bound 999 and the evidence key file format (A739); **OD-P-134** `LEXICON_REF_WITHOUT_FILE` (the Steward's wording; see below); **OD-P-135** the `DOCS_READ_TOKEN` remediation (A746). |
| **`LEXICON_REF_WITHOUT_FILE`** | The code is in the model service's lexicon loader (`understanding/compiler/lexicon.py`, `SKIPPED_CODE`) and its tests: a lexicon reference that names no file is skipped and logged under this code. A636 says Yoruba, Hausa and Igbo are measured only, with no lexicon. **The message named the entry without text:** the Steward wrote it from the code and A636; the Architect confirms or corrects it. |
| **A746** | The Founder's remediation (the `docs-read` Environment, main-only, secret moved) is recorded as done on the Founder's statement; the Steward cannot see GitHub's settings and records it as stated. The `tushe-fixture` Environment condition (SR's #1007) stays open in OD-P-135. |
| **A747's table** | Recorded as ruled, with its owners. The Steward does not move `tasks.csv` for it. |
| **A739 to A745** | Other owners' work; nothing for the Steward beyond this record. |
| **Next free ruling** | **A748** |
