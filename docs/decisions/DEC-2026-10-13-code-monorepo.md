# DEC-2026-10-13 · One code repository for the POC; what every other repository is for

| | |
|---|---|
| **Status** | Proposed. Founder approval required before merge |
| **Date** | 13 October 2026 |
| **Owner** | Founders (TODO: name). Reviewer: engineering lead (TODO: name) |
| **Amends** | SoT §51 "Repository and module boundaries" (the repository list and its [OPEN] mapping note) |
| **Supersedes** | Only the repository list in DEC-2026-10-06-architecture-and-contracts. Every other decision in that record stands |
| **Closes** | The OD-P entries mirroring PERD OQ-04 (repository mapping) and OQ-05 (purpose of `brain`): OD-P-17 and OD-P-18. OD-P-13 tracks the same mapping question (OD-P-17 says to decide both together) and is closed with them. Closes plan task GOV-02 |
| **Unblocks** | Plan task PLT-01 (repository skeleton), and through it every week-1 build task |

**Record fields (decisions README template).** The table above already gives Status, Date, Owner, Amends, Supersedes and Closes; the template headings it lacks point to the sections below.

- Status: Proposed (see the table above)
- Date: 13 October 2026 (see the table above)
- Closes: OD-P-13, OD-P-17, OD-P-18 (see the table above)
- Owner: see the table above
- Decision: see section 3
- Rationale and evidence: see sections 1, 2, 5 and 6
- Affected requirement IDs / SoT sections: see sections 7 and 8
- Migration notes: see R8 in section 3
- Supersedes: see the table above

---

## 1. The short version

All POC code lives in **one repository, `noema`**. The Go core and the Python model service stay **two separate programs**, each with:

- its own dependency manifest;
- its own build;
- its own container image;
- its own credentials;
- its own network.

One repository does not mean one application. The separation Noema depends on, that a model can never hold power over execution, is enforced at run time by processes, credentials, networks and CI checks. A repository split never enforced it.

Every other repository keeps a clear, single job:

| Repository | Job | Change |
|---|---|---|
| `docs` | Governing documents: SoT, PERD, plan, decisions, Tushe correspondence | None |
| **`noema`** (new) | All POC code | Created |
| **`benchmark-heldout`** (new, private) | Held-out cases and oracles. Benchmark owner only; no agent access | Created, if GOV-03 has not already created it |
| `brain` | Founder documentation outside the build. Not part of the build's chain of authority | None. Its purpose is now recorded |
| `backend`, `intent-engine` | Superseded by `noema` | Archived read-only, after any code built under the current architecture is moved into `noema` with its history |

## 2. Why one code repository

**Our situation:**

- one small team with coding agents;
- one product, with one release (the 6 November demo);
- a contract shared between Go and Python that will change often in weeks 1 and 2.

**With two code repositories, every contract change is a chain:**

1. change the schema in one repository;
2. publish a versioned package;
3. bump it in the other repository;
4. open a second pull request;
5. land both in the right order.

**With one repository, it is a single pull request,** tested end to end by CI, and a coding agent can see and test the whole change from one task card.

**What a repository split would have protected: nothing that matters to Noema.** Splitting stops nobody adding a model SDK to the core's dependency file. Our CI boundary checks (PLT-03) stop that in either layout. The real protections stay in place and are listed in section 4.

**The decision is reversible and cheap.** If a later need appears, a folder can be split out with its full history in about an hour (`git filter-repo`). Examples of such needs:

- delivering only the core to a bank;
- open-sourcing a component;
- separate teams with separate release cycles.

## 3. The decisions

### R1. `noema` is the only code repository for the POC

The layout follows PERD §64.2, with the repository prefix removed:

```
noema/
  AGENTS.md, CLAUDE.md        copied from docs; each states the docs commit it was copied from
  .github/CODEOWNERS
  .github/workflows/          one workflow per area, each filtered by path
  Makefile                    the only build orchestration (no Bazel, Nx or Pants)
  contracts/                  JSON Schemas, fixtures, errors.v1.json, codegen config
  services/core/              Go: go.mod; cmd/core, edge, orchestrator, trust, execution,
                              outcome, record, evidence, adapters/synthetic_tushe, workflows,
                              platform, migrations, internal/contracts (generated, committed)
  services/model/             Python 3.13: pyproject.toml; understanding, explanation, voice,
                              providers/{llm,speech}, platform, contracts (generated, committed), tests
  packs/                      fintech; telecom, insurance, healthcare_admin (conformance)
  tools/lint/, tools/packcheck/, tools/codegen/
  ui/                         overlay, inspector, bench (package.json)
  benchmark/                  generator, cases, fixtures, fault_plans, runner, oracle_client,
                              scoring, arms, evil_provider, hostility_proxy, partner_listener, reports
                              (never the held-out set)
  synthetic/mock_case/        the synthetic case service (DEC-2026-10-12, REQ-ENV-008)
  deploy/compose/             docker-compose.yml, profiles (dev, ci, bench, demo), network policy
  docs/                       as-built documentation and session files (AGENTS.md section 9)
```

**Contracts:**

- `/contracts` is the single source.
- Generated Go and Python types are committed inside each service.
- CI fails if regenerating them produces any difference (PLT-02).
- **No package is published** between services.

### R2. The two services stay physically separate

All of these are checked in CI from day one (PLT-01 to PLT-04):

- **Builds.** Each service builds from **its own folder only**:
  - the core image is built with `services/core/` as its Docker build context;
  - the model image is built with `services/model/` as its build context.
  - Neither image contains the other's code or configuration.
- **Dependencies.** Each service has its own manifest:
  - the core's `go.mod` may contain no model or speech provider SDK;
  - the model service's `pyproject.toml` may contain no database driver for the core schemas and no Temporal client (INV-29, SoT §51 boundary rules).
- **No cross-references.** No file in `services/core/` references a path in `services/model/`, and the reverse. Shared shapes come only from `/contracts`.
- **Networks.** The runtime networks of PERD §65.1 are unchanged.

### R3. Secrets are scoped by environment, never by repository

The one real risk of a single repository is that CI secrets are, by default, visible to every workflow in it. So:

- **No secrets at repository level.**
- **Secrets live only in GitHub Environments:**

  | Environment | Holds | Used only by |
  |---|---|---|
  | `core-ci` | Tushe read-only key; test database and grant-signing test keys | Core workflows |
  | `model-ci` | Model and speech provider keys | Model-service workflows |
  | `bench` | Tushe administrator and fixture credentials; `mock-case` truth access | Benchmark workflows, with the benchmark owner as required reviewer |

- **Each workflow is filtered by path,** and can reach only its own environment.
- **A CI check fails** if any workflow references an environment outside its area.

### R4. Code ownership is by path

`.github/CODEOWNERS` enforces at least:

| Path | Required reviewers |
|---|---|
| `services/core/trust/`, `execution/`, `outcome/`, `record/`; `contracts/`; `packs/` | Engineering lead plus C1 or C2 |
| Safety-threshold configuration (REQ-AGT-005) | Engineering lead plus a founder |
| `synthetic/mock_case/` and `benchmark/hostility_proxy/` | Integration lead or engineering lead. **Core engineers cannot approve** (DEC-2026-10-12 D1, SR-19) |
| `benchmark/` | Benchmark owner |
| `.github/` | Engineering lead plus a founder |

Every coding-agent task still carries a module allowlist (REQ-AGT-002). One repository widens what an agent can touch, so the allowlist matters more, not less.

### R5. `benchmark-heldout` stays separate and private

- It holds the held-out cases and oracles.
- Only the benchmark owner and the founders can read it.
- No coding agent, and no builder, gets a credential for it (REQ-AGT-004, OD-16).

This is the one repository boundary that is a real security boundary.

### R6. `docs` stays the home of governance

It holds the SoT, PERD, plan, decisions, registers and Tushe correspondence. Its documentation-only rule (OD-P-01) stands. No POC code goes there.

### R7. `brain` keeps its purpose and stays as it is

- `brain` holds founder documentation that sits outside the build.
- It is **not part of the build's chain of authority.** Nothing in it is a specification, a requirement or a decision for the POC unless that content is first moved into `docs` through a decision record.
- Coding agents don't read or cite it for build work.
- Nothing about it is archived or changed.

### R8. `backend` and `intent-engine` are archived

