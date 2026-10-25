# DEC-2026-10-25 · ENV-03 starts, the Go Postgres driver and Temporal SDK are approved, the mock-case secret names, CODEOWNERS for `.gitleaksignore`

| | |
|---|---|
| **Status** | Accepted by the requesting Founder on 25 October 2026 (instructions given in a working session, in the words summarised in §1; they count once this record is merged). The other Founder confirms by approving the pull request that adds it |
| **Date** | 25 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None. Answers the AGENT-14 approval the Go core's Postgres driver and Temporal SDK needed |
| **Amends** | None. No SoT, PERD or plan text changes |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the requesting Founder (see the table above)
- Date: 25 October 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: REQ-ENV-001, REQ-NFR-006, REQ-EXE-007, REQ-ENV-002 (ENV-03); AGENT-14 (dependencies); PERD §36.1 (stack), §34.4. No requirement is added or changed
- Migration notes: none. The first code that adds a dependency cites this record and passes `check_pins`
- Supersedes: None

---

## 1. The decisions

| | Decision |
|---|---|
| D1 | **ENV-03 starts.** The Go adapter interfaces are built in slices. Only the slice that needs no Tushe behaviour is built now: the interface and client of `mock-case` (noema#67). |
| D2 | **The Go Postgres driver is approved** under AGENT-14 for the core service (PERD §36.1: Postgres is the only authoritative store). |
| D3 | **The Temporal SDK is approved** under AGENT-14 for the core service (PERD §36.1: Temporal is the durable workflow engine, never authoritative, INV-30). |
| D4 | **The first end-to-end case is approved:** G2 escalate (`fin.cap.create_escalation_case`) against `mock-case`. |
| D5 | **The secret names for the two `mock-case` listeners are approved**, names only, file-mounted (OD-P-22): `MOCK_CASE_RUNTIME_TOKEN_FILE` (the core's case adapter) and `MOCK_CASE_BENCH_TOKEN_FILE` (the benchmark runner only; the core never holds it, REQ-ENV-002). |
| D6 | **CODEOWNERS covers `/.gitleaksignore`** with both founders, like the other protected paths. |
| D7 | **No further gitleaks allowlist entries** are added. The one entry approved on 24 October 2026 (docs#58, finding 1) stands. |
| D8 | **Tushe-dependent work is paused** until the Founder confirms: the webhook-relay pull client, the Tushe entries in `.env.example`, and the interfaces and clients of the Tushe-hosted logical services. |
| D9 | **The `contracts/fixtures/README.md` line about `secret_hex`** (a public test vector, never a real key) is added only after the Founder confirms in writing, on a pull request, that `secret_hex` is test-only. That confirmation is not yet given. |

## 2. Rationale and evidence

**D2, D3.** The core's Postgres ledger and Temporal workers are the missing half of the spend-and-dispatch controller (PERD §27.1; the controller was built against ports and a simulation) and of the first end-to-end case. PERD §36.1 fixes Postgres and Temporal as the stack; AGENT-14 requires approval for the dependency that connects to them. `synthetic/mock_case` already uses `pgx` v5 in its own module; no core module has a driver or SDK yet.

**D5.** The names are the ones `mock-case` already reads (`synthetic/mock_case/internal/config/config.go`: `MOCK_CASE_RUNTIME_TOKEN_FILE`, `MOCK_CASE_BENCH_TOKEN_FILE`). Its database password file names are not part of this approval.

**D6.** `.gitleaksignore` is scanner configuration. `/.github/` is already protected; the root file was not (docs#58).

**D8.** PERD §34.4 fixes the Tushe payload field names only when the Tushe OpenAPI is frozen (Phase A exit); a stop condition in AGENTS §14 forbids relying on a Tushe behaviour that has not been shown.

## 3. Agent decisions (defaults for the Founders to confirm or change)

1. D2 and D3 name the capability, not a library or version. My default is `github.com/jackc/pgx/v5` (already used by `mock-case`) and `go.temporal.io/sdk`, each pinned at its first use under `check_pins`, in its own pull request, citing this record. A different choice replaces this default.
2. "Approved" is read as permission to add the dependency in a later task pull request, not as permission to add it unpinned or inside an unrelated change.
3. D1 is read as slices: the Tushe-hosted interfaces and `mock-clock`, `fault-controller` and `fixture-loader` wait. The last three are benchmark-only and "never reachable by the runtime" (PERD §34.4); where they live needs its own decision.
4. D5 covers the two names above only. No Tushe secret name is added (D8).

## 4. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted by the requesting Founder (one Founder) | 25 October 2026 | Instructions in a working session, summarised here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
