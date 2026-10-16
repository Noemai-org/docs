# DEC-2026-10-16 · Contract and pack clarifications: evidence-set hash, intent model, pack status, team rules

| | |
|---|---|
| **Status** | Accepted by the Founder on 16 October 2026. The Technical Co-Founder confirms by approving the pull request that adds this record |
| **Date** | 16 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Amends** | DEC-2026-10-16-execution-reset, E2 and E12; PERD v1.5 §21.3 and REQ-CTX-004 (by PERD v1.6); plan v1.5 (by plan v1.6) |
| **Does not amend** | The SoT. Every item here applies or makes precise what SoT §13.2, §15.3, §34.3, §35.5 and §38.5 already say |
| **Evidence** | Agent report on PRs docs#1 to #8, brain#1 and noema#1 (16 Oct 2026); recomputation of every vector in `contracts/fixtures/golden_vectors.json` (16 Oct 2026); the ported `packs/fintech_v1.json` and `tools/packcheck.py` read against SoT §15.3 and PERD §20 |


**Record fields (decisions README template).** The table above gives Status, Date, Owner, Amends, Does not amend and Evidence; the template headings it lacks point to the sections below.

- Status: Accepted by the Founder (see the table above)
- Date: 16 October 2026
- Closes: none. No entry of SoT §46 is decided here
- Owner: Founder and Technical Co-Founder
- Decision: C1 to C8 and the settlement in C10 (C9 lists what stays the same)
- Rationale and evidence: the Evidence row above, and the "Background", "The problem" and "What was rejected, and why" paragraphs in C1 and C2
- Affected requirement IDs / SoT sections: PERD §20.4, §21.3, §27.2, REQ-INT-005, REQ-CTX-004 (by PERD v1.6); plan v1.6 (G7, §4, task cards); no SoT change; the requirement count (153) and every invariant are unchanged (C9)
- Migration notes: C3 (task status), C4 (noema#1 merges as a pure port; noema N2 follows), C7 (boundary map)
- Supersedes: None. It amends DEC-2026-10-16-execution-reset E2 and E12

---

## C1. `evidence_set_hash`: the construction

**Background.** The committed vectors use this construction, though it was never written down. The coding agent reported that it couldn't reproduce them. It can be reproduced: both committed vectors (`empty_evidence_set` → `e3b0c442…`, `unsorted_evidence_items` → `85f74074…`) match the construction below exactly. It reuses the length-prefix encoding `LP()` that PERD §27.2 already defines for the idempotency key, so the two languages implement one primitive, not two.

**The construction (normative):**

1. **Input.** The evidence items of one sealed context snapshot. Each item contributes exactly two strings: `evidence_id` and `payload_hash`.
2. **Validation.** Reject the whole input, with no hash computed, if:
   - any `evidence_id` is empty or appears more than once;
   - any `payload_hash` does not match `^sha256:[0-9a-f]{64}$`.

   Nothing is normalised silently.
3. **Order.** Sort the items ascending by the UTF-8 bytes of `evidence_id`. Arrival, database, map and adapter order never matter.
4. **Bytes.** `B = ‖ over sorted items of ( LP(evidence_id) ‖ LP(payload_hash) )`:
   - `LP(x)` is a 4-byte big-endian length followed by the UTF-8 bytes of `x`;
   - `payload_hash` is encoded as its full string, including the `sha256:` prefix;
   - there are no separators, prefix, BOM or trailing newline.
5. **Digest.** `evidence_set_hash = "sha256:" + lowercase_hex(SHA-256(B))`.
6. **Empty set.** The empty set hashes to `sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (SHA-256 of zero bytes). That is a fact about the function, not a permission: **Trust never issues a grant over an empty evidence set.**
7. **Scope.**
   - The hash covers only the `(evidence_id, payload_hash)` pairs.
   - Payload integrity is carried by each `payload_hash`.
   - Timestamps, freshness, `fact_status`, the snapshot ID and database metadata are excluded.
8. **Duplicates before sealing.** Two items with the same source, source record, version and payload hash are one fact (PERD §21.4). The snapshot keeps only the one with the bytewise-lowest `evidence_id` (the first read, since IDs are ULID-ordered). Duplicates never reach the hash input, so step 2's duplicate-ID rejection only ever fires on a bug.
9. **Immutability.**
   - A sealed snapshot and its hash never change.
   - Adding or changing evidence creates a new snapshot (REQ-CTX-004).
   - Recomputing from the stored rows must equal the stored value (nightly job).

**Golden vectors.** These are for the shared fixture file. The first two are already committed; the last two are new.

| Name | Input (`evidence_id` → `payload_hash`) | Expected |
|---|---|---|
| `empty_evidence_set` | none | `sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `unsorted_evidence_items` | `evd_03_transaction` → `sha256:cccc3333…1111`; `evd_01_account` → `sha256:aaaa1111…3333`; `evd_02_kyc` → `sha256:bbbb2222…4444` (as committed) | `sha256:85f7407496250253e53b326daa8e96960b8a338eaf8c04782f0d0507a648b48c` |
| `single_item` (new) | `evd_01_account` → `sha256:` + 64 × `0` | `sha256:47dfb81eb6a8175a50e80698b3fa944350b08eeb301d48ecb2fa7651cca67f3b` |
| `sort_key_is_evidence_id` (new), supplied in this order | `evd_02_switch` → `sha256:` + 64 × `0`; `evd_01_ledger` → `sha256:` + 64 × `f` | `sha256:15fd16c042481a7a3a366578ecc90be5eca5e255cd1d8d47ea68b33f97398177` |

- **Why the fourth vector is needed.** In the committed three-item vector, sorting by `evidence_id` and sorting by `payload_hash` happen to give the same order, so that vector cannot detect the wrong sort key. Sorting the fourth vector by `payload_hash` gives `sha256:98bbe936…`, so it can.
- **Negative fixtures, each of which must be rejected:**
  - a duplicate `evidence_id`;
  - a `payload_hash` in uppercase hex;
  - a `payload_hash` without the `sha256:` prefix;
  - a `payload_hash` of 63 hex characters;
  - an empty `evidence_id`.

**What was rejected, and why.** An outside proposal hashed a JCS array of pairs instead.

- It contradicts both committed vectors; its empty set, for example, gives `4f53cda1…`.
- It answers a question that was already answered, and would have orphaned the committed vectors.

Its validation, immutability and test rules are good, and they are kept above.

**The idempotency key.** Both committed `idempotency_key_vectors` reproduce exactly under PERD §27.2 (LP encoding, `idk_v1_` prefix). No change is needed.

## C2. Intent model: two nodes, not ten classes

**The problem.**

- The ported fintech pack defines ten upper-case `intent_classes` (`TRANSFER_FUNDS`, `VERIFY_TRANSACTION`, `DISPUTE_TRANSACTION`, `RECOVER_FUNDS`, `VIEW_PAYMENT_STATUS`, `VIEW_TRANSFER_STATUS`, `SELECT_BENEFICIARY`, `REQUEST_REFUND`, `REPORT_UNAUTHORIZED_TRANSACTION`, `INVESTIGATE_EXCEPTION`).
- That is a different model from the one the SoT and PERD define, not a naming problem.
- It also contradicts the money boundary in two places:
  - `TRANSFER_FUNDS` is an intent marked `WRITE`;
  - `REQUEST_REFUND` is "routed via escalation case".

  In the SoT and PERD, a refund or transfer request is a prohibited remedy that Trust rejects (REQ-INT-005, golden example G-E).

**The decision.** Every pack is rewritten to SoT §15.3 shapes. The fintech pack has exactly **two intent nodes**:

| Node | Slots | Outcome definitions |
|---|---|---|
| `fin.payments.exception.investigate` | `subject_resource`, `amount`, `counterparty`, `when`, `question_type` (Reference; vocabulary from PERD §20.4), `requested_remedy` (Reference to a `fin.cap.*` ID) | `fin.outcome.exception.status_explained`, `fin.outcome.exception.case_opened`, `fin.outcome.complaint.logged` |
| `fin.meta.out_of_scope` | none | none. Trust returns REJECT `OUT_OF_SCOPE`; no capability is evaluated (PUS-03) |

**The ten classes, mapped and then deleted:**

| Ported class | Becomes |
|---|---|
| `VERIFY_TRANSACTION`, `VIEW_PAYMENT_STATUS`, `VIEW_TRANSFER_STATUS`, `INVESTIGATE_EXCEPTION` | `investigate` with `question_type` = `STATUS` (or `WHY`, `REVERSAL_STATUS`, `CASE_STATUS` as said) |
| `DISPUTE_TRANSACTION`, `REPORT_UNAUTHORIZED_TRANSACTION` | `investigate` with `question_type` = `ESCALATION_REQUEST`; routing by policy (fraud to `FRAUD_REVIEW`) |
| `TRANSFER_FUNDS` | `investigate` with `requested_remedy` = `fin.cap.transfer_funds`, then REJECT `PROHIBITED_CAPABILITY` |
| `REQUEST_REFUND` | `investigate` with `requested_remedy` = `fin.cap.initiate_refund`, then REJECT |
| `RECOVER_FUNDS` | `investigate` with `requested_remedy` = `fin.cap.reverse_transaction`, then REJECT; the customer may still ask for `ESCALATION_REQUEST` |
| `SELECT_BENEFICIARY` | Not an intent. It is counterparty resolution inside the node (`candidate_search`, CLARIFY) |

**Rules:**

- **No legacy labels anywhere.** Nothing outside the pack uses the upper-case labels yet, so they are deleted, not kept "at a boundary".
- **Node IDs.**
  - An Intent Object's `intent_node` must exist in the loaded pack.
  - A `question_type` value is never a node.
  - An unknown node or slot is rejected at the schema gate.
- **The conformance packs follow the same shapes,** within the SoT §15.4 cap: ≤ 3 nodes, 1 trust profile, 1 outcome definition, no adapters, no executed capabilities.

**What was rejected, and why.** An outside proposal mapped `TRANSACTION_EXCEPTION`, `POLICY_INQUIRY` and `OUT_OF_SCOPE`. Those three values come from an older specification and appear nowhere in this pack. The proposal didn't read the pack it was fixing, and it assumed noema#1 had already merged.

## C3. Status of CON-04, PCK-01 and PCK-02 (amends E12)

E12 said PCK-01 and PCK-02 would be done once the port merged. That was too generous.

| Task | Status | Why |
|---|---|---|
| CON-04 | **Open** | Every committed vector now reproduces (C1). Done only when Go and Python each compute every vector in CI |
| PCK-01 | **In progress** | Reusable as ported: the 20 capability descriptors, which match SoT §34.3 (12 allowed, 8 prohibited), and the Action Graph. To rewrite to SoT §15.3 shapes, against the CON-01 pack schema: intent nodes (C2), trust profiles (SoT fields: `risk_class`, `authority`, `policy_templates`, `clocks`, `approvals`, `prohibited_capabilities`, `evidence_required`, `max_evidence_age_seconds`, `data_sensitivity`), outcome definitions (success predicate in the §43.7 expression language, verification sources, settle window), evidence-source descriptors (vendor-free IDs), and policy rules as evaluable templates rather than prose |
| PCK-02 | **In progress** | `packcheck` checks references, risk against consequence, prohibited graph nodes, cycles and write requirements, and its eight bad packs fail correctly. It lacks three things the task requires: validation against the CON-01 pack schema, predicate type-checking, and template coverage |

## C4. noema#1 merges as a pure port

- No item-4 or item-5 commit is added to noema#1.
- It merges as the port, plus the item 1 to 3 fixes already on it.
- C1's extra vectors, a fixture README and a status banner on `packs/` go in a separate pull request (noema N2) after noema#1 merges.
- The pack rewrite (C2, C3) is PCK-01 work in week 1, after CON-01's pack schema exists.

## C5. PR 9 is not needed

The `brain` folders for incidents, benchmarks, systems and integrations hold only README scaffolds (checked at `876091b`). There is nothing to move. PR B1's pointer files are enough.

## C6. G7 is "External readiness"

- **The names differ.** The PERD (§69) names G7 "External readiness"; plan v1.5 says "Demo readiness". The PERD outranks the plan.
- **The rename.** The plan is renamed to match.
- **The conditions are the union of the two:**
  - DoD signed;
  - every external number has n, method, bound and CI;
  - clocks labelled SYNTHETIC;
  - no ROI claim;
  - D1 to D10 run from the engine;
  - kill switch, rollback and incident playbook drilled.

  The Fri 13 Nov 09:00 dry run is how G7 is met for the demo.

## C7. Repository mapping is closed

`docs/engineering/boundary-map.md` still calls the repository mapping open. DEC-2026-10-13 closed it: one code repository `noema` with the R1 layout, `benchmark-heldout` separate, and `docs` and `brain` for documentation. The file is updated to say so.

## C8. Team rules (amends E2)

1. **The benchmark owner is the Founder.**
   - The Founder does not drive C1 or C2 build tasks: Record, investigation state, Trust, Execution, Outcome, Temporal workflows, the model service, the Evidence Layer, reconciliation and ambiguity. Plan §4 says B "must not be C1 or C2"; that is the independence the benchmark depends on (OD-16).
   - The Founder may review those pull requests, since reviewing is not building.
   - Every other role is shared, and either founder picks it up.
2. **Two external people for the comparison arms,** as plan §4 already requires:
   - ARM (arm builder for A, B and D in week 4);
   - REV (independent arm reviewer, a few hours, OQ-02).

   Both are confirmed, under NDA, by GOV-11 (G2 review, Fri 30 Oct). E2's "one external engineer" is corrected.
3. **Work in progress is a flow limit on open pull requests.** Counting tasks per day does not measure work in progress: the plan's daily dates are targets, and coding agents do the execution, so the real constraint is review.
   - **Limit.** Each founder may have at most 4 open pull requests they drive, of which at most 2 are P0. The agent starts no new task for that founder until one of them merges.
   - **Review time.** Each pull request is reviewed by the other founder within the same working day, and by 09:00 the next day at the latest.
   - **Slippage.** Gates handle it, not daily dates. At the G1 review (GOV-07, Mon 26 Oct 10:00), if G1 has not passed, or fewer than 80% of the week-1 P0 tasks have merged, cut-line items 4 and 5 below are applied that day.
   - **A later gate fails.** Its date moves (SoT §40.2), and the founders set the new demo date in the gate record.
4. **Scope.** Two people is below the plan §4 staffing table, which triggers SR-03: "apply the cut line from the top". Items 1 to 3 are cut now:
   1. demo voice breadth beyond English and Pidgin (the other three locales are still measured);
   2. UI polish beyond the PERD §40 minimum;
   3. comparison arms E and F (reported "not tested").

   Items 4 and 5 (arm D then A0; P2 requirements) are applied at the G1 review on Mon 26 Oct if the trigger in point 3 fires (see C10 for the settlement of this point). The never-cut list is unchanged.

## C9. What stays the same

- The SoT.
- Every invariant.
- 153 requirements.
- Every gate's conditions (C6 only joins the two wordings of G7; C10 only says when G7's DoD condition is assessed).
- Every Tushe date.
- The money boundary.

