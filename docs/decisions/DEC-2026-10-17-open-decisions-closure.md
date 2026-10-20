# DEC-2026-10-17 · Closure of every open decision

| | |
|---|---|
| **Status** | Accepted by the Founder on 17 October 2026. The Technical Co-Founder confirms by approving the pull request that adds this record |
| **Date** | 17 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | Canonical OD-01, OD-02, OD-03, OD-06, OD-08, OD-10, OD-12, OD-13, OD-14, OD-15, OD-16. Provisional OD-P-02, 04, 05, 07, 09, 10, 11, 12, 20, 21, 22, 24, 25, 27, and 28 to 41. Conflicts SOT-C-03, 04, 05, 12, 13, 14, 16, 18 |
| **Confirms as already closed** | OD-P-13, 16, 17, 18, 23 (DEC-2026-10-12, DEC-2026-10-13); OD-P-14, 15 (DEC-2026-10-16 execution reset E2, clarifications C8); OD-P-19, 26 (DEC-2026-10-16 money and value lists); OD-P-42 (execution reset E3, E4); OD-P-43 (execution reset E6) |
| **Amends** | SoT §46 (canonical rows), §19.3 (pricing wording), INV-20 (freeze wording), §47.1 (identity granularity), Appendix A (WAIT, UNKNOWN); PERD §67.2 and §67.3 (adoption status); the conflicts register |
| **Inputs reviewed** | Five agent decision packs dated 17 Oct 2026. Where they disagree with each other, with the PERD's specified values, or with decisions already accepted, this record states the ruling; see §4 |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Confirms as already closed, Amends and Inputs reviewed; the template headings it lacks point to the sections below.

- Status: Accepted by the Founder (see the table above)
- Date: 17 October 2026
- Closes: OD-01, OD-02, OD-03, OD-06, OD-08, OD-10, OD-12, OD-13, OD-14, OD-15, OD-16 (canonical; the provisional items and conflicts are listed in the table above and in §3)
- Owner: Founder and Technical Co-Founder
- Decision: §2 (canonical decisions), §3 (provisional items) and §5 (gates converted to tasks); §1 is the closure rule and §4 the rulings on the inputs
- Rationale and evidence: the "Inputs reviewed" row, §1 and §4; the verification and "Agent decisions" in the pull request that adds this record
- Affected requirement IDs / SoT sections: SoT §46, §19.3, INV-20, §47.1 and Appendix A (SoT v1.8); PERD §67.1 to §67.3, §37.1 and the adopted defaults (PERD v1.8); the conflicts register; plan tasks for the §5 gates (plan v1.8); the requirement count (153) and every other invariant and gate condition are unchanged
- Migration notes: none; no code, contract or `noema` change
- Supersedes: None. It confirms OD-P-13 to OD-P-19, OD-P-23, OD-P-26, OD-P-42 and OD-P-43 as closed by their existing records

---

## 1. The closure rule

**"Closed" means the decision is made.** Evidence that can only come from reality (a partner's baseline, a voice field run, a named person, counsel's review) is not an open decision. It is a **gate** with an owner and a plan task, and it passes only on evidence. No gate is marked passed by this record.

**Where the PERD specifies a value, the PERD value is adopted as written.** Nothing is re-derived and no number is invented. Changes to thresholds, TTLs, budgets and schedules still need a full benchmark run and human approval (AGENT-16).

## 2. Canonical decisions (SoT §46)