1. **Inspect first.** Before archiving, the engineering lead lists what each repository contains.
2. **Move only current work.** Anything built under the current architecture (DEC-2026-10-06 or later) is moved into `noema` with its history. Anything older stays behind, so agents never pick up superseded patterns.
3. **Archive.** Both repositories are then set to read-only (GitHub "Archive"), and their READMEs point to `noema`.

## 4. What stays exactly the same

- **The model boundary:** INV-01 and INV-29, two deployables, separate credentials, the PERD §65.1 networks, and the CI checks.
- **`/contracts` as the single source,** generated into both languages (AGENT-15).
- **Held-out custody** (OD-16).
- **The documentation-only `docs` repository.**
- **Every requirement, invariant and gate.** Requirement count: 153. Task count: unchanged.

## 5. Options we rejected

| Option | Why not |
|---|---|
| Keep `backend` and `intent-engine` as two code repositories | Every contract change needs package publishing and two ordered pull requests; agents lose whole-change visibility; nothing is protected that runtime checks don't already protect |
| One repository for everything, including `docs` | Governing documents have their own review rules and checker. Mixing them with code makes both noisier |
| Put the held-out set in `noema` with restricted paths | GitHub cannot restrict reading by path. Anyone with read access sees everything. Held-out custody needs a separate repository |
| Adopt a monorepo build tool (Bazel, Nx, Pants) | Overkill for three toolchains and a four-week POC; would need AGENT-14 approval |
| Archive `brain` | It has a purpose outside the build; archiving it would remove a working space for no gain |

## 6. Risks and how we contain them

| Risk | Containment |
|---|---|
| A CI secret leaks across services | Environment-scoped secrets only; path-filtered workflows; a CI check on environment references (R3) |
| One image accidentally includes the other service | Per-service build contexts; a CI check that inspects each image's file list (R2) |
| An agent edits outside its task | Module allowlist per task card, enforced by CI (REQ-AGT-002); path CODEOWNERS (R4) |
| CI gets slow running three toolchains on every PR | Path-filtered workflows; the full suite runs nightly (plan §5) |
| Old `backend` code confuses agents | Archive after inspection; only current-architecture work moves (R8) |

## 7. The SoT edit that lands with this record (AGENT-29)

**SoT §51, the opening paragraph, becomes:**

> Noema uses four repositories: `docs` (governing documents), `noema` (all POC code), `benchmark-heldout` (held-out cases and oracles; benchmark owner only) and `brain` (founder documentation outside the build's chain of authority). `backend` and `intent-engine` are archived (DEC-2026-10-13-code-monorepo, superseding the repository list in DEC-2026-10-06-architecture-and-contracts). The internal structure below lives in the `noema` repository. `/contracts` is the single source; generated Go and Python types are committed inside each service and checked by CI. The Go core and the Python model service remain separate deployables with separate manifests, build contexts, images, credentials and networks.

**SoT §51, the tree:** the `/docs` line becomes:

> `/docs` (in `noema`): as-built documentation and session files. Governing documents live in the `docs` repository.

**SoT §51 boundary rules:** add two:

> each service's container image is built from that service's folder only; CI secrets are scoped to GitHub Environments per service, never to the repository.

## 8. The SoT §52 questions

- **Which requirement does this serve?** SoT §51; INV-29; AGENT-14, AGENT-15, AGENT-19; PERD REQ-AGT-002, REQ-AGT-004, REQ-API-001, REQ-NFR-004.
- **What breaks without it?**
  - PLT-01 cannot start, and every week-1 build task waits on it.
  - Every contract change costs two pull requests and a package release.
- **Which benchmark cases prove it?** Not a product behaviour. It is proven by:
  - the CI boundary checks (PLT-03);
  - the per-image file-list check (R2);
  - the environment-reference check (R3).
- **What business value?** Faster, safer changes in the four weeks that matter most.
- **Core, pack, adapter or nowhere?** Repository structure only. Nothing in the product changes.
- **Does it increase or decrease the unsafe autonomy surface?**
  - Neither at run time.
  - In CI it decreases it: secrets become environment-scoped, and image contents are checked.

## 9. Sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Founder | TODO | Approve / amend / reject | |
| Founder | TODO | Approve / amend / reject | |
| Engineering lead | TODO | Reviewed | |
