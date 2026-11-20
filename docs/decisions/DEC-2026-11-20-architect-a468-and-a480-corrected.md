# DEC-2026-11-20 · Architect rulings: A468, and A480 corrected (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 20 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 20 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | The text of **A468** (the re-read gate), and the **corrected text of A480** (the Codex-outage flow). |
| **Supersedes** | **A480's first bullet** in `DEC-2026-11-20-architect-rulings-a469-a485` (the Codex-outage bullet) is replaced by §1. The record is not edited; this one says it is replaced. **A468** had no text in that record (§2); §1 supplies it. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 20 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A468; A480 (corrected)
- Decision: §1
- Rationale and evidence: the Architect's text, relayed to the Steward on 20 Nov 2026 through the Founder's instruction
- Affected requirement IDs / SoT sections: AGENT-22; AGENTS §11 (reviews, approval and merge); plan §4 (tiers), §13.1; A111, A288, A317, A334, A463
- Supersedes: see the Supersedes row above
- Migration notes: none

## 1. The rulings, as given

### A468 (interim): The re-read gate.

A PR whose findings are fixed and whose CI is green is mergeable. There is no re-read gate: a merge-main commit voids nothing.

Limits:

- It removes the reader's re-read gate only.
- It does not remove CI, Codex's first read or A111.
- It does not remove a Tier 1 migration's independent read (A463).
- It does not remove SR on `.github`, deploy and security paths.

### A480 (interim, corrected): The Codex-outage flow.

During a Codex outage:

- SR is required on `.github`, deploy and security paths.
- Tier 1 keeps SR READY (standing in for Codex, which reads after merge) and the migration independent read from a different role than the author and the SR READY.

*Supersedes or changes:* replaces the Codex-outage bullet of **A480** as recorded in `DEC-2026-11-20-architect-rulings-a469-a485` ("a Tier 1 independent read comes from SR or another role. Tier 2 and 3 need no read. A455 stands"). The other bullets of that A480 (noema#832, noema#821, noema#786) are not mentioned by the correction and stand.

## 2. What the Steward did, and where the rulings are silent

- **docs#216 had merged** (it carried "A468 has no text" and the first A480). The merged record is not edited; this record carries the text.
- **Named without text.** The Steward's instruction also names **A474 (the follow-up by C1)**, **the conditions of A475**, **the re-read wording of A476** and **A486**. **No text for any of them was received.** The Steward adds none and invents none; A474, A475 and A476 stay as recorded in `DEC-2026-11-20-architect-rulings-a469-a485`. The Architect sends the text, and the Steward records it exactly as given in the next record. **Next free ruling: A487** (A486 is named, without text).
- **Every ruling here stays Interim**, as instructed.
- **What A468 changes in practice, and the Steward's reading.** On noema#183 the Steward's table said that a head that moved after a read means "re-read owed" (noema#756, whose head moved to `6bfd491e` after a merge of `main`, a helper rename and the dropped README hunk). Under A468 a PR whose findings are fixed and CI green is mergeable and a merge-`main` commit voids nothing. **Not removed, so still owed on noema#756:** the migration's independent read from a role other than the author and the SR READY (A463), SR's READY, CI green, Codex's first read at the time Codex reads, and a non-author Founder (A111). The Steward does not decide whether #756's fixes count as "findings fixed"; the Founder and the reviewers say.
- **A480 and the Steward's earlier reading.** The Steward's note in `DEC-2026-11-20-architect-rulings-a469-a485` §2 (A480 read as a rule for the length of a Codex outage) is consistent with the corrected text, which names an outage. The correction removes "Tier 2 and 3 need no read" from the outage rule; the standing tiers (A288, A334) are unchanged.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-architect-rulings-a358-a453` | A358 to A362, A380 to A453 | |
| `DEC-2026-11-20-architect-rulings-a454-a467` | A454 to A466 (A467 named, no text) | |
| `DEC-2026-11-20-architect-rulings-a469-a485` | A469 to A485 (its A480 first bullet replaced here) | |
| This record | A468; A480 corrected | |
| Named without text | A467, A474 follow-up (C1), A475 conditions, A476 re-read wording, A486 | **A487** |
