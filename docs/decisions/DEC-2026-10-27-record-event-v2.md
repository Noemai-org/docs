# DEC-2026-10-27 · Record event v2: the PERD §32.1 event, the tenant-scoped genesis hash, nine grant-void reasons and the DUPLICATE_CREATE error code

| | |
|---|---|
| **Status** | Accepted by the Founders on 27 October 2026 (decisions given in a working session; they count once this record is merged). The Technical Co-Founder confirms by approving the pull request that adds it |
| **Date** | 27 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None. Resolves the two CONFLICT blocks of noema#77 (Record event contract against PERD §32.1; grant-void reasons against PERD §27.1). Applies [OD-P-34](../open-decisions.md#od-p-34), already closed by [DEC-2026-10-17](DEC-2026-10-17-open-decisions-closure.md) §3 ("Record event additions") |
| **Amends** | `contracts/` in `Noemai-org/noema` (a new major of `record-event`, of `reconstruction` and of `errors`). No PERD or SoT text changes |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the Founders (see the table above)
- Date: 27 October 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: REQ-AUD-001, REQ-AUD-002, REQ-AUD-003, REQ-EXE-001, REQ-EXE-003, REQ-EXE-004, REQ-EXE-007, REQ-API-002; INV-11; SoT §43.6; PERD §32.1, §32.2, §27.1, §26, §39.1. No SoT change; the requirement count stays 154
- Migration notes: §4
- Supersedes: None

---

## 1. The decisions

