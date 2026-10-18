# DEC-2026-10-16 · Money representation (OD-P-19) and contract value lists (OD-P-26)

| | |
|---|---|
| **Status** | Accepted by the Founder on 16 October 2026. The Technical Co-Founder confirms by approving the pull request that adds this record |
| **Date** | 16 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | OD-P-19 (OQ-06, SOT-C-11) and OD-P-26 (OQ-13, SOT-C-26). CON-02's diff is this record's §2 |
| **Supersedes in part** | DEC-2026-10-06-architecture-and-contracts, item 4 (contract enums): two values removed, one list completed, one value renamed in the PERD. Reasons in §2 |
| **Amends** | SoT §43.1 example (major units → minor units), giving SoT v1.7; PERD §20.1, §23 and §27.2; `docs/engineering/state-registry.md` §2 and §6; plan task text for CON-01, CON-04, PCK-01 and UND-05 |
| **Authority order applied** | SoT → decision records → PERD → plan. A decision record overrides the SoT only by editing it (AGENT-29). DEC-2026-10-06's enum values were never written into the SoT, so where a value contradicts a SoT rule, the SoT wins |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Supersedes in part, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the Founder (see the table above)
- Date: 16 October 2026
- Closes: OD-P-19 (OQ-06, SOT-C-11) and OD-P-26 (OQ-13, SOT-C-26)
- Owner: Founder and Technical Co-Founder
- Decision: §1 (M1 to M10, money) and §2 (the value lists and the drift guard); "Agent decisions" records what the pull request that adds this record chose where the record was silent
- Rationale and evidence: the reasons in §1 and §2, and the verification in the pull request that adds this record (the reason-code scan, the legacy-value search and the M3 check in Go and Python)
- Affected requirement IDs / SoT sections: SoT §43.1 (SoT v1.7); PERD §20.1, §23.2, §23.3, §27.2, REQ-TRU-001 (PERD v1.7); `docs/engineering/state-registry.md` §2 and §6; plan task text for CON-01, CON-02, CON-04, PCK-01, PCK-02, UND-05 and one new CON task (plan v1.7); the requirement count (153) and every invariant are unchanged (§3)
- Migration notes: M9 (none needed: `/contracts` v1 is not tagged and no data exists)
- Supersedes: DEC-2026-10-06-architecture-and-contracts, item 4, in part (§2)

---

## 1. Money: integer minor units, one meaning per contract version (OD-P-19)

**M1. Representation.**

- A currency amount is an **integer count of the currency's minor unit**. NGN 20,000.00 is `2000000`.
- The currency is an ISO 4217 code in its own field.
- The minor-unit exponent comes from one versioned table, `contracts/currencies.json`. For the POC it holds only NGN, with exponent 2.
- Core code never hard-codes an exponent: no literal `100` multipliers on money, and a lint rule catches them.

**M2. One meaning, no marker.**

- In `/contracts` v1, every currency amount is in minor units, without exception.
- There is no `minor_units: true/false` flag. A flag that can be false creates two meanings for one field, and consumers would have to guess.
- **Field names:**
  - The SoT-fixed `Quantity` slot keeps `value` and `unit`. When `unit` is a currency, `value` is minor units, and the schema says so.
  - Every other money field is named `<name>_minor` (for example `amount_minor`) next to `currency`.

**M3. Bounds.**

- **Range:** `0 ≤ amount ≤ 9,007,199,254,740,991` (2⁵³ − 1).
- **Why that ceiling.** RFC 8785 (JCS), which every Noema hash uses, serialises numbers as IEEE-754 doubles. Integers above 2⁵³ would canonicalise differently across languages and silently change `intent_hash`, `binding_hash` and grant signatures. The TypeScript UI reads numbers the same way. The ceiling is ₦90 trillion, which no POC value approaches.
- **Sign.** Amounts are non-negative. Direction (debit or credit, in or out) is always a separate field, never a sign.

**M4. No floating point, enforced at every layer.**