| ID | Decision | Gate that remains (owner) |
|---|---|---|
| **OD-01 Pricing** | First pilot: fixed fee, time-bounded, one exception subtype. Success criteria, eligible-case definition, denominator, exclusions, data source and dispute process are agreed in writing before signature. Never per seat. Outcomes are counted from day one in four buckets: verified success, verified safe refusal, verified escalation, unresolved or unknown. **A correct refusal or escalation is a paid outcome, priced below a verified success. A wrong action earns nothing. Noema is paid for being right, never merely for acting.** Outcome-linked pricing is tested only after both sides agree on what counted. The pilot price is set by the Founder per partner from delivery cost; no figure is fixed here | First partner baseline measured (Founder) |
| **OD-02 Policy evaluation** | Deterministic, versioned policy-as-data evaluated **only in the Go core**. No Cedar or OPA in the POC. No policy logic in the model service. Missing, malformed or conflicting policy never yields ALLOW | Revisit Cedar/OPA import only with a parity suite and a buyer need (Phase 4) |
| **OD-03 Ambiguity thresholds** | 0.35 auto-resolve margin; escalate above 4 candidates. These are **pack data** (intent-node `disambiguation`, SoT §15.3), versioned and recorded in the Decision Record, not hard-coded. They are separate controls from the PERD resolution values (OD-P-30), and no score ever authorises an action | Changes need a full benchmark run, locale and family slices, and human approval |
| **OD-06 Record integrity** | POC: append-only, hash-chained Record in Postgres. Canonical serialisation, a chain verifier in CI and the nightly job, and restricted write roles. No anchoring, blockchain or notarisation. It is described as **tamper-evident within the POC threat model**, never as immutable. Before Phase 2 production: periodic anchoring of chain heads to a separately controlled write-once store, with the mechanism chosen in the Phase 2 threat model | Anchoring design before Phase 2 (Technical Co-Founder) |
| **OD-08 Data retention** | Minimal by default. Raw audio is discarded after transcription unless a documented dispute needs it, with consent, purpose, expiry and restricted access recorded. Identifiers are masked before any model-provider call. Logs carry no secrets, full account numbers, raw audio or unredacted transcripts. Synthetic data only until a partner-specific schedule exists (data classes, purpose, region, access, retention, deletion, sub-processors, incident owner). **No universal retention period is invented here** | Partner schedule approved with counsel before partner data flows (Founder) |
| **OD-10 Public benchmark scope** | Publish taxonomy, case schema, fault model, scoring method, evaluation protocol and aggregate results, **including failures and safety-gate results**, with case counts, versions, confidence bounds and limitations. Never publish the held-out set, oracle labels, partner data, secrets, or exploit detail that enables abuse. A synthetic result is never presented as production performance. The independent reviewer (REV) checks for leakage and reproducibility before anything is published | End of Phase 1 |
| **OD-12 First design partner** | One Nigerian bank or large fintech, through an overlay in its own app or support channel. Qualifying conditions: a named executive owner of the KPI; measurable exception volume; access to authoritative evidence; a technical integration owner; agreement to baseline measurement, shadow mode and stop conditions; willingness to review failures and refusals, not only successes. Exactly one exception subtype is chosen from discovery evidence ("debited, not credited" is a hypothesis, not a given). If no candidate qualifies, discovery continues; scope is not widened | 10–20 discovery conversations before Phase 1 ends; partner chosen (Founder) |
| **OD-13 First production deployment** | Single-tenant SaaS, in a partner-approved region, with separate credentials, database, keys, network boundary and operator access. No multi-tenant production until tenant-isolation, cross-tenant negative tests, backup/restore and independent review pass. Customer VPC only when a qualified buyer requires it and sponsors the cost. Two deployables, unchanged | Region and contract requirements confirmed before shadow mode (Technical Co-Founder) |
| **OD-14 Certifications** | Keep the SoT §50.3 roadmap: SOC 2 Type I in Phase 2, Type II in Phase 3, ISO/IEC 27001 and 42001 in Phase 4. Build the controls now (access reviews, change management, incident response, vendor review, backup/restore, evidence collection). Never claim a certification before the report exists | Buyer requirements confirmed before Phase 3 spend (Founder) |
| **OD-15 Mode 2 contract** | Not defined or implemented in the POC. Only the concept is frozen: request → decision → optional grant → execution → verdict, with the delegation chain. Noema re-evaluates at its own boundary and never trusts an upstream ALLOW. The exact contract is derived from Mode 1 production evidence | Phase 4 planning |
| **OD-16 Held-out custody** | The held-out set lives in `Noemai-org/benchmark-heldout`. **The Founder is the custodian and runs release evaluations** (execution reset E2, C8: the benchmark owner never drives C1 or C2 build work). The Technical Co-Founder and every coding agent have no access. Release runs evaluate a frozen commit with pinned configuration and produce a signed result bundle. Because the custodian is a founder rather than an outsider, every published benchmark report states this, and REV reviews leakage controls before any public claim | Repository permissions verified (Founder) |

