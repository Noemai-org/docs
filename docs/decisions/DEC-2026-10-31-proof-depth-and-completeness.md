# DEC-2026-10-31-proof-depth-and-completeness

- **Date:** 31 October 2026
- **Status:** Decided by the Founder on 31 October 2026. The Technical Co-Founder confirms by approving the pull request that adds this record. Items marked **FOUNDER ACTION** below need a further explicit founder step before the work they gate can start.
- **Deciders:** Founders (the Founder and the Technical Co-Founder; DEC-2026-10-16 E2).
- **Prepared by:** the Principal System Architect, from four founder review discussions held 30–31 October 2026.
- **Applies to:** SoT v1.9 → **v1.10**; PERD v1.18 → **v1.19**; four-week plan v1.9 → **v1.10**; `tasks.csv`; gate record G3; the debt register; a new derived architecture map; the role-agent prompts.
- **Change control:** this record is the written change request required by plan §19 and AGENT-29. The SoT edit, the PERD edit, the plan edit, the regenerated task list and the regenerated indexes move together in one docs pull request, followed the same day by the vendored-copy re-point in `noema` (REQ-OPS-005).

## Context

On 30–31 October the Founder reviewed the architecture, the test strategy and the product strategy against the SoT v1.9, the PERD v1.18 and the plan v1.9, and compared Noema's approach with what two leading enterprise-agent companies (Sierra and Intercom Fin) have said publicly about their engineering. The review found that:

1. Every subsystem the Founder asked about (context, disambiguation, the Action Graph, the three taxonomies, identity, authorisation, confirmations, human escalation, the scorecard) is specified, mostly under canonical names that differ from the names used in conversation; most of it is not yet built and proven (G0-N, G0-T, G1 and G2 have not been held; all 226 tasks are `Unassessed`).
2. Several items the SoT deferred beyond the POC are core to Noema's proposition and are pulled into the POC: the Context Fabric, compensation declared and executed per capability, authenticated Record writers and external anchoring of the Record.
3. The test strategy needs explicit crash-consistency and corrupted-payload testing, and every relevant merge must pass a chaos subset.
4. A small number of practices from the market are worth adopting, and a small number are explicitly rejected so they are not proposed again.

## Decisions

### A. Names, map and human escalation

**D1. Canonical names stay; a derived architecture map is added.** The SoT and PERD component names are the names used in code, contracts and documents (PERD §18.2). The Repo Steward adds `docs/architecture-map.md`: the founders' terms, the canonical names, the governing sections, the code paths, the tasks, the owning roles and the live build status. It is derived and non-normative, like `docs/requirements-index.md`; where it disagrees with the SoT or the PERD, they win.

**D2. Human-in-the-loop design confirmed.** When Noema escalates or reaches UNKNOWN, it routes the case into the enterprise's own case system (`ROUTE_TO_INTERNAL_OWNER`) with the deterministic operator evidence packet (REQ-EXP-004). Approvals use the confirmation contract (SoT §43.2a) with approver principals from the IdP. `mock-case` stands in for the enterprise's case system in the POC; it is not a Noema console. The evidence panel (POC-FR-17) is for the demo. An operations console (Studio, maker-checker approvals; PLAT-FR-15, PLAT-FR-17) is post-POC.

**D3. The Repo Steward's evidence-based status assessment of all tasks is the test of what is built.** No subsystem is reported as built without merged code and tests that meet its `done_when`.

### B. Understanding, context and disambiguation

**D4. The Context Fabric is built in the POC.** It moves from "not in the POC build list" into SoT §35.1. Scope: the authenticated session (principal, tenant, channel, locale), the conversation history of the open journey, the requester's prior cases read fresh from the enterprise's case system, and the requester's prior Noema journeys read from the Record. Rules: identity comes only from the session (INV-12); every prior-case fact is read through the Evidence Layer with provenance and FactStatus and is principal-scoped; nothing is copied into a standing replica of enterprise data (PLAT-NFR-06); context informs interpretation and Entity Resolution but never authorises anything; history and prior cases are bounded by count and age set in pack data. PERD: REQ-CTX-009, REQ-CTX-010.

