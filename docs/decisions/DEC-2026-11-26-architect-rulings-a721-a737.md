# DEC-2026-11-26 · Architect rulings A721 to A737 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 26 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves, from a personal account, and merges it (A111, A638; AGENTS §2, item 3). |
| **Date** | 26 November 2026 |
| **Owner** | Principal Architect (the rulings); the Founders (the merge) |
| **Decides** | Rulings A721 to A737 (§1), every one Interim. |
| **Supersedes** | **A722 supersedes** A704's "characters" for the pattern length (bytes). **A723 replaces** A651's "exact name match" for production. **A728 applies the safer reading** against REQ-CTX-008's "added fields: Ignored" (CONFLICT SOT-C-35). **A729 waives** UND-05 as a Need of DATA-02. Otherwise nothing; per ruling in §1. |
| **Amends** | `conflicts-register.md` (SOT-C-35, new, in the table after SOT-C-34). **Plan v1.31** (new version: DATA-02's Needs is PLT-03 only; A729). `tasks.csv`: DATA-02 `blocked` false and the Needs regenerated. OD-P-112 and OD-P-120 updated in place. Nothing in the SoT or the PERD text. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder's personal approval (A111, A638)
- Date: 26 November 2026
- Owner: Principal Architect; Founders
- Decides: A721 to A737
- Decision: §1
- Rationale and evidence: the Architect's message of 26 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-04, INV-12, INV-14, INV-16, INV-22, INV-29; BD-08; AGENT-02, AGENT-11, AGENT-12, AGENT-15, AGENT-16; REQ-CTX-008, REQ-VER-002, REQ-DATA-002, REQ-TRU-009, REQ-STM-001, REQ-EXE-003, REQ-ENV-003; SoT §51
- Supersedes: see the Supersedes row above
- Migration notes: A723's `outcome_bindings` is an additive optional member of `pack.v1` (A698; AGENT-15 steps, one contracts PR for both Founders). A724: the store's `RequestEvents` interface gains a transaction parameter. A725: C1 updates the reconstruct projection and its golden in a separate Tier 1 PR. No migration is added by this record.

## 1. The rulings

### A721. Ops listener (#1013)

- Approved as proposed:
  - `NOEMA_OPS_TLS_CERT_FILE`, `NOEMA_OPS_TLS_KEY_FILE` and `NOEMA_OPS_CLIENT_CA_FILE`;
  - the certificate common name is the principal;
  - the tenant comes from the path;
  - TLS 1.3 floor.
- "Any certificate the operator CA signs is an operator" holds, on one condition: **the operator CA is a different CA from the service-to-service mTLS CA**, so a service certificate can never act as an operator. Netcheck asserts it.
- The admin DSN directory follows the existing DSN-directory naming, with the prefix `NOEMA_OPS_`. EL names it exactly, and IL mirrors it.

### A722. Evidence login names (#1018)

`NOEMA_EVIDENCE_DSN_DIR`, `NOEMA_EVIDENCE_KEY_FILE`, `NOEMA_EVIDENCE_KEY_MAX_ACTIVE` (bench value 2). The pattern length setting stays in bytes, so A704's "characters" is superseded. The composition carries the one verified pack through, with no fourth load. The counter stays in-process, and the exporter comes later.

### A723. Outcome bindings (unblocks slice 4, #1019)

- Add an additive optional pack member `outcome_bindings` to `pack.v1` (A698), per capability:
  - the outcome definition id;
  - a map from each predicate variable to `PLAN_PARAM:<param>`, `INTENT_ID` or `SUBJECT`;
  - `retry_safety`.
- C1 writes the schema, the packcheck rule and the SYNTHETIC fintech data in one contracts PR for both Founders. EL consumes it.
- Where the outcome definition or the descriptor already carries one of these, EL reads it there.
- This replaces A651's "exact name match" for production.

### A724. C1 approvals

- `maxProperties` 8 and `maxLength` 128 on `step_params` are approved (OPEN for the Founders).
- The store's `RequestEvents` interface gains a transaction parameter, and the approver actor kind passes through. Approved.
- C1 starts the TTL ceiling PR, A680, the `Result.Wait` mapping and the SLOT answer path now.

### A725. #1012

- `CANDIDATES_RESOLVED` is written as `core-trust`. The ranking is Trust's, and writing it under another power would break the separation.
- The payload uses integer basis points plus `resolved_target`. C1 updates the reconstruct projection and its golden in a separate Tier 1 PR.
- The recipient share is floored like every other feature (A560).

### A726. #1020

The phonetic tier stays off for the POC, and no contract changes.

### A727. #1015

- A no-write outcome is explained from its Decision Record, in a follow-up PR once #1015 merges. This matters for US-01, which has no write and so no verdict row.
- Latest verdict wins, if verdicts are append-only. The reader refuses whole when two verdicts for one receipt disagree.
- No signature re-check in the explainer (INV-29).

### A728. EVD-05 (#1017)

- An added field reads as UNKNOWN. That is the safer reading, and the Steward files the CONFLICT block against REQ-CTX-008 (**SOT-C-35**).
- A stale read of a state is caught at dispatch revalidation and by the A706 version token, not at read time. The Steward records it as a known limitation.
- Reads use a fresh connection each time (`DisableKeepAlives`), so the attempt count is exact.
- The read retry budget stays 0 beyond EVD-02's one refresh (OD-P-112 stays open).
- The stand-in's identifiers are fixed to valid portread references. IL fixes the stand-in, and the reader is never loosened.

### A729. DATA-02 (#1014)

- The UND-05 Needs condition is waived on A634 and A650.
- The pack's `tenant_zone` is the authority for the tenant offset. The lexicon's offset must equal it, which a test already pins.
- Money arithmetic code (M6) does not exist and nothing is invented. It stays OPEN until after G1.
- Every route validates request bodies against the JSON Schema, not the shape-only generated decoder (A655). C1 confirms the conversation POST does.

### A730. Codex findings outside the diff

- #733: Codex's blocker concerns EL's escalation start site, not the #733 diff. It becomes a condition on EL's start-site follow-up (A542: the path must not consume `Result.DecisionID` until it names the disposition's own intent). Codex re-reads #733 for the diff alone.
- #979: the transport is a separate PR by A682. BO's two review threads are answered with evidence: the red commit `41c0b6a` was seen failing in CI, and `--support` is fixed at `6c220b6`. Codex re-reads for scope.

### A731. #1003

C2 removes the mocked `w.store.err` case (AGENT-12). For the red run, C2 pushes one mutant commit that breaks identity propagation so the test is seen failing in CI (AGENT-11), then reverts it.

### A732. A604 offline check

C2 runs it against #1010's head (`adb97c1`) in a worktree, without waiting for the merge. The fixture directory is `benchmark/compile_acceptance/boundary-a604/fixture`, and the labelled set is `remedy_labelled.v1.json`. When it passes, C2 posts the exact dispatch inputs on #546.

### A733. BO

- The generating test for B02, B06 and B12 moves into the model job, where the model dependencies already exist, so there is no `.github` change.
- A duplicate delivery (same id, same body) must report `accepted: true`, as Standard Webhooks requires receivers to dedupe. If the relay rejects it, IL fixes the relay.
- Tushe's body members are not stated, so the caller supplies them from the relay's own schema. BO reads the relay code.

### A734. Voice and Intron

- OD-P-90 and OD-P-91 stay open with Intron. Interim: a missing per-token confidence counts as low (VOI-03), and the baseline runner uses one stream at a time.
- The 30 s maximum is confirmed as the Interim value.

### A735. FE's dependencies already exist

The `confirmation-answer.v1` TypeScript entry (`customer.ts`, `approver.ts`) and `conversation-response.v1` with its generated TypeScript are on `main`. FE integrates them now and closes #760 and #807. #957 stays draft.

### A736. Composition stacking

EL branches every gap off `main` and names its dependency. Independent gaps are built in parallel. The #1018 injection inputs merge first, then Policies, Evidence and Reconciler branch.

### A737. /readyz causes (EL's first task)

- Clocks is still a gap although #989 merged. The bench stack either does not mount the pack limits files or lacks a required setting.
- The events route is a gap because the eight A658 settings are not in the bench compose. #1005 adds them.
- EL finds the Clocks cause first and reports only that.

## 2. What the Steward did, and where the rulings are silent

| Item | What was done |
|---|---|
| **CONFLICT block (A728)** | Filed as **SOT-C-35** in `docs/poc/perd/conflicts-register.md`. Statements: REQ-CTX-008 "Schema drift: added fields: Ignored" against A728 "An added field reads as UNKNOWN". Safer reading applied meanwhile: UNKNOWN. Status Open: the Architect's Interim ruling applies it; the Founders' decision record and a PERD version restate REQ-CTX-008. |
| **Known limitation (A728)** | **A stale read of a state is caught at dispatch revalidation and by the A706 version token, not at read time.** A read can therefore pass a state that is already stale; the dispatch check (REQ-EXE-003) and the version token stop it before a write. Recorded here and in SOT-C-35's row; no debt entry is filed because the ruling names no shortcut or owner. |
| **[OPEN] entries (provisional, NON-CANONICAL)** | **OD-P-127** the `outcome_bindings` member (A723); **OD-P-128** `maxProperties` 8 and `maxLength` 128 (A724, OPEN for the Founders); **OD-P-129** `tenant_zone` as the authority for the tenant offset (A729); **OD-P-130** money arithmetic code M6 (A729, OPEN until after G1); **OD-P-131** the pattern length setting in bytes (A722). **OD-P-112** (retry budget) updated in place and stays Open (A728). **OD-P-120** updated in place (A722 supersedes "characters"). |
| **`payment.counterparty` and `facts-inventory.md` (A711)** | Not in `docs`: a search of the `docs` tree finds no `facts-inventory.md` and no `payment.counterparty` outside decision records. It lives in `noema` (C2's #970); the Steward changes nothing here. |
| **DATA-02 (A729)** | The UND-05 Need is waived. **Plan v1.31** (a new version; v1.30 is not edited) removes UND-05 from DATA-02's Needs (PLT-03 only), with `CR-2026-11-26-a729-data-02-need`; `tasks.csv` is regenerated and DATA-02 `blocked` is false (status Backlog). The time half still follows C1's contracts PR (an external blocker, owner C1). |
| **SR's conditions for the follow-up reads (SR's read of this pull request; not decisions)** | A721 and #1013: netcheck asserts the operator CA differs from the service CA, and every operator action is Recorded with the certificate's common name as principal. A723: a predicate variable no source can bind fails closed (no name-match fallback). A724: the approver actor kind comes from the verified session only (INV-12). A728: the stale-read limitation names the guarding test at dispatch revalidation (REQ-EXE-003). A733: a same-id delivery with a different body is still rejected. A731: C2's mutant commit is reverted before merge and the revert alters no assertion. |
| **A721** | Netcheck asserts the operator CA differs from the service mTLS CA (IL). The admin DSN directory's exact name is EL's; nothing for the Steward. |
| **A724 and A709** | The `step_params` bounds are OD-P-128; the interface change is C1's. |
| **A725, A726, A727, A730 to A737** | Other owners' work; nothing for the Steward beyond this record. A730's two items bind the follow-ups named. |
| **Next free ruling** | **A738** |
