# NOEMA × TUSHE — Synthetic Enterprise Environment
## Technical Requirements & Acceptance Specification
**Version 1.0** · Prepared by Noema for the Tushe team · **CONFIDENTIAL — FOR THE TUSHE TEAM**

> **Repository status: frozen record (issued v1.0).** This is the version issued to Tushe. Do not edit it. Requested changes are recorded in delta files in this folder (for example `tushe-spec-delta-v1.1.md`) and become a new version only when re-issued. The original export is kept unchanged in `source/`.

## Contents

- [What We Are Asking For, in One Paragraph](#what-we-are-asking-for-in-one-paragraph)
- [1. Scope](#1-scope)
- [2. Design principles](#2-design-principles)
- [3. Synthetic enterprise architecture](#3-synthetic-enterprise-architecture)
- [4. Domain model](#4-domain-model)
- [5. State models](#5-state-models)
- [6. Unknown outcomes](#6-unknown-outcomes)
- [7. Deterministic chaos / failure injection](#7-deterministic-chaos--failure-injection)
- [8. Scenario engine](#8-scenario-engine)
- [9. Controlled time](#9-controlled-time)
- [10. Events & webhooks](#10-events--webhooks)
- [11. Idempotency & concurrency](#11-idempotency--concurrency)
- [12. Identity, authorization & business policy](#12-identity-authorization--business-policy)
- [13. Nigerian payment-rail semantics](#13-nigerian-payment-rail-semantics)
- [14. Evidence, reconciliation & timeline](#14-evidence-reconciliation--timeline)
- [15. Ground truth, control plane & isolation](#15-ground-truth-control-plane--isolation)
- [16. Synthetic data & test isolation](#16-synthetic-data--test-isolation)
- [17. API & integration contract](#17-api--integration-contract)
- [18. Audit, provenance & observability](#18-audit-provenance--observability)
- [19. Access & mutation boundary](#19-access--mutation-boundary)
- [20. Non-functional requirements](#20-non-functional-requirements)
- [21. Required deliverables](#21-required-deliverables)
- [22. Acceptance criteria](#22-acceptance-criteria)
- [23. Minimum scenario pack for initial readiness](#23-minimum-scenario-pack-for-initial-readiness)
- [24. What we’d like Tushe to confirm](#24-what-wed-like-tushe-to-confirm)
- [25. Readiness sign-off](#25-readiness-sign-off)
- [Appendix A — Example composite scenario](#appendix-a--example-composite-scenario)
- [Appendix B — Glossary](#appendix-b--glossary)

## What We Are Asking For, in One Paragraph

We would like to use the Tushe platform as a synthetic enterprise environment — a controlled, realistic stand-in for a live fintech’s transaction and operations landscape that we can integrate against and test repeatedly. We are not asking for a customer-facing banking product or a polished demo. We are asking for an environment that behaves like real enterprise infrastructure behaves on its bad days: multiple systems that don’t always agree, state that arrives late, events that duplicate or go missing, outcomes that can’t be read off a single response, and failures we can reproduce on demand. This document describes exactly what that environment must do, and how we will jointly confirm it is ready.

> **THE ONE PRINCIPLE BEHIND EVERYTHING HERE**
>
> **The environment must make shortcuts fail.** It should not be possible to determine the correct outcome of a transaction by reading one convenient status field. Independent evidence has to exist across systems, some of it delayed or conflicting, so that the true outcome must be investigated and reconciled rather than simply read. If a clean happy-path API were enough, we wouldn’t need Tushe for this. Making that difficulty real, controllable, and repeatable is the whole job.

A short note on why this matters to us: our software’s entire purpose is to act safely and correctly against messy enterprise reality. We can only prove it does that if we test it somewhere the mess is genuine but controlled. That is the role we’re asking Tushe to play. Everything below serves that single goal — nothing more, nothing less.

Requirements are tagged P0 (required before we begin integration) or P1 (required before serious end-to-end testing). Where a capability isn’t native to Tushe today, we’re glad to discuss an agreed control hook rather than assume it must be rebuilt — see §24.

## 1. Scope

Tushe provides — the synthetic enterprise substrate:

- A realistic synthetic financial domain and its underlying state.
- Independent representations of the same business event across several logical systems.
- Controlled asynchronous processing, delayed outcomes, and state transitions.
- Deterministic, reproducible failure conditions — natively, or through agreed control hooks.
- A privileged, isolated ground-truth view for testing and acceptance.
- Controllable time, events, scenarios, seed data, reset, and replay.
- Versioned, documented API and event contracts.
- Enough diagnostics to tell a simulator defect apart from an injected fault or an integration bug.

Explicitly not required — please don’t build these:

- A consumer-facing banking or mobile application.
- A complete core-banking product beyond the domains named here.
- A general workflow, reporting, or automation suite.
- Any real customer data, production credentials, or production integrations.

The discipline cuts both ways: depth in a small number of domains is far more valuable to us than shallow coverage of many banking features.

## 2. Design principles

| PRINCIPLE | WHAT IT MEANS FOR THE BUILD |
|---|---|
| Not CRUD-only | Model state, lifecycle, events, failure, and reconciliation — not just request/response. |
| Multi-system | Represent one business event independently across the relevant domains. |
| Controlled inconsistency | Configured systems may deliberately disagree, without the environment losing authoritative ground truth. |
| Deterministic | A named scenario plus a seed must reproduce the same material behaviour every time. |
| Ground truth is sacred | Authoritative internal state is kept separate from what an ordinary client can observe. |
| Isolation | Control and ground-truth capabilities are never reachable with ordinary integration credentials. |
| Synthetic realism | Realistic Nigerian fintech/payment semantics, with entirely synthetic data. |
| Safe mutation | Money-moving capabilities exist for realism but are independently gated and off by default (§19). |
| Observable to us | Requests, transitions, events, and injected faults are traceable in privileged diagnostics. |

## 3. Synthetic enterprise architecture

The environment must expose the following logical domains. They may share physical infrastructure internally, as long as each one’s state and behaviour is independently observable and controllable.

| LOGICAL DOMAIN | MINIMUM RESPONSIBILITY |
|---|---|
| Customer / Identity | Synthetic customers, identity/KYC state, risk tier, customer-to-account relationships. |
| Accounts / Ledger | Accounts, balances, holds, and strict double-entry postings. |
| Transaction Service | Business transaction lifecycle, references, status, and history. |
| Payment Switch / Rail | An independent downstream processing state, with its own reference and response semantics. |
| Beneficiary / Name Enquiry | Beneficiary records and account-name validation, including ambiguity and mismatch. |
| Settlement | Settlement lifecycle, including delayed and batched settlement and its evidence. |
| Events / Webhooks | Asynchronous state-change events and their delivery behaviour. |
| Case / Dispute | Operational complaint/dispute records and their lifecycle. |
| Policy / Authorization | Roles, capabilities, business restrictions, and approval requirements. |
| Audit / Provenance | Immutable record of material state changes with causal metadata. |

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| SE-01 | P0 | Independent system state | Ledger, transaction, switch, settlement, and beneficiary/credit state must be independently queryable. |
| SE-02 | P0 | Cross-system divergence | The environment must support configured cases where two or more systems report different states for the same business event. |
| SE-03 | P0 | Correlation | A business event must be traceable across system-specific identifiers via a shared correlation/reference model. |
| SE-04 | P0 | No forced convergence | A change in one system must not automatically make every other system synchronously consistent, unless the scenario is configured that way. |

## 4. Domain model

### 4.1 Customers & Identity

Synthetic customer IDs and stable identity references; profile and status; configurable KYC state and timestamps; synthetic BVN/NIN-style identifiers where useful (never real ones); risk tier and restrictions; customer-to-account relationships; and the ability to hold duplicate, partial, stale, or ambiguous identity records.

### 4.2 Accounts & Balances

Account ID, owning customer, status, and currency; ledger balance and available balance; pending amounts and holds; account restrictions and status changes; account transaction history; and multiple accounts per customer.

### 4.3 Ledger

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| LED-01 | P0 | Double-entry integrity | Every authoritative posting maintains balanced debit/credit entries. |
| LED-02 | P0 | Ledger metadata | Entries carry entry ID, transaction/reference ID, account ID, direction, amount, currency, posting timestamp, sequence/version, and correlation reference. |
| LED-03 | P1 | Pending & compensating entries | Support holds, pending postings, releases, reversals, and compensating entries. |
| LED-04 | P0 | Partial / uncertain posting | Support a controlled scenario where one leg posts and another is delayed or uncertain, while ground truth remains known. |
| LED-05 | P0 | Money representation | Integer minor units (kobo for NGN) or exact decimal arithmetic. Floating-point money is not acceptable. |
| LED-06 | P1 | Fees & net amounts | Support configurable fees/charges so that gross, fee, and net amounts can be reconciled against each other. |

### 4.4 Cross-system references

A single transaction should be able to carry or link, as applicable: a client/request reference, a transaction-service ID, a ledger posting reference, a switch/session reference, an RRN-style reference, a settlement reference, a beneficiary-credit reference, a case/dispute reference, and event IDs. Discovering that these all describe one underlying event is exactly the kind of work the environment needs to make necessary.

## 5. State models

Transaction, settlement, beneficiary credit, case, and dispute are separate lifecycles. They must not be collapsed into one flat transaction status, because several of them are legitimately true at the same time — a transaction can be PROCESSING while settlement is PENDING and beneficiary credit is UNKNOWN.

| LIFECYCLE | MINIMUM STATES |
|---|---|
| Transaction | CREATED \| INITIATED \| SUBMITTED \| PROCESSING \| SUCCESSFUL \| FAILED \| REJECTED \| TIMED_OUT \| EXECUTION_OUTCOME_UNKNOWN \| DUPLICATE \| PARTIAL |
| Settlement | NOT_REQUIRED \| PENDING \| SETTLED \| FAILED \| REVERSED \| UNKNOWN |
| Beneficiary credit | NOT_APPLICABLE \| PENDING \| CREDITED \| NOT_CREDITED \| UNKNOWN |
| Case / resolution | NOT_OPEN \| OPEN \| INVESTIGATING \| AWAITING_EXTERNAL_RESPONSE \| ACTION_REQUIRED \| ESCALATED \| RESOLVED \| CLOSED |
| Dispute | NONE \| OPEN \| UNDER_REVIEW \| UPHELD \| REJECTED \| RESOLVED |

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| STM-01 | P0 | Transition contract | Document the legal transitions, terminal states, and the trigger (time or event) for each lifecycle. |
| STM-02 | P0 | State invariants | Document which states must never coexist in authoritative state (e.g. a transaction cannot be both SUCCESSFUL and REJECTED in the same authoritative version). |
| STM-03 | P0 | Transition history | Historical transitions must be queryable with timestamps and causal metadata. |

## 6. Unknown outcomes

This is the single most important behaviour in the environment, so we’re calling it out on its own.

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| UNK-01 | P0 | Post-commit unknown | Support the case where an operation commits internally but the initiating request returns a timeout, 5xx, or disconnect, so the client never learns the outcome. |
| UNK-02 | P0 | Pre-commit uncertainty | Support failures where no commit occurred but the client still receives an ambiguous transport-level failure. |
| UNK-03 | P0 | Evidence retrieval | Expose enough independent evidence to investigate an unknown outcome — without revealing privileged ground truth. |
| UNK-04 | P0 | Never normalise | The environment must not silently convert an unknown transport outcome into a confirmed success or failure. “Unknown” has to survive as a real, observable condition. |

## 7. Deterministic chaos / failure injection

Controlled fault injection is a first-class requirement. Randomness alone is not sufficient — every important failure must be reproducible from a scenario ID and seed. Native support is preferred; where a behaviour is better implemented at the edge, a stable control hook that permits deterministic injection is acceptable.

| FAILURE CLASS | REQUIRED EXAMPLES |
|---|---|
| Transport | Timeout, disconnect, connection reset, 502/503/504, delayed response. |
| Application | Validation failure, authorization failure, conflict, 429/rate limit, dependency unavailable. |
| State | Stale read, missing record, duplicate record, contradictory state, partial state. |
| Execution | Commit-then-timeout, partial execution, silent success, silent failure, recovery timeout. |
| Events | Duplicate, missing, delayed, out-of-order, replayed, malformed, stale-version. |
| Identity | Ambiguous match, duplicate identity, stale identity, name mismatch. |
| Policy / auth | Authorization denied, approval required, stale authorization, policy change mid-flight. |

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| CHA-01 | P0 | Scenario ID | Every controlled run has a unique scenario/run identifier. |
| CHA-02 | P0 | Deterministic seed | Fault generation supports a seed; the same scenario + seed reproduces the same material fault sequence. |
| CHA-03 | P0 | Scripted faults | Support explicit scripts such as commit then return 504, drop event X, deliver event Y twice, return stale state for N seconds. |
| CHA-04 | P1 | Scoped faults | Faults can be applied at the system, endpoint, transaction, request, event, or scenario level. |
| CHA-05 | P0 | Hidden injection | Injected conditions are visible in privileged diagnostics but never disclosed to the ordinary integration client as a shortcut. |
| CHA-06 | P0 | Fault trace | Diagnostics record what was injected, when, against what target, the configured behaviour, and the actual underlying outcome. |

## 8. Scenario engine

Named, reproducible scenarios — not manual reconstruction of failures each time.

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| SCN-01 | P0 | Scenario definition | A scenario defines initial state, the resources involved, injected faults, the event schedule, timing, the authoritative outcome, and the invariants that must hold. |
| SCN-02 | P0 | Reset & replay | A scenario can be reset and replayed with no manual database intervention. |
| SCN-03 | P0 | Composite failures | Scenarios can combine multiple simultaneous or ordered faults; real incidents rarely arrive one at a time. |
| SCN-04 | P0 | Authoritative outcome | Each scenario retains the authoritative final state needed to grade a run. |

The concrete starting set is listed in §23.

## 9. Controlled time

Financial systems are temporal, and we can’t wait real hours for settlement or reversal windows during testing.

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| TIM-01 | P0 | Virtual clock | Provide a controllable simulated clock or an equivalent deterministic time mechanism. |
| TIM-02 | P0 | Freeze & advance | The control plane can freeze and advance simulated time. |
| TIM-03 | P0 | Temporal metadata | Expose the relevant timestamps where applicable: occurred, processed, posted, settled, delivered, observed. |
| TIM-04 | P0 | Scheduled transitions | Delayed settlement, delayed credit, and event delivery must be schedulable and replayable against the simulated clock. |

## 10. Events & webhooks

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| EVT-01 | P0 | Event schema | Events carry event ID, type, aggregate/resource ID, version/sequence where applicable, occurred/published/delivered timestamps, correlation ID, causation ID, and payload. |
| EVT-02 | P0 | Duplicate delivery | Support both the same event delivered twice and the same business effect represented by two different event IDs. |
| EVT-03 | P0 | Ordering | Support deliberate reordering while retaining sequence information. |
| EVT-04 | P0 | Loss, delay, replay | Support dropped, delayed, and replayed events, including a late event arriving after a later case state. |
| EVT-05 | P1 | Authenticity | Where webhooks are used, provide HMAC signing or equivalent, with documented replay protection. |
| EVT-06 | P0 | Delivery history | Privileged diagnostics expose delivery attempts and outcomes. |

## 11. Idempotency & concurrency

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| IDP-01 | P0 | Idempotency contract | Define key scope, enforcement, persistence, and required behaviour for every state-mutating endpoint. |
| IDP-02 | P0 | Same key, same payload | A repeated equivalent request must not create a second business effect. |
| IDP-03 | P0 | Same key, different payload | A different request under the same key returns a deterministic conflict. |
| IDP-04 | P0 | Retry after timeout | Support the case where the first request may already have committed before the timeout, and a retry then arrives with the same key. |
| IDP-05 | P0 | Different keys, same operation | Support controlled duplicate-business-operation scenarios. |
| IDP-06 | P0 | Retention | Document idempotency-key TTL/retention and persistence. |
| CON-01 | P1 | Concurrency control | Support versioning / optimistic concurrency (e.g. version or ETag) so stale mutations can be detected. |
| CON-02 | P0 | Concurrent modification | Provide scenarios where a resource changes between our read and our subsequent operation. |

## 12. Identity, authorization & business policy

The environment must distinguish technical authentication (is this a valid credential?) from business authorization (is this actor actually allowed to do this, at this amount, under this policy?).

| CAPABILITY | REQUIRED BEHAVIOUR |
|---|---|
| Principal | Synthetic users/services with stable identity. |
| Role | Configurable role / organisational assignment. |
| Capability | Explicit action-level permissions. |
| Resource scope | Authorization tied to customer / account / transaction / tenant. |
| Amount threshold | Rules that depend on transaction value. |
| Approval | Actions that require an additional approval step. |
| Restrictions | Account / customer / transaction restrictions that block an otherwise valid operation. |
| Policy version | Rules that are versioned and time-aware. |
| Stale authorization | Authority that changes between observation and execution. |
| IAM instability | Injected 401/403 that is distinguishable, in privileged diagnostics, from genuine configuration. |

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| AUTH-01 | P0 | Business authorization | Support cases where authentication succeeds but business authority is insufficient. |
| AUTH-02 | P1 | Approval states | Support pending, granted, rejected, and expired approvals. |
| AUTH-03 | P0 | Policy mutation | Policy versions and effective times are queryable and reproducible, including a policy that changes during an in-flight scenario. |
| AUTH-04 | P0 | Tenant / resource isolation | Cross-tenant and cross-resource access fails deterministically and is testable. |

## 13. Nigerian payment-rail semantics

Because this environment models a Nigerian fintech, it should reflect Nigerian payment concepts rather than generic international abstractions.

- NUBAN-style account numbers and bank identifiers, using synthetic values.
- Name Enquiry / account-name validation around transfer initiation.
- NIP-style transfer and session references, and RRN-style identifiers where applicable.
- A documented response-code taxonomy that clearly separates success, pending, rejected, and timeout/unknown/retryable conditions.
- Interbank transfer processing and settlement behaviour.
- Debited-but-not-credited scenarios, with configurable auto-reversal / reconciliation windows.
- Failed transaction, duplicate debit, erroneous transfer, reversal, and dispute cases.
- NGN throughout, at kobo-level precision.

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| NG-01 | P0 | Rail semantics | Payment-rail behaviour follows the agreed Nigerian model and is documented in the API/event contract. |
| NG-02 | P0 | Reference propagation | Session/reference identifiers stay traceable across transaction, switch, settlement, ledger, and event records. |
| NG-03 | P0 | Response taxonomy | Codes clearly distinguish a confirmed failure from an unresolved outcome, and are stable and documented. |

## 14. Evidence, reconciliation & timeline

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| REC-01 | P0 | Transaction history | Provide a chronological history of material transaction state changes. |
| REC-02 | P0 | Timeline | Provide a timeline correlating request, ledger posting, switch interaction, settlement, beneficiary credit, and event delivery. |
| REC-03 | P0 | Evidence by source | Expose source-specific records without collapsing them into one synthesised answer. |
| REC-04 | P0 | Reconciliation surface | Provide machine-readable access to the records needed to compare transaction, ledger, switch, settlement, and beneficiary state. |
| REC-05 | P0 | Preserve contradictions | Conflicting source records remain independently retrievable; the environment must not “resolve” them for us. |

Illustrative timeline for one transaction:

| TIME | SOURCE | OBSERVED EVENT |
|---|---|---|
| 10:00:01 | Transaction service | Request received |
| 10:00:02 | Ledger | Debit committed |
| 10:00:31 | API | Client response timed out |
| 10:00:34 | Payment switch | Accepted |
| 10:00:37 | Events | Webhook delivered |
| 10:01:02 | Settlement | Pending |
| 10:03:15 | Beneficiary | Credit not yet confirmed |

## 15. Ground truth, control plane & isolation

Non-negotiable. The environment must maintain authoritative ground truth separately from the ordinary integration surface. Ground truth exists for testing and acceptance only, and must never be reachable with ordinary integration credentials. Without a trusted, isolated way to ask “what actually happened?”, we cannot objectively grade a run — this is as important as the chaos engine itself.

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| GT-01 | P0 | Authoritative state | Maintain authoritative internal state for actual commits, events, and scenario configuration. |
| GT-02 | P0 | Privileged oracle | Provide a privileged read that establishes the actual underlying outcome, independent of whatever response the integration client received. |
| GT-03 | P0 | No ordinary-client access | Ordinary integration credentials cannot reach ground-truth or control-plane endpoints. |
| GT-04 | P0 | Run trace | Ground truth shows the actual sequence of state changes and injected conditions for a run. |
| GT-05 | P1 | Export | Ground-truth state, event history, and scenario metadata are exportable in machine-readable form. |

Control-plane capabilities P0: create/load a scenario · seed/reset the environment · set and reproduce a seed · configure a fault profile · freeze/advance the clock · schedule/drop/delay/reorder events · snapshot · restore · replay · inspect ground truth · export run artefacts.

## 16. Synthetic data & test isolation

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| DATA-01 | P0 | Synthetic only | No production customer, account, identity, transaction, or credential data. |
| DATA-02 | P0 | Deterministic seed data | Seed datasets for customers, accounts, transactions, beneficiaries, settlements, events, and cases. |
| DATA-03 | P1 | Scale tiers | At least small, medium, and large datasets, enough for realistic histories and concurrent activity. |
| DATA-04 | P0 | Adversarial data | Fixtures or generation for duplicate customers, similar/ambiguous names, multiple matching accounts, repeated amounts, stale records, and conflicting metadata — enough that a trivial single-record lookup is never sufficient. |
| DATA-05 | P0 | Isolation | Parallel developer/CI runs must not corrupt one another’s state. |
| DATA-06 | P0 | Reset | An environment can be reset to a known baseline without manual database work. |

## 17. API & integration contract

Exact URL paths can be agreed jointly; the capabilities below are what we need.

| DOMAIN | MINIMUM CAPABILITIES |
|---|---|
| Customer | Get customer; list accounts; get identity/KYC; get risk/restrictions. |
| Account | Get account; balances; ledger; holds/pending; account transactions. |
| Transaction | Get transaction; query/search; history/timeline; linked events & references. |
| Beneficiary | Name enquiry/resolve; match quality; ambiguity outcomes. |
| Switch | Independent downstream switch transaction/reference state. |
| Settlement | Settlement state/history and delayed-settlement behaviour. |
| Case / Dispute | Create/query/update a case or dispute; retrieve linked evidence. |
| Evidence / Audit | Transaction-linked evidence, audit history, and state transitions. |
| Reconciliation | Source-specific records to compare transaction / ledger / switch / settlement / beneficiary. |
| Events | Delivery/subscription plus event detail and delivery metadata. |

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| API-01 | P0 | OpenAPI | A complete, machine-readable OpenAPI specification. |
| API-02 | P0 | Versioning | A defined versioning and backward-compatibility policy for the POC window. |
| API-03 | P0 | Error contract | Documented HTTP status, business error codes, retryability, and known/unknown outcome semantics. |
| API-04 | P0 | Correlation | Request ID and correlation ID propagate across API, event, and audit records. |
| API-05 | P1 | Pagination & filtering | Documented, stable pagination and query semantics for large histories. |

For every mutating operation, please document: authentication/authorization, request/response schema, error schema, idempotency, side effects, correlation IDs, timeout/latency behaviour, retry safety, and how success can be verified.

## 18. Audit, provenance & observability

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| AUD-01 | P0 | Immutable audit | Append-only or tamper-evident records of material state changes. |
| AUD-02 | P0 | Transition provenance | Each record captures actor, actor type, request ID, correlation ID, causation ID, source system, previous and new state, and timestamps. |
| AUD-03 | P1 | Policy provenance | Record the applicable policy/version for policy-governed actions. |
| AUD-04 | P0 | Event provenance | Link events to the causal request or state transition. |
| AUD-05 | P0 | Audit query | Retrieve by transaction, account, customer, case, and correlation/reference ID. |
| OBS-01 | P0 | Diagnostic visibility | Privileged diagnostics distinguish domain behaviour, injected fault, infrastructure error, and client error — so we can always answer “was that our bug, or the simulator?” |
| OBS-02 | P0 | Fault visibility | Diagnostics expose the injected fault, the actual outcome, and event delivery history. |
| OBS-03 | P1 | Latency | Capture request/event latency and the relevant configured vs actual timestamps. |

## 19. Access & mutation boundary

Please read this one carefully — it governs what our integration credentials may do. The environment may fully support money-moving operations (reversals, credits, compensating entries) for realism and for later phases. For the initial phase, however, the credentials we integrate with must be restricted to reads, investigation, and non-monetary case operations. Money-moving operations must be independently gated and off by default for our integration, enabled only by explicit written agreement.

| ID | Priority | Requirement | Detail |
|---|---|---|---|
| MUT-01 | P0 | Independent permissioning | Financial-mutation capabilities are permissioned separately from read/investigation capabilities. |
| MUT-02 | P0 | Simulation integrity | Any supported reversal, credit, or compensating behaviour is represented consistently across ledger and audit state. |
| MUT-03 | P0 | Initial read-first access | Our initial credentials are constrained to the agreed non-monetary capability set. |
| MUT-04 | P1 | Preview capability | Where feasible, provide non-mutating eligibility/preview operations for financial actions (i.e. “would this be allowed, and what would it do?” without doing it). |

## 20. Non-functional requirements

| AREA | REQUIREMENT |
|---|---|
| Reliability | The environment stays stable while it simulates downstream unreliability. |
| Determinism | Named scenarios and seeds are replayable. |
| Latency | Normal and degraded latency profiles are configurable; exact values agreed for the POC workload. |
| Concurrency | Concurrent transactions and isolated parallel test runs are supported. |
| Data volume | Histories are large enough to exercise pagination and reconciliation. |
| Availability | Available across the agreed POC testing window. |
| Observability | Simulator faults are diagnosable independently of injected faults. |
| Compatibility | API and event contracts are stable within the agreed POC version. |

## 21. Required deliverables

| DELIVERABLE | MINIMUM CONTENT |
|---|---|
| Synthetic environment | An accessible environment with the agreed domains, behaviour, and seeded data. |
| OpenAPI specification | A versioned, machine-readable REST contract. |
| Event specification | Schemas, delivery semantics, and the authenticity mechanism. |
| State model | Separate lifecycle diagrams with transitions, triggers, and invariants. |
| Scenario pack | The agreed initial adversarial scenarios, with reproducible configuration. |
| Control-plane API | Scenario, seed, clock, fault, reset, snapshot/replay, and diagnostics. |
| Ground-truth interface | Privileged authoritative state and run-artefact access, isolated from ordinary integration. |
| Seed datasets | Deterministic synthetic data at the agreed scale tiers. |
| Credentials | Least-privilege integration credentials, separate from control/diagnostic credentials. |
| Runbook | Setup, reset, scenario execution, troubleshooting, and known limitations. |
| Acceptance evidence | Evidence that all P0 acceptance criteria (§22) have been demonstrated. |

## 22. Acceptance criteria

The environment is ready for meaningful integration once these are demonstrated in a joint session. All are P0.

| ID | Test | How we check | Pass condition |
|---|---|---|---|
| AT-01 | Deterministic replay | Run the same scenario twice with the same seed. | Material fault sequence and authoritative outcome reproduce. |
| AT-02 | Ground-truth isolation | Attempt ground-truth access with ordinary credentials. | Access denied. |
| AT-03 | Post-commit timeout | Run commit-then-timeout. | Client sees ambiguity; privileged oracle confirms the actual outcome. |
| AT-04 | Stale state | Write, then read under a stale-state profile. | Read returns the configured prior version; authoritative state stays correct. |
| AT-05 | Event loss | Drop a configured event. | State changes; event absent from normal delivery; diagnostics show the drop. |
| AT-06 | Duplicate event | Duplicate a configured event. | Configured duplicate deliveries occur and are traceable. |
| AT-07 | Out-of-order event | Reorder configured events. | Events arrive in the configured order with sequence metadata intact. |
| AT-08 | Cross-system conflict | Configure ledger/switch/settlement disagreement. | Each source stays independently queryable and contradictory. |
| AT-09 | Ambiguous beneficiary | Run an ambiguous name enquiry. | Multiple/conflicting candidates returned; no silent auto-selection. |
| AT-10 | Idempotency conflict | Reuse a key with a different payload. | Deterministic conflict; no unintended second effect. |
| AT-11 | Retry after timeout | Time out the first request, retry the same key. | Configured business-effect semantics reproduce deterministically. |
| AT-12 | Authorization boundary | Use an authenticated but unauthorized principal. | Action denied, with a traceable reason. |
| AT-13 | Policy mutation | Change policy during a scenario. | Both policy versions and their effective times are traceable. |
| AT-14 | Concurrent update | Modify a resource between read and mutation. | Stale/concurrent mutation detected as documented. |
| AT-15 | Time control | Freeze, then advance the clock. | Scheduled transitions fire according to simulated time. |
| AT-16 | Reset & replay | Reset, then replay a named scenario. | No manual reconstruction required. |
| AT-17 | Ground-truth export | Export a completed run. | Machine-readable scenario/state/event artefacts are produced. |
| AT-18 | Mutation isolation | Attempt a monetary mutation with initial credentials. | Denied unless explicitly enabled. |
| AT-19 | Audit completeness | Inspect a material transition. | Actor / request / correlation / state / timestamp metadata all present. |
| AT-20 | Simulator diagnostics | Trigger an injected fault and a genuine platform error separately. | Privileged diagnostics tell them apart. |

## 23. Minimum scenario pack for initial readiness

| # | SCENARIO | REQUIRED CONDITION |
|---|---|---|
| 1 | Normal successful transfer | Relevant systems converge normally. |
| 2 | Failed before commit | No financial mutation occurs. |
| 3 | Commit then timeout | Authoritative commit occurs; client outcome is unknown. |
| 4 | Debited / not credited | Originating debit established; beneficiary credit absent or pending. |
| 5 | Duplicate webhook | Same logical event delivered multiple times. |
| 6 | Missing webhook | State changes without the expected event. |
| 7 | Out-of-order webhook | Events arrive out of causal order. |
| 8 | Stale read | Read returns a prior version after a successful write. |
| 9 | Contradictory evidence | Independent systems report different outcomes. |
| 10 | Delayed settlement | Outcome established while settlement stays pending. |
| 11 | Beneficiary ambiguity | Name/account resolution returns multiple or conflicting matches. |
| 12 | Duplicate submission | Repeated request tests deduplication. |
| 13 | Recovery uncertainty | A recovery/retry operation itself becomes unknown. |
| 14 | Unauthorized principal | Authentication succeeds; business authority is insufficient. |
| 15 | Approval required | Action requires an additional approval. |
| 16 | Policy changed | Applicable rule changes mid-scenario. |
| 17 | Concurrent modification | State changes between read and mutation. |
| 18 | Malformed / stale event | Event is invalid or references an old version. |
| 19 | Impossible state | A controlled invariant violation is introduced. |
| 20 | Composite failure | Several independent faults occur in one scenario. |

## 24. What we’d like Tushe to confirm

So we can plan realistically, please respond to each item with Supported / Requires extension / Not supported, plus a short implementation note where useful.

- Which of the logical domains (§3) exist natively today?
- Which failure/chaos behaviours (§7) are available natively?
- Which behaviours would need custom work or a control hook?
- Can you provide an isolated, privileged ground-truth read path (§15)?
- Can you provide deterministic scenario IDs and seeded, replayable execution (§7–8)?
- Can you provide a controllable virtual clock (§9)?
- Can you expose independent ledger, transaction, switch, settlement, and beneficiary state (§3)?
- Can you preserve cross-system inconsistencies without normalising them (§14)?
- Can you provide event loss / delay / duplication / reordering controls (§10)?
- Can you provide reset / snapshot / restore / replay (§8, §15)?
- Can you provide isolated environments for parallel testing (§16)?
- What are the expected delivery dates for the P0 capabilities?
- What known limitations should we document before integration?

We’re very open to using existing Tushe capabilities wherever they already fit — the aim is to get to a reliable, reproducible environment quickly, not to have you rebuild things you already do well. Where something isn’t native, we’d rather hear that early and design an agreed hook together than discover it mid-integration.

## 25. Readiness sign-off

The environment is accepted for integration when:

- All P0 requirements are implemented, or explicitly accepted as agreed exceptions.
- All P0 acceptance tests (§22) pass.
- The minimum scenario pack (§23) is executable and reproducible.
- OpenAPI and event specifications are delivered and versioned.
- Integration credentials are isolated from control-plane and ground-truth capabilities.
- Synthetic data, reset, and replay are operational.
- Known limitations and unsupported behaviours are documented.

## Appendix A — Example composite scenario

Illustrative only — this shows the level of control we need, not a required internal syntax.

`COMMIT_THEN_TIMEOUT_WITH_DELAYED_CREDIT`

A transfer is initiated. The ledger debit commits. The initiating API returns a timeout. The payment switch records acceptance. The expected success event is delayed. Beneficiary credit is delayed. Settlement remains pending. A duplicate event is later delivered. The control plane retains the exact configured sequence, timing, and authoritative outcome, so the whole run can be reset and replayed identically.

## Appendix B — Glossary

| TERM | MEANING |
|---|---|
| Synthetic enterprise | A controlled, entirely synthetic representation of interconnected financial enterprise systems and their state. |
| Observable state | State available through the ordinary integration interfaces. |
| Ground truth | Authoritative internal state, retained for testing/acceptance and isolated from ordinary integration access. |
| Control plane | The privileged interface used to configure scenarios, faults, time, reset/replay, and diagnostics. |
| Unknown outcome | A condition where the business effect of an attempted operation cannot be established from the initiating response alone. |
| Scenario | A named, reproducible combination of initial state, actions, timing, and injected conditions. |
| Fault injection | The controlled introduction of a transport, state, event, authorization, or execution failure. |
| Business invariant | A condition that must remain true in authoritative enterprise state. |

*This document defines the minimum environment we need in order to use Tushe as our synthetic enterprise substrate. We’re looking forward to building this with you.*