**D5. Three disambiguation diagnostics join Tier 1:** turns to resolution, the unnecessary-clarification rate, and auto-resolve precision. They are reported with every run; targets are set after the first full-suite run and adopted by a later decision record. PERD §48.3, REQ-BEN-009.

**D6. Consistency is measured as pass^k for every model-dependent case.** Each Understanding-dependent case runs k = 5 times; a case passes only when all five runs are correct. pass^k is a Tier 1 diagnostic beside D5. The deterministic Trust layer is expected to be identical across runs (INV-21). PERD REQ-BEN-009.

**D7. Scoped speculative prefetch is allowed.** Candidate evidence reads may start while the Intent Compiler runs, only through the principal-scoped candidate API (REQ-CTX-006), within data minimisation (PLAT-NFR-10). Results not used by the final Intent Object are discarded, never cached across journeys and never written to the Record as facts. PERD REQ-CTX-006 (amended).

**D8. Voice stays a modular pipeline in production: transcribe, reason, synthesise.** Speech-to-speech models are not in a production path until a benchmark run shows no increase in safety failures; the transcript is what key-slot confidence depends on (REQ-AMB-007). Before every field session, the voice subset runs through a simulation library (Lagos street and market noise, Nigerian accents, Pidgin, Yoruba, Hausa and Igbo code-switching, low-quality microphones, 3G jitter and loss), and native-speaker testers check each of the four languages plus en-NG. The field gate G5 stays the real test. PERD REQ-VOI-006, REQ-VOI-007.

### C. Execution, state and planning

**D9. The Action Graph must be a graph, never a list of endpoints.** The Engineering Lead verifies the fintech pack's graph (PERD §24): real nodes with preconditions and postconditions, edges with `depends_on` and conditions, and recovery and escalation references, and that the planner selects its path through the graph. `packcheck` (PCK-02) rejects a graph that is a flat list: a node other than a root with no incoming edge, a node with no postcondition, a write node with no precondition, or a plan that is not a path in the graph. If the graph is a flat list today, that is the first fix. PERD REQ-AG-001 (amended), REQ-AG-003.

**D10. Convergence windows separate expected lag from real contradiction.** Each reconciled fact pair in `packs/fintech/recon_rules/` declares a convergence window. Inside the window, a disagreement yields WAIT with an Outcome-style watch and a deadline; outside it, the state is CONTRADICTORY, writes on the target freeze (INV-20) and the case escalates. Windows are pack data, versioned, never loosened without a benchmark run (AGENT-16). PERD REQ-RES-005.

**D11. Compensation is declared per capability and executed in the POC.** Every capability descriptor declares its compensation (`NONE_REQUIRED`, `INVERSE_CAPABILITY` with the registered capability and parameter mapping, or `ESCALATE_ONLY`). `packcheck` rejects a `REVERSIBLE` or `COMPENSABLE` capability with no declared compensation and an `IRREVERSIBLE` one that declares anything but `ESCALATE_ONLY`. A compensation is a write like any other: it runs only after Trust decides it as recovery, under a new ALLOW and a new grant, and Outcome verifies it (INV-15, AGENT-08). Monetary capabilities and their compensation stay out of the POC (BD-08). SoT §35.1 moves "multi-step compensations" for non-monetary capabilities into the POC. PERD REQ-CAP-004, REQ-RCV-005.

**D12. Legacy-API protection.** In addition to per-capability limits, timeouts and circuit breakers (CAP-01), tenant and principal rate limits (TRU-11), the 429 case (US-21), the two-dispatch recovery budget and no retry without a new grant: Execution and the Evidence Layer honour `Retry-After`, use jittered exponential backoff on reads, and cap concurrent requests per target system. Each is proven against the hostility proxy's 429 and near-timeout faults. PERD REQ-CAP-005.

