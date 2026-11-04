# Task card: EVD-01

Plan task EVD-01 (owner C2+AG; Needs PLT-06, ENV-03; gate G1/G2 path). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Repository: `noema` (the card lives in `docs`). Drafted 4 Nov 2026 by the Core Engineer 2 role agent, on the Founder's order of 4 Nov 2026 ("EVD-01 slice 1 starts at once, with `execution/e2e` as the story-test location"). **Status: DRAFT until the Founder approves and merges it.** Slice 1 is built on a branch with its tests first in the meantime, and no slice-1 pull request is marked Ready before this card is merged.

```
TASK-EVD-01  EVD-01 · Evidence Layer: evidence items with every SoT §43.5 field; immutable payload rows; the FactStatus function; absence never negative
Priority: P0
Requirement IDs: REQ-CTX-001, REQ-CTX-002; SoT IDs: POC-FR-05, INV-10, INV-19, BD-10, PLAT-FR-04
Rationale: Every fact Trust, Outcome or Resolution uses is an evidence item with full provenance, persisted before use and immutable; its status comes from one pure, total function in which absence is never a negative fact. [REQ-CTX-001, REQ-CTX-002]
Modules touched (allowlist; paths in `noema`):
  slice 1: services/core/evidence/layer/                (the FactStatus function and its tests; the package already exists and is empty)
           services/core/evidence/README.md, services/core/evidence/layer/doc.go
           status/EVD-01.md
  slice 2 (a later card amendment or PR): services/core/migrations/ (evidence_item, evidence_payload and their immutability triggers), services/core/evidence/layer/ (the item builder)
  ← nothing else may change. contracts/ is read-only (the evidence-item, evidence-payload, evidence-source and FactStatus contracts exist). No new dependency (AGENT-14): the standard library only; Go's built-in fuzzing is used for totality.
Contracts: none; bump required? N
Inputs/outputs (slice 1): `AssignStatus(read Read, source Source, now time.Time) FactStatus`, a pure function. `Read` is what the adapter and the Evidence Layer know about one read: its class (OK, TIMEOUT, SERVER_ERROR, RATE_LIMITED_BEYOND_BUDGET, CIRCUIT_OPEN, NOT_FOUND, MALFORMED, OUT_OF_SCOPE), whether a not-found carried the terminal flag, whether the value is well-formed and determinate, and `read_at`. `Source` is the pack's evidence-source descriptor: its authority for the fact (AUTHORITATIVE, CORROBORATING, NONE), its freshness limit and the trust profile's limit, and its declared absence semantics (none declared in the POC).
Acceptance criteria:
  REQ-CTX-002:
  - FactStatus SHALL be assigned deterministically by the rules of PERD §21.1 (the table). No rule may turn absence into a negative fact.
  - For generated reads with missing records, the status SHALL be UNAVAILABLE or UNKNOWN unless the descriptor declares `AUTHORITATIVE_NEGATIVE`.
  - The function SHALL be total (no panics) over fuzzed inputs, and any unhandled branch SHALL default to UNKNOWN.
  REQ-CTX-001 (slice 2):
  - 100% of Decision Records reference evidence IDs that exist and have `read_at` ≤ `evaluated_at`.
  - No payload is mutable after insert (a database trigger).
Task "Done when" (plan): Fuzzed payloads give total, correct statuses
Tests to write FIRST (AGENT-11), slice 1:
  - a table, one case per row of the §21.1 table that `assign_status` can decide on its own (KNOWN, STALE, UNAVAILABLE, UNKNOWN, UNAUTHORIZED) and per failure class of REQ-CTX-001 (a malformed response is UNKNOWN; an adapter exception is UNAVAILABLE)
  - absence: for every read class that means "no record" (NOT_FOUND, with and without the terminal flag), the result is UNAVAILABLE or UNKNOWN and never KNOWN, for every source authority, unless the descriptor declares AUTHORITATIVE_NEGATIVE and the read carries the terminal flag (EC-S11, EC-S19)
  - totality: a Go fuzz target and a seeded generator drive arbitrary reads, sources and times (negative and zero limits, a `read_at` in the future, the zero time); the function never panics and always returns one of the eight values
  - staleness uses the effective limit, the stricter of the source limit and the profile limit, measured from `read_at` on the injected `now` (INV-23); a limit that is zero or negative is UNKNOWN, never KNOWN
  - determinism: the same inputs give the same status, with no clock read inside the function
Faults to exercise (AGENT-12): none in slice 1 (a pure function). Slice 2 exercises real adapter faults (TIMEOUT, 5xx, malformed, 429) from the Tushe FaultPlans.
Record events asserted: none in slice 1 (`EVIDENCE_READ` arrives with slice 2).
Dependencies: PLT-06 (migrations; slice 2), ENV-03 (adapter interfaces; slice 2). Slice 1 needs neither.
Out of scope:
  - INFERRED, AMBIGUOUS and CONTRADICTORY: they need more than one item and a reconciliation rule (RES tasks); `AssignStatus` never returns them
  - the pack field `absence_semantics`: the evidence-source contract does not carry it, and the POC fixtures declare none; slice 1 takes it as an input defaulting to "none" and adds no contract field (AGENT-15)
  - context snapshots (REQ-CTX-004), refresh (REQ-CTX-003), the candidates API, scope enforcement (UNAUTHORIZED is decided from the scope check's result, which arrives as an input)
Definition of done: tests green; boundary/lint green; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: C2 (a founder) with the Core Engineer 2 role agent. Needs: PLT-06, ENV-03 (slice 2). Gate: none named.

## Decisions taken by the agent (reversible; the Founder can change them at approval)

| # | Question | Agent's default |
|---|---|---|
| D1 | A well-formed value from a CORROBORATING-only source within its limit: KNOWN or something else? PERD §21.1 says KNOWN needs an authoritative source and is silent on a corroborating one | **UNKNOWN** (the safer reading: corroboration never confers KNOWN on its own; a reconciliation rule can raise it to INFERRED). **[OPEN]** for the Architect |
| D2 | A well-formed value from a source with authority NONE (a customer's own claim) | **UNKNOWN** (SoT §43.5: authority NONE is never authoritative) |
| D3 | `read_at` later than `now` (clock skew) | **UNKNOWN** (never KNOWN on a read from the future) |
| D4 | The order of the rules, most restrictive first | out of scope, then source unreadable (UNAVAILABLE), then malformed (UNKNOWN), then absence, then not authoritative, then stale, then KNOWN |
| D5 | Where the function lives | `evidence/layer` (its package doc already names FactStatus and provenance) |

## Slices

1. **Slice 1 (this card, first PR):** the pure `AssignStatus`, its types and tests.
2. **Slice 2:** `evidence_item` and `evidence_payload` tables (a later migration number than the Outcome migration `0007`), the DB immutability trigger, and the item builder that assigns the status before persisting, with real adapter faults and `EVIDENCE_READ` events.
3. **Slice 3:** the story tests for G1, in `execution/e2e` (the Founder's order of 4 Nov 2026; docs#106 R10).
