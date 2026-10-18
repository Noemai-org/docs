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

**The repository mapping is closed.** [DEC-2026-10-13](../decisions/DEC-2026-10-13-code-monorepo.md) decided it (SoT §51, v1.5; [OD-P-13](../open-decisions.md#od-p-13)): all POC code lives in one repository, [`Noemai-org/noema`](https://github.com/Noemai-org/noema), laid out as in the next section. `benchmark-heldout` is separate and private; `docs` and `brain` hold documentation only. [DEC-2026-10-16](../decisions/DEC-2026-10-16-execution-reset.md) (E1) made `Noemai-org` the canonical organisation.

**Module paths are relative to the root of `noema`.** The paths below are the module boundaries named in SoT §51, written with a leading slash (`/services/core/trust` is `services/core/trust/` in the layout below). They show what each module may import. The code is built during the POC; where a module does not yet exist, the path is where it will live, not proof that it does. This repository (`docs`) contains no application code.

## Repositories (DEC-2026-10-13 R1, R5 to R8)

| Repository | What it holds | Rule |
|---|---|---|
| [`Noemai-org/noema`](https://github.com/Noemai-org/noema) | **The only code repository.** Both deployables, `/contracts`, packs, tools, UI, the benchmark harness and the synthetic test-environment components | Layout below (R1). Secrets only in GitHub Environments (R3). Ownership by path (R4) |
| `benchmark-heldout` (private) | The held-out cases and oracles | The one repository boundary that is a real security boundary (R5). Only the benchmark owner and the founders read it. No coding agent and no builder gets a credential for it (REQ-AGT-004, OD-16) |
| [`Noemai-org/docs`](https://github.com/Noemai-org/docs) | Governance: the SoT, the PERD, the plan, decisions, registers, Tushe correspondence | Documentation only; no POC code (R6, OD-P-01) |
| [`Noemai-org/brain`](https://github.com/Noemai-org/brain) | Founder knowledge outside the build: strategy, research, partner context and notes | Not part of the chain of authority; agents do not read or cite it for build work (R7, confirmed by DEC-2026-10-16 E8) |

`backend` and `intent-engine` are archived in the retired organisation and are not recreated; no skeleton of them exists (R8).

### The layout of `noema` (DEC-2026-10-13 R1)

```
noema/
  AGENTS.md, CLAUDE.md        copied from docs; each states the docs commit it was copied from
  .github/CODEOWNERS
  .github/workflows/          one workflow per area, each filtered by path
  Makefile                    the only build orchestration (no Bazel, Nx or Pants)
  contracts/                  JSON Schemas, fixtures, errors.v1.json, codegen config
  services/core/              Go: go.mod; cmd/core, edge, orchestrator, trust, execution,
                              outcome, record, evidence, adapters/synthetic_tushe, workflows,
                              platform, migrations, internal/contracts (generated, committed)
  services/model/             Python 3.13: pyproject.toml; understanding, explanation, voice,
                              providers/{llm,speech}, platform, contracts (generated, committed), tests
  packs/                      fintech; telecom, insurance, healthcare_admin (conformance)
  tools/lint/, tools/packcheck/, tools/codegen/
  ui/                         overlay, inspector, bench (package.json)
  benchmark/                  generator, cases, fixtures, fault_plans, runner, oracle_client,
                              scoring, arms, evil_provider, hostility_proxy, partner_listener, reports
                              (never the held-out set)
  synthetic/mock_case/        the synthetic case service (DEC-2026-10-12, REQ-ENV-008)
  deploy/compose/             docker-compose.yml, profiles (dev, ci, bench, demo), network policy
  docs/                       as-built documentation and session files (AGENTS.md section 9)
```

`/contracts` is the single source. Generated Go and Python types are committed inside each service, and CI fails if regenerating them produces any difference. No package is published between services.

## Two deployables (SoT §35.6)

| Deployable | Hosts | May reach | Never reaches |
|---|---|---|---|
| **Model service** (Python) | Understanding, voice pipeline, Explanation, all model and speech provider adapters | Model and speech providers (GPT, Gemini, Claude; Aethex AI, Indigenius, N-ATLAS; BD-16) | The core database, enterprise adapters, Temporal, grant keys (INV-29) |
| **Core service** (Go) | Trust, Execution, Outcome, the Record, the Evidence Layer, enterprise adapters, Temporal workers | Postgres, enterprise adapters, Temporal, grant keys | Any model or speech provider (INV-29, AGENT-05) |

The two talk only over mutual TLS using contracts from `/contracts` (§35.6, §47.1). Temporal orchestrates but is never the authoritative record (INV-30).

These are the only two deployables. The three test-environment components below are not deployables (DEC-2026-10-16 E5).

## Test-environment components (DEC-2026-10-16 E5)

| Component | Path in `noema` | What it is |
|---|---|---|
| `mock-case` | `synthetic/mock_case/` | Emulates the bank's case system (DEC-2026-10-12 D1, REQ-ENV-008); task ENV-08 |
| Hostility proxy | `benchmark/hostility_proxy/` | Injects faults; benchmark and test profiles only; task ENV-09 |
| Webhook relay | `synthetic/webhook_relay/` | Receives Tushe's webhooks from the internet (E6); task ENV-13 |

- They are not Noema deployables. The two deployables stay the Go core and the Python model service (SoT §35.6).
- None of them holds a decision, grant, Record, provider or core-database credential.
- None of them runs in a production profile.
- The relay runs on one small public HTTPS host that runs nothing else and holds only the webhook signing secret. The core pulls verified deliveries from it over an authenticated, outbound connection; nothing on the internet reaches the core. In the benchmark profile that pull runs through the hostility proxy, which never runs on the public host (E6).

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
| Vertical Packs | §15 | `/packs` (POC: fintech populated; telecom, insurance and healthcare_admin conformance packs skeletal) | Loaded as **data**, never imported as code. All industry and country terms live here (INV-14, AGENT-04, PLAT-NFR-08). Validated locally by the internal pack checker, `packcheck` (§15.4; ported to `noema` as `tools/packcheck.py`, with the R1 layout's `tools/packcheck/` as its home). |
| Providers | §17, §35.3 | `/services/model/providers` | Model, speech and TTS behind neutral interfaces. Changing provider is configuration plus a benchmark run (PLAT-NFR-09, BD-16, AGENT-28). |
| Contracts | §43 | `/contracts` (JSON Schemas, written by task CON-01; the golden vectors are already in `noema`) | One source of truth for every boundary object. Changes need a version bump (AGENT-15, PLAT-NFR-17). |
| Benchmark | §20.2, §38 | `/benchmark` (including `benchmark/hostility_proxy/`, a test-environment component) | The oracle is never reachable from runtime credentials (INV-22). The held-out set lives in `benchmark-heldout`, never in `noema`. |

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
