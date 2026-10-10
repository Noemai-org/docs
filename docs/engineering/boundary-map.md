# Boundary map

> **Derived, non-normative.** This page is a navigation aid for engineers, security reviewers and coding agents. For each power it shows the components that belong to it, what it may do, what it must never do, and the requirement IDs that enforce those boundaries. The architecture itself is defined only in [`NOEMA_SOURCE_OF_TRUTH.md`](../NOEMA_SOURCE_OF_TRUTH.md) (the SoT):
>
> - §12–17 for the platform;
> - §35 for the POC subset;
> - §43 for contracts;
> - §45 for invariants;
> - §47 for trust boundaries;
> - §51 for module boundaries.
>
> If this page and the SoT disagree, the SoT wins.

**Module paths are planned, not present.** The paths below are the module boundaries named in SoT §51. Noema uses several repositories; which repository hosts each deployable and `/contracts` is still [OPEN] (§51; [OD-P-13](../open-decisions.md#od-p-13)). This repository contains no application code. The paths show where code *will* live and what it may import; they do not mean the code exists.

## Two deployables (SoT §35.6)

| Deployable | Hosts | May reach | Never reaches |
|---|---|---|---|
| **Model service** (Python) | Understanding, voice pipeline, Explanation, all model and speech provider adapters | Model and speech providers (GPT, Gemini, Claude; Aethex AI, Indigenius, N-ATLAS; BD-16) | The core database, enterprise adapters, Temporal, grant keys (INV-29) |
| **Core service** (Go) | Trust, Execution, Outcome, the Record, the Evidence Layer, enterprise adapters, Temporal workers | Postgres, enterprise adapters, Temporal, grant keys | Any model or speech provider (INV-29, AGENT-05) |

The two talk only over mutual TLS using contracts from `/contracts` (§35.6, §47.1). Temporal orchestrates but is never the authoritative record (INV-30).

## The rule in one line

**Intelligence proposes. Trust determines. Deterministic infrastructure executes. Evidence proves the outcome.** (SoT §1, §13; BD-05.)

Understanding → Trust → Execution → Outcome, with an independent Record that witnesses everything and can do nothing. No power can do another power's job, and none holds enough power to make a consequential action happen on its own.

## The four powers and the Record

| Power | Components (SoT §14) | Planned module (§51) | Produces (§13.2, §43; authentication per §43 and §47.4) | May use a language model? (§13.1) | Must never (§13.1, §13.3) | Enforced by |
|---|---|---|---|---|---|---|
| **Understanding** | Input Gateway; Intent Compiler; Context Fabric; Entity Resolution | `/services/model/understanding` (model service; models only via `/services/model/providers`) | Intent Object, a *proposal* | Yes | Act; hold credentials; see policy rules or thresholds; assert identity; authorise (confidence is information, not authority) | INV-02, INV-06, INV-12, INV-29, AGENT-09, AGENT-10, AGENT-28, PLAT-NFR-07 |
| **Trust** | State Reconciliation (decision-time); Authority Engine (technical, policy, business); Policy Engine; Risk and Clock Evaluation; Decision Maker | `/services/core/trust` (core service; no models) | Decision Record; confirmation request on `CONFIRM` (§43.2a); Decision Grant only on `ALLOW` | **No** | Execute; change the intent; mark an outcome achieved; construct calls; infer that one policy version is "stricter" than another | INV-01, INV-06, INV-09, INV-16, INV-19, INV-20, INV-23, INV-25, INV-26, PLAT-NFR-01, PLAT-NFR-03 |
| **Execution** | Enterprise Action Graph; Planner; Capability Registry; Execution Controller; durable runner | `/services/core/execution` and `/services/core/workflows` (core service; no models) | Execution Receipt | **No** | Choose capabilities, targets or parameters beyond the grant; retry an unknown outcome without a new grant; declare business success; invent capabilities at runtime (Planner); retry a capability whose retry safety is `NONE`; write without the grant's version tokens where `CONDITIONAL_WRITE` is declared | INV-01, INV-03, INV-05, INV-07, INV-08, INV-15, INV-17, INV-18, INV-23, INV-24, INV-27, INV-30, AGENT-06, AGENT-07, AGENT-08 |
| **Outcome** | Outcome Verifier; Outcome Watch; Closure and Recovery Trigger | `/services/core/outcome` (core service; verifier and outcome watch; no models) | Outcome Verdict; `outcome.updated` event (§43.4a) | **No** | Execute; change a decision; reuse Trust's evidence snapshot for its verdict; leave a `PENDING_EXTERNAL` verdict without a durable watch and deadline | INV-01, INV-04, INV-15, INV-28, AGENT-21 |
| **Record** (independent) | Causal Record; Operational Memory | `/services/core/record` (core service) | Record events, append-only and hash-chained | No | Act; be treated as operational truth (systems of record stay authoritative); let a model write instructions into memory | INV-10, INV-11, PLAT-FR-12, PLAT-NFR-04 |
| **Explanation** (separate component, not a power) | Explanation Engine | `/services/model/explanation` (model service; models via `/services/model/providers`; reads verified facts only) | Plain-language explanation; its own output event | Yes, only to phrase facts Outcome has verified | Create facts; change state; influence a verdict; write to the Record except its own output event; feed a decision, grant or verdict | INV-13, INV-22, INV-29, AGENT-05, AGENT-17 |

## Shared utilities and data (not powers)

| Element | SoT | Planned location (§51) | Boundary |
|---|---|---|---|
| Evidence Layer | §14, §43.5 | `/services/core/evidence` (core service; includes the principal-scoped read API used by the model service) | Read-only adapters. Trust and Outcome each read it separately. Data minimisation (PLAT-NFR-10). |
| Enterprise (write) adapters | §14 | `/services/core/adapters` (POC: `synthetic_tushe`) | One per registered capability. Only Execution may call them. No adapter exists for a `PROHIBITED` capability (§34.2, BD-08). |
| Vertical Packs | §15 | `/packs` (POC: fintech populated; telecom, insurance and healthcare_admin conformance packs skeletal) | Loaded as **data**, never imported as code. All industry and country terms live here (INV-14, AGENT-04, PLAT-NFR-08). Validated locally by the internal pack checker, `/tools/packcheck` (§15.4). |
| Providers | §17, §35.3 | `/services/model/providers` | Model, speech and TTS behind neutral interfaces. Changing provider is configuration plus a benchmark run (PLAT-NFR-09, BD-16, AGENT-28). |
| Contracts | §43 | `/contracts` (JSON Schemas; not yet written) | One source of truth for every boundary object. Changes need a version bump (AGENT-15, PLAT-NFR-17). |
| Benchmark | §20.2, §38 | `/benchmark` | The oracle is never reachable from runtime credentials (INV-22). |

## Boundary rules (SoT §51, checked in CI)

- The core service's dependency manifest contains no model or speech provider SDK.
- The model service has no database driver configured for the core schemas, and no Temporal client.
- Within the core service, `/trust`, `/execution` and `/outcome` do not import each other's internals and communicate through contracts.
- Packs are loaded as data, never imported as code.
- `/explanation` output is never imported by decision, grant or verdict code.
- No module reaches into another module's internals. Modules communicate through contracts (AGENT-19).

## Where power moves between systems

Power moves only through the four objects in SoT §13.2, plus the confirmation request for `CONFIRM` (§43.2a). Their full definitions are in SoT §43; the value sets are in [`state-registry.md`](state-registry.md).

```
Intent Object ──▶ Trust ──(Decision Grant, ALLOW only)──▶ Execution ──(Execution Receipt)──▶ Outcome
      ▲                                                                                        │
      └──────────── CLARIFY / CONFIRM ◀── Trust ◀── RecoveryRequest (any verdict except ACHIEVED)┘
```

A `CONFIRM` never authorises anything by itself. Only an authenticated acceptance followed by a fresh `ALLOW` evaluation with the same binding hash leads to a grant (§43.2a, INV-25). A new policy version voids unspent grants (INV-26).

## Security boundaries

SoT §47 owns the trust-boundary list, the boundary/control table, the OWASP ASI mapping and the threat table. Read it there; it is not repeated here.

The baseline assumption: **the model can be manipulated, wrong, stale or compromised, and the consequence boundary must still hold** (§47).

## Scope reminders

- **POC vs platform:** the POC builds a thin Mode 1 slice of all four powers and the Record (§35.1 lists what is built and what is deferred). Mode 2 is not built in the POC. Only the Trust interface is kept clean for it (POC-FR-16, AGENT-03).
- **Temporal in the POC:** Temporal runs outcome watches, confirmation expiry, recovery and callback delivery, under the rules in §35.6. Postgres stays the only authoritative store, and single use of a grant is a Postgres constraint, not workflow history (INV-30, OD-07).
- **Not the canonical Noema interface:** separate public Intent, Action, Context, Trust and Execution APIs. The SoT defines:
  - the canonical input contract (PLAT-FR-01);
  - the reconstruction API (PLAT-FR-12);
  - the POC partner listener payloads, including `outcome.updated` (§39, §43.4a);
  - the Mode 2 request–decision–execution contract, which is OD-15 and deferred to Phase 4.