| Layer | Allowed | Forbidden |
|---|---|---|
| Contracts (JSON Schema) | `integer` with the M3 bounds | `number` |
| Wire (JSON) | Digit-only integer literals | Any literal with `.`, `e` or `E`, even if integral (`2000000.0`, `2e6`), and quoted numbers. JSON Schema alone accepts `2.0` as an integer, so both decoders must reject it themselves |
| Go | `int64`, decoded with `json.Number` plus a digit-only check | `float32`, `float64` |
| Python | `StrictInt` (Pydantic v2 strict) | `float`, `Decimal` |
| Postgres | `BIGINT` with `CHECK (x BETWEEN 0 AND 9007199254740991)` | `REAL`, `DOUBLE PRECISION`, `NUMERIC`, `MONEY` (locale-dependent) |
| TypeScript UI | `number` checked with `Number.isSafeInteger`; display only | Arithmetic on display strings |

**M5. Conversion only at the edges, deterministically, never by a model.**

- **Spoken or written amounts** ("20k", "₦50,000", "fifty thousand") become minor units in the **lexicon**, which is deterministic code using the M1 table. The model may extract the surface form; it never does arithmetic (AGENT rules on deterministic layers).
- **External systems.** An adapter for a system that supplies major units converts and validates at the adapter. Tushe already supplies integer kobo (our 13 Oct response, M5), so the Tushe adapter only validates: integer, within bounds, currency NGN.
- **Excess precision is rejected, never rounded.** For example, `1234.567` NGN.
- **No rounding in the POC.** There is no division or multiplication of money.

**M6. Arithmetic.**

- Only addition, subtraction and comparison, and only within one currency.
- A cross-currency operation is an error, not a conversion.
- Every addition is checked against the M3 ceiling. Overflow is an error, never a wrap.

**M7. Display.** The UI formats an amount from minor units plus the table exponent (`₦20,000.00`). Displayed strings are never parsed back.

**M8. Non-currency quantities.** A pack unit (for example, data volume in the telecom conformance pack) declares its own integer scale in the pack. The same integer, bound and no-float rules apply. Core never assumes that a `Quantity` is money.

**M9. No migration needed.**

- `/contracts` v1 is not yet tagged, and no data exists, so v1 is defined in minor units from the start.
- The SoT §43.1 example is corrected in the same pull request (`"value": 20000` → `"value": 2000000`), so no authoritative document shows major units.
- **Rule for any future change:** a change to the unit or exponent of an existing field is a major contract version, with a written migration.

**M10. Tests.** These are CON-01 fixtures, plus CON-04 vectors where hashing is involved. Each must pass in Go and Python. Every rejection is a schema or decoder rejection, never a silent fix.

| Case | Expected |
|---|---|
| `0`; `1`; `2000000`; `9007199254740991` | Accept |
| `9007199254740992`; `-1` | Reject |
| `2000000.0`; `2e6`; `"2000000"`; `null` where required | Reject |
| Currency missing; currency not in the table; exponent conflict | Reject |
| `"20k"` → `2000000`; `"₦50,000"` → `5000000` (lexicon) | Exact |
| `1234.567` NGN at an adapter | Reject |
| Addition crossing the ceiling | Error |
| NGN + another currency | Error |
| A JCS hash over an object containing `9007199254740991` | Byte-identical in Go and Python |

## 2. Contract value lists: the reconciliation (OD-P-26)

**Background.**

- DEC-2026-10-06 item 4 holds exactly three lists, mirrored as normative in `state-registry.md` §2 and §6.
- Each value below was compared with the SoT and PERD v1.4.
- **The rule for every value.** It is kept only if the SoT or PERD defines a step that produces it and a step that consumes it.
- **Where a value contradicts a SoT rule,** the SoT wins.
- **Where DEC-2026-10-06 and the PERD name the same meaning differently,** the decision record's name wins.

### 2.1 Intent Object `status`

