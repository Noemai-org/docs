# Session 2026-11-23 12:00 WAT · OPS-26 (registry hotfix)

## Session summary
- What changed: `docs/engineering/state-registry.md`, the `reason_codes` row lists the core code `NO_RUNNABLE_CAPABILITY`.
- Why: noema#896 (TRU-14, A531) added the code to `contracts/schemas/enums.v1.json` (20 to 21, with a migration note) and to noema's vendored copy of the registry, not to this original. noema `main` went red on `docs-drift` ("contracts/state-registry.md: differs from docs"). The docs original wins, so the original takes the row, as OPS-07 did for the A254 codes and the transaction classification. The row text is identical to noema's copy, so the copy needs no change.
- Risks, and how they are contained: documentation only; the registry follows the contract, it does not define the code (the code is A531's, Interim).
- Tests added: none. Regression cases: none. Debt: none. Conflicts raised: none.
- Lesson candidate (AGENTS §15): a PR that changes a vendored copy must change the docs original in the same change, or `docs-drift` goes red on `main`.

## Pre-work for the next agent
- Exact next step: confirm `docs-drift` is green on noema `main` after this merges.
- Open questions (owner): none.
- Files to read first: `docs/engineering/state-registry.md`.
- Do not touch: docs#221; merged records.