## 3. Provisional items

| ID | Decision |
|---|---|
| **OD-P-02 Decision log** | `docs/decisions/` holds founder and engineering decisions alike. Technology decisions never live in `brain` (execution reset E8). A record that changes the SoT lands with the SoT edit and the regenerated register (AGENT-29) |
| **OD-P-04 Runbooks** | No fictional runbooks. Before any customer-facing action, each of these must be written against the real system and **exercised**: kill switch, rollback, incident response, unknown-outcome reconciliation, credential rotation, backup/restore including Record integrity, provider outage, and data deletion. Each has an owner and a last-tested date. Scaffolds do not satisfy the gate |
| **OD-P-05 Legacy drafts** | No action; nothing is reconstructed. Originals are archived only if found, labelled non-authoritative |
| **OD-P-07 SEC-/PERF- IDs** | Not minted. Trace to PLAT-NFR, POC-NFR, INV, BD and AGENT IDs plus SoT §47 and §48 |
| **OD-P-09 Risk classes** | `PROHIBITED` is core and structural. R0–R3 are fintech pack data exactly as SoT §34.3. Declared risk is never below the consequence profile (`packcheck` already enforces this). An unknown risk label fails pack validation |
| **OD-P-10 Similar names** | Names unchanged. Distinct enum types per field in `/contracts` (for example, `ExecutionState.OUTCOME_UNKNOWN` versus the synthetic transaction state `EXECUTION_OUTCOME_UNKNOWN`; benchmark severity `S0–S3` versus data sensitivity), with negative contract tests proving they cannot be cross-assigned |
| **OD-P-11 POC-FR-17** | POC-only; no PLAT ID |
| **OD-P-12 Legacy concepts** | None adopted. A real failing case raises a specific AGENT-02 entry |
| **OD-P-20 Streaming TTS** | Provider-neutral per-locale routing. Where streaming TTS is missing or fails its gate, the verified answer is shown as text. Demo TTS is English and Pidgin only (C8 cut item 1); Yoruba, Hausa and Igbo are still measured. No locale is claimed until it passes |
| **OD-P-21 Field protocol** | PERD §45.4 is the gate, as written: Tecno Spark on Airtel 3G with 4G disabled; genuine Lagos noise; at least 100 sessions with at least 50% Pidgin; P95 ≤ 2.5 s from end of speech to admitted Intent Object; consent-recorded sessions. The Voice Lead role owns it. Extra devices and networks are allowed as non-gating diagnostics |
| **OD-P-22 Secrets** | Local: file-mounted secrets outside git only. CI: GitHub Environments (`core-ci`, `model-ci`, `bench`, DEC-2026-10-13) with OIDC where supported. Hosted: the managed secret store of the host the Engineering Lead records in the `local-setup` runbook (execution reset E6). Credentials are separated per deployable and environment. Grant and confirmation HMAC keys live only in the core. The model service holds no core-database, Temporal, adapter or grant credentials. No secret in source, images, logs, prompts, traces, Record payloads or agent context |
| **OD-P-24 Escalation without a case** | POC: a durable Noema-owned handoff record (reason, urgency, evidence references, target queue if known, correlation ID), shown in the ops inspector. The customer is told the truth: no case reference exists yet, and someone must act. Nothing claims a person accepted it without an acknowledgement. **No external `escalation.handoff` event in the POC.** It is added only after partner discovery specifies the receiver, acknowledgement and retry semantics |
| **OD-P-25 Time zone and reviewers** | Store UTC instants plus an IANA time zone. The tenant default is `Africa/Lagos` and is configurable. The zone is never inferred from language or phone number. Native reviewers are contracted for yo, ha, ig and pcm before labels freeze, and they adjudicate disagreements. Machine translation is not evidence |
| **OD-P-27 Synthetic clocks** | Every synthetic time, deadline and clock is labelled `SYNTHETIC` in UI, logs, exports and demo narration. No regulatory or legal claim without counsel review of the exact wording |
| **OD-P-28 Trust semantics** | PERD §23.1 adopted as written: the seven outcomes with WAIT and UNKNOWN defined, linked disposition and action decisions with `disposition_decision_id`, and R0 reads without grants (still principal-scoped, allow-listed and recorded). Closes SOT-C-03, 04, 05 |
| **OD-P-29 Investigation state** | **PERD §28.2 adopted exactly as written** (RECEIVED → INTERPRETING → …), as a projection changed only by named, guarded commands. It is kept separate from transaction state, execution state, verdict, case lifecycle and Temporal status. No invented state names |
| **OD-P-30 Resolution** | PERD values adopted: ranking weights, 0.70 floor, 0.85 key-slot threshold, 10-minute clarification, 2 rounds, 30-minute dormancy, 72-hour resume. These are independent of OD-03 |
| **OD-P-31 Grants and confirmations** | 10-minute TTL for both, single-use, exactly bound, with revalidation before dispatch. A confirmation is never a grant. Any change voids it |
| **OD-P-32 Recovery** | A budget of 2 dispatches, which is a ceiling, not an obligation. Verify before any retry. NONE retry-safety means one dispatch at most. Verification reads use the **PERD schedule: 3 attempts at 1, 3 and 9 s of simulated time** |
| **OD-P-33 Watches and callbacks** | **PERD schedules as written.** Watches: 5, 15 and 30 min, then every 60 min, plus named events, until the deadline (then UNKNOWN and a RecoveryRequest). Callbacks: at least once from the outbox, exponential from 1 s doubling, capped at 10 min, at most 12 attempts, then a metric and an ops alert. Delivery state is never business outcome |
| **OD-P-34 Contracts and identifiers** | JCS; LP key encoding; `policy_scope = policy_id`; the PERD ID scheme and Record events. **`evidence_set_hash` is the LP construction in DEC-2026-10-16 clarifications C1. The JCS-array construction proposed by one input is rejected.** Closes SOT-C-13 |
| **OD-P-35 Policy** | **The PERD §23.4 schema and ladder as written**: across classes SAFETY > PROHIBITION > TENANT_SECURITY > REGULATORY > WORKFLOW > DEFAULT; within the winning class REJECT > ESCALATE > CONFIRM > WAIT > PERMIT; no matching PERMIT gives `NO_PERMITTING_RULE`. No invented alternative ladder |
| **OD-P-36 Freeze** | **The PERD allow-list exactly**: escalation case, evidence record, routing, held as pack data. Nothing else, and specifically no "corrective action" exception. A model can never release a freeze. INV-20 is reworded to name the allow-list. Closes SOT-C-12 |
| **OD-P-37 Explanation** | PERD facts contract and claim validator. On validation failure, a deterministic fallback from verified facts |
| **OD-P-38 Fault injection** | PERD §37.1 FaultPlan and effect enum, **amended by DEC-2026-10-12**: `source` ∈ TUSHE, PROXY, MOCK_CASE; the `clock` block drives only Noema's simulated clock and `mock-case`, never Tushe, where time is per object. Deterministic release runs (probabilities 0 or 1); seeded stress runs are separate |
| **OD-P-39 Benchmark** | PERD case schema, the evil provider (test-only, no credentials), and A0 as a diagnostic that never appears in a comparative claim. Tier 0 results reported separately. Closes SOT-C-18 |
| **OD-P-40 Infrastructure** | PERD §36.1, §41.1 and §65.1 adopted: a separate `temporal` database that Noema code never reads; per-power Postgres roles with one core process identity in the POC (SoT §47.1 reworded); the PERD topology, **amended by execution reset E6** (the only public component is the webhook relay holding only the signing secret; the core pulls from it; the proxy sits on the pull in bench only). Closes SOT-C-14, 16 |
| **OD-P-41 Retention (synthetic)** | PERD §38.3 defaults for synthetic data. Partner data follows OD-08. Deletion covers derived artefacts and is recorded without keeping the deleted data |

