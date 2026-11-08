# Tushe specification delta v1.3 (DRAFT, internal, not sent)

Date: 5 November 2026 · Status: **draft for the Founders. Not sent to Tushe and not acceptance.** Written by the Repo Steward at the Architect's order (DEC-2026-11-05-architect-rulings D6). Sending is for the Founders. It follows [`tushe-spec-delta-v1.2.md`](tushe-spec-delta-v1.2.md), which is left unchanged.

## Proposed request

| # | Request | Date |
|---|---|---|
| R14 | **Account state and balance as a read surface.** A read of an account's state and balance on Noema's tenants, with the same history and fault-injection behaviour as the other read surfaces (R2), so a postcondition on account state or balance can be declared. Today no source covers them (DEBT-12) | To be set by the Founders |

## Why

The `lookup_account` postcondition is ownership-only and `core_ledger` is authoritative only for `debit_posted_or_reversed`. Without this surface Noema declares no balance or state postcondition.
