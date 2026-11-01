# DEC-2026-10-26 · `fault-controller` and `fixture-loader` are benchmark-only; where the control-plane clients live

| | |
|---|---|
| **Status** | Accepted by the Founders on 26 October 2026 (decisions given in a working session; they count once this record is merged). The Technical Co-Founder confirms by approving the pull request that adds it |
| **Date** | 26 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None. Answers the question raised on noema#67 (where the control-plane logical services live) |
| **Amends** | PERD §34.1 (PERD v1.16) |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the Founders (see the table above)
- Date: 26 October 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: PERD §34.1; cites §34.2, §34.4, §64.2, §65.1, REQ-ENV-002, REQ-ENV-001. No SoT change; the requirement count stays 154
- Migration notes: PERD v1.16 is a new file; v1.15 stays unchanged. The vendored extracts in `noema` (PERD §32.2 and §28.2) name the current PERD file, so `noema` re-points them in the same session (REQ-OPS-005)
- Supersedes: None

---

## 1. The decisions

| | Decision |
|---|---|
| D1 | **`fault-controller` and `fixture-loader` are benchmark-only and never reachable from the core or the model service.** PERD §34.1 says so in a paragraph after the list of the nine logical services; the list and every other section are unchanged. This is the only PERD change |
| D2 | **Their clients live in the benchmark tree, never in the core:** `benchmark/runner/` (fault-controller) and `benchmark/fixtures/` (fixture-loader). Not written into the PERD (§64.2 is unchanged); this record is the authority |
| D3 | **`mock-clock`:** a read-only client in the core's adapters is allowed, and is added only when a slice needs it (PERD §64.2 already lists clock clients). Clock control (`simulate/advance`) stays benchmark-only (§34.4) |

## 2. Rationale and evidence

PERD §34.1 lists nine logical services that "Noema's adapters address", including these two. The same PERD says the control plane is "Benchmark credentials and network only; never reachable by the runtime" (§34.4), puts `fault-controller` on `bench_net`, "Unreachable from core and model" (§65.1), gives the benchmark runner the "Tushe control credential" (the service-identity table in the security section), and lists no `fault-controller` or `fixture-loader` client in the core's `adapters/synthetic_tushe/` (§64.2: "ledger, switch, destination, customer, policy, case, clock clients"). D1 removes the contradiction in favour of the isolation rules (REQ-ENV-002).

## 3. Agent decisions

1. D2 and D3 are recorded here and not in the PERD, because the instruction was to change only §34.1. If the Founders want §64.2 to name `benchmark/runner/` and `benchmark/fixtures/`, that is a further PERD version.
2. I kept the original list of nine services unchanged, so §34.1 still says Noema's adapters "address" nine services; the new paragraph qualifies two of them.

## 4. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted | 26 October 2026 | Working session, summarised here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |

## Amendment 1 · 1 November 2026 · a test-only control client for core tests (OUT-01)

**Status:** Proposed by the Principal System Architect on 1 November 2026, in answer to question Q3 of the [OUT-01 task card](../poc/execution/task-cards/OUT-01.md). It counts once the Founder approves and merges the pull request that adds it (docs#74). Every section above stays as written, except where this amendment changes it.

- **What it allows.** A Go test in the core tree may call `mock-case`'s control listener (`/control/v1/...`) and truth listener (`/truth/v1/...`) with the bench credential, **only** in `_test.go` files, against a `mock-case` that the test itself starts on a throwaway database. The first use is OUT-01's US-06 test, which applies `contracts/fixtures/valid/fault-plan/mock_case_commit_then_drop.json` and counts the cases and create commands for the key from the truth endpoint.
- **What stays as D1 and D2 say.** No non-test file in `services/` holds a control or truth client, the bench credential or a path to either listener; nothing in `services/` imports a package under `benchmark/` or the hostility proxy; `fault-controller` and `fixture-loader` remain benchmark-only, and their clients remain in `benchmark/runner/` and `benchmark/fixtures/`. The runtime is never given the bench credential or network.
- **How it is enforced.** A static test fails if any non-test file under `services/` references a control or truth path, the bench credential or a benchmark or proxy package; the architecture lint passes. Both run in CI on every pull request that touches `services/core/`.
- **Why.** Criterion 7 of OUT-01 requires the real fault fixture, never a mock (AGENT-12), and the case it covers (the target commits, the response is lost) cannot be produced any other way until the public API and the benchmark runner can drive the core end to end. A replay of a recorded exchange does not show one logical case from the truth endpoint.
- **Affected IDs:** REQ-ENV-002, REQ-ENV-008, REQ-VER-001, REQ-RCV-002, AGENT-12, US-06. No SoT or PERD change.
