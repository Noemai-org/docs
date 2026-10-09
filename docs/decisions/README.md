# Decisions

This directory holds **decision records**: dated, owned records of decisions. It is the home for the founder decision log and the engineering decision log that SoT §0.4 ranks in its order of authority.

**A founder decision counts only once it is committed** to the SoT or to this directory, with date, owner, rationale, affected requirement IDs and migration notes. Decisions made in conversation, calls, chat apps or AI sessions are not authoritative until then (SoT §0.4). If an instruction disagrees with the SoT and has not been committed, follow the SoT and raise the conflict (AGENT-27).

## Records

| Record | Subject |
|---|---|
| [DEC-2026-10-02-sot-v1.2](DEC-2026-10-02-sot-v1.2.md) | SoT v1.2: pre-development fixes |
| [DEC-2026-10-06-architecture-and-contracts](DEC-2026-10-06-architecture-and-contracts.md) | Temporal, repository layout, contract value lists (superseded in part by DEC-2026-10-09) |
| [DEC-2026-10-06-vendor-benchmarks](DEC-2026-10-06-vendor-benchmarks.md) | Benchmark candidates for Understanding and speech (superseded in part by DEC-2026-10-09) |
| [DEC-2026-10-09-deployment-temporal-providers](DEC-2026-10-09-deployment-temporal-providers.md) | Two deployables, Temporal, multi-provider Understanding and speech |

## Where decisions already live

| Kind | Where it is defined | Changed by |
|---|---|---|
| Binding decisions BD-01 to BD-15 ([CONVICTION] or [DECISION]) | [SoT](../NOEMA_SOURCE_OF_TRUTH.md) §0.5 | A new SoT version only |
| [DECISION] and [CONVICTION] items in the SoT body | SoT, at the tagged statement | [DECISION]: the open-decisions process (§46). [CONVICTION]: new evidence plus a version change (§0.2). |
| Open decisions OD-01 to OD-16 | SoT §46. Status in [`../open-decisions.md`](../open-decisions.md). | A decision record here, then a SoT revision if it changes a [DECISION] or [CONVICTION] |
| Provisional migration items OD-P-xx (NON-CANONICAL) | [`../open-decisions.md`](../open-decisions.md) | Adoption into a SoT revision, or closure by a decision record |
| Legacy ADR-001 to ADR-019 | [`../archive/legacy-canon-2026-09/decisions/`](../archive/legacy-canon-2026-09/decisions/) | **Superseded; non-authoritative.** Mapped to SoT sections in [`../archive/README.md`](../archive/README.md#legacy-adr-supersession-map). |

## When to write a decision record

Write one when any of these happens:

- a founder decision is made (§0.4 item 1);
- an open decision (OD-xx or OD-P-xx) is decided;
- a significant engineering choice is made that the SoT does not already settle. This includes any new dependency, service, datastore or framework, which first needs an [OPEN] entry and approval (AGENT-14).

**Do not write a record that restates the SoT.** If the SoT already decides something, cite the section instead. Do not rewrite a record after it is committed; supersede it with a new one.

For anything larger than a small change, answer the questions in SoT §52 in the record, including **does it increase or decrease the unsafe autonomy surface?**

## Template

Name files `DEC-YYYY-MM-DD-<slug>.md`.

```markdown
# DEC-YYYY-MM-DD-<slug>

- Status:
- Date:
- Owner:
- Decision:
- Rationale and evidence:
- Affected requirement IDs / SoT sections:
- Migration notes:
- Supersedes:
```