## 4. What was rejected from the inputs, and why

| Proposal | Ruling |
|---|---|
| Replacing `docs/open-decisions.md` with a hand-written file whose rows link to unrelated decision records | **Rejected.** The canonical table is generated, and the links fabricated provenance |
| The Technical Co-Founder / "Chief Architect" as benchmark owner | **Rejected.** That person builds the core; this breaks OD-16 and C8 |
| Benchmark repository in `noema-org` | **Rejected.** The organisation is `Noemai-org` (execution reset E1) |
| A fixed pilot price band ($150k–$250k), a ">10M monthly transfers" qualifier, "logs purge at 90 days", specific cloud vendors and regions | **Rejected.** Invented facts or premature vendor choices |
| Policy evaluated in "Go/Python" | **Rejected.** The model service never evaluates policy (INV-01) |
| "Hard-coded" ambiguity thresholds | **Rejected.** They are pack data |
| A gRPC and webhook Mode 2 contract now | **Rejected.** OD-15 is defined after Mode 1 production |
| An invented investigation state machine (NEW → GATHERING_EVIDENCE …), verification schedule (0.5/2/5 s), watch schedule (2 s … 10 min), callback schedule (1 s … 10 min), policy ladder, and freeze "corrective action" exception | **Rejected.** Each contradicts values the PERD already specifies |
| `evidence_set_hash` as JCS array of pairs | **Rejected.** It contradicts the committed and verified C1 construction |
| "No G1 attempt until G0 passes" | **Rejected.** Execution reset E4: G1 may run before G0-T and counts only once G0 passes |
| A receiver that writes to the inbox or forwards into the core | **Rejected.** Execution reset E6: the relay holds only the signing secret, and the core pulls |
| "DEC-2026-10-06 governs the enum lists" | **Superseded.** DEC-2026-10-16 money and value lists §2 |
| Field protocol with invented device and utterance counts | **Rejected as gates.** PERD §45.4 is the gate; extra devices are diagnostic only |
| An `escalation.handoff` external event now | **Deferred.** No receiver is specified; a durable internal handoff covers the POC |

