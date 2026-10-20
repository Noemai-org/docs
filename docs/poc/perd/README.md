# POC PERD (Product & Engineering Requirements Document)

> **Status: Accepted** ([DEC-2026-10-11-poc-perd-v1.1](../../decisions/DEC-2026-10-11-poc-perd-v1.1.md), re-pointed to the current PERD by [DEC-2026-10-16](../../decisions/DEC-2026-10-16-execution-reset.md) E11). The PERD is the POC's detailed engineering specification (SoT §0.4, item 4). It **ranks below the [SoT](../../NOEMA_SOURCE_OF_TRUTH.md)**: where they disagree, the SoT wins (PERD P.1).

| File | What it is |
|---|---|
| [`NOEMA_POC_PERD_v1.11.md`](NOEMA_POC_PERD_v1.11.md) | **Current.** The PERD, v1.11 (20 October 2026; 153 requirements): v1.10 with the changes of [DEC-2026-10-20 architecture-depth](../../decisions/DEC-2026-10-20-architecture-depth.md) (the §64.2 depth with `harness/`, `understanding/pipeline/` and `internal/predicate/`; clarification by attribute; the composed recipient matcher; signed Record checkpoints and replay; the spend-and-dispatch acceptance; Temporal write activities at most once; decision models behind `harness.decide()`), listed in its "Changes in v1.11". |
| [`NOEMA_POC_PERD_v1.10.md`](NOEMA_POC_PERD_v1.10.md) | The PERD, v1.10 (20 October 2026; 153 requirements): v1.9 with one tag correction under [DEC-2026-10-17 open-decisions-closure](../../decisions/DEC-2026-10-17-open-decisions-closure.md) (its correction note of 20 October 2026; no new decision record): the §38.3 table "Retention and data-handling defaults" is retagged from [REC] to [ADOPTED DEC-2026-10-17], values unchanged, listed in its "Changes in v1.10". Superseded by v1.11; kept unchanged. Do not edit it. |
| [`NOEMA_POC_PERD_v1.9.md`](NOEMA_POC_PERD_v1.9.md) | The PERD, v1.9 (18 October 2026; 153 requirements): v1.8 with the changes of [DEC-2026-10-18 con01-gap-closure](../../decisions/DEC-2026-10-18-con01-gap-closure.md) (ALLOW needs three PASS layers, the recovery request for a voided grant, the clarification answer, retryable errors, four Record event types in §32.2), listed in its "Changes in v1.9". Superseded by v1.10; kept unchanged. Do not edit it. |
| [`NOEMA_POC_PERD_v1.8.md`](NOEMA_POC_PERD_v1.8.md) | The PERD, v1.8 (17 October 2026; 153 requirements): v1.7 with the changes of [DEC-2026-10-17 open-decisions-closure](../../decisions/DEC-2026-10-17-open-decisions-closure.md) (the §67.3 defaults adopted and tagged [ADOPTED DEC-2026-10-17], §67.1 and §67.2 marked, the §37.1 clock note, the reason-code block moved to §23.3), listed in its "Changes in v1.8". Superseded by v1.9; kept unchanged. Do not edit it. |
| [`NOEMA_POC_PERD_v1.7.md`](NOEMA_POC_PERD_v1.7.md) | The PERD, v1.7 (16 October 2026; 153 requirements): v1.6 with the changes of [DEC-2026-10-16 money-and-value-lists](../../decisions/DEC-2026-10-16-money-and-value-lists.md) (integer minor units for money, the Intent Object `status` and `REJECTED_AT_GATE`, the authority results, the two-tier reason codes, the case reason), listed in its "Changes in v1.7". Superseded by v1.8; kept unchanged. Do not edit it. |
| [`NOEMA_POC_PERD_v1.6.md`](NOEMA_POC_PERD_v1.6.md) | The PERD, v1.6 (16 October 2026; 153 requirements): v1.5 with the changes of [DEC-2026-10-16 contract-and-pack-clarifications](../../decisions/DEC-2026-10-16-contract-and-pack-clarifications.md) (the `evidence_set_hash` construction and golden vectors, the two-node intent model), listed in its "Changes in v1.6". Superseded by v1.7; kept unchanged. Do not edit it. |
| [`NOEMA_POC_PERD_v1.5.md`](NOEMA_POC_PERD_v1.5.md) | The PERD, v1.5 (16 October 2026; 153 requirements): v1.4 with the changes of [DEC-2026-10-16](../../decisions/DEC-2026-10-16-execution-reset.md) (G0 in two halves, per-object time in AT-15 and TEN-05, the test-environment components, the webhook relay), listed in its "Changes in v1.5". Superseded by v1.6; kept unchanged. Do not edit it. |
| [`NOEMA_POC_PERD_v1.4.md`](NOEMA_POC_PERD_v1.4.md) | The PERD, v1.4 (13 October 2026): v1.3 with the changes of [DEC-2026-10-13](../../decisions/DEC-2026-10-13-code-monorepo.md) (one code repository, `noema`), listed in its "Changes in v1.4". Superseded by v1.5; kept unchanged. Do not edit it. |
| [`NOEMA_POC_PERD_v1.3.md`](NOEMA_POC_PERD_v1.3.md) | The PERD, v1.3 (13 October 2026): v1.2 with the changes of [DEC-2026-10-12](../../decisions/DEC-2026-10-12-tushe-environment-scope.md) Amendment 1 (the joint G0 session on Fri 16 Oct, webhooks kept active, OQ-15), listed in its "Changes in v1.3". Superseded by v1.4; kept unchanged. Do not edit it. |
| [`NOEMA_POC_PERD_v1.2.md`](NOEMA_POC_PERD_v1.2.md) | The PERD, v1.2 (12 October 2026): v1.1 with the changes of [DEC-2026-10-12](../../decisions/DEC-2026-10-12-tushe-environment-scope.md) (how the POC uses Tushe), listed in its "Changes in v1.2". Superseded by v1.3; kept unchanged. Do not edit it. |
| [`NOEMA_POC_PERD_v1.1.md`](NOEMA_POC_PERD_v1.1.md) | The PERD, v1.1, committed byte-for-byte as issued. Superseded by v1.2; kept unchanged. Do not edit it. |
| [`requirements-index.csv`](requirements-index.csv) | Generated index of every `REQ-` ID. Run `python3 tools/perd_index.py --write`; CI runs `--check`. Never edit by hand. |
| [`conflicts-register.md`](conflicts-register.md) | PERD §72 conflicts (SOT-C-01 to SOT-C-31) with their status. |
| [`templates/`](templates/) | Task card, conflict block and benchmark-case templates. |

