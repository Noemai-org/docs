# DEC-2026-11-23 · Architect rulings A602 to A605 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge, and the decision A605 reserves) |
| **Decides** | Rulings A602 to A605 (§1), every one Interim. |
| **Supersedes** | **A603 changes the structure** of the compile service's decision (a two-stage gate instead of one choice with an abstain option) and states an interim threshold. **A605 is a stop rule** for the live compile runs. Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan, as written. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A602 to A605
- Decision: §1
- Rationale and evidence: the Architect's message of 23 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-22; AGENT-13, AGENT-16, AGENT-25; REQ-AMB-003 (as the gate's neighbour), the compile service; AGENTS §8, §10
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. A603's threshold is pack data; any new pack data kind is additive and follows AGENT-15 (a migration note) in C2's pack PR.

## 1. The rulings

### A602 (interim, evidence first).

Stop tuning the prompt against the goldens. The first change is evidence: C2 makes the job log print, for each golden, the option the model chose, the top five probabilities including abstain, and the threshold applied. Job logs are readable by agents, so the next run is no longer blind. The values are option ids and probabilities only, so nothing sensitive is printed.

### A603 (interim, structure).

Split the decision into two stages.

- **Stage 1:** a yes/no gate: "Does the customer explicitly ask for something to be done for them?"
- **Stage 2:** pick the capability only if stage 1 says yes, with no abstain option.
- A one-in-21 abstain choice is the fragile part, and a gate shows a wrong answer as one number.
- **Threshold:** AGENT-16 says an agent never sets it. The Architect's interim value is 9000 basis points, held in pack data and labelled as a Founder decision to confirm. A false assertion is the harmful error, so doubt abstains.

### A604 (interim, offline set).

BO builds a labelled set of 24 to 30 synthetic status-check and "resend" phrasings in en-NG and Pidgin. It is kept apart from the held-out set (INV-22). C2 fixes the gate against it with the replay provider first. Then run 8 repeats the five goldens three times (about three cents) to see variance, since one run of five cases can pass or fail by luck.

### A605 (interim, stop rule).

At most two more live compile runs: run 8 and, only if its now-readable evidence shows a threshold problem, run 9. If a golden still fails after run 9, there is no run 10 without a Founder decision. The Founder chooses between two options:

- **An asymmetric pass rule:** zero false assertions on status checks are required, and misses of an explicit request are recorded and logged (the safe error).
- **Delay.**

No golden is edited (A533).

## 2. What the Steward did, and where the rulings are silent

- **A602.** The values printed are option ids and probabilities only, and the golden inputs are synthetic, so AGENT-13 and AGENTS §10 hold. C2 sends the lines through the existing redactor (AGENTS §7). A log line is diagnostic and never proof of an outcome (AGENT-21).
- **A603 and the open decision.** The 9000 basis-point threshold is the Architect's **interim** value; AGENT-16 forbids an agent setting it, and the ruling labels it a Founder decision to confirm. The Steward filed **OD-P-101** (Open, provisional, NON-CANONICAL) in `docs/open-decisions.md`, so the value is tracked until the Founders confirm it; the Steward does not treat it as final. The ruling says "pack data" without naming the file; C2 names it in its pack PR (an additive pack member, AGENT-15 steps where a contract changes), and the Steward invents no location. A603 changes the compile decision's shape; the PERD's compile text is unchanged here, and any PERD or contract change it needs goes through a change request or C2's contract PR.
- **A604 and INV-22.** BO's set is kept apart from the held-out set (INV-22); nobody reads or infers the held-out set (REQ-AGT-004). All phrasings are SYNTHETIC (AGENT-25). It is a separate set from the A538 lexicon (pack data); neither replaces the other.
- **A605 and the gate.** The stop rule bounds the live runs: run 8, and run 9 only if run 8's readable evidence shows a threshold problem. **No run 10 without a Founder decision.** The Founder's choice between an asymmetric pass rule and a delay is **not made here and is not due yet**; it falls due only if a golden still fails after run 9. The Steward notes one consequence for that day: an asymmetric pass rule would change what counts as a pass for a gate case, so it would need a Founder decision record and, where it changes a plan gate condition, a change request (AGENTS §1 and §4: an agent never changes a gate). No golden is edited (A533). The Steward does not choose and does not recommend a side here.
- **Cost.** About three cents for run 8 (three repeats of five goldens), as the ruling says; the Steward adds no figure of its own (AGENT-18).
- **Task status (`tasks.csv`)** is unchanged here. **Migration ledger on noema#183** is unchanged: 0037 #922, 0038 #923, 0039 #925, 0040 reserved; next free 0041.
- **Next free ruling: A606.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` records | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-*` and `DEC-2026-11-22-architect-rulings-a518-a524` | A489 to A492, A502 to A517, A518 to A529 | |
| `DEC-2026-11-23-*` records, `a530-a533` to `a593-a601` | A530 to A601 (A541 noted; A590 to A592 in full) | |
| This record | A602 to A605 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank, by ruling A592) | **A606** |