**D13. No two-phase commit.** Third-party enterprise APIs cannot take part as resource managers, and a blocking coordinator reduces availability. Noema keeps: one local Postgres transaction for the grant spend, the idempotency key and the outbox event; at most one dispatch per grant; idempotency at the target where supported; then independent verification, recovery and declared compensation. PERD §70 ED-18.

**D14. Crash-point matrix for Execution, as a G3 requirement.** The core process is killed at each of four points: before the spend commits; after the spend commits and before dispatch; after dispatch and before the response; after the target commits with the response lost. After each restart, a test asserts exactly one effect at the target and the correct final state of grant, receipt, attempt, verdict and Record. This is a scope change to G3, approved. PERD REQ-TST-008; plan §3.1 G3 row; gate record G3.

**D15. Corrupted-payload fault families.** The hostility proxy adds truncated bodies, invalid JSON, a wrong `Content-Type`, an empty body with a success status, and a valid body with an extra or missing required field. Each must be observed by the adapter as UNAVAILABLE or a schema rejection, never as a fact or a success. PERD REQ-ENV-005 (amended).

**D16. A chaos subset runs on every merge that touches Trust, Execution, Outcome, the Evidence Layer or the adapters; the full chaos matrix runs nightly.** The 30-case smoke run (TST-02) is extended with the four crash points and one fault from each proxy family. PERD REQ-TST-009.

**D17. The integration suite exists, not only its specification.** US-01 to US-22 run as one suite with one command; the chaos matrix (SEC-10), the evil provider (SEC-06) and the full suite of at least 320 cases (at least 300 hidden-oracle; BEN-16) are built in the POC and runnable from a clean environment. Plan task BEN-29.

### D. Proof: the Record, receipts and memory

**D18. Record writers are cryptographically authenticated per event.** Each power that writes the Record signs each event with its own Ed25519 key, over the canonical (JCS) event including the previous hash; the database refuses an event whose signature does not verify against the trusted public key for its `written_by` identity; the chain verifier checks every signature. This shares one signing design with DEBT-01's Option B receipt signatures: the Engineering Lead's W1 design covers receipts and Record events together. Limit stated plainly: inside one core process, a compromise of the process itself exposes its keys; authentication defeats a stolen database credential, not a compromised core. PERD REQ-AUD-006.

**D19. External anchoring of the Record is built in the POC.** REC-07 moves from "after the POC" into the POC: chain heads are anchored on a schedule and at every run boundary to a separately controlled write-once store; the core holds a write-only credential (no delete, no overwrite) and the store's retention cannot be shortened by any account. The chain verifier proves that the live chain matches every anchor. SoT §46 OD-06 is amended accordingly. PERD REQ-AUD-007. **FOUNDER ACTION:** the store is a new datastore (AGENT-14). The Security Reviewer evaluates candidates (the leading candidate is an S3-compatible store with object lock in compliance mode, such as MinIO, run in Compose for the POC) and the founders approve one before implementation.

**D20. External wording stays "tamper-evident".** With D18 and D19, the Record is *tamper-evident, writer-authenticated and externally anchored*: undetected rewriting of history becomes infeasible. It is not "tamper-proof": software cannot stop an administrator from deleting or corrupting a database; it can only make every such act detectable and attributable. OD-06's rule that the Record is never described as immutable stands. The word "tamper-proof" is not used internally or externally.

**D21. Record priorities.** REC-03 (reconstruction), REC-04 (completeness) and REC-05 (chain verification) come before D18 and D19 in Core Engineer 1's order.

**D22. Labelled pairs by design; Trust stays model-free forever.** The Record and operational memory are structured so that labelled pairs (request, resolved target, verified outcome) can be extracted later to train Understanding and Entity Resolution, with tenant scope and provenance. Data rights for such use are covered in customer contracts before any partner data is used (GOV-25). No model is ever trained for, or placed in, Trust, Execution or the Outcome verdict (INV-01). PERD REQ-MEM-003.

