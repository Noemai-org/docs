# Trust-boundary map (POC)

All content below is copied verbatim from [`../poc/perd/NOEMA_POC_PERD_v1.1.md`](../poc/perd/NOEMA_POC_PERD_v1.1.md) and is **Proposed** with the PERD ([DEC-2026-10-11-poc-perd-v1.1](../decisions/DEC-2026-10-11-poc-perd-v1.1.md)). The [SoT](../NOEMA_SOURCE_OF_TRUTH.md) governs: §35.6 (two deployables), §45 (INV-29, INV-30), §47 (security boundaries).

## Shape (PERD §18.1, lines 651–683)

**Two deployables split at the model boundary** [SoT §35.6, OD-11, INV-29]. Inside the core service, the four powers are packages with import rules, not services [SoT §45.1].

```
            Partner app (overlay, React/TS)                 Partner callback listener
            text ─┐            voice (audio stream)             ▲  signed events:
                  │                    │                        │  confirmation.recorded
                  ▼                    ▼                        │  case.created · outcome.updated
 ┌───────────────────────────┐   ┌────────────────────────────────────────────────────────┐
 │ CORE SERVICE (Go)         │   │ MODEL SERVICE (Python 3.13 · FastAPI · Pydantic v2)    │
 │                           │   │  stateless · no DB · no Temporal · no grant keys       │
 │ edge/   session authn,    │──▶│  understanding/  Input Gateway → Intent Compiler →     │
 │         rate limit, ids   │◀──│                  schema gate → Entity Resolution       │
 │                           │   │  explanation/    facts in → text out (nothing else)    │
 │ trust/  reconcile,        │   │  voice/          streaming ASR / TTS pipeline          │
 │   authority, policy,      │   │  providers/      GPT · Gemini · Claude                 │
 │   clocks, decisions,      │   │                  Aethex AI · Indigenius · N-ATLAS      │
 │   grants, confirmations   │   └───────────────▲────────────────────────────────────────┘
 │ execution/ planner,       │                   │ mTLS, /contracts only
 │   registry, controller,   │   principal-scoped│ candidate reads (Evidence API)
 │   recovery                │◀──────────────────┘
 │ outcome/  verifier, watch │
 │ record/   hash chain,     │      ┌──────────────────────┐   ┌─────────────────────────┐
 │   reconstruction, memory  │─────▶│ PostgreSQL (only     │   │ Temporal (self-hosted;   │
 │ evidence/ Evidence Layer  │      │ authoritative store) │   │ own persistence DB;      │
 │ adapters/ synthetic_tushe │      │ + transactional      │   │ never authoritative)     │
 │ workflows/ Temporal       │─────▶│   outbox             │   └─────────────────────────┘
 └────────────┬──────────────┘      └──────────────────────┘
              │ integration credential (reads + non-monetary case ops only)
              ▼
 ┌─────────────────────────────────────────────────────────────────────────────────────────┐
 │ TUSHE synthetic enterprise: mock-ledger · mock-switch · mock-destination · mock-customer│
 │ mock-policy · mock-case · mock-clock · fault-controller · fixture-loader               │
 │ Ground-truth oracle ── reachable ONLY by benchmark credentials, never by runtime        │
 └─────────────────────────────────────────────────────────────────────────────────────────┘
```

## Trust boundaries crossed by a request (PERD §18.4, lines 722–733)

| # | Boundary | Control | REQ |
|---|---|---|---|
| 1 | Client → core edge | Session token verified by core; principal from the enterprise IdP assertion only | REQ-INP-002, REQ-SEC-001 |
| 2 | Core → model service | mTLS with service identities; contracts only; no credentials passed | REQ-SEC-002 |
| 3 | Model → core Evidence API | mTLS; principal-scoped; candidate-shaped data only, masked | REQ-AMB-002 |
| 4 | Intent Object → Trust | Schema gate re-run in core; unknown fields rejected; status VALIDATED; principal re-bound from the session | REQ-INT-001 |
| 5 | Trust → Execution | Decision Grant (HMAC, single use, bound) | REQ-TRU-008, REQ-EXE-001 |
| 6 | Execution → Tushe | Integration credential (non-monetary); conditional writes; idempotency key | REQ-EXE-002..004 |
| 7 | Tushe output → Noema | Evidence only; schema-validated; untrusted strings delimited | REQ-CTX-007 |
| 8 | Outcome → Record | Append-only role | REQ-AUD-003 |
| 9 | Core → partner | Signed callbacks; at-least-once delivery; `event_id` deduplication | REQ-API-006 |
| 10 | Benchmark → oracle | Separate credential; unreachable from runtime | REQ-ENV-002 |

