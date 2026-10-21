# Vendor and partner register

This is the single place that lists every outside provider, vendor and partner Noema depends on: what we need from each, where it goes once we have it, and who chases it.

**Never put a secret in this file or anywhere in a repository.** Secrets go only into the named GitHub Environment, under the exact secret name in the table. The names match `noema/.env.example` and the service configuration, and a CI check in `noema` fails a workflow that references a secret name missing from `.env.example`. If the code uses a different name, the code's name wins and this file is corrected.

Status values: `not started` · `requested` · `in hand` · `wired` · `not needed yet`

## 1. Model providers (model service only, never the core)

| Vendor | Used for | What we need from them | Where it goes | Data terms to confirm before any non-synthetic data | Status | Owner |
|---|---|---|---|---|---|---|
| **OpenAI** | GPT (generation: slot values, explanations); **Decisions API** (the only decision-model adapter built; D9, narrowed by the decision-model scope update) | API key with billing; Decisions API beta access; the pinned model identifier for `gpt-6-luna` | `OPENAI_API_KEY` in Environments `model-ci` and `bench` | Zero data retention eligibility; US or EEA processing region; DPA | not started | Founder |
| **Anthropic** | Claude (generation, failover) | API key with billing | `ANTHROPIC_API_KEY` in `model-ci` and `bench` | Retention, region, DPA | not started | Founder |
| **Google** | Gemini (generation, failover) | API key (AI Studio or Vertex) | `GOOGLE_API_KEY` in `model-ci` and `bench` | Free-tier inputs may be used by the vendor, so synthetic data only on a free tier; DPA on a paid tier | not started | Founder |
| **Microsoft Foundry** | Microsoft-Decision-1 (decision model; no adapter is built unless the bake-off shows the OpenAI Decisions adapter falls short on a task) | Foundry deployment; endpoint; key; confirmation that the model version can be pinned | `AZURE_FOUNDRY_ENDPOINT`, `AZURE_FOUNDRY_API_KEY` in `bench` | Request-data retention (not stated in launch material); version pinning | not needed yet | Founder |
| **TypeSafe** | Jev (decision model; no adapter is built unless the bake-off shows the OpenAI Decisions adapter falls short on a task) | Early access (signups paused in September); API key; pinned version (for example `jev-1.13.0`) | `TYPESAFE_API_KEY` in `bench` | Hosting region and retention (not published) | not needed yet | Founder |
| **OpenRouter** (optional gateway) | One key for several model vendors, including Microsoft-Decision-1 | API key with billing | `OPENROUTER_API_KEY` in `model-ci` and `bench` | It is an extra processor; synthetic data only | not started | Founder |

## 2. Speech providers (model service, voice track)

| Vendor | Used for | What we need from them | Where it goes | Data terms | Status | Owner |
|---|---|---|---|---|---|---|
| **Aethex AI** | Nigerian-language speech recognition and synthesis | API access; per-token or per-slot confidence in results (REQ-VOI-003); supported languages | `AETHEX_API_KEY` in `model-ci` and `bench` | Audio retention; region; DPA | not started | Founder |
| **Indigenius** | Nigerian-language speech recognition | As above | `INDIGENIUS_API_KEY` in `model-ci` and `bench` | As above | not started | Founder |
| **N-ATLAS** | Nigerian-language speech recognition | Confirm the access model (hosted API or downloadable weights) and licence. If weights, the hosting needed | To be decided once the access model is confirmed | Licence terms | not started | Founder |

## 3. The synthetic enterprise (Tushe)

| Item | What we need | Where it goes | Status | Owner |
|---|---|---|---|---|
| G0-T date and the R5 window | Dates from Tushe | `docs/poc/tushe/` and the plan | requested | Founder |
| Hosted API base URL | URL per environment | `TUSHE_BASE_URL` in `core-ci` | not started | Founder |
| Runtime integration credential (reads plus non-monetary case operations only) | Client ID and secret | `TUSHE_INTEGRATION_CLIENT_ID`, `TUSHE_INTEGRATION_CLIENT_SECRET` in `core-ci` | not started | Founder |
| Oracle credential (ground truth) | Separate credential, **benchmark only, never runtime** | `TUSHE_ORACLE_*` in `bench` only; Founder custody (REQ-ENV-002) | not started | Founder |
| Fixture loader and fault-controller access | Credential and documentation | `TUSHE_FIXTURE_*` in `bench` only | not started | Founder |
| Webhook signing secret | For the public webhook relay (execution reset E6) | `WEBHOOK_RELAY_SIGNING_SECRET` in the relay's own Environment | not started | Founder |

## 4. Platform and infrastructure

| Vendor | What we need | Status | Owner |
|---|---|---|---|
| **GitHub** | Team plan (branch protection and required reviews on private repositories); Environments `core-ci`, `model-ci`, `bench` | Environments `core-ci` and `model-ci` exist; **`bench` does not exist yet** (checked in Settings > Environments on 20 Oct 2026) and must be created before any benchmark workflow or any `TUSHE_ORACLE_*` / `TUSHE_FIXTURE_*` secret is added; Team plan pending | Founder |
| **Read-only access to `Noemai-org/docs`** (the vendored-docs drift guard) | `DOCS_READ_TOKEN`: a repository secret in `noema`, read-only, scoped to `Noemai-org/docs` only (contents: read), with an expiry. Without it the drift guard fails with "DOCS_READ_TOKEN is not set. See docs/vendors/README.md." | not started | Founder |
| **Hosting for the public webhook relay** (E6) | A provider and an account; the relay holds only the signing secret | not started; provider to be chosen | Founder |

## 5. People and partners

| Who | What we need | Status | Owner |
|---|---|---|---|
| **ARM and REV** (two external people, execution reset E2) | Engagement agreed; their GitHub handles; scope of review | requested | Founder |
| **Independent arm reviewer** (REQ-BEN-007, OQ-02) | A named person who did not build the arms | not needed yet (arms come after Noema passes its gates) | Founder |
| **Design partner** (Phase 2) | Written consent for anonymised cases; the two scoped credentials (§39.5) | not needed yet | Founder |

## Rules

- A vendor is used with real customer or partner data only after its "Data terms" column is checked off and a DPA is in place. Until then: synthetic data only.
- Model versions are pinned. A vendor that cannot pin a version is not used for anything the Record must replay.
- Adding a vendor means adding a row here in the same PR as the code that calls it.
