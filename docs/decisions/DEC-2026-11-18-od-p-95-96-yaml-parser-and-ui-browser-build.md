# DEC-2026-11-18 · OD-P-95 and OD-P-96: the YAML parser for the CI safeguards and the UI's browser build are approved

| | |
|---|---|
| **Status** | **Decided** once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). The Founder approved both packages in comments on noema#667 and noema#696 (17 and 18 Nov 2026); an instruction given in a comment is not authoritative until committed, so this record is that commit. |
| **Date** | 18 November 2026 |
| **Owner** | Founder (the approvals); Repo Steward (the entries and this record) |
| **Closes** | OD-P-95 (opened and closed here) and OD-P-96 (opened and closed here) |
| **Amends** | `docs/open-decisions.md` (two entries). No SoT, PERD or plan text changes. |
| **Supersedes** | Nothing. D5 of [DEC-2026-11-13-ui-01-frontend-dependencies](DEC-2026-11-13-ui-01-frontend-dependencies.md) ("not approved: a bundler or dev server") is lifted for `esbuild` only, in `ui/`. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided (merged); counts once a Founder who did not author this pull request approves and merges it (A111)
- Date: 18 November 2026
- Closes: OD-P-95, OD-P-96
- Owner: Founder
- Decision: §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: AGENT-14; REQ-SEC-007 (the workflow checks), REQ-UI-001, POC-FR-11. No requirement is added or changed
- Migration notes: none. noema#622 and #629 are the first changes to use PyYAML; noema#699 is the first to add esbuild
- Supersedes: nothing (see the Supersedes row for D5)

---

## 1. The decisions

| | Decision |
|---|---|
| D1 | **PyYAML approved under AGENT-14, for `tools/ci` only:** hash-pinned (an exact version with hashes in a `tools/ci/requirements.lock`), `yaml.safe_load` only (never `load`), installed in the `safeguards` job only, no other use. The Security Reviewer chooses the version (a release older than two weeks) and commits its hashes. The line scanners of noema#622 and #629 are replaced by checks that walk the parsed document, with the same tests and canaries, in the same change. |
| D2 | **`esbuild` approved under AGENT-14, for `ui/` only,** pinned exactly, as a dev dependency that bundles the existing React and TypeScript entry point locally; `react` and `react-dom` stay as approved by D1 of DEC-2026-11-13. The Frontend Engineer proposes 0.28.2. Conditions: a committed lockfile; `npm audit` shown; the install works under `npm ci --ignore-scripts` with the platform binary verified; Security Reviewer review. A high or critical audit finding returns the package to the Founders. |
| D3 | **Not approved by this record:** any other YAML parser or use of PyYAML; any other bundler, dev server, plugin or loader; esbuild outside `ui/`; a runtime CDN; a hand-written module loader. A need for one raises a new [OPEN] entry. |

## 2. Rationale and evidence

**D1.** The two safeguards read workflow files by lines, and Codex found a bypass in each, round after round (quoted keys, flow mappings, `permissions :`, a quoted `#`, escaped keys; the Security Reviewer's summary on noema#667). A283 told the team to stop line-scanning YAML; A294 asked the Founder to approve PyYAML. No YAML parser was a `tools/ci` dependency (the Security Reviewer read the manifests: `tools/ci` is standard library only, `tools/contracts` pins `jsonschema` only, and `gopkg.in/yaml.v3` is an indirect Go requirement only). Facts read from PyPI on 18 Nov 2026: PyYAML's latest release is 6.0.3, uploaded 25 Sep 2025, licence MIT.

**D2.** The approved React 19 packages ship CommonJS entry points and the current build emits ES modules without bundling them, so a browser cannot run them; the alternatives (a CDN, a hand-written loader) are forbidden by the UI record and by AGENTS §10. Facts read from the npm registry on 18 Nov 2026: esbuild 0.28.2 is the `latest` tag, published 8 Aug 2026, licence MIT, no runtime dependencies, 26 optional platform-binary packages, `postinstall` is `node install.js` (which does not run under `--ignore-scripts`, hence the condition). The Founder's comments name the packages and the constraints, not the version; the version is the Frontend Engineer's proposal until a Founder or the Architect confirms it.

**D3.** The approval is narrow on purpose: one parser, one place, one load function; one bundler, one directory, one purpose.

## 3. What the Steward did

- Filed OD-P-95 and OD-P-96 in `docs/open-decisions.md` as CLOSED (opened and approved the same day) and regenerated the register.
- Did not choose the PyYAML version or hashes (the Security Reviewer's) and did not choose esbuild's version for the Frontend Engineer.
- Did not read the packages' source or run an audit: the Security Reviewer and the Frontend Engineer do that in their pull requests.
