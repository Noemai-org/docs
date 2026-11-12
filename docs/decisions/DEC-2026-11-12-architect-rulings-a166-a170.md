# DEC-2026-11-12 · Architect rulings A166 to A170 (Founder-approved)

| | |
|---|---|
| **Status** | **Decided by the Principal Architect and approved by the Founder on 12 Nov 2026, relayed to the Repo Steward; recorded by the Repo Steward.** Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 12 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder (the approval); Founder and Technical Co-Founder (the merge) |
| **Decides** | Five rulings, A166 to A170 (§1). Each states what it supersedes. |
| **Closes** | The four decisions asked on noema#484 (A166), the Codex P1 on noema#466 (A168) and the Codex P2 on noema#465 (A169). |
| **Supersedes** | Per ruling, in §1. In short: A167 resolves the 0022 clash recorded in `DEC-2026-11-12-architect-rulings-a148-a160`, §2; its statement that noema#410 holds 0022 is corrected by A171. |
| **Amends** | Nothing in the SoT, the PERD or the plan. The task row for A170 is a change request (§2): [CR-2026-11-12-A170-sse-events-task-row](../poc/execution/change-requests/CR-2026-11-12-A170-sse-events-task-row.md). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 12 Nov 2026; counts once a Founder who did not author this pull request approves and merges
- Date: 12 November 2026
- Closes: the questions on noema#484, noema#466 (P1) and noema#465 (P2)
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A166 to A170
- Decision: §1
- Rationale and evidence: the Architect's message of 12 Nov 2026, approved by the Founder, relayed to the Steward
- Affected requirement IDs / SoT sections: REQ-API-001 (PERD §39.2), REQ-SEC-001; INV-12, INV-29; AGENT-02, AGENT-15, AGENT-29; SoT §0.4
- Migration notes: A167 sets who orders the migration numbers; no migration is added by this record
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A166** | **Intent route (noema#484), for C2.** (1) The core computes the hash and signature after the gate, using the REC-08 emitter signer. The model service never signs and never computes the authoritative hash (INV-29). (2) Do not loosen the canonical JSON rule to accept fractional confidences. If your default does that, replace it with integer basis points through a contract bump (AGENT-15), with C1 as co-owner. (3) The model's output does not contain `principal_type` or `asserted_by`. The core sets them from the session (INV-12). If the model sends them anyway, the gate refuses it as a shape error. There is no security event on a normal compile. (4) Intent nodes come from the mounted pack data (`packs/fintech_v1.json`). If they are missing, file an [OPEN] entry. Never hard-code them in core. (5) **A163 is confirmed:** `asserted_by` allows `-` so `noema-poc-idp` passes, and nothing else changes. Fix `Session.valid()` in noema#453 in the same way, in one push. | Nothing. It applies INV-29 and INV-12 and **confirms A163**. |
| **A167** | **Migrations.** C1 publishes the order in the A141 table on noema#183 now. noema#478 goes first because it clears red `core`. noema#471 renumbers off 0022, which noema#410 holds. EL's 0024 and 0025 are only proposals. Nobody renumbers except on C1's table. | **The 0022 clash** between noema#410 and the admitted-intent store (A151), recorded in `DEC-2026-11-12-architect-rulings-a148-a160`, §2: noema#410 holds 0022. It also makes **the numbers 0023 (A153) and 0024 (A165) and EL's 0024 and 0025 proposals** until C1's table fixes them. |
| **A168** | **Stranded runs (Codex P1 on noema#466).** `Start` from noema#490 is the retry path. On retry, if a durable `INPUT_RECEIVED` exists with no investigation, call `Start`. Do not skip it as a duplicate. C1 checks that `Trust.Decide` returns the existing decision for the same input and appends nothing. EL builds resume after that. | Nothing. It refines the deduplication rule of **A161**. |
| **A169** | **noema#465, P2.** The Record lookup must also bind the request or turn ID, not just tenant, principal and correlation. | Nothing. It refines the reference check of **A161**. |
| **A170** | **SSE events and reader pools.** EL builds the SSE events now under REQ-API-001 (PERD §39.2), with no waiting for a task row. The Steward adds the row by change request. For the per-tenant reader pools, the default is a file-mounted, read-only DSN per tenant. The route stays unmounted until it is configured. EL files this as an [OPEN] entry through the Steward. | Nothing. For this one task it lets work start before its task row exists (AGENTS §3, step 2); the change request adds the row. |

## 2. What the Steward did where the rulings are silent

- **The A170 task row.** The change request `CR-2026-11-12-A170-sse-events-task-row` is written. It proposes the row's fields, which the ruling does not give: the ID, the gate date and the done_when are the Steward's smallest defaults, marked as such, for EL or the Architect to correct. **The plan version that adds the row is written after docs#157 merges**, because plan v1.17 (A159) is in that pull request and a second plan version cannot be started from v1.16 beside it.
- **The A170 [OPEN] entry.** The Steward filed `OD-P-82` from the ruling's own words (the default, the unmounted route). EL, who the ruling says files it, states the missing fields ("what would change it", the deadline) on noema#484 or in a reply on docs.
- **A167 and the board.** The migration table on noema#183 is C1's from now on; the Steward's board points to it and renumbers nothing.
- **A167 and noema#410: corrected by A171.** noema#410 is closed without a merge, so A167's words "which noema#410 holds" are no longer true. A171 (in `DEC-2026-11-12-architect-rulings-a171-a175`) corrects them: **0022 stays reserved for C2's evidence-set binding; no other PR uses it.** C1's migration table on noema#183 governs every migration number. The Steward does not restate any PR's current number here; the table is the source (a reviewer read noema#471 at head `9403e0b7` as using `0026_admitted_intent.sql`).
- **A166 and A163.** A163 is in `DEC-2026-11-12-architect-rulings-a162-a165` (docs#158, open). A166 "confirms" it; the Steward adds no text to A163.
- **Numbering.** A148 to A161 are in docs#157 and A162 to A165 in docs#158, both open when this was written. This record follows them; next free is **A171**.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records (merged) | A41 to A147 | |
| DEC-2026-11-12-architect-rulings-a148-a160 (docs#157, open) | A148 to A161 | |
| DEC-2026-11-12-architect-rulings-a162-a165 (docs#158, open) | A162 to A165 | |
| This record | A166 to A170 | **A171** |
