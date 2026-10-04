# Requirement index

> **Derived, non-normative.** This index exists for traceability (AGENT-01). Every requirement is *defined* only in [`NOEMA_SOURCE_OF_TRUTH.md`](NOEMA_SOURCE_OF_TRUTH.md) (the SoT). The "Summary" column is a verbatim prefix of the SoT text, cut at a word boundary and marked "…" where truncated. Read the SoT section before acting on any ID. If this file and the SoT disagree, the SoT wins and this file is wrong.

Generated from SoT v1.2 (2 October 2026). IDs are stable and must not be renamed (SoT §0.3, Appendix B). This file adds no requirements.

## How to read this index

| Column | Meaning |
|---|---|
| SoT § | Section where the ID is defined. |
| Scope | **POC** = built now (Part VII). **PLATFORM** = target the POC must not block; not built unless a POC ID asks for it (AGENT-03). **ALL** = binds every phase, including the POC. |
| Realised in POC by | POC IDs whose "Maps to" column in SoT §37.1 names this platform ID. Empty means the POC does not implement it. |
| Verification | How the SoT says the ID is proven. "Not specified" means the SoT names no mechanism; AGENT-11 still requires a failing test first. |
| Implementation status | This repository is documentation-first and contains no implementation ([OD-P-01](open-decisions.md#od-p-01)). Every ID is therefore **not implemented here**. Update this column only with evidence (a merged test or benchmark run). |

Prefixes: Appendix B of the SoT. The prefixes `SEC-` and `PERF-` are named in SoT §0.3 but no IDs with them are defined anywhere in the SoT; see [OD-P-07](open-decisions.md#od-p-07).

## Binding decisions (BD)

SoT §0.5. Settled [CONVICTION] or [DECISION] items; changed only by a new SoT version.

| ID | SoT § | Summary | Defined at | Scope |
|---|---|---|---|---|
| BD-01 | §0.5 | Noema is a global, cross-industry product. It is not Nigeria-only and not fintech-only. | §0.1, §22 | ALL |
| BD-02 | §0.5 | Enterprises integrate Noema into their customer-facing products and platforms so *their* customers get outcomes. It is … | §0.1, §11 | ALL |
| BD-03 | §0.5 | The first proving ground is voice-fronted transaction-exception resolution inside Nigerian fintech, chosen for … | §31–32 | ALL |
| BD-04 | §0.5 | The POC is not the product definition. POC numbers never define the company's market, architecture or ceiling. | §30 | ALL |
| BD-05 | §0.5 | Understanding, Trust, Execution and Outcome are separate systems with separate authority. | §13 | ALL |
| BD-06 | §0.5 | Intent, Trust and Outcome Taxonomies are abstract schemas from day one; only fintech nodes are populated first. | §15 | ALL |
| BD-07 | §0.5 | The POC runs on a synthetic enterprise environment with deterministic fault injection. | §36 | ALL |
| BD-08 | §0.5 | In the POC, monetary state is read-only. Only constrained, non-monetary case-management writes exist. Prohibited … | §34 | ALL |
| BD-09 | §0.5 | Zero unsafe consequential actions is a release gate, not a target. | §38 | ALL |
| BD-10 | §0.5 | Unknown state and unknown execution outcomes are first-class, explicit results. | §13, §43 | ALL |
| BD-11 | §0.5 | Model output is untrusted input. Models get no credentials, no arbitrary HTTP or SQL, and no direct adapter access. | §44–47 | ALL |
| BD-12 | §0.5 | Verification, recovery and the causal Record are core, not add-ons. | §13–14 | ALL |
| BD-13 | §0.5 | Mode 1 is built first. Mode 2 shapes the architecture now and ships only when earned. | §16, §41 | ALL |
| BD-14 | §0.5 | Correctness is benchmarked text-first; the voice front door is built in parallel on the same core. | §32, §40 | ALL |
| BD-15 | §0.5 | Engineering is global-grade from day one; certifications are claimed only once completed. | §47, §50 | ALL |

## Platform functional requirements (PLAT-FR)

SoT §21.1. The full Noema the POC must not block.

| ID | SoT § | Summary | Scope | Realised in POC by |
|---|---|---|---|---|
| PLAT-FR-01 | §21.1 | Accept intent from any channel through the Input Gateway and produce one canonical input contract. | PLATFORM | POC-FR-01 |
| PLAT-FR-02 | §21.1 | Compile intent into a schema-valid Intent Object using the active Intent Taxonomy; flag every material ambiguity. | PLATFORM | POC-FR-02, POC-FR-03, POC-FR-13 |
| PLAT-FR-03 | §21.1 | Resolve references to ranked candidate targets using evidence; never auto-resolve below the pack's safety margin. | PLATFORM | POC-FR-04 |
| PLAT-FR-04 | §21.1 | Reconstruct state per decision with a FactStatus, source and freshness on every fact. | PLATFORM | POC-FR-05 |
| PLAT-FR-05 | §21.1 | Return exactly one Trust outcome (ALLOW, CLARIFY, CONFIRM, WAIT, ESCALATE, REJECT, UNKNOWN) with reasons, evidence and … | PLATFORM | POC-FR-06, POC-FR-14 |
| PLAT-FR-06 | §21.1 | Evaluate technical, policy and business authorisation, bound to the resolved target. | PLATFORM | POC-FR-07 |
| PLAT-FR-07 | §21.1 | Issue single-use, scoped, expiring Decision Grants only on ALLOW. | PLATFORM | POC-FR-08 |
| PLAT-FR-08 | §21.1 | Execute only registered capabilities, idempotently, with revalidation immediately before acting. | PLATFORM | POC-FR-08 |
| PLAT-FR-09 | §21.1 | Verify outcomes independently against the Outcome Taxonomy; return a verdict. | PLATFORM | POC-FR-09 |
| PLAT-FR-10 | §21.1 | Route every non-ACHIEVED verdict back to Trust for recovery; never retry blindly. | PLATFORM | POC-FR-10 |
| PLAT-FR-11 | §21.1 | Explain outcomes to the person using only verified facts. | PLATFORM | POC-FR-11 |
| PLAT-FR-12 | §21.1 | Record a hash-chained causal record for every consequential action; expose a reconstruction API. | PLATFORM | POC-FR-12 |
| PLAT-FR-13 | §21.1 | Load, version and validate Vertical Packs; run conformance tests for every pack in CI. | PLATFORM | POC-FR-15 |
| PLAT-FR-14 | §21.1 | Support Mode 2: accept proposed actions from external agents as untrusted input with the principal and delegation chain. | PLATFORM | POC-FR-16 |
| PLAT-FR-15 | §21.1 | Support human approval steps (including maker-checker) as first-class Trust outcomes through the confirmation contract … | PLATFORM | — |
| PLAT-FR-16 | §21.1 | Provide multi-tenant isolation of data, policy, packs, keys and records. | PLATFORM | — |
| PLAT-FR-17 | §21.1 | Provide enterprise configuration (Studio) for packs, policies and capabilities, with versioning and approvals. | PLATFORM | — |

## Platform non-functional requirements (PLAT-NFR)

SoT §21.2. Items tagged [TARGET] in the SoT are commitments, not measured results.

| ID | SoT § | Summary | Scope |
|---|---|---|---|
| PLAT-NFR-01 | §21.2 | Determinism: identical intent, evidence, policy and pack versions always produce the identical Trust decision. | PLATFORM |
| PLAT-NFR-02 | §21.2 | Safety over autonomy: when in doubt, clarify, wait or escalate. | PLATFORM |
| PLAT-NFR-03 | §21.2 | Fail closed: any dependency failure that prevents a safe decision yields ESCALATE or UNKNOWN, never ALLOW. | PLATFORM |
| PLAT-NFR-04 | §21.2 | Reconstructability: every consequential decision can be reconstructed from the Record alone. | PLATFORM |
| PLAT-NFR-05 | §21.2 | Idempotency under duplicate submission, retries, restarts, duplicate events and network loss. | PLATFORM |
| PLAT-NFR-06 | §21.2 | Systems of record stay authoritative; Noema holds a reconstructed view, never a competing truth. | PLATFORM |
| PLAT-NFR-07 | §21.2 | No modality-specific business logic below the Input Gateway. | PLATFORM |
| PLAT-NFR-08 | §21.2 | No vertical-specific or country-specific logic in core; all of it in packs and adapters. | PLATFORM |
| PLAT-NFR-09 | §21.2 | Model independence: provider change is configuration plus benchmark, not code. | PLATFORM |
| PLAT-NFR-10 | §21.2 | Data minimisation: Noema reads only what a decision needs, under the requester's scope. | PLATFORM |
| PLAT-NFR-11 | §21.2 | Data residency: deployable per region (EU, US, Nigeria at minimum) with region-pinned data and keys. | PLATFORM |
| PLAT-NFR-12 | §21.2 | Availability [TARGET, from Phase 3]: Decision API 99.95% monthly; Record writes durable before any grant is issued. | PLATFORM |
| PLAT-NFR-13 | §21.2 | Performance [TARGET]: Trust decision P95 under 50 ms excluding evidence reads; see §48. | PLATFORM |
| PLAT-NFR-14 | §21.2 | Security and compliance: pass enterprise security reviews (SOC 2 Type II, ISO/IEC 27001, ISO/IEC 42001 on the roadmap … | PLATFORM |
| PLAT-NFR-15 | §21.2 | Observability: one correlation chain across all four powers and the Record. | PLATFORM |
| PLAT-NFR-16 | §21.2 | Durability: execution state survives process failure; long-running work resumes without duplicating effects. | PLATFORM |
| PLAT-NFR-17 | §21.2 | Compatibility: every public API, event and pack schema is versioned; breaking changes follow a deprecation window. | PLATFORM |
| PLAT-NFR-18 | §21.2 | Scalability: horizontal scaling for concurrent executions, with explicit concurrency control (version-aware writes) on … | PLATFORM |
| PLAT-NFR-19 | §21.2 | Recovery semantics: every capability declares retry, compensate, escalate and unknown behaviour; there is no undeclared … | PLATFORM |
| PLAT-NFR-20 | §21.2 | Continuous security testing: application, infrastructure and adversarial (prompt-injection and tool-misuse) tests run … | PLATFORM |
| PLAT-NFR-21 | §21.2 | Reproducibility: any decision or benchmark run can be replayed against the same evidence, policy, pack and seed. | PLATFORM |

## Platform user stories (PLAT-US)

SoT §21.3.

| ID | SoT § | As a… | I can… (summary) | Scope |
|---|---|---|---|---|
| PLAT-US-01 | §21.3 | customer of an enterprise | express a goal naturally without knowing which internal systems are involved. | PLATFORM |
| PLAT-US-02 | §21.3 | customer | receive a verified outcome rather than an optimistic AI message. | PLATFORM |
| PLAT-US-03 | §21.3 | enterprise product team | expose consequential actions without giving any model unrestricted access. | PLATFORM |
| PLAT-US-04 | §21.3 | security team | define who may perform which action against which resource, under which conditions. | PLATFORM |
| PLAT-US-05 | §21.3 | operations lead | see why Noema acted, asked, waited, escalated or refused. | PLATFORM |
| PLAT-US-06 | §21.3 | compliance officer | reconstruct request → decision → execution → outcome for any case. | PLATFORM |
| PLAT-US-07 | §21.3 | engineer | replay a failed execution against the same recorded state. | PLATFORM |
| PLAT-US-08 | §21.3 | product team | add a new interface without rewriting the execution substrate. | PLATFORM |
| PLAT-US-09 | §21.3 | platform team | swap models without changing business execution semantics. | PLATFORM |
| PLAT-US-10 | §21.3 | enterprise | add a new domain taxonomy without rewriting the core. | PLATFORM |
| PLAT-US-11 | §21.3 | agent developer | call Noema as the trust boundary before any consequential tool (Mode 2). | PLATFORM |

## POC functional requirements (POC-FR)

SoT §37.1. What is built now.

| ID | SoT § | Summary | Maps to (SoT) | Scope |
|---|---|---|---|---|
| POC-FR-01 | §37.1 | Accept requests by voice and text; normalise both to the canonical input contract before any business logic. | PLAT-FR-01 | POC |
| POC-FR-02 | §37.1 | Interpret code-switched English, Pidgin, Yoruba, Hausa and Igbo, including slang, truncated names and colloquial money … | PLAT-FR-02 | POC |
| POC-FR-03 | §37.1 | Emit only schema-valid Intent Objects; never emit free-form instructions to any capability. | PLAT-FR-02, INV-02 | POC |
| POC-FR-04 | §37.1 | Resolve the specific transaction from vague references with ranked candidates; auto-resolve only above the pack margin … | PLAT-FR-03 | POC |
| POC-FR-05 | §37.1 | Reconstruct transaction state from ledger, switch, settlement, beneficiary and case sources with FactStatus on every … | PLAT-FR-04 | POC |
| POC-FR-06 | §37.1 | Return exactly one of the seven Trust outcomes with reason code, evidence set, policy version and pack version. | PLAT-FR-05 | POC |
| POC-FR-07 | §37.1 | Evaluate technical, policy and business authorisation bound to the resolved transaction; refuse before resolution can … | PLAT-FR-06 | POC |
| POC-FR-08 | §37.1 | Execute only registered, non-monetary capabilities; spend a Decision Grant exactly once; revalidate immediately before … | PLAT-FR-07, PLAT-FR-08 | POC |
| POC-FR-09 | §37.1 | Verify every write independently through the Outcome Verifier; never infer success from an HTTP status. | PLAT-FR-09 | POC |
| POC-FR-10 | §37.1 | On timeout or silence, record OUTCOME_UNKNOWN and verify before any retry; any retry needs a new grant. | PLAT-FR-10 | POC |
| POC-FR-11 | §37.1 | Explain outcomes in the user's language register, stating unknowns as unknown. | PLAT-FR-11 | POC |
| POC-FR-12 | §37.1 | Produce a complete, hash-chained causal record per case and a reconstruction endpoint. | PLAT-FR-12 | POC |
| POC-FR-13 | §37.1 | Bind clarification answers to the open Intent Object as a new version; support abandon-and-resume and cross-channel … | PLAT-FR-02 | POC |
| POC-FR-14 | §37.1 | Advise against resending money whenever a prior transfer's outcome is pending, unknown or contradictory. | PLAT-FR-05 | POC |
| POC-FR-15 | §37.1 | Load the fintech pack and the three conformance packs; run the core contract tests against all four in CI. | PLAT-FR-13 | POC |
| POC-FR-16 | §37.1 | Keep the Trust interface able to accept an externally proposed action (Mode 2) without code changes in Trust, Execution … | PLAT-FR-14 | POC |
| POC-FR-17 | §37.1 | Provide an evidence panel showing the Intent Object, candidates, evidence, reconstructed state, decision, plan, … | Demo evidence | POC |

## POC non-functional requirements (POC-NFR)

SoT §37.2.

| ID | SoT § | Summary | Scope | Verification |
|---|---|---|---|---|
| POC-NFR-01 | §37.2 | Determinism: identical inputs, evidence and versions produce the identical Trust decision (property-tested). | POC | Property test (stated in SoT) |
| POC-NFR-02 | §37.2 | Zero unsafe consequential actions across the full benchmark; this gate outranks every autonomy and latency target. | POC | Not specified |
| POC-NFR-03 | §37.2 | Fail closed on any dependency failure (ESCALATE or UNKNOWN). | POC | Not specified |
| POC-NFR-04 | §37.2 | Idempotent under duplicate submission, retries, process restart, duplicate webhooks and network loss. | POC | Not specified |
| POC-NFR-05 | §37.2 | Every adapter behind an interface so the synthetic environment can be replaced by a real enterprise without touching … | POC | Not specified |
| POC-NFR-06 | §37.2 | Masking: account numbers shown only as the last four digits on every surface; secrets never in logs or model context. | POC | Not specified |
| POC-NFR-07 | §37.2 | Raw audio discarded after transcription unless the case is disputed and consent is recorded. | POC | Not specified |
| POC-NFR-08 | §37.2 | Every fault reproducible from configuration; every benchmark case repeatable. | POC | Not specified |
| POC-NFR-09 | §37.2 | Latency budgets in §48 hold for clean cases; complex cases may take longer to stay safe. | POC | Not specified |
| POC-NFR-10 | §37.2 | No vertical or country terms in `/core` (lint-enforced). | POC | Lint (stated in SoT) |

## POC user stories (US)

SoT §37.3. Each is an automated, release-gating benchmark case (SoT §37.3 heading). Full Given/When/Then text is in the SoT only.

| ID | SoT § | Title | Scope | Verification |
|---|---|---|---|---|
| US-01 | §37.3 | Unique transaction | POC | Release-gating benchmark case |
| US-02 | §37.3 | Two Tundes | POC | Release-gating benchmark case |
| US-03 | §37.3 | Systems disagree | POC | Release-gating benchmark case |
| US-04 | §37.3 | "Should I send it again?" | POC | Release-gating benchmark case |
| US-05 | §37.3 | One case, even if asked twice | POC | Release-gating benchmark case |
| US-06 | §37.3 | Silent success | POC | Release-gating benchmark case |
| US-07 | §37.3 | Confused deputy | POC | Release-gating benchmark case |
| US-08 | §37.3 | Policy changes mid-case | POC | Release-gating benchmark case |
| US-09 | §37.3 | Prompt injection in data | POC | Release-gating benchmark case |
| US-10 | §37.3 | Prohibited request | POC | Release-gating benchmark case |
| US-11 | §37.3 | Abandon and resume | POC | Release-gating benchmark case |
| US-12 | §37.3 | Why did this happen? | POC | Release-gating benchmark case |
| US-13 | §37.3 | Reversal lands mid-investigation | POC | Release-gating benchmark case |
| US-14 | §37.3 | Money appears in two places | POC | Release-gating benchmark case |
| US-15 | §37.3 | Stale evidence | POC | Release-gating benchmark case |
| US-16 | §37.3 | Success that is not | POC | Release-gating benchmark case |
| US-17 | §37.3 | Settlement arrives later | POC | Release-gating benchmark case |
| US-18 | §37.3 | Confirmation that goes stale | POC | Release-gating benchmark case |
| US-19 | §37.3 | Someone else changed the case | POC | Release-gating benchmark case |
| US-20 | §37.3 | Policy changes after the grant | POC | Release-gating benchmark case |
| US-21 | §37.3 | The system says "slow down" | POC | Release-gating benchmark case |
| US-22 | §37.3 | Close it for me | POC | Release-gating benchmark case |

## Invariants (INV)

SoT §45. Each is enforced in code and asserted as a property test on every merge. "Primarily exercised by" is derived from SoT §13–14 and §51 for navigation only; the invariant text governs.

| ID | SoT § | Summary | Primarily exercised by (derived) | Scope | Verification |
|---|---|---|---|---|---|
| INV-01 | §45 | No code path in Trust, Execution or the Outcome verdict calls a language model. | Trust, Execution, Outcome | ALL | Property test on every merge |
| INV-02 | §45 | No free-form model output reaches an execution path; only schema-valid objects cross the schema gate. | Understanding → schema gate | ALL | Property test on every merge |
| INV-03 | §45 | Execution acts only with a valid, unexpired, unused, correctly signed Decision Grant whose target and parameter hash … | Execution | ALL | Property test on every merge |
| INV-04 | §45 | Only Outcome can mark an outcome ACHIEVED, using evidence it read itself after the definition's settle window. | Outcome | ALL | Property test on every merge |
| INV-05 | §45 | No capability outside the registry is callable; PROHIBITED capabilities always reject. | Execution (Capability Registry) | ALL | Property test on every merge |
| INV-06 | §45 | An unresolved material ambiguity makes any Trust outcome other than CLARIFY or ESCALATE unrepresentable. | Trust | ALL | Property test on every merge |
| INV-07 | §45 | A timeout or silence yields OUTCOME_UNKNOWN, never SUCCEEDED or FAILED. | Execution | ALL | Property test on every merge |
| INV-08 | §45 | Every write carries an idempotency key created and stored before the call. | Execution | ALL | Property test on every merge |
| INV-09 | §45 | Every decision records the policy and pack versions that governed it. Each policy rule is evaluated under the version … | Trust | ALL | Property test on every merge |
| INV-10 | §45 | Every consequential decision is reconstructable from the Record alone. | Record | ALL | Property test on every merge |
| INV-11 | §45 | The Record is append-only and hash-chained; any break in the chain raises a security alert. | Record | ALL | Property test on every merge |
| INV-12 | §45 | Identity is never derived from model output or user text. | Understanding, Trust | ALL | Property test on every merge |
| INV-13 | §45 | No user-facing statement presents a non-KNOWN fact as certain. | Explanation (separate component) | ALL | Property test on every merge |
| INV-14 | §45 | `/core` contains no vertical or country terms; all four packs pass contract tests. | Core / packs (CI lint, conformance) | ALL | Property test on every merge |
| INV-15 | §45 | Every non-ACHIEVED verdict returns to Trust; Execution never re-runs on its own. | Outcome → Trust | ALL | Property test on every merge |
| INV-16 | §45 | Any dependency failure that prevents a safe decision results in ESCALATE or UNKNOWN, never ALLOW. | Trust | ALL | Property test on every merge |
| INV-17 | §45 | Execution revalidates, immediately before every write: grant signature, scope, expiry and single use; decision and … | Execution | ALL | Property test on every merge |
| INV-18 | §45 | The Planner can emit only registered capability IDs; a plan containing an unregistered or prohibited ID cannot be … | Execution (Planner) | ALL | Property test on every merge |
| INV-19 | §45 | Absence of evidence is never recorded as a negative fact; a missing record yields UNAVAILABLE or UNKNOWN. | Trust (State Reconciliation), Evidence Layer | ALL | Property test on every merge |
| INV-20 | §45 | A CONTRADICTORY_STATE classification freezes all consequential writes on that target until Trust records a resolution … | Trust, Execution | ALL | Property test on every merge |
| INV-21 | §45 | Replay determinism: the same scenario, seed, evidence, policy and pack versions produce the same Trust decisions and … | All powers (benchmark replay) | ALL | Property test on every merge |
| INV-22 | §45 | No runtime credential can read the benchmark oracle; `/core/explanation` cannot write to any store except its own … | Benchmark; Explanation (`/core/explanation`) | ALL | Property test on every merge |
| INV-23 | §45 | Trust and Execution apply the stricter of the source's freshness limit and the trust profile's limit (including any … | Trust, Execution | ALL | Property test on every merge |
| INV-24 | §45 | A capability whose retry_safety is NONE is never retried automatically. Any uncertain result for it is recorded as … | Execution | ALL | Property test on every merge |
| INV-25 | §45 | A Decision Grant can be issued only by an ALLOW evaluation. For a CONFIRM decision, that requires a valid, unexpired … | Trust | ALL | Property test on every merge |
| INV-26 | §45 | Publishing a new policy version voids every outstanding, unspent Decision Grant governed by an earlier version of that … | Trust, Execution | ALL | Property test on every merge |
| INV-27 | §45 | When a capability declares CONDITIONAL_WRITE, every write passes the grant's target version tokens to the target; a … | Execution | ALL | Property test on every merge |
| INV-28 | §45 | No PENDING_EXTERNAL verdict exists without a durable watch and a deadline. At the deadline the verdict becomes UNKNOWN … | Outcome (Outcome Watch) → Trust | ALL | Property test on every merge |

## Rules for coding agents (AGENT)

SoT §44. Apply to every AI coding agent and every human working with one. See also [`AGENTS.md`](../AGENTS.md).

| ID | SoT § | Summary | Scope |
|---|---|---|---|
| AGENT-01 | §44 | Every change references at least one requirement ID from this document in the PR description. No ID, no merge. | ALL |
| AGENT-02 | §44 | If a task needs something this document does not specify, do not invent it, even if it looks useful. Instead: (1) … | ALL |
| AGENT-03 | §44 | Build the POC (Part VII). Do not implement full-platform features unless a POC requirement explicitly asks for them. … | ALL |
| AGENT-04 | §44 | Never put industry-specific or country-specific terms, rules or constants in `/core`. They go in `/packs` or … | ALL |
| AGENT-05 | §44 | Never call a language model from /core/trust, /core/execution or /core/outcome. Models are allowed only in … | ALL |
| AGENT-06 | §44 | Never add a capability to the registry without risk class, consequence profile, retry safety, concurrency control, … | ALL |
| AGENT-07 | §44 | Never treat a timeout, a 5xx or silence as success or failure. It is `OUTCOME_UNKNOWN` until Outcome says otherwise. | ALL |
| AGENT-08 | §44 | Never retry a write without a new Decision Grant. | ALL |
| AGENT-09 | §44 | Never let text from users, models, enterprise fields or tool outputs become a capability name, a parameter outside the … | ALL |
| AGENT-10 | §44 | Never take identity from model output or user text; take it from the authenticated session only. | ALL |
| AGENT-11 | §44 | Write the failing test first for any invariant or benchmark case you implement. Do not delete or weaken a test to make … | ALL |
| AGENT-12 | §44 | Never mock away a failure mode in tests. Use the synthetic environment's fault injection. | ALL |
| AGENT-13 | §44 | Never log secrets, full account numbers, raw audio or full personal identifiers. Mask to the last four digits. | ALL |
| AGENT-14 | §44 | Do not add a new dependency, service, datastore or framework without an [OPEN] entry and approval. | ALL |
| AGENT-15 | §44 | Do not change a contract in `/contracts` without a version bump, a migration note and updated generated models. | ALL |
| AGENT-16 | §44 | Do not loosen any threshold (ambiguity margins, freshness limits, retry budgets) without a full benchmark run showing … | ALL |
| AGENT-17 | §44 | Do not write user-facing text that states a fact as certain unless its FactStatus is KNOWN. | ALL |
| AGENT-18 | §44 | Do not quote external numbers in code comments, docs or UI unless they appear in this document with a source. | ALL |
| AGENT-19 | §44 | Keep functions small and boundaries explicit. No module reaches into another module's internals; communicate through … | ALL |
| AGENT-20 | §44 | When unsure between two readings of this document, implement the safer one, note the ambiguity in the PR, and ask. | ALL |
| AGENT-21 | §44 | Never treat a tool response, an HTTP 200, a completed workflow or a model's statement as proof of a business outcome. … | ALL |
| AGENT-22 | §44 | Never write code that lets any component authorise itself: Understanding cannot allow, the Planner cannot create … | ALL |
| AGENT-23 | §44 | Every bug, incident or benchmark failure becomes a named, permanent regression case before the fix merges. | ALL |
| AGENT-24 | §44 | Every new integration or adapter ships with contract tests against its documented and its observed behaviour, including … | ALL |
| AGENT-25 | §44 | Label synthetic fixtures as synthetic (for example switch response codes); never present them as real NIBSS or other … | ALL |
| AGENT-26 | §44 | When two sources of instruction conflict, follow the order of authority in §0.4 and record the conflict in the PR. | ALL |
| AGENT-27 | §44 | Never change, weaken or work around an invariant, binding decision or [CONVICTION] item to make an implementation fit. … | ALL |

## Open decisions (OD)

SoT §46. Sixteen canonical open decisions, OD-01 to OD-16, each with a recommended default that applies until decided (OD-09 is closed in v1.2). Their status is tracked in [`open-decisions.md`](open-decisions.md). They are not requirements.

## Other ID families

| IDs | SoT § | Meaning | Notes |
|---|---|---|---|
| B1–B8 | §20.2 | Benchmark families (Understanding, State, Trust, Execution, Outcome, Security, Record, Business) | The POC edition is "Noema Trusted Execution Benchmark v0.1 (Transaction Exceptions)" (§38). |
| S0–S3 | §38.3 | Severity classes for benchmark and incident findings | Release gates: zero S0 anywhere, zero S1 in the release suite (§38.3). |
| AT-01 to AT-20 | §36, §40.1, §41 | Synthetic-environment acceptance tests from the Tushe specification | Only the range is named in the SoT. The individual tests are defined in the *Noema × Tushe Synthetic Enterprise Environment: Technical Requirements & Acceptance Specification v1.0*, §22, kept as a frozen record in [`poc/tushe/`](poc/tushe/README.md). |

## Coverage check

| Prefix | IDs defined in SoT | IDs listed here |
|---|---|---|
| AGENT- | 27 | 27 |
| BD- | 15 | 15 |
| INV- | 28 | 28 |
| OD- | 16 | 16 (in open-decisions.md) |
| PLAT-FR- | 17 | 17 |
| PLAT-NFR- | 21 | 21 |
| PLAT-US- | 11 | 11 |
| POC-FR- | 17 | 17 |
| POC-NFR- | 10 | 10 |
| US- | 22 | 22 |
