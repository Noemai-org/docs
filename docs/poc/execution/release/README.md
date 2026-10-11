# Release evidence bundle

The release evidence bundle for the G6 release run (plan §13.4, REQ-BEN-008).

- **Who assembles it:** the runner assembles the bundle from the release run ID without manual editing (REQ-BEN-008). The task is BEN-27 (owners B and EL); IL's clean-room reproduction (REL-02) checks it; the founders sign it at the G6 review (GOV-16).
- **A missing item blocks G6.**
- **The oracle and held-out cases are referenced by hash, never included.**
- **The bundle hash is recorded in this folder** once the bundle exists.

Nothing else goes in this folder until the release run happens.

**Contents (plan §13.4, verbatim):**

| File | Contents |
|---|---|
| `release-manifest.md` | Commit hashes of every repository, dependency lock hashes, SBOM snapshot; contract, pack and policy versions |
| `environment.md` | Tushe version, scenario-pack version, seed set, fault configuration, oracle version |
| `suite-manifest.md` | Generator version and seeds; per-layer and per-category case counts; share of Pidgin or code-switched cases |
| `heldout-attestation.md` | The benchmark owner's attestation that the held-out set was not exposed; access log; split hash |
| `test-results/` | Full results by layer, including property-test seeds |
| `scorecard.md` + per-case outputs | Tiered scorecard by family B1 to B8 with numerators, denominators, confidence intervals and the rule-of-three note |
| `tier0-evidence.md` | Negative tests proving no prohibited path and no oracle access; the eleven gates |
| `providers.md` | Results per provider, spread across three runs, pinned model versions |
| `voice-report.md` | Voice subset results and the real-conditions gate report, if voice is shown |
| `performance.md` | P50, P95 and P99 latency by path; per-stage error rates |
| `comparison.md` | Arm configurations, versions, dates, engineering hours, reviewer sign-off, results including where arms win |
| `business.md` | Business metrics with every assumption and data source labelled; the simulated manual baseline labelled as such |
| `record-samples.md` | At least three reconstructions, including one unknown and one contradictory path; chain verification result |
| `limitations.md` | Regression list, known limitations, untested arms and providers, open decisions, approved debt register |
| `claims.md` | The exact external claim wording the results permit |
| `clean-room.md` | REL-02 report |

Source: `docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v1.1.md`, lines 834–851.
