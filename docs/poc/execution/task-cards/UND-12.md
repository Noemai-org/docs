# Task card: UND-12

Plan v1.10 task UND-12 (added by [DEC-2026-10-31-proof-depth-and-completeness](../../../decisions/DEC-2026-10-31-proof-depth-and-completeness.md) D24; dated TBC). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Repository: `noema` (the card lives in `docs`). Drafted 1 Nov 2026 by the Core Engineer 2 role agent, on the Principal System Architect's instruction of 1 Nov 2026 (the proving test plus a bounded worker pool that fails fast on saturation, never an unbounded queue). The owner's questions were answered by the Principal System Architect on 1 Nov 2026 ("Decisions" below). **Status: DRAFT until the Founder approves and merges it. No code starts before then.**

```
TASK-P5-002  UND-12 · Async safety of the model service's blocking HTTP transports: prove a provider call never runs on the event loop; run blocking calls on a bounded worker pool that fails fast when full
Priority: P1
Requirement IDs: REQ-TST-010, REQ-NFR-002; SoT IDs: INV-16, POC-NFR-03 (cited by REQ-NFR-002; REQ-TST-010 cites no SoT ID)
Rationale: Explicit errors, context and deadlines, and async safety must be verified in code, not assumed. [REQ-TST-010]
Modules touched (allowlist; paths in `noema`):
  services/model/noema_model/providers/llm/transport.py
  services/model/noema_model/evidence/transport.py      (the same blocking pattern; see "Scope note")
  services/model/noema_model/platform/                  (one new module for the shared bounded pool, if both transports use it)
  services/model/tests/test_transport.py, services/model/tests/test_evidence_client.py, services/model/tests/test_transport_async_safety.py (new)
  services/model/README.md (or the README of the touched module)
  status/roles/core-engineer-2.md
  ← nothing else may change. contracts/ is read-only. No new dependency (AGENT-14): the standard library's concurrent.futures and asyncio only.
Contracts: none; bump required? N
Inputs/outputs: unchanged. `post(url, headers, body, timeout_s, max_bytes)` → HttpResponse, or ProviderError / CandidateSourceError. A saturated pool is a new failure path that maps to an existing failure kind (see Q2)
Acceptance criteria:
  REQ-TST-010:
  - (the REQ states no SHALL; its requirement is copied) CI enforces, for Python: `mypy --strict` and Ruff (pinned) including its `ASYNC` rules.
  REQ-NFR-002:
  - (fail closed) a saturated pool refuses the call at once with a typed failure; it never queues, blocks or waits for a slot
  Task "Done when" (plan v1.10): A test proves the event loop is never blocked by a provider call
  Architect's criteria (1 Nov 2026), restated as tests:
  1. `_post_blocking` never runs on the event loop thread (both transports).
  2. Blocking calls run on a bounded worker pool owned by the transport, not on asyncio's shared default executor.
  3. When every worker is busy, a new call fails fast with a typed failure; there is no unbounded queue, and no call waits for a slot.
Tests to write FIRST (AGENT-11):
  - loop thread: `_post_blocking` records the thread it runs on; the test asserts it is never the event loop's thread, for both transports
  - loop responsiveness: against a real loopback HTTP server that holds the response for longer than the call's timeout, a ticker coroutine on the same loop keeps ticking on schedule while N calls are in flight (the loop's lag stays below a bound stated in the test), and each call ends in TIMEOUT
  - saturation: with the pool full of held calls, call N+1 fails at once with the saturation failure (Q2) and is never sent (the loopback server counts requests); after the held calls finish, a new call succeeds. The test sets a small pool size through configuration; it does not depend on the defaults
  - configuration: each transport reads its own pool size; with no value set, the model transport uses 16 and the evidence transport 8; a size below 1 is refused at start-up
  - slot accounting: a call that times out on the asyncio side keeps its slot until its worker thread actually returns (a thread cannot be cancelled), so saturation is reported honestly; the slot is then released, also when `_post_blocking` raises
  - no leak: the saturation failure and every new error message carry no header, body or credential (extends test_transport_header_leak.py; INV-29, AGENT-13)
  - static: no call to asyncio.to_thread or loop.run_in_executor(None, ...) remains in either transport
Faults to exercise (AGENT-12): a slow and a non-answering loopback server, real sockets (the existing test style of test_transport.py); the hostility proxy's near-timeout fault once it is reachable from the model service's tests. Never a mocked socket.
Dependencies: none (plan v1.10); UND-02 (the transport exists, merged)
Out of scope:
  - tuning the pool sizes beyond the initial defaults of Q1, or changing any timeout, retry budget or provider default (REQ-AGT-005, AGENT-16, AGENT-28)
  - provider failover logic (UND-08), rate limiting, circuit breakers (CAP-01), REQ-CAP-005 concurrency caps on enterprise targets (Execution and the Evidence Layer in core)
  - adding Ruff or golangci-lint to CI (PLT-09); this code is written to pass them
  - any change to the request, response or error shapes other than the saturation failure
Definition of done: tests green; boundary/lint green; Record events asserted (none: the model service writes no Record events); docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: C2 (a founder) with the Core Engineer 2 role agent. Needs: none. Gate: none named.

## What was checked on 1 Nov 2026 (read-only, `noema` main)

- `providers/llm/transport.py:80` and `evidence/transport.py:88` both run `_post_blocking` through `asyncio.to_thread`, so it does not run on the event loop today. No test proves it, and the plan's "done when" asks for that test.
- **The risk the pool removes:** `asyncio.wait_for` cancels the coroutine, not the worker thread, so a timed-out call keeps its thread until the socket gives up. `urllib`'s `timeout` applies to each socket operation, not to the whole call, so a slow-dripping server can hold a thread for longer than `timeout_s`. `asyncio.to_thread` uses the loop's shared default executor, which is bounded but queues without limit. Enough hung provider calls would therefore delay every later blocking call in the service, including the evidence calls, behind them, silently and without a typed failure. They would not block the event loop itself.

## Decisions (Principal System Architect, 1 Nov 2026)

Given in the session of 1 Nov 2026 and recorded here; they count once the Founder approves and merges this card (AGENTS.md §2 item 3).

| # | Question | Decision |
|---|---|---|
| Q1 | Pool size | **A configuration value per transport.** Initial defaults: **model-provider transport 16, evidence transport 8**. They are starting values, to be tuned later from measured load; the agent does not change them (REQ-AGT-005). The values in effect are written to the service's start-up log |
| Q2 | The failure when the pool is full | **As recommended.** Model-provider transport: `ProviderError(UNAVAILABLE)`, so UND-08 fails over to the next provider (BD-16). Evidence transport: `CandidateSourceError`, which the Evidence Layer reports as UNAVAILABLE (INV-19). No new enum value and no contract change |
| Scope | Include the evidence transport? | **Yes.** Both transports are in scope |

## Scope note

The evidence transport (`evidence/transport.py`) is the model service's client of the core's candidate API, not a model provider. It has the same `_post_blocking` code and the same risk, and the plan's "done when" speaks of "a provider call" only. Both transports share the loop, and the Architect's decision of 1 Nov 2026 puts both in scope.
