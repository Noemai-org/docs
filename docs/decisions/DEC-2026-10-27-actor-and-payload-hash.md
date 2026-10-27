# DEC-2026-10-27 · The Record event's emitter, principal and payload hash

| | |
|---|---|
| **Status** | Accepted by the Founders on 27 October 2026 (decisions given in a working session; they count once this record is merged). The Technical Co-Founder confirms by approving the pull request that adds it |
| **Date** | 27 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None. Replaces D4 of [DEC-2026-10-27-record-event-v2](DEC-2026-10-27-record-event-v2.md), which recorded the form of `actor` and the `payload_hash` of an event with no object as defaults to confirm. Applies [OD-P-34](../open-decisions.md#od-p-34), closed by [DEC-2026-10-17](DEC-2026-10-17-open-decisions-closure.md) §3 ("Record event additions") |
| **Amends** | The PERD: a new version, [v1.17](../poc/perd/NOEMA_POC_PERD_v1.17.md) (§32.1, §38.2). `contracts/` in `Noemai-org/noema`: a new major of `record-event` and of `reconstruction` (v3). No SoT text changes |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the Founders (see the table above)
- Date: 27 October 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: REQ-AUD-001, REQ-AUD-002, REQ-AUD-003, REQ-SEC-001, REQ-ENV-001, REQ-VER-001; INV-11, INV-12; SoT §43.6; PERD §32.1, §38.2, §41.1, §34.1, §7. No SoT change; the requirement count stays 154
- Migration notes: §4
- Supersedes: D4 of DEC-2026-10-27-record-event-v2

---

## 1. The decisions

The Founder's answers of 27 October 2026, recorded as given:

| | Decision |
|---|---|
| D1 | **`written_by` is the emitter.** The emitters are the service identities of PERD §41.1, plus any per-adapter identity that §29 or §34 names; each name is cited with its section (PERD v1.17 §32.1) |
| D2 | **Principal kinds:** `customer`, `operator`, `approver`, `auditor`, `regulator`, `admin`. `service` is not a principal kind |
| D3 | **`actor` is required on every event.** Each event carries an emitter and a principal. For an event no authenticated person caused, the principal is the emitter's service identity. A person's or administrator's principal is `<kind>:<id>`, the kind from D2's closed list and the id a stable principal identifier |
| D4 | **Route: v3.** `record-event.v3.json` and `reconstruction.v3.json` are added beside v1 and v2. v2 is left unchanged |
| D5 | **`payload_hash = SHA-256(JCS(payload) encoded as UTF-8)`, JCS being RFC 8785, integers only.** A non-integer number in a payload is rejected |
| D6 | **The golden vectors for the hash** are the empty object, a nested object, a Unicode string and an integer. Each expected hash is computed with an implementation independent of the code under test, and the input bytes are recorded beside it |

## 2. Rationale and evidence

The exact PERD lines (PERD v1.16, `docs/poc/perd/NOEMA_POC_PERD_v1.16.md`) that left the two fields open:

> §32.1: "`payload_hash` (the hash of the referenced object's canonical JSON); `actor` (the power or service identity, plus the principal where relevant)."

Checked on 27 October 2026: §32.1 is the only place v1.16 defines either field. It gives no string form for `actor`, no rule for the identifier of a principal, and says nothing about an event that refers to no object or about numbers in a payload. D4 of the earlier record said so and stopped.

The sets in PERD v1.17 are read from these PERD lines:

> §41.1, identities table: `core-edge`, `core-trust`, `core-execution`, `core-outcome`, `core-record`, `core-evidence`, `core-workflows`, `model-service`, `benchmark-runner`, `admin` (control plane).
>
> §34.1: "Noema's adapters address them as **nine logical services**: `mock-ledger`, `mock-switch`, `mock-destination`, `mock-customer`, `mock-policy`, `mock-case`, `mock-clock`, `fault-controller`, `fixture-loader`." and "`fault-controller` and `fixture-loader` are **benchmark-only** … **never reachable from the core or the model service**".
>
> REQ-ENV-001 (§34.3), Security: "Per-adapter service identity [SoT §47.1]." REQ-VER-001 (§29), Security: "Outcome uses its own adapter identity (read-only) [REC; SoT §47.1 …]."
>
> REQ-SEC-001 (§41.2): "… signed session tokens … for synthetic customers, operators and approvers, with roles." and, under Security, "The token's `sub` is the only principal source."
>
> §7: the actor rows "End customer", "Enterprise operator", "Auditor or regulator (enterprise-side)". REQ-AUD-003 (§32.4): "Ops and audit role only." §38.2: `confirmation_event`, provenance "Authenticated approver".

## 3. Agent decisions

1. **The emitter set has 17 values:** the ten identities of the §41.1 table and the seven §34.1 logical services that the core's adapters address. `fault-controller` and `fixture-loader` are left out: §34.1 says they are never reachable from the core, so no runtime event can name them. If the Founders want them in, it is one more value and a v3 minor.
2. **`admin` is both an emitter (the §41.1 identity) and a principal kind** (the administrator). They sit in different fields: `written_by: admin` with `actor: admin:<id>` is the control plane acting for a signed-in administrator. The text of §32.1 says so.
3. **`core-outcome` is read as the "own adapter identity" of REQ-VER-001**, which names none: §41.1 gives `core-outcome` the Tushe read credential.
4. **The identifier of a principal** is the session token's `sub`, which is the `principal_id` (REQ-SEC-001; INV-12). The PERD gives no pattern, so `^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$` is the smallest form that accepts the PERD's and the SoT's own examples (`usr_88213`, `usr_synth_014`) and cannot hold the colon that separates kind and id.
5. **`regulator` is separate from `auditor` by the Founder's decision (D2).** §7 names them in one row and REQ-AUD-003 has one "ops and audit role"; the PERD v1.17 table says so.
6. **The SoT §43.6 example `"written_by": "TRUST"`** uses a power name in upper case. It is an example, not a value list, and the PERD narrows the field; the SoT is not edited here. The next SoT version should change the example to an emitter value such as `core-trust`.
7. **An event that refers to no object has the payload `{}`.** That is the earlier default (D4 (b)), now a consequence of the definition: the hash of the two bytes `{}` is `sha256:44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`. No earlier hash changes.
8. **Integers are from −(2^53−1) to 2^53−1,** the range the Go canonicaliser (`platform/crypto`) already accepts for grants and signatures. Zero is written `0`.

## 4. Migration notes (AGENT-15)

- **Route.** `actor` changes meaning and form (D3), so the change is not additive: existing v2 events would stop validating. By the Founder's rule that is a new major (v3) and v2 stays as it is. No v2 event exists outside tests and fixtures (checked 27 October 2026: the writer is not wired into `cmd/core`, the `record_event` table holds rows only in throwaway test databases, and `chain.Verify` has no caller outside tests). Nothing is migrated.
- **`payload_hash` is additive in effect.** The Go writer already hashed the RFC 8785 form of integer payloads, and the independent vectors agree with it. The Python reference had two defects found on 27 October 2026 (members sorted by code point instead of UTF-16 code units; fractions written in Python's form) and is fixed; no existing fixture used either, so no v2 or v1 hash changes.
- **Writers, verifier, readers move together** in the noema pull request: `services/core/record/chain` (schema version `3.0`, the closed sets, integers-only payloads), `execution/ledger` (the emitter is `core-execution`), the benchmark runner's reconstruction reader (`reconstruction.v3`).
- **Golden vectors.** The v2 chain vectors are not touched. A v3 chain family and a payload-hash family (empty object, nested object, Unicode string with an astral-plane key, integers) are added, with the input bytes beside each hash, computed with a Node implementation and with `sha256sum` of the recorded bytes.
- Generated models: none exist yet (codegen is CON-03).

## 5. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted | 27 October 2026 | Working session, summarised here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