## 5. Gates converted to tasks

These are tracked in the plan, not as open decisions.

| Gate | Owner role | Due |
|---|---|---|
| First partner selected, with a qualified KPI owner and subtype; baseline measured | Founder | End of Phase 1; before any paid pilot or ROI claim |
| Partner data schedule and provider due diligence approved with counsel | Founder | Before partner data flows |
| Held-out repository permissions verified; release procedure written | Founder (B) | Before the first held-out run |
| ARM and REV engaged under NDA (GOV-21) | Founder | Fri 30 Oct |
| Native reviewers for yo, ha, ig, pcm contracted | Founder | Before labels freeze |
| Field protocol run and evidence bundle (PERD §45.4) | V | G5 |
| Counsel review of any regulatory wording | Founder | Before any external regulatory claim |
| Runbooks written and exercised (OD-P-04 list) | EL | Before any customer-facing action |
| Region and deployment requirements confirmed | Technical Co-Founder | Before shadow mode |
| Buyer certification requirements gathered | Founder | Before Phase 3 spend |
| Record-head anchoring designed | Technical Co-Founder | Before Phase 2 production |

## Agent decisions

Where this record was silent, the pull request that adds it chose the following. Each keeps the SoT, the PERD and the plan consistent and leaves every gate's conditions and invariants unchanged.

