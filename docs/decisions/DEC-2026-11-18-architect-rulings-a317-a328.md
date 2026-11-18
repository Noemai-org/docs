# DEC-2026-11-18 · Architect rulings A317 to A328 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 18 Nov 2026, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 18 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Twelve rulings, A317 to A328 (§1). The message was headed "A317 to A334"; it carried A317 to A328. A314 to A316 and A329 to A334 did not reach the Steward (§2). |
| **Closes** | The flow rules (A317); EL's, C1's, C2's, SR's, BO's, IL's, Voice's and FE's questions (A318 to A326); the Steward's own list (A327); the Codex lanes (A328). Closes the audit issue noema#597. |
| **Supersedes** | **A317** supersedes the merge rule of **A162**/**A176** and amends **A143** (Tier 1). **A320** supersedes the wiring order of **A286**/**A296**. Otherwise per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. The debt register (DEBT-48 to DEBT-51, DEBT-46's expiry), `docs/open-decisions.md` (OD-P-97 to OD-P-99) and the G0-N checklist change in this pull request. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 18 November 2026
- Closes: the questions named above; noema#597
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A317 to A328
- Decision: §1
- Rationale and evidence: the Architect's message of 18 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-22; AGENT-11, AGENT-14, AGENT-16, AGENT-18, AGENT-29; REQ-TRU-005, REQ-TRU-010, REQ-EXE-006, REQ-EXE-008, REQ-OPS-003, REQ-SEC-004, REQ-VER-005; PERD §23.1, §36.1, §41.1; SoT §0.4, §48
- Migration notes: A319's `kind` field is a minor contract change with a migration note (DEBT-48); the two EXE-10 event kinds go in place as a minor change before the tag
- Supersedes: see the Supersedes row above

## 1. The rulings, as given

### A317 (interim): Flow rules.

None of these touches a safety invariant.

- The WIP cap is suspended until G1 passes.
- A merge-main refresh push is always allowed. This supersedes A162/A176's "merge only on conflict".
- Tier 1 means Codex READY and SR READY at the same head, plus CI and one Founder. An independent role read is required only for migrations. This amends A143.
- If Codex has not read a head within 3 hours of READY FOR CODEX, SR plus one named agent's one-line read substitutes (SR plus two for Tier 1).
- Lane owners add their own one-line wiring to `compose.go`. EL reviews after merge, not before.
- Anyone may re-run a failed job once.
- A302, in full: the red proof is the failing job of the new tests, read as soon as that job completes. After that the agent pushes green at once. AGENT-11 still holds.

*Supersedes or changes:* **Supersedes** the "merge only on conflict" rule of **A162**/**A176**. **Amends A143** (Tier 1: the independent role read only for migrations). Suspends the WIP limit of plan §5 and the reading of **A253** until G1 passes (**A199** already lifted it for G1-lane pull requests). Restates **A302**.

### A318 (interim): EL.

- `Trust.Decide` carries `CorrelationID`, so T1 becomes a real check. Do it in a follow-up pull request after noema#710 merges.
- The bound and the dispatch count come from Trust's own decision and grant tables, read as the tenant with a read-only login. The dispatch count is the ledger row count by key (A153), not a chain re-verification.
- SSE reads the Record in chain order, with the chain position as `Last-Event-ID`. It does not wait on noema#693. EL owns `wire_events.go`.
- `wire_gateway.go` (EL): the input gateway's Start adapter, the per-tenant Recorder and Index, mounting `POST /v1/conversations`, and `/readyz` naming the gateway.
- The PLANNED→ESCALATING change request is approved: an exhausted budget after the plan exists escalates. The runner follows with a regression test (Tier 1).
- Amounts like "NGN 1,234.50" unblock when noema#709 merges.
- PLT-09 stays approved (A296): golangci-lint 2.5.0 pinned, gating after the 12 baseline findings are fixed.
- DEBT-46 expires before the G3 review.
- A306/A310 are ratified. The dispatch limit is at least 1, and `orchestrator.PERDMaxDispatchesPerKey` is the only source.

*Supersedes or changes:* Extends **A313** (`wire_events.go` and `wire_gateway.go` are EL's). Applies **A296**, **A306**, **A310**. Changes DEBT-46's expiry. noema#709 has merged (17 Nov).

### A319 (interim): C1.

- The A306 combination rule is confirmed. Most restrictive wins, in this order: REJECT, ESCALATE, CONFIRM, WAIT, PERMIT. A missing PERMIT means REJECT. EL adds a packcheck test that every action-graph capability has a PERMIT.
- TRU-10: inject the escalation set from the composition root now. A `kind` field on the action graph is a minor change with a migration note (a debt entry, due before G3).
- Every grant-issuing action decision must link a disposition. Flip C1's default to require it.
- The 40001 race (noema#714): C1 owns it. Add a bounded retry on SQLSTATE 40001 inside `Ledger.Spend`: 3 attempts, set as `NOEMA_DB_SERIALIZATION_ATTEMPTS=3` in Compose with no default in code. A forced-contention test is required.
- EXE-10: accept all of C1's recommendations with one change. The two event kinds go in place as a minor change before the tag, not a v4.
  - The clearing role comes from `init.sh` (protected, Founder approval in the pull request).
  - The listener gets its own network and Compose profile (IL).
  - MFA is deferred, as a debt entry.
  - It starts after G1.
- Fix U+001C to U+001F in the 17 schema members in place. In the same pull request, mask or refuse comma-joined runs of 10 or more digits outside the money shape (SR's A3, accepted).
- Money: "NGN 1,234.50" may be shown once noema#709 merges. The prefix stays any three capitals.
- Classification follow-ups: `reconstruction.v3` first. Tighten noema#664's minted-ID branch to the exact ULID body in one small pull request. Unify the write predicate (T11/T12) in one follow-up.
- noema#716: remove the `record_read` grant and test through a role that already has the privilege. Tenant creation becomes an init-time superuser step in `init.sh`, with no runtime creation. Keep the verifier's WITH CHECK policy beside the trigger. Merge #716 first, then #658 flips its exception.
- `KEY_ROTATED` is emitted by C1 at startup when the highest key version changes.
- Also C1: the REC-05 verifier bug (a tenant with no events or head row trips the kill switch), with a regression case first. The stale verify README. `ParseIntentRef` next to the generated type. `none_option_id` in the contract, now.
- noema#715: mark ready. The reader read bound is `NOEMA_READ_TIMEOUT_MS=2000`.

*Supersedes or changes:* Confirms **A306**. Applies **A297** (TRU-10), **A309** (EXE-10), **A275** (`none_option_id`), **A278**/**A279** and **A308** (digit rules). Opens the debt entries DEBT-48 (the `kind` field) and DEBT-50 (EXE-10's MFA) and DEBT-51 (`KEY_ROTATED`). Answers the 40001 race diagnosed on noema#663 and #457.

### A320 (interim): C2: the wiring config surface.

Names follow the `NOEMA_*` pattern. The values are bench values set in Compose, with no defaults in code. They come from SoT §48 and PERD's 1,200 ms provider timeout [REC]. You ratify them by merging.

- `NOEMA_PACK_DIR`: one mounted directory read at fixed relative paths.
- `NOEMA_STORE_TIMEOUT_MS=1000`.
- `NOEMA_COMPILE_TIMEOUT_MS=3000` (two provider attempts at 1,200 ms plus the hop).
- `NOEMA_SEAL_TIMEOUT_MS=1000`.
- `NOEMA_OUTBOX_INTERVAL_MS=1000`.
- Tenants: one instance per tenant from the mounted DSN directory. An unknown tenant is refused, with no fallback and no count in code.
- Evidence reads in G1 use the stand-in client through the egress gateway. Credentials are file-mounted, one setting per source, and C2 lists the names in the pull request. Live Tushe evidence counts only after G0.
- The session reference is `ses_` plus the first 26 Crockford characters of SHA-256 over the session's `jti` and tenant. No token material.
- Wiring order is superseded by A313: lanes run in parallel.

INP-01:

- A terminal-state follow-up is refused, and the customer is asked for a new request, until a decision record says otherwise.
- No `prior_intent` contract change.
- The contradiction rule is deterministic in the gate, and the model's flag is advisory.
- No eager void (D8: lazy refusal at spend and execute).

REC-02: OpenTelemetry is approved (PERD §36.1). `rapid` is already in `go.mod` and in use, so the Steward records it as adopted.

EVD-06: strip control characters, then cap, then detect. The cap is 256 as a bench setting. The call site is the Evidence layer after the payload read. One read id per read is the ObjectRef. The pack manifest is hash-pinned now, signatures later.

PLT-08:

- The STM-04 worker loop runs the dispatcher.
- `platform/outbox` stays and is noted in the next PERD version.
- Producers' raw inserts move to `Enqueue` in a separate refactor pull request.
- Retention belongs to DATA-01.
- 0031 is confirmed.

REC-06: a narrow ALLOW_WRITE alert entry (SR reads it). Add the CODEOWNERS line for record-verify in noema#687.

SR's noema#654 condition, as a follow-up pull request before the live run: do not record the reply body of a non-2xx provider response.

Mark noema#687, #688 and #693 out of draft.

*Supersedes or changes:* Supersedes the wiring order of **A286** (A313: the lanes run in parallel). Applies **D8** (no eager void) to INP-01. Opens OD-P-97 (OpenTelemetry) and OD-P-98 (`rapid` adopted). Confirms migration 0031 (**A299**).

### A321 (interim): SR.

Rulings A317 to A320 cover your items. In addition:

- A306 is ratified.
- noema#572's authorized-set defaults are confirmed. The T12 over-escalation is a debt entry (the runner stays the backstop).
- The comma gap is accepted.
- The grant key mount is a directory. `keyfiles.Load` is wired in `wire_trust.go` through `NOEMA_GRANT_KEY_DIR`. If Compose cannot give the file mode, an entrypoint copies the keys to a tmpfs. The loader is not loosened.
- DEBT-46 is owned by IL and EL, due before the G3 review.
- noema#716's `record_read` grant is removed.
- `reconstruction.v3` is first for the classification follow-up.

*Supersedes or changes:* Opens DEBT-49 (the T12 over-escalation). Sets DEBT-46's expiry.

### A322 (interim): BO.

- 24 of 28 fault effects is accepted. The four missing effects are named in the package and covered by the chaos subset.
- C2 states "read lane complete at SHA X" on noema#436.
- The M-02 fold and AT-19 join wait for noema#711 to merge.
- MEM-03: reconstruction is the source, the target is a typed RESOLUTION, AMBIGUITY stays out of v1, and a table test now. Update noema#704 to the final spec.
- Fix noema#717's two P2s: row 5 needs the owner's attestation, and row 10 must accept named exclusions.
- G0-N status: not yet passed. The Steward records the list.
- The held-out author is the GOV-03 Benchmark Owner named earlier, outside the agent system.
- Smoke runs nightly first, and on every merge only after G1 passes.
- Preconditions 4, 5, 9: not met, per section 2.
- A263 stands for the read-only key's scopes.

*Supersedes or changes:* Applies **A267**. The G0-N list is in `docs/poc/execution/sessions/2026-11-17-1000-G0-N-checklist.md` (updated in this pull request).

### A323 (interim): IL.

- Temporal client authentication (DEBT-46) is split before G3.
- SEC-09: `grantdrill` is a Go command in the core image. The setting is `NOEMA_GRANT_KEY_DIR`. Rotation is a restart. C1 writes `KEY_ROTATED`. There is no grant-minting endpoint.
- TEN-08a/b needs a Tushe-documented route that is always refused. The Founder asks Tushe.
- noema#711 stays parameterised with no defaults.
- Build SR's two first-dispatch conditions now: the `RECORD_ACCESSED` count and the job-log scan.
- Add a `mode=smoke` to the stack workflow: bring up the stack, check `/readyz` and the netcheck, and run no cases. You dispatch it, so first-run bugs show up now.
- Fix noema#698's P1, #700's three P2s, #670, #655's P1 and #711's P2s. For the #655 P1, the failure answers must come from the hostility proxy (AGENT-12). IL's own report says the P1 was addressed in `4edc9fce`, but Codex still reads a handwritten server at that head. IL checks Codex's thread and fixes whatever remains.
- The Intron URL test gets a narrow exemption (A325).

*Supersedes or changes:* Applies **A263**/**A276** (the `/partner` probe) and **A310**. Founder action: ask Tushe for a documented route that is always refused.

### A324 (interim): Voice.

- `PlaybackBounds` values for the lab run: `read_s=2`, `close_s=1` and `hold_s=5`, as bench values with no code defaults.
- Speech and TTS deadlines, and the audio budget, are required arguments with no defaults. The baseline run decides their values. The Architect sets them after that run.
- Your free-minutes split (20 baseline and 40 for the new endpoints) is accepted. The VOI-16 verdict is taken on Intron's real-time endpoints.
- noema#621: fix the unhashable `AudioSource` P2.
- The replaced test is accepted: the new type makes a bad bound unrepresentable, which is a stronger invariant, and this is recorded as the one replacement.
- noema#625's independent reader is C2. SR reads noema#689.
- The merge order is #689, #640, the connect factory, then the live latency run.
- The Founder asks Intron for the DPA draft.

*Supersedes or changes:* Applies **A266**/**A268**. Founder action: ask Intron for the DPA draft. The one test replacement is recorded here as AGENT-11 requires.

### A325 (interim): noema#625 versus A268.

AGENT-18 requires sources for external numbers, and Codex's P1 is right. A268 stays for API endpoints. A narrow exemption in IL's strict test lets that one notes file carry documentation-page URLs (docs hosts only, never an API endpoint). Voice adds the URLs and IL adds the exemption.

*Supersedes or changes:* Narrows **A268** (the Intron URL test stays strict) by one exemption.

### A326 (interim): FE.

- The benchmark inspector loads a static `scorecard-view.v1` file the bench runner emits, in the bench profile. No core route, because the core must not touch benchmark data (INV-22).
- noema#702 and #707 merge, which unblocks the generated parser.
- noema#609 and #699 wait for the wiring, then run Playwright against the real route.

*Supersedes or changes:* Applies **A311**.

### A327 (interim): Steward.

- `wire_events.go` and `wire_gateway.go` are EL's.
- Record A314 to A316 and these rulings.
- Post the G0-N status as "not yet", with the item list.
- File the debt entries: the pack `kind` field, the T12 over-escalation, `KEY_ROTATED`, and the A310 Temporal debt.
- Record the OD-P decisions: OpenTelemetry approved, `rapid` adopted, golangci-lint approved.
- Register EXE-10 and EXE-06's Needs. PLT-08's owner is C2. Mark PLT-06 done.
- Close noema#597 as an accepted exception.

*Supersedes or changes:* Extends **A313**. See §2 for what was done and what could not be.

### A328 (interim): Codex.

- Session A takes the core lane only, and Session B takes `.github`, tools, deploy, docs, benchmark, voice, ui and status.
- noema#658 stays NOT READY until #716 merges. Then C1 flips the exception and it is re-read.
- noema#714: the 3-attempt bounded retry (A319).
- Drafts noema#688, #693, #687, #715 and #716 are marked ready by their owners.

*Supersedes or changes:* Applies **A295** (two Codex lanes) and **A319**.

## 2. What the Steward did, and what it could not

- **A314 to A316 were not received.** A327 says "Record A314 to A316 and these rulings". The message carried A317 to A328 and nothing numbered A314, A315 or A316 (A313 is in `DEC-2026-11-18-architect-ruling-a313-split-composition`). The Steward records no text it has not seen. **The Architect needs to resend A314 to A316** (and A329 to A334 if they exist; the header said A334). The next free ruling is therefore not A329 until the Architect says so.
- **OD-P decisions filed (A320, A318, A327).** OD-P-97: OpenTelemetry approved (PERD §36.1). OD-P-98: `rapid` adopted (already approved by DEC-2026-11-03-rapid-test-dependency; the PERD label is dropped in the next PERD version). OD-P-99: golangci-lint 2.5.0, pinned, gating after the 12 baseline findings are fixed (A318; PLT-09, A296). All three are CLOSED in `docs/open-decisions.md`.
- **Debt filed (A319, A321, A327).** DEBT-48: the action graph has no `kind` field (A319; due before G3). DEBT-49: the T12 over-escalation (A321; the runner is the backstop). DEBT-50: EXE-10's clearing role has no MFA (A319; deferred). DEBT-51: `KEY_ROTATED` is not emitted yet (A319, A323; C1). **DEBT-46** (the A310 Temporal debt) keeps its number and now expires **before the G3 review** (A318, A321), and its split before G3 is noted (A323). Owners and tiers are the Steward's proposals where the rulings name no tier.
- **EXE-10, EXE-06 and PLT-08 (A327).** Already registered in plan v1.23 (docs#202): EXE-10 (owner C1, Needs EXE-06), PLT-08 (owner C2). EXE-06's row is unchanged (Needs SEC-04). Nothing is added. **PLT-06 is already Done** in `tasks.csv` (the audit of 17 Nov), so nothing changes there.
- **G0-N status (A322, A327): not yet passed.** The list, with states and owners, is `docs/poc/execution/sessions/2026-11-17-1000-G0-N-checklist.md` (rewritten from the evidence of 18 Nov) and is posted on noema#183.
- **noema#597** is closed as an accepted one-time exception (A327), with the facts in the comment.
- **The PLANNED→ESCALATING change request (A318) is approved** and recorded. The Steward found no such request in `docs/`; the text of the change (the investigation state machine, PERD §28.2 and the state registry) is the runner's, and any PERD or registry edit it needs is a separate change (the registry is vendored into noema: a drift-safe order is needed). EL or the Architect names where the request lives.
- **Held-out author (A322).** The ruling names a person; this record says only "the GOV-03 Benchmark Owner named earlier, outside the agent system".
- **Founder actions in these rulings:** ask Tushe for a documented route that is always refused (A323); ask Intron for the DPA draft (A324); approve `init.sh` changes in the pull request that makes them (A319, protected path).
- **Not done by the Steward:** the pull-request moves of A317 to A326 (marking drafts ready, merge order, fixes) are the named owners'.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A313 (A314 to A316 not received) | |
| This record | A317 to A328 | **to be set by the Architect** (see §2) |
