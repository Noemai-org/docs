# DEC-2026-10-19 · Repository-infrastructure code is permitted in `docs`, in two directories only

| | |
|---|---|
| **Status** | Accepted by the Founders on 19 October 2026 (written instruction to the coding agent). The Technical Co-Founder confirms by approving the pull request that adds this record |
| **Date** | 19 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | The open question raised in Noemai-org/docs#35: the merge-audit guard is JavaScript, and `docs` forbids source code |
| **Amends** | DEC-2026-10-16 E7 ("`contracts/` and `packs/` leave `docs`", "Afterwards. `docs` holds no `contracts/`, `packs/` or product code") |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the Founders (see the table above)
- Date: 19 October 2026
- Closes: the open question listed above
- Owner: Founder and Technical Co-Founder
- Decision: the rule in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: none. The SoT and the PERD do not quote E7
- Migration notes: `tools/check_docs_consistency.py` exempts the two directories instead of two named files (§3); nothing else moves
- Supersedes: None. It narrows the "no product code" sentence of E7 only by defining what is not product code

---

## 1. The decision

E7 forbids **product source code** in `docs`: no service, contract or pack implementation. **Repository-infrastructure code that governs the `docs` repository itself is permitted**, confined to two directories:

- `.github/scripts/`
- `.github/tests/`

Nothing outside those two directories may contain code. Nothing inside them may import or duplicate product code. Everything else in `docs` stays under the no-code rule of E7, enforced by `tools/check_docs_consistency.py` (and the checkers' own files, exempted as before).

## 2. Why

The merge-audit guard (`main-merge-audit`, GOV-22) is the enforcement of the pull-request rules until branch protection is available. It needs logic that can be tested without the network, so the workflow and its tests must import the same file. A workflow cannot hold that in YAML. The first version of the guard was an inline script that no test ran, and it misreported every commit (noema#21, docs#35). An exact-path exemption for two files, with no recorded decision, would have left a hole in the rule that nobody would remember agreeing to.

## 3. How it is enforced

- `tools/check_docs_consistency.py` exempts the two directories, not named files. A code file anywhere else fails the check, including a new file in `.github/` outside those directories.
- `tools/test_check_docs_consistency.py` tests both: files in the two directories pass, and a code file in `.github/workflows/`, `tools/`, `docs/` or the repository root still fails.
- "Imports or duplicates no product code" is a review rule: a reviewer rejects a change in those directories that copies logic from `noema` (contracts, packs, services).

## 4. What this does not change

- E7's archive of the draft OpenAPI schema, and the rule that `contracts/` and `packs/` live in `noema`.
- Every invariant, gate and requirement.

## Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Approved | 19 Oct 2026 | Written instruction to the coding agent |
| Technical Co-Founder | Confirms | Date of approval | Approving review on the pull request that adds this record |
