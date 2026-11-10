# Decisions

This directory holds **decision records**: dated, owned records of decisions. It is the home for the founder decision log and the engineering decision log that SoT §0.4 ranks in its order of authority.

**A founder decision counts only once it is committed** to the SoT or to this directory, with date, owner, rationale, affected requirement IDs and migration notes. Decisions made in conversation, calls, chat apps or AI sessions are not authoritative until then (SoT §0.4). If an instruction disagrees with the SoT and has not been committed, follow the SoT and raise the conflict (AGENT-27).

**Where the decision log lives (OD-P-02, closed by DEC-2026-10-17).** This directory holds founder decisions and engineering decisions alike. Technology decisions never live in `brain` (DEC-2026-10-16 execution reset E8). A record that changes the SoT lands in the same pull request as the SoT edit and the regenerated register (AGENT-29).

## Records

| Record | Subject |
|---|---|
| [DEC-2026-10-02-sot-v1.2](DEC-2026-10-02-sot-v1.2.md) | SoT v1.2: pre-development fixes |
| [DEC-2026-10-06-architecture-and-contracts](DEC-2026-10-06-architecture-and-contracts.md) | Temporal, repository layout, contract value lists (superseded in part by DEC-2026-10-09; **repository list superseded by DEC-2026-10-13**; **contract enums (item 4) superseded in part by DEC-2026-10-16-money-and-value-lists**) |
| [DEC-2026-10-06-vendor-benchmarks](DEC-2026-10-06-vendor-benchmarks.md) | Benchmark candidates for Understanding and speech (superseded in part by DEC-2026-10-09) |
| [DEC-2026-10-09-deployment-temporal-providers](DEC-2026-10-09-deployment-temporal-providers.md) | Two deployables, Temporal, multi-provider Understanding and speech |
| [DEC-2026-10-11-poc-perd-v1.1](DEC-2026-10-11-poc-perd-v1.1.md) | Adopt the POC PERD as the POC engineering specification; re-pointed to the current PERD by DEC-2026-10-16 (Accepted) |
| [DEC-2026-10-11-poc-4week-plan](DEC-2026-10-11-poc-4week-plan.md) | Adopt the four-week POC execution plan; Phase A in parallel with week 1; re-pointed to the current plan and the E3 schedule by DEC-2026-10-16 (Accepted) |
| [DEC-2026-10-12-tushe-environment-scope](DEC-2026-10-12-tushe-environment-scope.md) | How the POC uses Tushe: `mock-case`, ground truth, time, faults, credentials and the G0 gate; amends SoT §36 (SoT v1.4) (Accepted; Amendments 1 and 2) |
| [DEC-2026-10-13-code-monorepo](DEC-2026-10-13-code-monorepo.md) | One code repository (`noema`) for the POC; what every other repository is for; amends SoT §51 (SoT v1.5) (Accepted; Amendment 1 re-points it to `Noemai-org`) |
| [DEC-2026-10-16-execution-reset](DEC-2026-10-16-execution-reset.md) | Execution reset: `Noemai-org` canonical, two-person team, schedule to 13 Nov, G0-T and G0-N, test-environment components, webhook relay, what leaves `docs`, `brain`'s purpose, the Tushe delta v1.2, the port to `noema`, no direct pushes; amends SoT §35.6, §40.3, §51 (SoT v1.6) (Accepted) |
| [DEC-2026-10-16-contract-and-pack-clarifications](DEC-2026-10-16-contract-and-pack-clarifications.md) | The `evidence_set_hash` construction (C1), the two-node intent model (C2), the status of CON-04, PCK-01 and PCK-02 (C3), noema#1 as a pure port (C4), G7 "External readiness" (C6), the repository mapping closed (C7), team rules, the work-in-progress limit and the cut line (C8); the settlement of the open items (C10); amends DEC-2026-10-16-execution-reset E2 and E12; no SoT change (Accepted by the Founder; the Technical Co-Founder confirms by approving) |
| [DEC-2026-10-16-money-and-value-lists](DEC-2026-10-16-money-and-value-lists.md) | Money as integer minor units (M1 to M10) and the contract value lists (Intent Object `status`, authority results, two-tier reason codes, the drift guard); closes OD-P-19 and OD-P-26; amends SoT §43.1 (SoT v1.7) (Accepted by the Founder; the Technical Co-Founder confirms by approving) |
| [DEC-2026-10-17-open-decisions-closure](DEC-2026-10-17-open-decisions-closure.md) | Closure of every open decision: the canonical OD-01, 02, 03, 06, 08, 10, 12, 13, 14, 15, 16 and the provisional items; the PERD defaults adopted; eleven gates converted to plan tasks; amends SoT §46, §19.3, INV-20, §47.1 and Appendix A (SoT v1.8) (Accepted by the Founder; the Technical Co-Founder confirms by approving) |
| [DEC-2026-10-18-con01-gap-closure](DEC-2026-10-18-con01-gap-closure.md) | Seven decisions found while building the contract schemas: ALLOW needs three PASS layers, the recovery request for a voided grant, the clarification answer, retryable errors, the `recev` and `idk_v1_` forms, and four Record event types added to §32.2 (SoT v1.9, PERD v1.9) (Accepted) |
| [DEC-2026-10-19-docs-infrastructure-code](DEC-2026-10-19-docs-infrastructure-code.md) | Repository-infrastructure code that governs `docs` itself is permitted in `.github/scripts/` and `.github/tests/` only; amends DEC-2026-10-16 E7 (Accepted) |
| [DEC-2026-10-20-architecture-depth](DEC-2026-10-20-architecture-depth.md) | Nine decisions from the architecture review: the §64.2 skeleton depth, the model harness and pipeline, the clarification question by attribute, the composed recipient matcher, signed Record checkpoints and replay, the spend-and-dispatch acceptance, Temporal write activities at most once, decision models as a provider class (PERD v1.11) (Accepted) |
| [DEC-2026-10-20-reconciliation-ruleset-v1](DEC-2026-10-20-reconciliation-ruleset-v1.md) | Where reconciliation rule set v1 differs from PERD §22.3 (R1, R3, single-valued conflicts, certainty tiers) (Accepted) |
| [DEC-2026-10-21-int-002-refusal-failover](DEC-2026-10-21-int-002-refusal-failover.md) | REQ-INT-002: a refused reply (a reply in the wrong format that fails the schema check) triggers failover to the next provider; `PROVIDER_FAILOVER` carries the reason; the output still passes the schema gate and is never repaired (Accepted) |
| [DEC-2026-10-21-compose-topology](DEC-2026-10-21-compose-topology.md) | PERD §65.1: the `tushe_egress` network is confirmed and written in; the benchmark runner reaches the core API over `edge_net` (Accepted) |
| [DEC-2026-10-21-egress-layout-fault-reading](DEC-2026-10-21-egress-layout-fault-reading.md) | `tushe_egress` carries the hostility proxy and the webhook relay; the candidate client lives in `noema_model/evidence/`; IMPOSSIBLE_STATE is produced by the proxy; the REQ-ENV-004 example (Accepted) |
| [DEC-2026-10-22-impossible-state-and-no-window](DEC-2026-10-22-impossible-state-and-no-window.md) | §37.2 names the hostility proxy as the producer of impossible-state fixtures; a candidate request with no time window gives `NO_TRANSACTION_MATCH` (Accepted) |
| [DEC-2026-10-23-vendored-copies-and-scope-code](DEC-2026-10-23-vendored-copies-and-scope-code.md) | REQ-OPS-005: vendored copies are re-pointed in the same change set and the drift check fails when a copy differs; §39.3 names `TENANT_SCOPE_MISMATCH`; a candidate request with no time window is `INPUT_INVALID` (Accepted) |
| [DEC-2026-10-26-session-notes-in-status](DEC-2026-10-26-session-notes-in-status.md) | AGENTS §9: in `noema`, session notes are kept in `status/<task-id>.md` (one file per task) instead of `docs/sessions/` (Accepted) |
| [DEC-2026-10-25-engine-dependencies-and-case-secrets](DEC-2026-10-25-engine-dependencies-and-case-secrets.md) | ENV-03 starts (mock-case slice); the Go Postgres driver and Temporal SDK are approved (AGENT-14); the two `mock-case` secret names; CODEOWNERS for `/.gitleaksignore`; Tushe-dependent work paused (Accepted) |
| [DEC-2026-10-26-control-plane-services](DEC-2026-10-26-control-plane-services.md) | PERD §34.1: `fault-controller` and `fixture-loader` are benchmark-only and never reachable from the core or the model service; their clients live under `benchmark/runner/` and `benchmark/fixtures/`; a read-only `mock-clock` client in core adapters only when a slice needs it (Accepted; Amendment 1, proposed 1 Nov: a test-only control client in core `_test.go` files) |
| [DEC-2026-10-27-record-event-v2](DEC-2026-10-27-record-event-v2.md) | Record event v2 (`record-event.v2.json`, `reconstruction.v2.json`): the PERD §32.1 event with `seq`, `payload_hash`, `actor` and the tenant-scoped genesis hash; nine grant-void reasons; `errors.v2` with the `DUPLICATE_CREATE` code; v1 unchanged; no migration tooling (Accepted) |
| [DEC-2026-10-27-actor-and-payload-hash](DEC-2026-10-27-actor-and-payload-hash.md) | The Record event's emitter (`written_by`, closed set of service identities of PERD §41.1 and §34.1), principal (`actor`, required, six principal kinds) and `payload_hash` (SHA-256 of the RFC 8785 form, integers only); `record-event.v3` and `reconstruction.v3`, v2 unchanged; PERD v1.17; replaces D4 of DEC-2026-10-27-record-event-v2 (Accepted) |
| [DEC-2026-10-28-spent-grant-void](DEC-2026-10-28-spent-grant-void.md) | PERD §38.2: a SPENT `decision_grant` becomes VOID only for a confirmed `REJECTED_STALE_VERSION` refusal; receipt, invalidation, RecoveryRequest and outbox in one transaction; the Record keeps `GRANT_SPENT`; PERD v1.18 (Accepted in principle) |
| [DEC-2026-10-29-receipt-signature-alert](DEC-2026-10-29-receipt-signature-alert.md) | A failed receipt signature alerts a human: the five rules and the exact PERD sections the next PERD version changes; recipient and channel are placeholders (Proposed; keeps DEBT-02 open) |
| [DEC-2026-10-31-proof-depth-and-completeness](DEC-2026-10-31-proof-depth-and-completeness.md) | Context Fabric, compensation, authenticated Record writers, external anchoring, crash-point and corrupted-payload testing, per-merge chaos subset and pass^k pulled into the POC; practices not adopted; SoT v1.10, PERD v1.19, plan v1.10 |
| [DEC-2026-11-03-demo-date-and-no-scope-cut](DEC-2026-11-03-demo-date-and-no-scope-cut.md) | The Founder's orders of 3 Nov: demo Sat 12 Dec 2026 14:00 WAT, fixed; Monday to Saturday are work days; no scope is cut (plan §2's cut line and C8's cut-now rows are not applied); the gate-failure protocol; the gate calendar (targets and latest dates); supersedes the dates of plan v1.10 and the gate records (Proposed until merged) |
| [DEC-2026-11-03-action-graph-shape](DEC-2026-11-03-action-graph-shape.md) | Action Graph shape (REQ-AG-001): roots are required; every non-root node needs an incoming edge; a root has none; a graph of more than one node must be weakly connected (a flat list fails); the exact PERD v1.20 text (settles the graph shape only, nothing about PCK-02; Proposed until merged) |
| [DEC-2026-11-01-receipt-and-record-signing](DEC-2026-11-01-receipt-and-record-signing.md) | W1 (GOV-28): one Ed25519 signing design for execution receipts, Record events and Outcome verdicts; one key per writing identity; database verification by pgsodium behind a migration-owned trigger; the `noema_migrator` role; Option C as the fallback; the exact PERD v1.20 text (Proposed; opens OD-P-72 and OD-P-73) |
| [DEC-2026-11-03-rapid-test-dependency](DEC-2026-11-03-rapid-test-dependency.md) | `pgregory.net/rapid` v1.3.0 is approved as a test-only dependency of the core (MPL-2.0, no dependencies); first used for REC-01 and TST-01 |
| [DEC-2026-11-04-architect-rulings](DEC-2026-11-04-architect-rulings.md) | The Architect's rulings of 4 Nov 2026 (R1 to R14): lone CONFIRM, log_complaint_reference PERMIT, PCK-02 split and template format, PCK-04 descriptor key, DEBT-03 accepted, OpenTelemetry Go dependency, init.sh roles, DEBT-06, record_insert_t, G1 story test locations, SEC-14 put-only credential, Tushe GitHub Environments, ENV-05 pause lifted, TEN-02 partial (Proposed) |
| [DEC-2026-11-04-g1-named-open-exclusion](DEC-2026-11-04-g1-named-open-exclusion.md) | BEN-05: G1's text needs one US-01 and one US-06 case; a case no producer can yet drive may be a named open exclusion, reported as non-full coverage and never as a pass; every other errored or missing case is NOT_COMPARABLE (Proposed) |
| [DEC-2026-11-05-architect-rulings](DEC-2026-11-05-architect-rulings.md) | The Architect's rulings of 5 Nov 2026: policy-version rule for grants, OD-P-74 adopted as canonical, migration numbering, production anchor retention (365 days, Compliance mode), RELAY_PULL_TOKEN scope, PCK-04 postcondition sources, the identity contract, alert channels (Proposed) |
| [DEC-2026-11-06-architect-rulings](DEC-2026-11-06-architect-rulings.md) | The Architect's rulings of 6 Nov 2026 (A2 to A25): pgsodium approved on a condition, pack values for breaker and dispatch budget, emitter secrets, signed Decision Record, row-security ownership, EXP-01 templates in the pack, Caddy relay, contracts tag deferred, Decision Record v2 signing form, review rule, qualification records, clock skew, docs merge order, bounded rollback, CI check runs as test evidence (Proposed) |
| [DEC-2026-11-07-architect-rulings](DEC-2026-11-07-architect-rulings.md) | The Architect's rulings of 7 Nov 2026 (A27 to A40): the SoT/PERD edit, docs#112 closed for docs#123, fix matrices and no Codex trigger, TST-05 option B, REVERSAL_PENDING, suite scope, migration ledger, DEBT numbering, owners, reconstruction wording (Proposed) |
| [DEC-2026-11-07-benchmark-suite-definition-v1](DEC-2026-11-07-benchmark-suite-definition-v1.md) | Ruling A26: benchmark suite definition v1 (arms C, A, B, D, M0; RESOLVE R1 to R12, RESIST S1 to S11 and X1 to X10, IMPACT; measures and pre-registered rules) (Proposed) |
| [DEC-2026-11-08-rulings-a41-onward](DEC-2026-11-08-rulings-a41-onward.md) | Founder decisions and Architect rulings A41 to A98 (gate 1 wording, pass^k floor, credential classes, signature domain separation, and the rulings sent to the agents) |
| [DEC-2026-11-07-founder-decisions-block-d](DEC-2026-11-07-founder-decisions-block-d.md) | Founder decisions D1 to D14 (Block D): plan v1.12 and the gate count, quota meaning, kill switch, Record keys, migration numbers, R7 |
| [DEC-2026-11-07-sot-perd-edit](DEC-2026-11-07-sot-perd-edit.md) | Ruling A27: SoT v1.11 and PERD v1.21 (two more safety gates, key policy, arm labels, identity contract, benchmark quota, case contract v2); draft for the Founders to issue |
| [DEC-2026-11-07-founder-decisions-block-e](DEC-2026-11-07-founder-decisions-block-e.md) | Founder decisions E1 to E7 (Block E): push rule, reviewer table, audit correction, open-decision rulings, quota bound, housekeeping, unowned PRs |
| [DEC-2026-11-08-perd-39-4-control-plane-callers](DEC-2026-11-08-perd-39-4-control-plane-callers.md) | Ruling A110 (Founders, option A): the reconstruction and record-verify routes stay audit-only; no PERD v1.22; the SEC-04 matrix is unchanged |
| [DEC-2026-11-06-model-qualification-floor](DEC-2026-11-06-model-qualification-floor.md) | UND-13 / A17: the pass^k floor for a first model or speech-provider qualification (DRAFT; the number is the Founder's to set) |
| [DEC-2026-11-08-rec-09-record-export](DEC-2026-11-08-rec-09-record-export.md) | Ruling A109: the Founders approve new task REC-09, the Noema record export (a library function, not a route), on four conditions |
| [DEC-2026-11-09-one-founder-approval](DEC-2026-11-09-one-founder-approval.md) | Ruling A111 (Founder): one approval from the Founder who did not drive the pull request merges any pull request in `docs` or `noema`; supersedes the "both Founders" wording |
| [DEC-2026-11-09-sec-15-per-login-secrets](DEC-2026-11-09-sec-15-per-login-secrets.md) | Ruling A112 (Principal Architect, noema#385): DEBT-13 does not block noema#181; new task SEC-15 (per-login secrets for tenant and power logins, owner C1, reviewer SR) |
| [DEC-2026-11-10-architect-sync-3-a127-a128](DEC-2026-11-10-architect-sync-3-a127-a128.md) | Rulings A127 and A128 (afternoon Architect sync): noema#168's text fix goes in a follow-up with its head unchanged; merge only after the reviewer-role READY at the current head, on the owner's READY TO MERGE line |

## Where decisions already live

| Kind | Where it is defined | Changed by |
|---|---|---|
| Binding decisions BD-01 to BD-16 ([CONVICTION] or [DECISION]) | [SoT](../NOEMA_SOURCE_OF_TRUTH.md) §0.5 | A new SoT version only |
| [DECISION] and [CONVICTION] items in the SoT body | SoT, at the tagged statement | [DECISION]: the open-decisions process (§46). [CONVICTION]: new evidence plus a version change (§0.2). |
| Open decisions OD-01 to OD-16 | SoT §46. Status in [`../open-decisions.md`](../open-decisions.md). | A decision record here, then a SoT revision if it changes a [DECISION] or [CONVICTION] |
| Provisional migration items OD-P-xx (NON-CANONICAL) | [`../open-decisions.md`](../open-decisions.md) | Adoption into a SoT revision, or closure by a decision record |
| Legacy ADR-001 to ADR-019 | [`../archive/legacy-canon-2026-09/decisions/`](../archive/legacy-canon-2026-09/decisions/) | **Superseded; non-authoritative.** Mapped to SoT sections in [`../archive/README.md`](../archive/README.md#legacy-adr-supersession-map). |

## When to write a decision record

Write one when any of these happens:

- a founder decision is made (§0.4 item 1);
- an open decision (OD-xx or OD-P-xx) is decided;
- a significant engineering choice is made that the SoT does not already settle. This includes any new dependency, service, datastore or framework, which first needs an [OPEN] entry and approval (AGENT-14).

**Do not write a record that restates the SoT.** If the SoT already decides something, cite the section instead. Do not rewrite a record after it is committed; supersede it with a new one.

For anything larger than a small change, answer the questions in SoT §52 in the record, including **does it increase or decrease the unsafe autonomy surface?**

## Template

Name files `DEC-YYYY-MM-DD-<slug>.md`.

```markdown
# DEC-YYYY-MM-DD-<slug>

- Status:
- Date:
- Closes: <OD IDs this record decides or closes, or none>
- Owner:
- Decision:
- Rationale and evidence:
- Affected requirement IDs / SoT sections:
- Migration notes:
- Supersedes:
```