| Value | DEC-06 | PERD | SoT | Disposition |
|---|---|---|---|---|
| `EXTRACTED` | yes | absent | absent | **Kept.** Compiler output before the schema gate |
| `VALIDATED` | yes | yes | yes (§43.1 example) | **Match** |
| `REJECTED_AT_GATE` | yes | `INADMISSIBLE` | absent | **Kept; the PERD is corrected** (same meaning; the DEC name wins) |
| `SUPERSEDED` | yes | absent | conflicts | **Removed.** SoT §43.1: an Intent Object is immutable once admitted. Storing `SUPERSEDED` on an admitted object would mutate it. Supersession is derived from the `supersedes` link, and T1 rejects a non-latest version with `INTENT_INVALID` |

**Lifecycle.** `EXTRACTED` → `VALIDATED` or `REJECTED_AT_GATE`. The status is set once, at the gate, and is never changed afterwards. Only `VALIDATED` crosses into Trust.

### 2.2 Decision Record `authority` layer result

| Value | DEC-06 | PERD | SoT | Disposition |
|---|---|---|---|---|
| `PASS`, `FAIL`, `NOT_EVALUATED` | yes | yes (§23.2) | `PASS`, `NOT_EVALUATED` (§43.2 example) | **Match** |
| `OVERRIDDEN` | yes | absent | conflicts | **Removed.** Nothing in the SoT or PERD produces it, and PERD §23.2 states that nobody can override the business layer ("This is Noema's layer"). A stored "overridden" result is a bypass state in a safety field. An approver's ACCEPT does not override anything: it triggers a fresh evaluation (SoT §43.2a, INV-25) |

### 2.3 Trust reason codes: two tiers

**The conflict.** DEC-06 treats reason codes as a closed core list of six. PERD REQ-TRU-001 says `reason_codes[]` come "from the pack's reason catalogue", and PERD §23.3 gives the engine eight more codes that aren't in DEC-06. Followed literally, DEC-06 would leave P0 refusal steps in the fail-closed ladder without a legal code.

**The decision: two tiers.**

**Core reason codes** are a closed enum in `/contracts`. They are vertical-agnostic and produced by the engine itself. There are 14:

| Code | Producer |
|---|---|
| `PROHIBITED_CAPABILITY` | T4 |
| `AMBIGUOUS_COUNTERPARTY` | T7 material ambiguity → CLARIFY or ESCALATE |
| `DECLINED_BY_APPROVER` | Confirmation DECLINE (§43.2a) |
| `POLICY_VERSION_MISMATCH` | Confirmation ACCEPT, where the fresh evaluation's policy version differs from the one bound in the confirmation's `binding_hash` |
| `INSUFFICIENT_EVIDENCE` | T9: a required source UNAVAILABLE |
| `STALE_EVIDENCE` | T9: evidence past its effective limit and not refreshable |
| `INTENT_INVALID` | T1 |
| `UNAUTHENTICATED` | T2 |
| `WRITES_DISABLED` | T3 |
| `OUT_OF_SCOPE` | T5 |
| `NOT_AUTHORIZED` | T6 |
| `NOT_FOUND_OR_NOT_AUTHORIZED` | T8 (identical to not-found) |
| `PLAN_INVALID` | T14 |
| `NO_PERMITTING_RULE` | T11 default deny |

The first six come from DEC-06; the other eight come from the PERD. (Agent decision A1 adds three more engine-produced codes that PERD v1.6 already used, making 17.)

**Pack reason codes** are namespaced strings from the pack's reason catalogue. The format is `<vertical>.reason.<name>`, for example `fin.reason.contradictory_state`. They are:

- produced by pack policy rules (T11) and by the pack mappings for T10 (contradiction, unknown outcome) and T12 (clocks);
- validated by `packcheck` against the catalogue;
- opaque strings to core.

A Decision Record's `reason_codes[]` may hold both tiers.

**Not reason codes,** so they are excluded:

- `NONE`: an empty array means no reason;
- grant-void reasons, such as `POLICY_SUPERSEDED`;
- classifications, such as `CONTRADICTORY_STATE` and `POLICY_STALE`;
- execution states, such as `REJECTED_STALE_VERSION`.