- **A1. Base and already-closed items.** The pull request is based on the top of the docs stack, because D12 (money and value lists) had merged into it. OD-P-13, 16, 17, 18, 19, 23, 26 and 43 were already shown as closed with their records linked. OD-P-14, OD-P-15 and OD-P-42 were still shown open, so they are closed with a pointer to their existing records (execution reset E2 and clarifications C8; clarifications C8 and GOV-21; execution reset E3 and E4), not to this one.
- **A2. PERD values.** Every value this record quotes "as written" matches PERD v1.7 (the table is in the pull request). Three wording points: the retention defaults for synthetic data are in the retention column of PERD §38.2, not §38.3 (§38.3 holds the data requirements), so PERD §38.2 is the adopted text; OD-P-41's sentence that deletion covers derived artefacts has no PERD counterpart, so this record governs it and the PERD is unchanged; and the freeze allow-list is the three capabilities `CREATE_ESCALATION_CASE`, `RECORD_INVESTIGATION_EVIDENCE` and `ROUTE_TO_INTERNAL_OWNER`.
- **A3. Notes already in the PERD.** PERD §65.1 already carries the execution reset E5 and E6 text (the relay holds only the signing secret, the core pulls, the proxy sits on the pull in the benchmark profile only), and §37.1 already has the three `source` values. No duplicate is added. PERD v1.8 adds the one missing piece to §37.1: the `clock` block drives only Noema's simulated clock and `mock-case`, never Tushe.
- **A4. A misplaced block, corrected.** The reason-code block of DEC-2026-10-16 money-and-value-lists was inserted in PERD v1.7 under §23.1; it belongs in §23.3, where the brief for that record put it. PERD v1.8 moves it, unchanged.
- **A5. What `[ADOPTED]` covers.** `[REC]` becomes `[ADOPTED DEC-2026-10-17]` only on statements that belong to the fourteen groups of PERD §67.3, in the sections that carry them (listed in PERD v1.8, "Changes in v1.8"). Every other `[REC]` stays, because this record does not adopt it. The three reason codes marked `[REC]` by DEC-2026-10-16 money-and-value-lists also stay.
- **A6. SoT label.** In §19.3 the tag `[OPEN — OD-01, decide before the first paid pilot]` becomes `[DECISION — OD-01, DEC-2026-10-17-open-decisions-closure]`, because the row it pointed to is decided. The decided §46 rows show "Closed" in the "Decide by" column, as OD-07, OD-09 and OD-11 do.
- **A7. Plan tasks.** Of the eleven rows of §5, GOV-21 (ARM and REV), GOV-08 (native reviewers) and VOI-08 to VOI-14 (the field protocol and its evidence) already exist. The others become tasks. Gates that fall due after Fri 13 Nov are listed under a new plan heading, "After the build window", with the date and week `AFTER`, so that none is shown as due inside the four weeks; `tools/plan_index.py` accepts that heading.
- **A8. Conflicts.** SOT-C-03, 04, 05, 12, 13, 14, 16 and 18 are resolved. The ten that remain open are listed in the pull request; none is decided here.

## Correction note (20 October 2026): the OD-P-41 source reference

Raised by the retrospective review on Noemai-org/docs#36. The §3 row for **OD-P-41 Retention (synthetic)** cites "PERD §38.3 defaults for synthetic data", while A2 above says the retention defaults are in the retention column of PERD §38.2 "not §38.3 (§38.3 holds the data requirements)". Reading both sections of PERD v1.9 (the text is unchanged since v1.8):

- **§38.2 (Entities)** has a "Retention (POC)" column on the entity table, tagged `[ADOPTED DEC-2026-10-17]`.
- **§38.3 (Data requirements)** also holds a table headed "Retention and data-handling defaults for the POC `[REC]`" (benchmark fixtures, utterances, recordings, raw audio, prompts and responses, logs, Record objects, secrets), followed by REQ-DATA-003, which says to apply "the retention column above".

So neither side was right alone. The §3 row's citation of §38.3 points at a real retention table, and A2's statement that §38.3 holds only the data requirements, and that the defaults are "not" there, was wrong. **What this record now says:** OD-P-41's retention defaults are in two places, the §38.2 retention column (the text that carries the adoption tag, and the one A2 names as adopted) and the §38.3 retention and data-handling table. The §3 citation is therefore correct as one of the two, and A2's "not §38.3" is withdrawn. The original wording above is left as it was.

**Open point, not decided here.** The §38.3 table still carries `[REC]` in PERD v1.9, although OD-P-41 is shown as adopted. This correction does not adopt it. Whether the §38.3 table is adopted, and a PERD edit to its tag, is a founder decision (a new PERD version and a decision record).

## Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founder | Approved | 17 Oct 2026 | Written instruction to the coding agent |
| Technical Co-Founder | Confirms | Date of approval | Approving review on the pull request that adds this record |