## C10. Settlement (16 Oct)

The open items from the review of docs#9, docs#10, docs#11 and noema#2 are decided here. C8 point 3 above already carries the work-in-progress rule (F1) in its final form. Nothing here needs an SoT edit, changes a gate's conditions beyond the clarification in point 5, or touches `benchmark-heldout` or `noema-org`.

1. **BEN-17 is split, to keep benchmark-owner independence (F2).** Same date as BEN-17.

   | Task | Owner | Scope | Done when |
   |---|---|---|---|
   | BEN-17a | B | Triage the full-suite failures: assign every Tier 0 and S1 failure, and write its regression case first (development suite only; never held-out) | Every failure assigned, with a regression case |
   | BEN-17b | C1, C2 | Fix each assigned failure until its regression case passes. Depends on BEN-17a | 0 open Tier 0 or S1 failures at 17:00 |
2. **CON-01 owns the pack schema (F3).** JSON Schemas for every contract object, including packs, live in `/contracts` (PERD §36.1). CON-01 delivers the pack schema in its first pull request, on Mon 19 Oct, so that PCK-01 can start.
3. **PCK-01 and PCK-02 dates are confirmed (F4).** PCK-01 is on Tue 20 Oct and PCK-02 on Wed 21 Oct. Every task that depends on them is dated on or after Wed 21 Oct; any that was not is corrected in plan v1.6.
4. **GOV-21 and GOV-23 are confirmed (F5).** GOV-21 (engage ARM and REV under NDA) is due Fri 30 Oct, and GOV-11 depends on it. GOV-23 (archive `noema-org`) no longer depends on PCK-02: noema#1 has merged, so it is ready, and the Founder archives `noema-org` now.
5. **The cut line, item by item (F6), and G7 (F7).**

   | Item | What is cut | How it is recorded |
   |---|---|---|
   | 1 | Demo voice beyond English and Pidgin | VOI-04: TTS for English and Pidgin only. The other three locales are still recorded and measured (VOI-06, VOI-09, G5 unchanged) |
   | 2 | UI polish beyond the PERD §40 minimum | UI-01 to UI-06 carry "Scope: PERD §40 minimum only (DEC C8)". WCAG 2.2 AA stays, because it is in the requirement |
   | 3 | Comparison arms E and F | ARM-04: E and F written up as "not tested". A0 stays, pending the trigger in C8 point 3 |

   G7 must pass before the demo, so its "DoD signed" condition reads: *DoD signed at G6 (GOV-16, Thu 12 Nov 18:00) for every PERD §68 item that does not depend on the demo itself.* GOV-17 (Fri 13 Nov 16:00) stays the POC-done decision (GO, CONDITIONAL or NO-GO) and closes the demo-dependent items. "DoD (pre-demo items)" is added to GOV-16's Done when.
6. **`AGENTS.md` (F8).** §3 step 3 is updated to the C8 point 3 rule, version-agnostic: "at most 4 open PRs per driving founder, at most 2 of them P0; see the current plan §5".
7. **Additions accepted (F9).** The "Record fields" block in this record and the Tests-line entry on REQ-CTX-004 in PERD v1.6 stay.

## Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founder | Approved | 16 Oct 2026 | Written instruction to the coding agent |
| Technical Co-Founder | Confirms | Date of approval | Approving review on the pull request that adds this record |