Each keeps its own field.

**The case reason.** In PERD §27.2, `reason_code` (inside the idempotency key and plan parameters) is the **case reason**, from the pack's case-reason catalogue (for example `CUSTOMER_DISPUTE_UNRECOGNIZED`). It is not a Trust reason code. The field name stays the same, because the key bytes don't change; the PERD says so explicitly.

### 2.4 Drift guard

- `state-registry.md` is the single normative home of every core value list.
- **CON-01 adds a CI check that fails when the `/contracts` enums and `state-registry.md` differ** in any way: a value added, removed or renamed. Because codegen runs from the schemas, nothing can drift silently.
- **`packcheck` rejects:**
  - a pack reason code outside its namespace;
  - a pack code that reuses a core code.

## 3. What this does not change

- Every invariant.
- 153 requirements.
- Every gate's conditions.
- The money boundary.
- Every Tushe date.
- The committed golden vectors. Their bytes are unchanged; see the note on CON-04 in the prompt.

## Agent decisions

Where this record was silent, the pull request that adds it chose the following. Each keeps the SoT, the PERD and the plan consistent and leaves every gate unchanged.

- **A1. Three more core reason codes.** The verification scan of PERD v1.6 found three engine-produced results that are not among the 14, each with a producer. They are added to the core enum (17 in all), marked [REC] until the founders confirm them:
  - `RATE_LIMITED`: the policy-layer check on the descriptor's `limits.rate_per_principal_per_hour` (T11; REQ-TRU-012, EC-U05);
  - `INTERNAL_ERROR`: the Trust boundary handler, where a panic at any step becomes UNKNOWN `INTERNAL_ERROR` (REQ-TRU-001, failure behaviour);
  - `MODE_NOT_ENABLED`: the Trust entry point, origin check before T1, where a MODE_2 proposal is rejected at runtime (REQ-TRU-011).
- **A2. Producers of three of the 14.** `POLICY_VERSION_MISMATCH` is not named in PERD v1.6 or the SoT; its only producer is §2.3 of this record (the confirmation ACCEPT revalidation of REQ-TRU-009 produces "a new decision, never a grant", without naming a code). `INSUFFICIENT_EVIDENCE` and `STALE_EVIDENCE` appear in PERD v1.6 and the SoT as classifications; §2.3 gives them a reason-code producer at T9. None is dropped, and PERD v1.7 §23.3 states all three producers.
- **A3. `INADMISSIBLE` is renamed everywhere in PERD v1.7**, not only as the Intent Object status: the investigation state, the Record event (`INTENT_INADMISSIBLE` becomes `INTENT_REJECTED_AT_GATE`) and the provider-outage row follow, so one name means one thing. No other file outside the frozen PERD versions used the old name.
- **A4. A reason-code example.** PERD §23.5 gave a classification (`EXECUTION_OUTCOME_UNKNOWN`) as the reason of a disposition decision. Under §2.3 that is a pack reason code, so the example now reads "a pack reason code for the unknown outcome (T10 mapping, for example `fin.reason.execution_outcome_unknown`)". The code name is an example of the namespace, not a catalogue entry.
- **A5. One acceptance criterion** is added to REQ-TRU-001: every `reason_codes[]` entry is a core code or a code in the pack's catalogue, in the pack's namespace. The requirement count stays 153.
- **A6. `state-registry.md`** said it was derived and non-normative. Its header now says it is the single normative home of the core value lists (as §2.4 requires) and that every other row stays derived.
- **A7. Status lines.** DEC-2026-10-06's status line is marked "superseded in part" by this record (item 4) and by DEC-2026-10-13 (item 2), following the convention that its earlier supersession was recorded the same way; its body is untouched. OD-P-06 and OD-P-08 name this record's amendments; OQ-06 and OQ-13 are answered in PERD v1.7 §67.2.

## Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founder | Approved | 16 Oct 2026 | Written instruction to the coding agent |
| Technical Co-Founder | Confirms | Date of approval | Approving review on the pull request that adds this record |
