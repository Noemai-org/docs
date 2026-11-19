# DEC-2026-11-18 · Architect rulings A314 to A316 and A329 to A340 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 18 Nov 2026, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 18 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | A314 and A315 (as relayed), the withdrawal of A316 and of **A328**, and A329 to A340 (§1). The message was headed "A329 to A340" and carried A329 to A340; A314 to A316 reached the Steward as one line each. |
| **Closes** | The missing numbers A314 to A316 of the docs record `DEC-2026-11-18-architect-rulings-a317-a328`; the intake-adapter ownership (A329); the setting-name rule (A330); the digit-rule questions (A331); the pack manifest and the session reference (A333); the Tier 2 definition (A334); the escalation set (A335); the follow-up body (A336); CON-08 and the small items (A337); the PLANNED to ESCALATING change request (A338); the 40001 race (A339). |
| **Supersedes** | **Withdraws A316 and A328** (the Codex lanes) and, with them, the two-lane reading of **A295**. **Withdraws the session-reference formula of A320** (A333). **A334** amends **A143** Tier 2 and **A288**/**A303**. **A339** adds to **A319**. Otherwise per ruling, in §1. |
| **Amends** | The plan (v1.24: CON-08 added). Nothing in the SoT or the PERD. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 18 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A314, A315, the withdrawals of A316 and A328, A329 to A340
- Decision: §1
- Rationale and evidence: the Architect's message of 18 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-01, INV-12, INV-22, INV-29; AGENT-11, AGENT-13, AGENT-15, AGENT-16, AGENT-27, AGENT-29; REQ-API-001, REQ-TRU-010, REQ-RCV-003, REQ-STM-001; PERD §23.1, §28.2, §39.2; SoT §0.4
- Migration notes: A336's `message-request.v1` is an additive contract with a migration note (AGENT-15); A331 changes two valid fixtures; plan v1.24 adds one task
- Supersedes: see the Supersedes row above

## 1. The rulings, as given

### A314 (interim): (as relayed)

Every agent gets G1 batches to do in parallel.

*Supersedes or changes:* Sets the work mode for the G1 lane. No plan row: the batches are the lane owners' own lists. The full text of A314 did not reach the Steward; this is the one line given.

### A315 (interim): (as relayed)

After approving, enable auto-merge.

*Supersedes or changes:* The instruction as relayed, to the approver (a Founder, since only a Founder's approval merges, A111). The Steward never approves or merges. The full text of A315 did not reach the Steward; this is the one line given.

### A316 (interim): (withdrawn)

Withdrawn: no second Codex session.

*Supersedes or changes:* **Withdrawn.** It would have started a second Codex session; A334 and the withdrawal of A328 say one Codex. Also withdraws the two-lane reading of **A295**.

### A329 (interim): The 14 intake adapters (T7 to T15).

Each is its own pull request under `orchestrator/portadapters/trust/`, all started now.

- **C1:** Intents, Writes, Capabilities (including Authorized), Scope, Authority, Ownership, Policies and Clocks.
- **EL:** Confirmations, Planner and Recorder (next to Dispatches), plus `wire_trust.go`.
- **C2:** Candidates, Evidence and Reconciler (the read side C2 wrote).

*Supersedes or changes:* Applies **A313** (each lane owns its wiring file) to the Trust intake. Eight adapters for C1, three for EL, three for C2: fourteen.

### A330 (interim): Setting names.

Any `NOEMA_*` setting a lane owner proposes stands if it follows `NOEMA_<AREA>_<WHAT>[_MS|_BYTES]` with no code default. The owner lists it in the pull request body. No approval from the Architect.

EL's two names are renamed to `NOEMA_TRUST_DB_TIMEOUT_MS` and `NOEMA_GRANT_KEY_MAX_ACTIVE` (bench value 2, PERD's "two during rotation"). EL's gateway names stand on the same rule.

*Supersedes or changes:* Generalises **A320** (the C2 names) into a rule. Applies **AGENT-16** (no default in code).

### A331 (interim): The digit rules (C1).

- Comma-joined runs of 10 or more digits are refused. The broader reading is confirmed, so comma lists of 10 or more digits are refused too.
- Full-width and Arabic commas join as well.
- The money exemption goes into the schema's customer-visible text members only (customer-answer, overlay-card), not facts or IDs.
- Reference bodies must pass the same five-digit rule. The reconstruction projector masks reference bodies to the last four digits before serving (AGENT-13). C1 updates the two valid fixtures to four-digit references.
- DEBT-30 stays (the shape comes from the pack later).

*Supersedes or changes:* Extends **A319** (the comma-joined runs) and **A279** (the money exemption's scope). DEBT-30 is unchanged.

### A332 (interim): Authors decide.

Where a ruling is silent, the author takes the safer reading, lists it in the pull request body, and proceeds. It stands unless Codex or SR objects. Nobody waits on the Architect unless a ruling conflicts with the SoT, the PERD or an invariant. Open every pull request now, all in parallel, in the order C1 suggested.

*Supersedes or changes:* Changes who settles silences: the author, not the Architect (the Steward's own rule is unchanged: a conflict with the SoT, the PERD or an invariant still stops, AGENT-27).

### A333 (interim): C2's wiring decisions.

- The pack manifest is a go: `packs/fintech/manifest.v1.json` lists each pack file with its SHA-256 and names the expected mapping and rule-set ids. The core loads through it and refuses a mismatch. It is its own pull request, and it settles EVD-06's hash-pin.
- The gate bound reuses `NOEMA_MODEL_MAX_RESPONSE_BYTES`.
- A149 governs the session reference: `authn_ref` is a hash of the token's `kid`, `sub` and `iat`, never the token. The Architect's earlier A320 formula is withdrawn.

*Supersedes or changes:* **Withdraws the session-reference formula of A320** (`ses_` plus 26 Crockford characters over `jti` and tenant). Applies **A149**. Settles the hash-pin of EVD-06 (**A320**).

### A334 (interim): One Codex and simpler Tier 2.

Tier 2 means Codex READY, CI and one Founder. An independent or SR read is only needed where SR decides it is (security surfaces). Tier 1 stays as A317c: Codex and SR at the same head, plus an independent read for migrations.

*Supersedes or changes:* Amends **A143** Tier 2 and **A288**/**A303** (no independent read for Tier 2). Tier 1 unchanged (**A317**c). With the withdrawal of A316 and A328: one Codex.

