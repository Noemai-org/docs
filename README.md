# Noema

This repository is Noema's documentation and organisational memory.

**The single source of truth is [`docs/NOEMA_SOURCE_OF_TRUTH.md`](docs/NOEMA_SOURCE_OF_TRUTH.md)** (v1.2, 2 October 2026). It defines:

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
| `docs/archive/` | **Non-authoritative** historical material |
| `AGENTS.md`, `CLAUDE.md` | Operating instructions for coding agents |

The repository is documentation-first. It contains no application code ([OD-P-01](docs/open-decisions.md#od-p-01)).
