# Noema

This repository is Noema's documentation and organisational memory.

**The single source of truth is [`docs/NOEMA_SOURCE_OF_TRUTH.md`](docs/NOEMA_SOURCE_OF_TRUTH.md)** (v1.6, 16 October 2026). It defines:

- what Noema is and is not;
- what we are building first, and why;
- the architecture, requirements, invariants and open decisions.

When anything else disagrees with it, the SoT wins until it is formally revised.

This README intentionally does not restate the definition of Noema. Read SoT §1 (one sentence), §0.1 (five distinctions you must hold) and §12 (what Noema is and is not).

## Start here

| You are… | Read |
|---|---|
| New to Noema | SoT "How to use this document", §0.1 and §1, then [`docs/README.md`](docs/README.md) |
| An engineer | [`docs/README.md`](docs/README.md) → SoT Parts III, VII, IX → [`docs/poc/README.md`](docs/poc/README.md) |
| An AI coding agent | [`AGENTS.md`](AGENTS.md) first |

## What is in this repository

| Path | Status |
|---|---|
| `docs/NOEMA_SOURCE_OF_TRUTH.md` | **Canonical** |
| `docs/` (other files) | Derived indexes, registers and checklists. Non-normative. |
| `docs/poc/tushe/` | Issued Tushe environment specification (v1.0, frozen) and its original export |
| `docs/poc/perd/` | **POC build specification**: the [POC PERD](docs/poc/perd/README.md) v1.5 (applies [DEC-2026-10-16](docs/decisions/DEC-2026-10-16-execution-reset.md); earlier versions kept). Status: Accepted ([DEC-2026-10-11-poc-perd-v1.1](docs/decisions/DEC-2026-10-11-poc-perd-v1.1.md), re-pointed by [DEC-2026-10-16](docs/decisions/DEC-2026-10-16-execution-reset.md)). Ranks below the SoT. |
| `docs/poc/execution/` | **POC execution plan**: the [four-week implementation plan](docs/poc/execution/README.md) v1.5 (19 Oct to 13 Nov 2026, re-baselined by DEC-2026-10-16) and its task index. Status: Accepted ([DEC-2026-10-11-poc-4week-plan](docs/decisions/DEC-2026-10-11-poc-4week-plan.md), re-pointed by [DEC-2026-10-16](docs/decisions/DEC-2026-10-16-execution-reset.md)). Ranks below the SoT and the PERD. |
| `docs/security/`, `docs/runbooks/` | Threat model, trust-boundary and threat-to-test maps (from the PERD, Proposed); runbook scaffolds (no steps yet) |
| `docs/archive/` | **Non-authoritative** historical material |
| `tools/`, `.github/` | The `docs-consistency` check (`tools/check_docs_consistency.py`), the PERD and plan index checks (`tools/perd_index.py`, `tools/plan_index.py`), frozen-file hashes, CI workflow, PR template and code owners |
| `AGENTS.md`, `CLAUDE.md` | Operating instructions for coding agents |

The repository is documentation-first. It contains no application code ([OD-P-01](docs/open-decisions.md#od-p-01)).

## The repositories

Noema uses four repositories (SoT §51; [DEC-2026-10-13](docs/decisions/DEC-2026-10-13-code-monorepo.md)):

| Repository | Job | Change |
|---|---|---|
| `docs` | Governing documents: SoT, PERD, plan, decisions, Tushe correspondence | None |
| **`noema`** (new) | All POC code | Created |
| **`benchmark-heldout`** (new, private) | Held-out cases and oracles. Benchmark owner only; no agent access | Created, if GOV-03 has not already created it |
| `brain` | Founder documentation outside the build. Not part of the build's chain of authority | None. Its purpose is now recorded |
| `backend`, `intent-engine` | Superseded by `noema` | Archived read-only, after any code built under the current architecture is moved into `noema` with its history |

