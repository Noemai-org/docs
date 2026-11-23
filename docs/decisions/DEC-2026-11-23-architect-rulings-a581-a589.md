# DEC-2026-11-23 · Architect rulings A581 to A589 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A581 to A589 (§1), every one Interim. |
| **Supersedes** | **A584 amends A514** ("AssertedBy stays empty") and reserves migration 0039. **A582 is the additive contract change** for A563 (`clarification.v1`, `mode: "SLOT"`). **A583 states** what a tie at the top is. **A581 states** the key of an early (null-basis) decision (builds on A574 and A577). **A585 is a flow rule** for agents. Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan, as written. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A581 to A589
- Decision: §1
- Rationale and evidence: the Architect's message of 23 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-12, INV-21; AGENT-11, AGENT-15, AGENT-16; REQ-AMB-003, REQ-AMB-004, REQ-TRU-010; PERD §22; `decision-record.v2`, `clarification.v1`, `sse-event.v1`; AGENTS §5, §8, §11
- Supersedes: see the Supersedes row above
- Migration notes: A582 is an additive optional member on `clarification.v1`, which stays v1, with a migration note (AGENT-15; both Founders). A584 adds database migration **0039** (a nullable column; the author is C2, so the independent read comes from EL or C1 and SR reads as SR, A463). A581 and A588 may need additive contract changes with the AGENT-15 steps, in the same PR as the change.

## 1. The rulings

### A581 (interim, early-decision retries).

An early (null-basis) decision is keyed by the turn (request id) in addition to its intent hash, pack version, outcome and reason. A replay of the same turn returns the stored record. A new turn evaluates fresh and records a new one. No stale decision survives a world change, and no grant is ever involved.

### A582 (interim, A563; additive `mode: "SLOT"` on `clarification.v1`).

C1's proposal is accepted: an additive optional `mode: "SLOT"` on `clarification.v1`. In that mode `candidate_set_id` and its version are not required and `options` are empty. The question text comes from pack templates in plain language, with no internal codes. The contract stays v1 with a migration note. Both Founders approve, and FE regenerates its parser and builds the card.

### A583 (interim, ties).

A tie at the top means equal exact scaled sums, and the margin is then 0, so the outcome is AMBIGUOUS.

### A584 (interim, #919).

Option (b): store the verified issuer with the session, so INV-12 means what it says. It is migration 0039 (0038 is C1's) with a nullable column. Recovery refuses a row without it, and legacy rows are never given an invented issuer. C2 builds the store and migration, and EL fills the issuer at the gateway start. A514's "AssertedBy stays empty" is amended.

### A585 (interim, flow rule).

After pushing a red, the agent stays subscribed to that PR until it has read the red CI and pushed the green. Then it unsubscribes. That is how CI wakes an agent without polling. Unsubscribing immediately after the push is what keeps producing "tell me when to read".

### A586 (interim, row 12).

BO's recommendation is accepted. The scan output, the inventory and the file list go in a second artifact (`bench-g1-stack-evidence-<run id>`), and the main artifact holds exactly the scanned files. No exception in the package.

### A587 (interim, #824 report file).

If a run fails before any session, it removes the zero-byte report file it created. It never deletes a non-empty report.

### A588 (interim, #616 integration).

The events route projects clarification and confirmation card events from the Record as `sse-event.v1` card events. EL owns the projection, and C1 adds any missing member additively. It is after G1, because G1 runs through the API on text.

### A589 (interim).

Lane 5 traces to task STM-01 (the red check on #917 was the invalid id LANE-5).

## 2. What the Steward did, and where the rulings are silent

- **A581.** It builds on A574 and A577 (an early decision holds `null` for the three basis members) and on the decision key of A186. The ruling does not say whether the key's shape needs a contract or migration change; if it does, C1 follows AGENT-15 and the ledger (the next free number is below). The Steward changes no code.
- **A582.** A contract change, so both Founders approve (AGENT-15). It is additive and optional; `clarification.v1` stays v1 with a migration note. FE regenerates its parser. The question text lives in pack templates, so it is C2's pack data (SYNTHETIC, AGENT-25).
- **A583 and the A555 change request.** PERD REQ-AMB-003 says "a tie means CLARIFY"; A583 says a tie at the top (equal exact scaled sums) makes the margin 0, so the ranker's outcome is AMBIGUOUS. The Steward reads these as consistent (AMBIGUOUS is the ranking result; Trust's decision follows REQ-AMB-003, which is CLARIFY), and C2 and C1 check that in the vector file. The Steward added the tie rule to the proposed REQ-AMB-003 note in `CR-2026-11-23-A555-perd-22-1-ranker-placement` (still a Draft; the PERD stays v1.28).
- **A584 and the migration ledger.** The Steward reserved **0039** on noema#183 for A584 (a nullable column for the verified issuer), after 0038 (A574, C1). The author is C2, so the independent read comes from EL or C1 (not C2, not SR), and SR reads as SR (A463). **Next free: 0040.** "AssertedBy stays empty" is from A514 (`DEC-2026-11-21-architect-rulings-a507-a517`, merged and not edited); this record states the amendment.
- **A585 and my own flow.** A585 is the Architect's rule for an agent that pushes a red (a failing test, test-first): stay subscribed until the red CI is read and the green is pushed, then unsubscribe. The Steward's pull requests in `docs` carry no red, so the Steward keeps unsubscribing from a docs pull request's automatic subscription, as the Founder asked earlier; where the Steward pushes a red in `noema`, it follows A585.
- **A586 and A587.** A586 is BO's and IL's (the G1 package artifacts); A587 is Voice's (noema#824). The Steward changes neither.
- **A588.** After G1; EL owns the projection; C1 adds any missing `sse-event.v1` member additively (AGENT-15 steps).
- **A589.** Lane 5 (A547) traces to task STM-01. The plan row STM-01 is titled "Investigation projection: transitions.yaml ... a Record event per transition" (owner C1+AG), while the Compose pull requests already use the id (`STM-01: Compose lane 1 ...`, noema#905). The Steward records the ruling and changes no plan row; if the Architect wants a plan row that names the composition lanes, that is a change request.
- **Migration ledger:** 0037 stays reserved for DEBT-54; 0038 for A574; **0039 for A584**. Next free: 0040.
- **Task status (`tasks.csv`)** is unchanged here; it moves only on merged evidence.
- **Next free ruling: A590.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` records | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-*` and `DEC-2026-11-22-architect-rulings-a518-a524` | A489 to A492, A502 to A517, A518 to A529 | |
| `DEC-2026-11-23-architect-rulings-a530-a533`, `-a534-a540`, `-a542-a553`, `-a554-a560`, `-a561-a580` | A530 to A533; A534 to A540; A541 noted, A542 to A553; A554 to A560; A561 to A580 | |
| This record | A581 to A589 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank) | **A590** |
