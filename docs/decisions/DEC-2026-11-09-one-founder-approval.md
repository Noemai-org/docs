# DEC-2026-11-09 · One approval from the Founder who did not drive the pull request, for every pull request (ruling A111)

| | |
|---|---|
| **Status** | **Decided by the Founder on 9 Nov 2026; recorded by the Repo Steward.** Counts once a Founder who did not author this pull request approves and merges it (AGENTS §2, item 3). |
| **Date** | 9 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Decides** | Every pull request in `docs` and in `noema`, whatever paths it changes, is approved by **one** Founder who did not author or drive it. |
| **Supersedes** | The wording "needs both Founders" in the rulings and records listed in §3, and the Steward's board convention of "both Founders" for migration, contract, workflow, Compose, pack and docs pull requests. It does not supersede [DEC-2026-10-16](DEC-2026-10-16-execution-reset.md) E2 and E13: this record applies them to every path. |
| **Amends** | `AGENTS.md` §11 (one sentence under **Reviews**). Because `AGENTS.md` is vendored in `noema`, a matching re-point pull request in `noema` merges with this one (REQ-OPS-005). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 9 Nov 2026; counts once a Founder who did not author this pull request approves and merges
- Date: 9 November 2026
- Owner: Founder and Technical Co-Founder
- Decides: who approves a pull request (every path, both repositories)
- Decision: ruling A111 in §1
- Rationale and evidence: the Founder's message of 9 Nov 2026 in the Repo Steward session ("I approve one unauthored approval rule for both docs and noema repo PRs. On all PRs."); the audit of 9 Nov 2026 found 110 of 111 open pull requests with no approval at their head, and a queue that two approvals per pull request made longer
- Affected requirement IDs / SoT sections: SoT §0.4; AGENT-29; REQ-AGT-001; REQ-OPS-005
- Migration notes: none for code. Pull requests already open need no change; the next approval is the only one needed
- Supersedes: see §3

---

## 1. The ruling

| ID | Ruling |
|---|---|
| **A111** | **One approval, from a Founder who did not author or drive the pull request, is enough to merge any pull request in `docs` or `noema`.** It applies to every path, including migrations, contracts, workflows, Compose and deploy files, packs, CODEOWNERS, the Source of Truth, the PERD and plan versions, and decision records. A pull request opened from one Founder account is approved by the other Founder; a pull request opened by an agent working through a Founder account is approved by the Founder who did not drive that session. The approver is the Founder who merges. |

## 2. What does not change

- A Founder never approves a pull request they authored or drove (E2, E13 of DEC-2026-10-16).
- Agents never approve or merge (AGENTS §11). An agent's report, a READY line or a comment is not an approval.
- The other gates stay as they are: CI green at the final head, the reviewer-role READY from a role that did not write the pull request (A14, A29), and two human reviews on a P0 path: EL plus C1 or C2 (plan §4). The Codex requirement of A14 and A29 and the re-read rule are **not** decided here.
- Held-out and oracle custody stays with the Founder (DEC-2026-10-16 E2, item 1).
- `.github/CODEOWNERS` is unchanged. It already lists both Founders on every protected path, so GitHub's code-owner rule is satisfied by either of them. Branch protection is not enabled, so nothing in repository settings changes.
- A change to an invariant, a binding decision or a [CONVICTION] item still needs the process in SoT §0.4; this record changes who approves, not what may be changed.

## 3. What this supersedes, exactly

| Where | Wording replaced | Now reads |
|---|---|---|
| [DEC-2026-11-06-architect-rulings](DEC-2026-11-06-architect-rulings.md), A5 | "needs both Founders" (the `decision-record.v2` contract change) | one non-author Founder approval |
| [DEC-2026-11-07-benchmark-suite-definition-v1](DEC-2026-11-07-benchmark-suite-definition-v1.md) | "needs both Founders" (the neutral result fields) | one non-author Founder approval |
| Every decision record's **Status** line "counts once both Founders approve and merge" (records of 4 to 8 Nov 2026) | both Founders | counts once a Founder who did not author the pull request approves and merges |
| The Repo Steward's merge board (noema#183) approver column | "both Founders" | the other Founder |
| [CR-2026-11-08-VOI-canonical-input-audio-ref](../poc/execution/change-requests/CR-2026-11-08-VOI-canonical-input-audio-ref.md) | "both Founders approve it" | one non-author Founder approval |

The older records are not edited. They keep their text; this record is the later decision (SoT §0.4, item 1).

## 4. The cost, stated plainly

A contract, a migration or a workflow now has one human approver where it had two. The checks that catch a defect before the approval are unchanged: CI, the Security Reviewer's READY on security paths, and the two human reviews on a P0 path. If a Founder wants a second look on one pull request, they may still ask for one in a comment; it is no longer required.

## 5. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| DEC-2026-11-08-rulings-a41-onward | A41 to A108 | |
| DEC-2026-11-08-rec-09-record-export | A109 | |
| DEC-2026-11-08-perd-39-4-control-plane-callers | A110 | |
| This record | A111 | **A112** |
