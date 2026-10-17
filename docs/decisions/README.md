# Decisions

This directory holds **decision records**: dated, owned records of decisions. It is the home for the founder decision log and the engineering decision log that SoT §0.4 ranks in its order of authority.

**A founder decision counts only once it is committed** to the SoT or to this directory, with date, owner, rationale, affected requirement IDs and migration notes. Decisions made in conversation, calls, chat apps or AI sessions are not authoritative until then (SoT §0.4). If an instruction disagrees with the SoT and has not been committed, follow the SoT and raise the conflict (AGENT-27).

**Where the decision log lives (OD-P-02, closed by DEC-2026-10-17).** This directory holds founder decisions and engineering decisions alike. Technology decisions never live in `brain` (DEC-2026-10-16 execution reset E8). A record that changes the SoT lands in the same pull request as the SoT edit and the regenerated register (AGENT-29).

## Records

| Record | Subject |
|---|---|
| [DEC-2026-10-02-sot-v1.2](DEC-2026-10-02-sot-v1.2.md) | SoT v1.2: pre-development fixes |
| [DEC-2026-10-06-architecture-and-contracts](DEC-2026-10-06-architecture-and-contracts.md) | Temporal, repository layout, contract value lists (superseded in part by DEC-2026-10-09; **repository list superseded by DEC-2026-10-13**; **contract enums (item 4) superseded in part by DEC-2026-10-16-money-and-value-lists**) |
| [DEC-2026-10-06-vendor-benchmarks](DEC-2026-10-06-vendor-benchmarks.md) | Benchmark candidates for Understanding and speech (superseded in part by DEC-2026-10-09) |
| [DEC-2026-10-09-deployment-temporal-providers](DEC-2026-10-09-deployment-temporal-providers.md) | Two deployables, Temporal, multi-provider Understanding and speech |
| [DEC-2026-10-11-poc-perd-v1.1](DEC-2026-10-11-poc-perd-v1.1.md) | Adopt the POC PERD as the POC engineering specification; re-pointed to the current PERD by DEC-2026-10-16 (Accepted) |
| [DEC-2026-10-11-poc-4week-plan](DEC-2026-10-11-poc-4week-plan.md) | Adopt the four-week POC execution plan; Phase A in parallel with week 1; re-pointed to the current plan and the E3 schedule by DEC-2026-10-16 (Accepted) |
| [DEC-2026-10-12-tushe-environment-scope](DEC-2026-10-12-tushe-environment-scope.md) | How the POC uses Tushe: `mock-case`, ground truth, time, faults, credentials and the G0 gate; amends SoT §36 (SoT v1.4) (Accepted; Amendments 1 and 2) |
| [DEC-2026-10-13-code-monorepo](DEC-2026-10-13-code-monorepo.md) | One code repository (`noema`) for the POC; what every other repository is for; amends SoT §51 (SoT v1.5) (Accepted; Amendment 1 re-points it to `Noemai-org`) |
| [DEC-2026-10-16-execution-reset](DEC-2026-10-16-execution-reset.md) | Execution reset: `Noemai-org` canonical, two-person team, schedule to 13 Nov, G0-T and G0-N, test-environment components, webhook relay, what leaves `docs`, `brain`'s purpose, the Tushe delta v1.2, the port to `noema`, no direct pushes; amends SoT §35.6, §40.3, §51 (SoT v1.6) (Accepted) |
| [DEC-2026-10-16-contract-and-pack-clarifications](DEC-2026-10-16-contract-and-pack-clarifications.md) | The `evidence_set_hash` construction (C1), the two-node intent model (C2), the status of CON-04, PCK-01 and PCK-02 (C3), noema#1 as a pure port (C4), G7 "External readiness" (C6), the repository mapping closed (C7), team rules, the work-in-progress limit and the cut line (C8); the settlement of the open items (C10); amends DEC-2026-10-16-execution-reset E2 and E12; no SoT change (Accepted by the Founder; the Technical Co-Founder confirms by approving) |
| [DEC-2026-10-16-money-and-value-lists](DEC-2026-10-16-money-and-value-lists.md) | Money as integer minor units (M1 to M10) and the contract value lists (Intent Object `status`, authority results, two-tier reason codes, the drift guard); closes OD-P-19 and OD-P-26; amends SoT §43.1 (SoT v1.7) (Accepted by the Founder; the Technical Co-Founder confirms by approving) |
| [DEC-2026-10-17-open-decisions-closure](DEC-2026-10-17-open-decisions-closure.md) | Closure of every open decision: the canonical OD-01, 02, 03, 06, 08, 10, 12, 13, 14, 15, 16 and the provisional items; the PERD defaults adopted; eleven gates converted to plan tasks; amends SoT §46, §19.3, INV-20, §47.1 and Appendix A (SoT v1.8) (Accepted by the Founder; the Technical Co-Founder confirms by approving) |

## Where decisions already live

| Kind | Where it is defined | Changed by |
|---|---|---|
| Binding decisions BD-01 to BD-16 ([CONVICTION] or [DECISION]) | [SoT](../NOEMA_SOURCE_OF_TRUTH.md) §0.5 | A new SoT version only |
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
- Closes: <OD IDs this record decides or closes, or none>
- Owner:
- Decision:
- Rationale and evidence:
- Affected requirement IDs / SoT sections:
- Migration notes:
- Supersedes:
```
