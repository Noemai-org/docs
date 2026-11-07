# GitHub Environments for the Tushe credentials: security checklist

Date: 2026-11-04 · Owner: Security Reviewer · Status: checklist, not yet verified against the live settings · Derived and non-normative: the credential scopes are those of [`trust-boundary-map.md`](trust-boundary-map.md) (DEC-2026-10-12 D6); this file adds no requirement.

Environments in `Noemai-org/noema`, created by the Founder: `tushe-runtime`, `tushe-fixture`, `tushe-admin` (the last holds no secret; see below). A tick below counts only against evidence the Founder attaches (a screenshot of each Environment page, or the output of `gh api repos/Noemai-org/noema/environments`). The Security Reviewer cannot read these settings; until they are attached, every row is **unknown**.

## Secret names (Founder, 5 Nov 2026)

`TUSHE_RUNTIME_KEY` (in `tushe-runtime`), `TUSHE_FIXTURE_KEY` (in `tushe-fixture`), `TUSHE_ADMIN_TOKEN` (held by the Founder; in no GitHub secret), `RELAY_PULL_TOKEN` (held only in the Environment `relay-pull`, below). A workflow that reads a name must have it listed in `.env.example` (E7).

## `relay-pull`

A fourth Environment, `main`-only with the Founder as required reviewer and administrator bypass off (rules E1 to E3). It holds one secret, `RELAY_PULL_TOKEN`, and no other Environment, repository or organisation level holds it (E4).

- **Scope: read-only pull of queued inbound events.** The token can read what the webhook relay has queued; it cannot write, acknowledge on behalf of another consumer, change relay configuration, or read anything else. **Verify when the relay is deployed** (what the relay's pull endpoint actually allows is UNVERIFIED until then; the check is a request with the token to a write route, which must be refused).
- Use: only the job that pulls queued events, on `main`. No pull-request job names this Environment.
- Founder ruling of 5 Nov 2026; binds once the Steward's decision record is merged.

## Rules for all three

| # | Rule | Why (source) | Evidence |
|---|---|---|---|
| E1 | Deployment branches: **Selected branches and tags**, one rule: `main`. Not "All branches"; not "Protected branches only" (branch protection is not enabled, so that setting may allow every branch). | A branch workflow must not reach a secret before review (AGENTS.md section 11). | Environment page, "Deployment branches and tags" |
| E2 | Required reviewers: the Founder (all three, including `tushe-admin`). | Human gate before the credential is released. | "Required reviewers" |
| E3 | "Allow administrators to bypass configured protection rules": **off**. | A bypass defeats E2. | Same page |
| E4 | Every Tushe secret exists **only** as an Environment secret. No repository or organisation secret of the same or any Tushe name. | A repository secret is readable by any workflow that names it, so it would skip E1 and E2. | Settings > Secrets > Repository secrets lists none |
| E5 | The three Environments hold **different** values, and no value is reused as another Environment's secret. | Scopes differ (D6). | Founder confirms in writing; the values are never shown to an agent |
| E6 | Only a workflow on `main` names the Environment (`environment: tushe-...`). No `pull_request_target`, no `secrets: inherit`, no reusable workflow from outside the repository, no secret in a step `run:` line, no `set -x`. | Secret exfiltration through workflow edits. | `git grep -n "tushe-" .github/workflows` read by the Security Reviewer |
| E7 | Secret names are listed in `.env.example` (the `check_secret_refs.py` rule), values are never in the repository, a log, an artifact or a PR. | AGENTS.md section 10. | CI `safeguards` green |
| E8 | The Environments exist before any workflow names them. A workflow naming a missing Environment creates it with **no** protection. | GitHub creates it on first reference. | Order of merges |

## `tushe-runtime`

- Secret: the runtime API key. Scope **reads only, test mode**; held by the core; egress allowlisted to the Tushe API host.
- Use: deployment of the core only. CI that does not deploy never names it.
- Checks: the key is rejected on `/partner/...` and on every monetary mutation (the isolation check, noema#152, run against Tushe once the key is attached; until then **unknown**).
- Rotation: a leaked key is revoked at Tushe, and a new value is set here, in that order.

## `tushe-fixture`

- Secret: the fixture key (test-mode payout creation, to build transaction histories). Held by the benchmark owner; fixture loader only; benchmark network only.
- Use: the fixture-loading job only, never the core and never a pull-request job.
- Check: the core's configuration contains no reference to this Environment (a `git grep` in CI).

## `tushe-admin`

Founder decision of 5 Nov 2026 (option a): the Founder runs admin reads by hand and attaches the results. **No workflow holds `TUSHE_ADMIN_TOKEN`.**

- The Environment `tushe-admin` exists only as a gate and a marker: it holds **no secret**, and no workflow names it. A secret named `TUSHE_ADMIN_TOKEN` at Environment, repository or organisation level is a FAIL of this checklist.
- The credential is held by the Founder and never reaches an agent, a workflow, a log, an artifact or a PR.
- What the Founder attaches is ground truth. It goes where the benchmark runner's store expects it, never into a PR comment or a place an agent can read (INV-22, REQ-AGT-004).
- Check (CI, I will add it): `git grep -n "TUSHE_ADMIN_TOKEN\|tushe-admin" .github` finds nothing except this decision's allowlisted references.

## After the Founder attaches the evidence

I tick each row, list what is unknown, and record the result in the Security Reviewer's status log. A row without evidence stays unknown; it never turns into a pass.