### A335 (interim): The escalation set and dispositions.

The escalation set is the pack's escalation plan: all three write capabilities (`log_complaint_reference` as the create-case step, `record_investigation_evidence` and `route_to_internal_owner`). C1's composition root injects all three. EXE-05 names them, and PERD §23.1 says each step is its own action decision. Every grant-issuing decision links a disposition. C1 flags any other write capability it finds as an exception.

*Supersedes or changes:* Confirms **A297** (TRU-10) and **A319** (inject the escalation set; every grant-issuing action decision links a disposition).

### A336 (interim): The follow-up body.

Add `message-request.v1` as an additive contract with exactly PERD §39.2's fields (`request_id`, `text?`, `option_id?`, `clarification_id?`), strict on unknown fields. EL's route validates against it and checks that a submitted `option_id` equals the clarification's own `none_option_id`.

*Supersedes or changes:* Applies **A275** (`none_option_id`). AGENT-15: an additive contract, with its migration note.

### A337 (interim): Small items.

- `ParseIntentRef` is registered as CON-08, with C1 owning it.
- The gate's supersedes link refuses `@007` (the contract cannot hold it).
- `KEY_ROTATED`: C1 takes the safer reading for each of its eight gaps, lists them, and proceeds (A332). The default is one event per tenant chain per key version.

*Supersedes or changes:* Registers **CON-08** (plan v1.24). Refines DEBT-51 (**A319**).

### A338 (interim): The change request.