The dated build plan that turns this PERD into tasks is the [POC execution plan](../execution/README.md) (Accepted).

## How to read it

Start with the reading path for your role in PERD **P.4** (founders, engineers, AI coding agents, benchmark owner, security reviewer). Every material statement carries a label (PERD P.2):

- **`[SoT §x]`**: a Source of Truth fact; binding.
- **`[INF]`**: an inference from the SoT; binding only through the SoT text it reads.
- **`[REC]`**: a recommended default; not binding until adopted (PERD §67).
- **`[ASM]`**: an assumption, with an owner and a check in PERD §67.
- **`[OQ]`**: an open question, with a minimum default to use meanwhile.

## Rules for coding agents

1. Cite at least one PERD `REQ-` ID **and** the SoT IDs that REQ cites (REQ-AGT-001, AGENT-01). Look them up in [`requirements-index.csv`](requirements-index.csv).
2. Work from a [task card](templates/task-card.md) (PERD §61.4). Touch only the modules on its allowlist (REQ-AGT-002).
3. On any conflict between the PERD, the SoT and the implementation: **stop** and put a [conflict block](templates/conflict-block.md) in the PR (REQ-AGT-003, AGENT-27). Check [`conflicts-register.md`](conflicts-register.md) first.

## Changing the PERD

One pull request (AGENT-29) that contains:

- a new version file `NOEMA_POC_PERD_v<x.y>.md` (the old version is kept, never edited);
- a decision record in [`docs/decisions/`](../../decisions/README.md);
- the regenerated `requirements-index.csv`;
- the updated statuses in `conflicts-register.md`.

## Where open items live

PERD §67 (open questions OQ-01 to OQ-15 and the [REC] defaults awaiting adoption) is mirrored as provisional, NON-CANONICAL entries OD-P-14 to OD-P-41 in [`docs/open-decisions.md`](../../open-decisions.md#od-p-14).
