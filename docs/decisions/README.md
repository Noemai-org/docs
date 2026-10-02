# Decisions

This directory holds **decision records**: dated, owned records of decisions taken after SoT v1.1. It is the home for both the founder decision log and the engineering decision log that SoT §0.4 ranks in its order of authority ([OD-P-02](../open-decisions.md#od-p-02)).

There are no decision records yet. None has been invented to fill the directory.

## Where decisions already live

| Kind | Where it is defined | Changed by |
|---|---|---|
| Binding decisions BD-01 to BD-15 ([CONVICTION] or [DECISION]) | [SoT](../NOEMA_SOURCE_OF_TRUTH.md) §0.5 | A new SoT version only |
| [DECISION] and [CONVICTION] items in the SoT body | SoT, at the tagged statement | [DECISION]: the open-decisions process (§46). [CONVICTION]: new evidence plus a version change (§0.2). |
| Open decisions OD-01 to OD-15 | SoT §46. Status in [`../open-decisions.md`](../open-decisions.md). | A decision record here, then a SoT revision if it changes a [DECISION] or [CONVICTION] |
| Provisional migration items OD-P-xx (NON-CANONICAL) | [`../open-decisions.md`](../open-decisions.md) | Adoption into a SoT revision, or closure by a decision record |
| Legacy ADR-001 to ADR-019 | [`../archive/legacy-canon-2026-09/decisions/`](../archive/legacy-canon-2026-09/decisions/) | **Superseded; non-authoritative.** Mapped to SoT sections in [`../archive/README.md`](../archive/README.md#legacy-adr-supersession-map). |

## When to write a decision record

Write one when any of these happens:

- a recorded founder decision is made (§0.4 item 1);
- an open decision (OD-xx or OD-P-xx) is decided;
- a significant engineering choice is made that the SoT does not already settle. This includes any new dependency, service, datastore or framework, which first needs an [OPEN] entry and approval (AGENT-14).

**Do not write a record that restates the SoT.** If the SoT already decides something, cite the section instead.

When records disagree, apply the order of authority in SoT §0.4. A lower-level choice may never silently override a higher-level product, safety or architectural decision.

## Record format

Name files `DR-YYYY-MM-DD-short-title.md`. Date-based names avoid colliding with SoT ID families. Every record carries the four things SoT §0.4 and §46 require (date, owner, rationale, evidence) plus traceability:

```markdown
# DR-YYYY-MM-DD: <title>

- Date:
- Owner:
- Decides: <OD-xx / OD-P-xx / new [OPEN] entry>
- Authority level (SoT §0.4): <founder decision / approved POC decision / engineering decision log / …>
- Requirement IDs served (AGENT-01):
- Status: <proposed / accepted / superseded by DR-…>

## Context
## Decision
## Rationale
## Evidence
## Alternatives considered
## What would make us reverse it (§52)
## Effect on the SoT (none / needs SoT revision vX.Y)
```

For anything larger than a small change, answer the questions in SoT §52 in the record, including **does it increase or decrease the unsafe autonomy surface?**

Do not rewrite a record after it is accepted. Supersede it with a new one.