CR-2026-11-18 (PLANNED to ESCALATING, docs#206) is approved. EL marks it ready and the Steward records it.

*Supersedes or changes:* Applies **A318** (the same change request approved). See §2: the request offers two options and the approval does not say which.

### A339 (interim): noema#714.

C1 takes a per-tenant advisory lock at the start of the spend transaction, so concurrent spends queue behind the chain head instead of failing. The 3-attempt retry stays as the backstop. A forced-contention test uses eight different keys. An exhausted retry returns a typed retryable error, never UNKNOWN.

*Supersedes or changes:* Adds the lock to **A319**'s bounded retry (`NOEMA_DB_SERIALIZATION_ATTEMPTS=3`, which stays). Answers the load-sensitive `execution/e2e` failures seen on noema#663, #457 and #708.

### A340 (interim): Process.

Agents do not poll CI, and report once per push. Stopped agents stay stopped. EL's doc fix (`KeyDispatches` counts `DISPATCH_ATTEMPTED` per correlation, capability and target, per migration 0023) goes in as one line.

*Supersedes or changes:* Nothing superseded. The Steward's own practice since the Founder's order of 16 Nov.

## 2. What the Steward did where the rulings are silent

- **A317d, the contingency, placed as written.** The Architect asked for it to be placed as written. It is the fourth bullet of A317 (recorded in `DEC-2026-11-18-architect-rulings-a317-a328`): "If Codex has not read a head within 3 hours of READY FOR CODEX, SR plus one named agent's one-line read substitutes (SR plus two for Tier 1)." It stands unchanged: A334 and the withdrawal of A316 and A328 keep one Codex, and the contingency is how a head moves when that one Codex has not read it. A317c is the Tier 1 definition A334 refers to.
- **A328 is withdrawn,** and it was recorded in `DEC-2026-11-18-architect-rulings-a317-a328` (merged, docs#205). That record is not edited; this one says it is withdrawn. A295's second Codex session is withdrawn with it; A295's read order ("Codex reads unread pull requests first") is not touched.
- **The held-out author** (A322, A159) is the person named in A159 (`DEC-2026-11-12-architect-rulings-a148-a160`: the GOV-03 Benchmark Owner, who holds the access list with the Founder only), outside the agent system. This record carries no name.
- **CON-08 is registered** in plan v1.24 (CR-2026-11-18-A337-con08-parseintentref): `ParseIntentRef` next to the generated type, owner C1, REQ-API-001, Needs CON-03, the date of CON-07 (18 Nov), joined to the G2 review row GOV-11 Needs. The ruling gave the ID and the owner; the REQ, the Need, the date and the done-when (including the `@007` refusal of A337) are the Steward's smallest defaults and C1 may correct them.
- **The change request docs#206 (A338, A318): approval recorded, one question left.** The request offers two options and recommends (b). **(a)** a new PERD §28.2 arrow PLANNED to ESCALATING, whose cited event is the Execution Controller's budget-spent refusal (a PERD change: a new PERD version file, the vendored extract, the register, AGENT-29); **(b)** no new arrow: on `ReceiptBudgetSpent` the runner takes the existing PLANNED to EVALUATING and Trust decides ESCALATE `DISPATCH_BUDGET_EXHAUSTED` at T12, so EVALUATING to ESCALATING follows with a recorded Trust decision. A318's words ("an exhausted budget after the plan exists escalates") fit either. The CR itself says (a) would be the first transition made without a Trust decision, contrary to PERD §28.2's principle. **The approval does not say which option.** Per A332 this is not a wait for the Architect unless it conflicts with the PERD or an invariant, and (a) does conflict with the PERD principle; so the safer reading applies meanwhile: **option (b), which needs no PERD change.** EL or the Architect says so if (a) was meant, and the PERD change then follows. EL marks docs#206 ready; the Steward records the decision it takes.
- **A315** is recorded as relayed and read as an instruction to the Founder who approves: enabling auto-merge is the Founder's act. The Steward never approves or merges.
- **A314 and A315 are one line each.** The Steward has no fuller text. If the Architect wants more recorded, he sends it.
- **Next free ruling: A341.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A313 and A317 to A328 | |
| This record | A314 to A316 (A316 withdrawn), A329 to A340 | **A341** |
