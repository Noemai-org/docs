# Pre-POC contract and pack drafts (archived 16 October 2026)

> **Nothing in this directory is authoritative.** It is kept so that the reasoning behind earlier work is not lost.
>
> - Do not implement, cite or quote from it as current guidance.
> - The only authority is [`../../NOEMA_SOURCE_OF_TRUTH.md`](../../NOEMA_SOURCE_OF_TRUTH.md) (the SoT), then the order of authority in SoT §0.4.
> - It does not inform any build. `CON-01` builds the JSON Schemas in `noema` from the SoT and the PERD, failing test first.

Archived by [DEC-2026-10-16](../../decisions/DEC-2026-10-16-execution-reset.md) E7. `docs` holds no `contracts/`, `packs/` or product code.

## What is here

| File | What it is |
|---|---|
| [`schema.yaml`](schema.yaml) | The draft OpenAPI source of truth for the core boundaries (first committed 8 Oct 2026). This is the version at commit `ce8897e` of the retired organisation (15 Oct 2026), so it includes the 15 Oct additions: `additionalProperties: false` on `IntentObject`, and the optional `principal_id`, `tenant_id` and `intent_hash` fields. It is a byte copy of that file |
| [`fixtures/intent_valid.json`](fixtures/intent_valid.json) | The one draft fixture for it, unchanged |

## Where it disagrees with the SoT

These are the mismatches that kept the draft out of the build (DEC-2026-10-16 E7).

| Draft | SoT and PERD |
|---|---|
| `FactStatus` has `CONFLICTED`, `VERIFIED` and `UNVERIFIED` | Statuses are KNOWN, INFERRED, AMBIGUOUS, UNAVAILABLE, STALE, CONTRADICTORY, UNKNOWN and UNAUTHORIZED (SoT §14, "State Reconciliation", and the Appendix A glossary). The draft lacks `CONTRADICTORY`, `AMBIGUOUS` and `UNAVAILABLE`, and adds three values the SoT does not define |
| `TrustReasonCode` includes `NONE` | The SoT has no reason code `NONE` |
| `DecisionGrant` has only `grant_id`, `intent_id`, `intent_version`, `outcome`, `reason_code` and `layer_results` | A grant is bound to the authenticated principal, the intent hash, one capability, one resolved target, one parameter hash, the evidence-set hash, the plan hash and step, the policy version, an expiry and a single-use nonce (SoT §13 and §43.2) |
| OpenAPI 3.0.3 with a placeholder path `/dummy` | The POC contracts are JSON Schemas in `/contracts` with generated Pydantic and Go types (PERD §36.1), not an OpenAPI document |
| `fixtures/intent_valid.json` uses `fact_statuses` of `VERIFIED` and `KNOWN`, an `id` of `intent-123` and a free `parameters` object | None of these is the SoT §43.1 Intent Object |

## What moved to `noema`

The golden vectors, the fintech and conformance packs, the eight bad-pack fixtures and `packcheck` were delivered on 14 and 15 Oct 2026 as commits `fd16980` and `ce8897e` in the retired organisation's `docs` repository, without review. They are ported to the `noema` repository by [PR N1](https://github.com/Noemai-org/noema/pull/1) (DEC-2026-10-16 E12):

| Was in `docs` | Now in `noema` (PR N1) |
|---|---|
| `contracts/fixtures/golden_vectors.json` | `contracts/fixtures/golden_vectors.json` |
| `packs/fintech_v1.json` (the 8 Oct version was removed from `docs`; the 15 Oct version is the one ported) | `packs/fintech_v1.json` |
| `packs/conformance/*.json` | `packs/conformance/*.json` |
| `packs/fixtures/bad_packs/*.json` | `packs/fixtures/bad_packs/*.json` |
| `tools/packcheck.py` | `tools/packcheck.py` |