| | Decision |
|---|---|
| D1 | **A new major of the Record event schema is added beside v1: `contracts/schemas/record-event.v2.json`.** `record-event.v1.json` is not edited and stays valid for v1 documents (AGENT-15). v2 carries the PERD §32.1 additions to the SoT §43.6 fields: `schema_version` (major 2), `tenant_id`, `seq`, `payload_hash`, `actor`. `hash = SHA-256(prev_hash ‖ JCS(event without hash))`. The first event of a tenant's chain carries the tenant-scoped genesis hash `SHA-256("noema:genesis:" ‖ tenant_id)`; 64 zeros is not a valid v2 `prev_hash`. Hashes are written in the contract's `sha256:<hex>` form |
| D2 | **`reconstruction.v2.json` is added beside `reconstruction.v1.json`.** The two differ only in that the events a response carries (and the timeline's event type) are `record-event.v2`. v1 is not edited |
| D3 | **Six grant-void reasons are added to the three v1 had, nine in all, kept distinct, unknown values rejected:** `SIGNATURE_INVALID`, `EXPIRED`, `BINDING_MISMATCH`, `WRITES_DISABLED`, `REVALIDATION_UNAVAILABLE`, `REJECTED_STALE_VERSION`, beside `INTENT_SUPERSEDED`, `STATE_CHANGED`, `POLICY_SUPERSEDED`. They are carried by `GRANT_VOIDED` only |
| D4 | **Two defaults for details the PERD leaves open, to confirm:** (a) `actor` is the power in upper case, optionally followed by `:` and the principal ID (for example `EXECUTION:usr_88213`); (b) an event that refers to no object carries, as `payload_hash`, the hash of the empty object `{}`. The object an event refers to or details is stored beside the event, outside the hashed fields, so the verifier can check it against `payload_hash` |
| D5 | **No migration tooling.** This is the synthetic POC: the only events written before v2 are in test databases (the chain code of noema#77 wrote the PERD §32.1 fields under `schema_version` 1.0) and they are not converted |
| D6 | **One error code is added in a new major of the catalogue, `contracts/schemas/errors.v2.json`: `DUPLICATE_CREATE`, non-retryable.** It names a create that is conditional on absence and was refused because the target already holds a case for the same subject and epoch, made under another idempotency key (mock-case answers `412 PRECONDITION_FAILED`). It is none of the codes that exist: not `IDEMPOTENCY_CONFLICT` (the same key with another payload), not `REJECTED_STALE_VERSION` (a version token that moved; a create has none) and not the same key sent twice (an acknowledgement, REQ-EXE-007). The case adapter reports the transport class `DUPLICATE_CREATE` (the same string); Execution classifies it as `REJECTED_BY_TARGET`, the E10 row "4xx validation/business rejection". No execution state or other value list changes, so the SoT and the state registry are untouched. `errors.v1.json` is not edited. Given by the Founder on 27 October 2026 (answer 3 of the reply recorded in `status/ENV-03.md` of `Noemai-org/noema`) |

## 2. Rationale and evidence

The exact PERD lines (PERD v1.16, `docs/poc/perd/NOEMA_POC_PERD_v1.16.md`):

> §32.1: "The SoT §43.6 fields are `event_id`, `prev_hash`, `hash`, `written_by`, `event_type`, `object_ref`, `correlation_id` and `at`. To these the PERD adds, as a minor contract version [REC]: `schema_version`; `tenant_id`; `seq` (a monotonic per-tenant chain position); `payload_hash` (the hash of the referenced object's canonical JSON); `actor` (the power or service identity, plus the principal where relevant)."
>
> §32.1: "The hash is computed as: `hash = SHA-256(prev_hash ‖ JCS(event without hash))`. There is one chain per tenant [REC]. A per-correlation index supports reconstruction. The genesis event of each tenant chain carries `prev_hash = SHA-256("noema:genesis:" ‖ tenant_id)`."
>
> §27.1 (the steps that void a grant, verbatim):
>
> ```
>  E1  load grant by grant_id; verify HMAC (any active key_id)                  → else VOID: SIGNATURE_INVALID
>  E2  check not_before ≤ now < expires_at (clock source)                        → else VOID: EXPIRED
>  E3  check intent_hash == latest admitted intent's hash                         → else VOID: INTENT_SUPERSEDED
>  E4  check decision outcome == ALLOW, decision policy_version still ACTIVE      → else VOID: POLICY_SUPERSEDED
>  E5  check plan_hash/plan_step match the stored plan; capability registered,
>      non-prohibited, adapter exists; params_hash == hash(params)               → else VOID: BINDING_MISMATCH
>  E6  check tenant kill switch off; circuit closed                               → else VOID: WRITES_DISABLED
>  E7  REVALIDATE: re-read only the descriptor's revalidation_reads (fresh, under
>      effective freshness); compare to evidence_set; check ownership; check
>      freeze                                                                     → else VOID: STATE_CHANGED / STALE
> ```
>
> REQ-EXE-003: "A read failure voids the grant (`REVALIDATION_UNAVAILABLE`), and Trust decides next."
>
> REQ-EXE-004: "A version mismatch gives `REJECTED_STALE_VERSION`: the grant is void, the case returns to Trust, and there is no automatic retry."
>
> §27.1 E10: "classify transport result → execution_state: 2xx with external ack → ACKNOWLEDGED; 409/412 version mismatch → REJECTED_STALE_VERSION; 409 duplicate (same key) → ACKNOWLEDGED (ack = existing ref); 4xx validation/business rejection → REJECTED_BY_TARGET; timeout / connection reset / 5xx / no response → OUTCOME_UNKNOWN; adapter-detected non-retryable defect → FAILED_TERMINAL" (the PERD lays these out one per line).
>
> REQ-EXE-007: "a duplicate-create response (200 with an existing reference, or 409 duplicate) becomes `ACKNOWLEDGED` with `external_ack` set to the existing reference [REC]".
>
> §39.1: "At minimum: `INPUT_INVALID`, … `IDEMPOTENCY_CONFLICT`, `REJECTED_STALE_VERSION`, … `INTERNAL_SAFETY_BLOCK`." (the catalogue is a minimum; no code for a create refused because the case exists under another key is in it, nor in `errors.v1.json`, `enums.v1.json` or the state registry).

**PERD silence, checked on 27 October 2026 (D4).** PERD v1.16 defines `payload_hash` and `actor` in one place, §32.1, in the words quoted above: "the hash of the referenced object's canonical JSON" and "the power or service identity, plus the principal where relevant". It gives no string form for `actor`, and says nothing about an event that refers to no object. D4 is therefore not read from the PERD; it stays a default until the Founders choose a form.

The bracketed `[REC]` labels in §32.1 are the "Record event additions" of the PERD §67.3 defaults that [DEC-2026-10-17](DEC-2026-10-17-open-decisions-closure.md) §3 closed as OD-P-34; this record applies them and does not reopen them. The PERD text stays as it is and drops the label at its next version (PERD P.2).

The conflict: `contracts/schemas/record-event.v1.json` says "The first event of a tenant's chain has prev_hash of 64 zeros", has none of `seq`, `payload_hash` or `actor`, and sets `additionalProperties: false`; its `GrantVoidReason` lists three values while PERD §27.1 and REQ-EXE-003 name nine. The Record writer built for noema#77 follows the PERD, so the two disagreed. v1 cannot be edited in place, so v2 is a new file (D1).

## 3. Agent decisions

1. D4 (a) and (b) are the smallest forms that make the PERD's words checkable (AGENT-02); both are recorded as defaults for the Founders to confirm. If the Founders choose another form, it is a v2 minor.
2. D6: `412 PRECONDITION_FAILED` is read as a business rejection (E10, `REJECTED_BY_TARGET`) because the write did not happen and no version token was involved; the Founder ruled out `REJECTED_STALE_VERSION`. `REJECTED_BY_TARGET` is the only existing state that fits; a new execution state would need a SoT change and was not made. The catalogue code and the transport class share one string so the receipt's `transport_result` names the same thing as the error catalogue; the receipt's `transport_result` value set stays undefined (state registry §4).
3. `REJECTED_STALE_VERSION` is both a receipt `execution_state` and, via a void grant, a void reason (PERD §26). The two are different fields and keep their own value sets. Today the controller never calls `Void` with it (the grant is already spent when the target refuses the version): wiring that is task EXE-04, not this record.
4. `reconstruction.v2` is added in the same change because a reconstruction response carries Record events; nothing serves either version yet (REC-03).

## 4. Migration notes (AGENT-15)

- A breaking change (new required fields, a different genesis rule, a larger enum), so a new major in a new file. Readers that accept v1 documents keep working on v1; the Go Record writer, the chain verifier and the benchmark runner's reconstruction reader move to v2 in the same pull request.
- Generated models: none exist yet (codegen is CON-03); nothing to regenerate.
- Golden vectors: no existing vector's digest changes (none involves a Record event or a void reason; the test-only key of `grant_signing_vectors` is untouched). A new family, `record_event_chain_vectors`, is generated by `tools/record_chain_ref.py` and replayed by the Go tests; `--check` proves it reproducible.
- Fixtures: `contracts/fixtures/{valid,invalid}/record-event.v2/` and `reconstruction.v2/`, generated by the same tool with real hashes.
- D6: `errors.v2.json` is `errors.v1.json` plus the one code (a larger closed enum is breaking for a strict reader of v1, hence a new major). Fixtures in `errors.v2/` carry every v1 fixture plus a valid and an invalid `DUPLICATE_CREATE` (marked retryable). No producer writes the code yet. The Go transport classes of the same name are added with it.

## 5. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted | 27 October 2026 | Working session, summarised here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
