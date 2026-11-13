# DEC-2026-11-13 · UI-01 frontend dependencies are approved (OD-P-84, AGENT-14)

| | |
|---|---|
| **Status** | **Decided** once this pull request is approved and merged. The Founder approved the recommendation below in a working session on 13 November 2026; an instruction given in a session is not authoritative until committed (AGENTS §2, item 3), so this record is that commit. |
| **Date** | 13 November 2026 |
| **Owner** | Founder |
| **Closes** | OD-P-84 |
| **Amends** | None. No SoT, PERD or plan text changes. PERD §36.1 already names React and TypeScript (thin) and Playwright; this record approves exact packages and versions only |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided (merged); counts once a Founder who did not author this pull request approves and merges it (A111)
- Date: 13 November 2026
- Closes: OD-P-84
- Owner: Founder
- Decision: the table in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: REQ-UI-001, POC-FR-11; AGENT-14; PERD §36.1 (stack rows "React and TypeScript (thin)" and "Playwright"), PERD §40.1. No requirement is added or changed
- Migration notes: none. UI-01 (noema#502) is the first change to add the packages; it cites this record
- Supersedes: None

---

## 1. The decision

| | Decision |
|---|---|
| D1 | **Approved under AGENT-14, for the UI manifest only:** `react` 19.3.1, `react-dom` 19.3.1, `@types/react` 19.3.0, `@types/react-dom` 19.3.0 and `@playwright/test` 1.64.1. TypeScript stays at 5.9.3. |
| D2 | **Exact pins.** Versions are written without a range (`"react": "19.3.1"`, not `^19.3.1`) and the lockfile is committed. The `@types` packages are versioned independently of React and stay on the 19.x line. |
| D3 | **Audit at install.** The UI-01 pull request runs `npm audit` on the committed lockfile and shows the result. A high or critical finding in a listed package is a reason to return the package to the Founder (the OD-P-84 invalidation clause); it is not waived by this record. |
| D4 | **Playwright browsers.** `@playwright/test` downloads browser binaries from a Playwright host. This record approves the package only. UI-01 states how CI obtains the browsers (a cached or pre-installed browser, or a named download host). Any network change that needs goes through the environment owner and is not part of this approval. |
| D5 | **Not approved by this record:** a bundler or dev server, a unit-test runner, a state library, a UI kit, a CSS framework, or any other direct dependency. If UI-01 needs one, it raises a new [OPEN] entry. "Thin" (PERD §36.1) and the "Never shown" list (PERD §40.1) still bind. |
| D6 | **Used first** by UI-01 (noema#502). |

## 2. Rationale and evidence

**D1.** React and Playwright are already in the fixed stack, so AGENT-14 is about the exact packages. `react` and `react-dom` are the runtime. `@types/react` and `@types/react-dom` are needed for strict-mode TypeScript (AGENTS §7). `@playwright/test` is the browser test layer the stack names in place of manual QA.

Evidence read from the npm registry on 13 November 2026:

| Package | Version | Published | Licence | Direct dependencies | Deprecated |
|---|---|---|---|---|---|
| `react` | 19.3.1 | 14 Oct 2026 | MIT | none | no |
| `react-dom` | 19.3.1 | 14 Oct 2026 | MIT | `scheduler` ^0.28.0 | no |
| `@types/react` | 19.3.0 | 9 Sep 2026 | MIT | `csstype` ^3.2.2 | no |
| `@types/react-dom` | 19.3.0 | 9 Sep 2026 | MIT | none | no |
| `@playwright/test` | 1.64.1 | 14 Oct 2026 | Apache-2.0 | `playwright` 1.64.1 | no |

Every version is more than two weeks old. Transitive packages (`scheduler`, `csstype`, `playwright`) arrive through the lockfile; D3 covers them.

**D2.** Floating versions let an install change without a review. AGENT-14 approves a version, so the version is what the manifest says.

**D3.** A dependency approval is not a vulnerability review. The audit result is the evidence the pull request carries.

**D4.** Browser binaries are a download, not a library. Naming how CI gets them keeps the environment's network rules a separate, visible decision.

**D5.** The approval is the smallest list that lets UI-01 start. A wider list would approve packages nobody has yet shown to be needed.

## 3. Agent decisions (defaults for the Founder to confirm or change)

1. The `@types` packages are approved with React rather than left to UI-01: strict mode makes them a prerequisite, and a second decision would only delay the work.
2. The decision record is written by C2 at the Founder's request; the Steward may reword it, not change D1 to D6.

## 4. SoT §52

1. Is it in the POC? Yes: UI-01 is a POC task (POC-FR-11).
2. Is it the simplest viable version? Five packages; no bundler, state library or UI kit.
3. Is it safe? The UI shows only backend-verified state and holds no secret (AGENTS §7); the audit condition guards the install.
4. Can the Record prove it? n/a (no runtime path in the core).
5. Is it deterministic? Exact pins and a lockfile.

**Does it increase or decrease the unsafe autonomy surface?** Neither. The UI is thin and holds no authority.

## 5. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founder | Approved the recommendation (D1 to D6) | 13 November 2026 | Working session; recorded here |
| Second Founder | Approves by approving this pull request | | |