## Identities and credentials (PERD §41.1, lines 3871–3882)

| Identity | Holds | Can reach | Cannot reach |
|---|---|---|---|
| `core-edge` | TLS certificate; session verification key (the IdP's public key) | Core internal packages | Providers |
| `core-trust` (DB role `trust_rw`) | Grant HMAC key (read from the secrets manager at start-up and kept in memory) | Postgres (trust tables); Evidence API | Providers; Tushe write APIs |
| `core-execution` (`execution_rw`) | Grant verification key; Tushe write credential (non-monetary) | Tushe case APIs | Providers; decision tables (write) |
| `core-outcome` (`outcome_rw`) | Tushe read credential | Tushe read APIs | Tushe write APIs |
| `core-record` (`record_append`) | — | Record tables (INSERT only) | — |
| `core-evidence` | Tushe read credential (principal-scoped calls) | Tushe read APIs | Writes |
| `core-workflows` | Temporal client credential | Temporal; core activities | Providers |
| `model-service` | Provider API keys; mTLS client certificate | Providers; three core internal endpoints | Postgres, Temporal, Tushe, grant keys (INV-29) |
| `benchmark-runner` | Oracle credential; Tushe control credential; benchmark DB | Oracle; fault controller; clock | Runtime DB write roles |
| `admin` (control plane) | Policy publish; pack load; kill switch; key rotation | Admin APIs | The data plane except through admin APIs |

**[REC] Identity granularity in the POC.** Postgres roles are split per power as shown. At the network and certificate level, core runs as one service identity, because it is one deployable. Per-power OS-level identities would mean splitting processes, which the SoT does not require for the POC. See SOT-C-16.

## Hosted Tushe sandbox and credentials (DEC-2026-10-12)

Added 12 Oct 2026 from [DEC-2026-10-12](../decisions/DEC-2026-10-12-tushe-environment-scope.md) (D1, D2, D6) and PERD v1.2 §34.2. The sections above are copied from PERD v1.1 and are unchanged.

**Additional boundary.**

| Boundary | Control | REQ |
|---|---|---|
| Noema ↔ hosted Tushe sandbox (internet, egress allowlist, read-only key) | The runtime API key reads only, in test mode; core egress is allowlisted to the Tushe API host; Tushe `/partner/...` routes refuse runtime identities | REQ-ENV-002 |
| Internet (Tushe) → Noema public webhook receiver (DEC-2026-10-12, Amendment 1) | HTTPS only, signature and timestamp verified, proxy in front, writes only to the inbox. Hosting decided by GOV-20 (PERD OQ-15) | REQ-API-008, REQ-SEC-002 |
| CI (GitHub Actions) | Per-service GitHub Environments; no repository-level secrets (DEC-2026-10-13 R3) | REQ-SEC-005 |

**Credentials (DEC-2026-10-12, D6).**

| Credential | Scope | Held by | Network |
|---|---|---|---|
| Runtime API key | Tushe **reads only**, test mode | Core service | Egress allowlisted to the Tushe API host only |
| Fixture key | Test-mode payout creation, to build transaction histories for scenarios | Benchmark owner; fixture loader only | Benchmark network only |
| Administrator credential | Read-only partner-administrator surface | Benchmark owner; benchmark runner only | Benchmark network only |
| `mock-case` write | Non-monetary case operations | Core service, through its adapter | Internal |
| `mock-case` truth | Read of the case service's true state | Benchmark runner only | Benchmark network only |