**D23. Escalation resolutions are recorded in the POC.** When an escalated case is resolved by enterprise staff, Noema reads the resolution as evidence and records it as a structured operational-memory observation linked to the case. Nothing is learned from it automatically in the POC; proposals for pack changes from these records are post-POC (D30). PERD REQ-MEM-004.

### E. Engineering standards and model safety

**D24. Language standards are enforced in CI and verified in code.** Go: `golangci-lint` (pinned) with `errcheck`, `contextcheck` and a `forbidigo` rule banning `panic` outside `main` and tests; the existing import-boundary lint; `go test -race`. Python: `mypy --strict`; Ruff (pinned) including its `ASYNC` rules; Pydantic v2 types generated from `/contracts`. These development dependencies are approved (AGENT-14). Core Engineer 2 verifies that `_post_blocking` in the provider transport never runs on the event loop, and fixes it if it does. PERD REQ-TST-010.

**D25. Model-drift canary.** Every model and speech provider version is pinned; every change of version or provider runs the qualification subset of the benchmark, including pass^k, before it is used, and the result is recorded in a decision record (AGENT-28). PERD REQ-INT-006.

**D26. Operators test the evidence packet.** At least three people who work escalations (from the founders' network until a design partner exists) work escalated cases from the packet alone; the time to understand the case and every lookup they needed are recorded, and each gap becomes a packet change. PERD REQ-EXP-004 (amended).

### F. Positioning, benchmark, roadmap

**D27. Positioning statements, written down once** (SoT §25.5):

1. Noema consumes enterprise identity and access management (IdP, directory, cloud IAM, secrets stores) and never replaces it.
2. Noema's own policy is typed, versioned data evaluated in Noema's deterministic code (ED-09); OPA, Cedar and Zanzibar-style systems are consumed as evidence at decision time.
3. The leading agent platforms treat action safety as an API-permission problem. Noema solves what permissions cannot see: stale and contradictory state, duplicate effects under timeouts, delegated sessions acting at machine speed, writes that report success and did not happen, and proof.
4. τ-bench measures whether an agent can complete the task; Noema's benchmark measures whether it is safe to let it.

**D28. Benchmark and publication strategy.** The public benchmark is legible to the research community: outcomes evaluated against the final state of the systems, pass^k, an open harness and public cases; the held-out set stays private (OD-16). It covers what task benchmarks do not: hostile environments, contradictory state, unknown outcomes, duplicates under timeouts and adversarial evidence. Publication rules: no cherry-picked numbers; the full distribution is shown; every number carries n, method, bound and confidence interval (SoT §38.8, G7); every demo runs from the engine, never scripted; voice is demonstrated live on a real phone only if G5 passes, otherwise the demo runs in text (SoT §37.5). These rules are added to the plan's demo section (§14) and to the discovery and publication documents. PERD REQ-BEN-010.

**D29. Platform roadmap: signed agent proposals with delegation chains (Mode 2).** In Mode 2, each proposal from an external agent is signed by that agent's key and carries the principal and the delegation chain; Noema verifies the signature and the chain before Trust evaluates it. SoT §16 and §41. Built in Phase 4; the POC keeps the Trust interface ready (POC-FR-16).

**D30. Post-POC roadmap** (SoT §41.2): shadow mode with an autonomy setting per capability, segment and time window, and replay of a prospect's historical cases; proposals for pack changes mined from escalation resolutions, approved by a person and benchmarked before release; a case-quality report over the Record; pricing per verified outcome with each billable event linked to its Record entry (as SoT §19.3 already decides); a standing model-qualification pipeline; a pack development lifecycle with Studio over the same data.

**D31. Practices explicitly not adopted** (PERD §70 ED-19), so they are not proposed again:

1. An LLM judge for anything that gates; allowed only as a non-gating diagnostic of explanation tone.
2. A supervisor model as the safety mechanism; allowed only as an extra signal.
3. A classifier as the defence against injection or abuse; the defence is structural (REQ-CTX-007, the schema gate); a classifier may only raise an alert.
4. Speech-to-speech models in a production path (until D8's condition is met).
5. Filler phrases that imply progress or success not yet verified (AGENT-17, REQ-EXP-002).
6. Training our own models in the POC; and never for Trust, Execution or the Outcome verdict (D22).
7. A no-code builder in the POC (Studio is post-POC).

### G. Schedule

**D32. Schedule impact: FOUNDER ACTION.** This record adds material scope (the Context Fabric, compensation, authenticated writers, anchoring, crash-point and corrupted-payload testing, a per-merge chaos subset, pass^k, voice simulation) while G0-N, G0-T, G1 and G2 have not been held. Under the plan's rules (§3.1 gate rules, §19; SoT §40.2) gates never move; dates do. The Repo Steward's status assessment (D3) is due first; within two working days of it, the Engineering Lead proposes re-baselined gate dates and the founders record them in the gate records. Until then, the Fri 13 Nov demo date is not confirmed, and no gate is described as on track without evidence.

## Documents changed by this record

| Document | Change |
|---|---|
| SoT v1.9 → v1.10 | §16 (D29), §25.5 new (D27), §35.1 (D4, D11, D18, D19), §38.8 (D28), §41.2 (D30), §46 OD-06 (D19, D20), Appendix D |
| PERD v1.18 → v1.19 | Changes in v1.19; REQ-CTX-006, REQ-AG-001, REQ-ENV-005, REQ-EXP-004 amended; 19 new requirements (REQ-CTX-009, REQ-CTX-010, REQ-AG-003, REQ-RES-005, REQ-CAP-004, REQ-CAP-005, REQ-RCV-005, REQ-TST-008, REQ-TST-009, REQ-TST-010, REQ-AUD-006, REQ-AUD-007, REQ-MEM-003, REQ-MEM-004, REQ-BEN-009, REQ-BEN-010, REQ-INT-006, REQ-VOI-006, REQ-VOI-007); §48.3 Tier 1; §70 ED-18, ED-19 |
| Plan v1.9 → v1.10 | Governing versions; §3.1 G3 row; week 3 definition of done; PCK-02, TST-02, GOV-12 rows; REC-07 moved into the POC; a new section of 35 tasks to be dated at the re-baseline; §14 publication rules |
| `tasks.csv` | Regenerated from the plan: changed rows above, 35 new rows (status `Unassessed`) |
| `gates/G3.md` | Must-be-true list gains the crash-point matrix, the chaos subset, authenticated writers and anchoring |
| `debt.md` | DEBT-01 names the W1 to W4 tasks and the shared signing design for Record writers |
| `docs/architecture-map.md` | New, derived (D1) |
| `docs/requirements-index.md` | Regenerated from SoT v1.10 |
| Role prompts | Updated for every role agent; a voice engineer prompt added |

## What this record does not do

- It does not mark any gate passed, and it does not set new gate dates (D32).
- It does not approve the Ed25519 database extension (that follows the Security Reviewer's W2 evaluation) or the write-once store (D19); both are new dependencies under AGENT-14.
- It does not add monetary capabilities or change any invariant or binding decision.

## Record fields (decisions README template)

Added by the Repo Steward so that `tools/check_docs_consistency.py` can read the record; it adds no decision and no new content, and each field points to the section above that holds it. The text above is unchanged.

- Status: see "Status" at the top of this record
- Date: 31 October 2026
- Owner: the Founders (see "Deciders" at the top of this record)
- Decision: sections A to G above (D1 to D32)
- Rationale and evidence: "Context" above
- Affected requirement IDs / SoT sections: "Documents changed by this record" above
- Migration notes: "Change control" at the top of this record and "Documents changed by this record" above
- Supersedes: none stated in this record
- Decides: none; D19 and D20 amend the text of a decision that is already closed (see section D)
