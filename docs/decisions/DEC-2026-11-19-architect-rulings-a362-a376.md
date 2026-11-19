# DEC-2026-11-19 · Architect rulings A362 to A376 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 19 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 19 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Fifteen rulings, A362 to A376 (§1). A362 is listed in the Architect's heading but has no text in the message the Steward received (§2). |
| **Supersedes** | **A363 withdraws the `planned:<node>` rule** (SR's noema#764, point 8) and **withdraws the last bullet of A345** (`produced_by`); it removes `produced_by` from noema#765. **A364 replaces `may_write` with `write_when`** (the `may_write` of A342 and `DEC-2026-11-19-architect-rulings-a341-a357`). **A366 adds to A186's lookup key.** **A370 settles** the reconstruction route (PERD §39.4 and A110 win). Otherwise per ruling, in §1. |
| **Amends** | PERD v1.27, a new Proposed version (REQ-TRU-009: the A365 clarification, §2); the debt register (DEBT-54); the migration ledger on noema#183 (0034). Nothing in the SoT or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 19 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A362 to A376
- Decision: §1
- Rationale and evidence: the Architect's message of 19 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-01, INV-12, INV-14, INV-17, INV-21; AGENT-11, AGENT-12, AGENT-13, AGENT-16, AGENT-27; REQ-TRU-002, REQ-TRU-009, REQ-CTX-004; PERD §21.3, §23, §39.4; SoT §43.2a
- Supersedes: see the Supersedes row above
- Migration notes: migration 0034 (C1; only if the decision lookup key needs a column, A366); `write_when` is a pack-schema change and graph-node `params` a further one (A364, A369; the owners write the migration notes)

## 1. The rulings, as given

### A362 (interim)

Named in the Architect's heading. No text came with it. See §2.

### A363 (interim): `planned:<node>` withdrawn.

SR's noema#764, point 8's road, is accepted in full.

- T11 never evaluates a rule over a produced fact.
- The plan is the graph's runnable steps: the ones whose preconditions hold on the current facts.
- Authorized is the capabilities of runnable steps, plus the intent's own.
- The first decision therefore plans `create_escalation_case` alone. Steps that need the case wait for a later Trust evaluation after the earlier step is verified. That later evaluation uses the real `case_id` from the case-system evidence. It is post-G1 continuation.
- `produced_by` is removed from noema#765, and A345's last bullet is withdrawn.

*Supersedes or changes:* withdraws the `planned:<node>` rule and the last bullet of **A345**. Changes noema#765.

### A364 (interim): NeedsWrite.

- `may_write` is replaced by `write_when`. It is a predicate in the pack's predicate language over the intent node's slots, and `packcheck` type-checks it.
- For the investigate node it is `question_type == 'ESCALATION_REQUEST' or requested_remedy != null`.
- NeedsWrite evaluates it on the admitted intent's resolved slots. An unevaluable predicate is an error, which ends in UNKNOWN.
- EL changes noema#765, and C1's Writes adapter reads the field.

*Supersedes or changes:* replaces `may_write` (**A342**).

### A365 (interim): The confirmation binding's evidence component (SR on noema#759).

- The Evidence layer mints a new id on every read, so a hash over ids never matches again and the approver is asked forever.
- The confirmation binding uses a content hash: the sorted (source, source record id, payload hash) triples, with ids left out.
- The decision's and the grant's `evidence_set_hash` stay as they are.
- Changed payloads still mean `BindingChanged` and a fresh CONFIRM.
- This is a clarification of "evidence set" in PERD v1.26. It stays a flagged note for the Founders' next SoT version.

*Supersedes or changes:* clarifies REQ-TRU-009 and SoT §43.2a's `binding_hash` member (flagged for the SoT; the PERD v1.27 text carries it, §2).

### A366 (interim): A186's key.

The decision lookup key adds the confirmation state: the request id plus its resolution, or "none". Without that, a declined or accepted CONFIRM would keep returning the stored CONFIRM. C1 adds a column if needed (ledger migration 0034).

*Supersedes or changes:* adds to **A186**'s key.

### A367 (interim): Composite policy version.

The shape is `sha256:<64 hex>`, which the Record guard already exempts by type. It is not `ps:`, which the payload guard blocks.

### A368 (interim): The confirmation store and route.

noema#756:

- one answer per request, enforced by the database;
- application times are bound to the database clock;
- `intent_version >= 1`;
- the trigger refuses an answer after expiry or supersession;
- the header comment about foreign keys is corrected.

noema#754:

- `ROLE:<role>` means the session role of that exact name (the A1 roles);
- a second answer returns 409 `IDEMPOTENCY_CONFLICT`;
- an ineligible attempt records a `SECURITY_EVENT` of kind `CONFIRMATION_REFUSED`;
- other refusals get a fixed-text log line only.

### A369 (interim): EL's four questions.

- **Plan on the new-request path:** the Confirmations adapter asks the Planner for the plan hash (Q-A). The intake builds the plan only at T14.
- **`CONFIRMATION_EXPIRED`:** the Recorder writes it, in the same transaction as the new CONFIRM decision for the superseding request. There is no sweeper in G1.
- **PackVersion:** it comes from the pack manifest (noema#734) through the loader.
- **Graph node params:** each graph node gets a `params` member of name to `{slot}` or `{const}`, validated by `packcheck`.

### A370 (interim): C1's questions.

- **noema#745:** `RequestedCapability` becomes a field on `AdmittedIntent`, replacing the second port. It is a follow-up PR before wiring, and noema#745 itself isn't held.
- **noema#771:** the same-version document change stays as DEBT-23.
- **Stub queriers (AGENT-12):** failure injection must be real. Replace the stubs in `keyannounce` and `policystore.Published` with real database-induced errors (triggers, as in noema#748).
- **Reconstruction route:** PERD 39.4 and A110 win. The route is audit-only. Ops see the investigation view.
- **noema#770:** the audit route is C1's, built next.

### A371 (interim): Wiring order.

The conflicts and the final `main.go` follow the lane files in A313. No new rule.

### A372 (interim): C2's questions and the compile run.

- **The next run:** one dispatch carrying all three fixes on luna: noema#774 diagnostics, noema#776 schema, noema#777 pool. No Terra.
- **A361:** the run also records the two arcs' own inputs, so the replay provider covers US-01 and US-06 exactly. The cost is negligible.
- **Pool-refused calls:** add a distinct failure class, `POOL_REFUSED`.
- **Injection screen:** a screener call refused locally must fail the compile closed (UNKNOWN). It must never pass silently. EL and C2 do this before G1.

### A373 (interim): Voice, FE and IL.

- A334 reading confirmed: Tier 2 is Codex, CI and one Founder.
- noema#640's missing redacted failure codes are accepted as a noted deviation.
- noema#625 pushes now. noema#728 merged.
- noema#616 pushes its request-id fix.

### A374 (interim): IL's missing text.

The A354 to A356 record is committed at `docs/decisions/DEC-2026-11-19-architect-rulings-a341-a357.md`. C1's publish command is `cmd/policypublish` (noema#771). The noema#727 and noema#728 follow-ups are the open Codex items on those PRs.

### A375 (interim): BO.

The package row for US-01 must show zero grants and no write. Only US-06 shows the single `GRANT_SPENT`, `DISPATCH_ATTEMPTED` and the key-verified unknown outcome.

### A376 (interim): Steward.

Record these rulings, and PERD v1.26 covers the A365 clarification. Instructions at its end: record A362 to A376; PERD v1.26 adds the A365 clarification (evidence component by content hash); file debt for the epoch increment; ledger entry migration 0034 (C1); docs#206 merges now (option (b)); merge docs#209 when Codex reads it.

## 2. What the Steward did, and where the rulings are silent

- **A365 is in PERD v1.27, not in v1.26.** The Architect asked for the clarification in v1.26. v1.26 was merged (docs#210) before this record, and a PERD is never edited in place (AGENTS §11; the PERD README), so the Steward made a new Proposed version, v1.27 (`CR-2026-11-19-A365-perd-v1.27`): REQ-TRU-009 says the evidence component of `binding_hash` is a content hash; everything else of v1.26 is carried. The SoT is not edited; the clarification stays a flagged note for the Founders' next SoT version, as A365 says. **Please confirm** that v1.27 is what the Architect meant by "v1.26 adds it", or say otherwise.
- **A345's last bullet is withdrawn (A363).** A345 is in `DEC-2026-11-19-architect-rulings-a341-a357` (docs#210, not yet merged). That record is not edited; this one says A363 withdraws it. If both merge, this record wins on the point.
- **`may_write` to `write_when` (A364).** The `may_write` of A342 is replaced. `packcheck` and the pack schema change belong to EL (noema#765); the Steward records only.
- **DEBT-54 is filed** (the `logical_resolution_epoch` increment path, A345 S1, which the earlier record left unfiled for want of an owner). Owner C2, tier 3 proposed, before G2: these are defaults, and the Architect may change them.
- **Migration 0034 is registered** on the ledger (noema#183, a comment posted by the Steward): C1, only if the decision lookup key needs a column (A366). The ledger then reads: on `main` 0029 and 0031; assigned 0030 (noema#716), 0032 (noema#756), 0033 (C2), 0034 (C1); reserved 0022; next free 0035.
- **A362 has no text** in the message the Steward received. A358 to A361 were not in it either (A361 is quoted in A372). The Steward records A362 as a heading only and invents nothing; the Architect sends the text, or says it is withdrawn.
- **docs#206 and docs#209.** A376 says docs#206 merges now (option (b)) and docs#209 merges when Codex reads it. docs#206 has since been merged by a Founder. **The Steward does not merge or approve** (AGENTS §11); a Founder who did not author the pull request merges each. PERD v1.26 (docs#210) already carries docs#209's T13 row, so the two do not conflict.
- **Next free ruling: A401** (A377 to A379 are the Founder's, recorded separately).

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-19-architect-rulings-a341-a357` | A341 to A357 | |
| This record | A362 to A376 (A363's `planned:<node>` rule and A345's last bullet withdrawn) | |
| `DEC-2026-11-19-founder-intron-data-terms-a377-a379` | A377 to A379 | |
| Not received | A358 to A361, A380 to A392, A393 to A400 (see `DEC-2026-11-19-architect-corrections-a371-a345s4`) | **A401** |
