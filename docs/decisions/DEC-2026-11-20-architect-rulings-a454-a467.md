# DEC-2026-11-20 · Architect rulings A454 to A467 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 20 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 20 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A454 to A466 (§1). The Architect's heading says "A454–A467"; no text came for A467 (§2). |
| **Supersedes** | **A454 amends A440** (slot kinds). **A458 clarifies A432** (what ErrNoneCombined covers). **A459 settles** the scope of `ConfirmationBindingEvidenceHash` (per request). **A460 settles** the details of A439. **A461 settles** the stand-in mapping of A438. **A464 answers** SR's questions on docs#212 (§2). **A465 states** that docs#212 may merge (it has merged). Otherwise per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. AGENTS §7 is not edited: A464 says the "no print" amendment lives in this record (§2). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 20 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A454 to A466
- Decision: §1
- Rationale and evidence: the Architect's message of 20 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-01, INV-02, INV-03, INV-12, INV-22; AGENT-11, AGENT-12, AGENT-13, AGENT-15, AGENT-16, AGENT-23; REQ-TRU-002, REQ-TRU-009, REQ-VOI-004, REQ-BEN-004; SoT §38.4; PERD §23, §39.2
- Supersedes: see the Supersedes row above
- Migration notes: none from this record (a pack-schema or contract change that a ruling asks for is its owner's, with the AGENT-15 steps)

## 1. The rulings, as given

### A454 (interim): Slot kinds (EL's noema#765 question).

The planner reads the resolved value's kind and resource_kind from the node's slot, the single authority. The param's resource_kind is a declaration that packcheck requires to equal the slot's. The slot types are Resource, Quantity, Party, TimeRef and Reference. Enum is not a slot type (enumerations are Reference with a vocabulary), so refusing it was correct. This amends A440.

*Supersedes or changes:* amends **A440**.

### A455 (interim): CI red evidence.

If GitHub doesn't create the red run within 15 minutes of a push, record the local red output and commit hash in the PR body and proceed, flagged as an exception. No empty commits, and no closing and reopening to kick CI.

### A456 (interim): Decisions for every outcome.

Decide returns the decision id for every recorded decision. Grants exist only for ALLOW. The Recorder port is documented for all outcomes: a non-ALLOW with no steps and no plan hash is allowed, an ALLOW requires both (guarded), and a REJECT, CONFIRM or UNKNOWN never carries a grant.

### A457 (interim): noema#726.

Cap every response the gateway writes at 65,536 bytes, including non-200/202 responses, with a fixed-text body. EL adds it.

### A458 (interim): noema#736.

The defect Codex found is that none: true with a rejected option is accepted and drops the rejection. Refuse it: ErrNoneCombined covers none combined with a selected or a rejected option.

*Supersedes or changes:* clarifies **A432**.

### A459 (interim): noema#759.

ConfirmationBindingEvidenceHash is per request, because there is one snapshot per decision. Status sits inside each digest entry. The partial-index form is accepted.

### A460 (interim): noema#811 and A439.

- The Go test that builds the five canonical inputs may live in orchestrator/portadapters/interpreter, C2's own package.
- The fixture sits under benchmark/replay/, pinned to BO's inputs_sha256, and CI proves it equals fresh output.
- The Python-rebuild fallback is rejected.
- The locale is en-NG for all five cases (what the UI sends). BO exports canonical_locale: "en-NG", locale_mix stays a tag only, and no locale_hint is sent.

*Supersedes or changes:* settles details of **A439** (which sent the canonical locale only).

### A461 (interim): Mapping.

The stand-in's case list is mock-case's CasePage. complaint_ref is its own list with its own completeness marker. EL's portread slice builds both.

*Supersedes or changes:* settles the stand-in case list of **A438**.

### A462 (interim): noema#799 and noema#808.

- BO follows SoT §38.4 for the curve and the operating point. The scorer picks the operating point by that stated rule, with a test.
- Rates are integer basis points, so they display exactly with no rounding. Spread is min and max across runs. Arm labels come from the arm manifest.

### A463 (interim): Independent migration reads.

Satisfied for noema#716, noema#756 and noema#769 by the existing independent reads plus SR's confirmation. noema#771 gets EL's independent read and noema#759 gets C2's.

### A464 (interim): SR's questions.

- A423's .gitleaksignore conditions cover history that can't be rewritten (noema#772's line and merged noema#640). New strings use a fresh branch (A429).
- The raw-audio store (A451) replaces the recording plan's bucket scan.
- "Consenting team members" wording stays for team recordings, and only the consent form is gone.
- The "no print" amendment lives in the decision record, and the lint rule is scoped to services/.
- C1 confirms DEPENDENCY_UNAVAILABLE is in the public error catalogue (errors.v3) and adds it additively if not.

### A465 (interim): docs#212.

It may merge now on two independent reads. Codex's read follows.

### A466 (interim): Ordering.

noema#821 before noema#730, and noema#717 and noema#795 any time.

## 2. What the Steward did, and where the rulings are silent

- **A467 has no text.** The heading says "A454–A467"; the message holds A454 to A466. The Steward invents none. Next free ruling: **A468**.
- **A452 stays a recommendation** until the Founder confirms or overrules it (the Architect's instruction). Nothing here changes it, and the plan does not carry it. **Nothing else is removed**: no ruling, plan row, debt entry or note of an earlier record is changed by this record.
- **The "no print" rule (A445, A464).** The rule of AGENTS §7 ("no `print`" in Python) applies to `services/`; it does not apply to `tools/` and the benchmark CLI scripts, whose standard output is their interface (A445). It does not loosen AGENT-13: those scripts still never print a secret or a scanned value. The amendment is written here, as A464 says; the lint rule is scoped to `services/`. The Steward does not edit AGENTS.md (its copies are taken from `docs`, and a change to it goes in its own pull request); the Architect or EL says if the file should change.
- **docs#212 has merged** (20 Nov 2026), so A465's "may merge now" is met. The Steward did not merge it.
- **SR's six questions on docs#212 and where they stand:**
  1. A429 against noema#772 and noema#640: **answered** (A464, first bullet).
  2. A451 and the recording plan: **partly answered** (A464, second bullet: the store replaces the bucket scan). Not answered: which user owns the 0700 volume, and that it is never mounted into a CI job or container other than the voice runner.
  3. Plan line 336 and the `TEAM_RECORDING` label: **partly answered** (A464, third bullet: "consenting team members" wording stays for team recordings, only the consent form is gone). The plan's line 336 ("keep raw audio without consent", in the never list) is untouched, as the instruction says remove nothing else.
  4. "No print": **answered** (above).
  5. A444's oracle credential statement (that no agent session ever holds it): **not answered**.
  6. `DEPENDENCY_UNAVAILABLE` in the error catalogue: **answered as an action for C1** (A464, last bullet).
- **A456 and the Recorder port, A457 (the 65,536-byte cap), A459, A460, A461 and A462** are for their owners (EL, C2, BO); the Steward records only.
- **A463:** the independent migration reads for noema#716, noema#756 and noema#769 are satisfied; noema#771 needs EL's independent read and noema#759 needs C2's. This is a review-gate fact for the merge board, not a task change.
- **A466** gives merge ordering for the Founder: noema#821 before noema#730; noema#717 and noema#795 at any time.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-19-architect-rulings-a341-a357` | A341 to A357 | |
| `DEC-2026-11-19-architect-rulings-a362-a376` | A362 to A376 | |
| `DEC-2026-11-19-founder-intron-data-terms-a377-a379` | A377 to A379 (Founder) | |
| `DEC-2026-11-19-architect-rulings-a384-a388` | A384 to A388 | |
| `DEC-2026-11-20-architect-rulings-a358-a453` | A358 to A362, A380 to A453 | |
| This record | A454 to A466 (A467 named, no text) | **A468** |
