# DEC-2026-11-25 · Architect rulings A673 to A684 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 25 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves, from a personal account, and merges it (A111, A638; AGENTS §2, item 3). |
| **Date** | 25 November 2026 |
| **Owner** | Principal Architect (the rulings); the Founders (the merge) |
| **Decides** | Rulings A673 to A684 (§1), every one Interim. |
| **Supersedes** | **A673 fixes the date of A670's end marker** (Codex returned 25 Nov 2026) and sets the review labels. **A674 narrows** PCK-05's matrix to three pairs and moves the reversal pair to OD-P-113; it settles OD-RES05-1's placement question (A659). **A675 confirms** A556 and A665 together. **A677 orders** #949 before #958. **A680 asks for** a PERD rewording (drafted as v1.30, Proposed). Otherwise nothing; per ruling in §1. |
| **Amends** | `AGENTS.md` §11 "Reviews" (A673: the date and the labels). PERD **v1.30** (Proposed; REQ-INT-004 only; A680). Nothing in the SoT or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder's personal approval (A111, A638)
- Date: 25 November 2026
- Owner: Principal Architect; Founders
- Decides: A673 to A684
- Decision: §1
- Rationale and evidence: the Architect's message of 25 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-07, INV-17, INV-22, BD-08; AGENT-14, AGENT-15, AGENT-16; REQ-AMB-002, REQ-CTX-008, REQ-INT-004, REQ-RES-005, REQ-TRU-011, REQ-EXE-003, REQ-ENV-001; AMB-02
- Supersedes: see the Supersedes row above
- Migration notes: A681's `SLA_EVALUATED` payload is one additive contract file with a migration note and regenerated models (AGENT-15), in one small pull request for both Founders. EXE-06 uses migration **0042** (A681, A666). No migration is added by this record.

## 1. The rulings

### A673. Review labels

- Only Codex posts "Codex Review". Every other agent labels its comments with its own role name (SR, EL, C1, and so on). FE does not adopt that format.
- From today the Tier 1 rule is Codex, or SR standing in, plus SR READY at the same head.
- The Steward records the day Codex returned: **25 November 2026** (§2).

### A674. PCK-05 (EL's three missing facts)

- **Entity-to-source link:** packcheck reads it from the evidence mapping. No new member goes in the rule file.
- **Window placement:** one value per matrix entry.
- **Reversal pair:** Tushe has not stated the `reversal_posted` shape, and nothing may be invented. EL ships the three computable pairs (300 s each) now. The reversal pair comes out of the active rule list into an OPEN entry with its rule text. It returns when Tushe answers the question list, which is on #690.

### A675. Lane 5 slice 4, and A556 against A665

- **Allowlist:** the reader port under `outcome/request`, a read-only reader under `outcome/store` on the outcome login (tenant in the WHERE, row security forced), and one `cmd/core` wiring file.
- It reads only what Execution wrote: the receipt, the plan, and the intent and plan hashes. The outcome definition comes from the pack. If a needed column does not exist, EL stops and lists it.
- **A556 and A665 both stand.** The candidate item is the payment-facts source (A556). EL's reader adds the transaction-level version token and complete marker to that payload (A665). If a real conflict remains, EL writes the CONFLICT block in the PR.
- EL's other calls are confirmed:
  - #954: equal instants are allowed.
  - #956: treating `ErrIncomplete` as "is a list" is right.
  - #973 is comment-only.

### A676. #960, privacy (HIGH)

Counterparty names are not returned at all. The endpoint returns an opaque counterparty reference, an amount and a local time only. That matches AMB-02's label rule. C2 fixes it red first.

### A677. #949 and #958

A waiting contradiction is never a freeze cause. C2 fixes #949 first, with separate waiting and expired sets. C1 then derives #958's labels and evidence from the same freeze-causing set. SR's three #958 conditions stand.

### A678. #964 and #965

- **#964:** move the pattern file and expected id from `@1` to `@2`. Detect `### Assistant`. Add the version gate, a nil-safe dereference, the shipped manifest bumped, and no Detector when there is no pattern data.
- **#965:** the parser refuses `note: null`, because the schema requires a string when present. Red test first.

### A679. #972 replay name

The setting is `NOEMA_MODEL_PROVIDER_PROFILE` with values `live` and `replay`. Absent means refuse to start. The demo profile refuses `replay`. If #972 uses another name, rename it.

### A680. UND-07 and INP-01

- The decline is a fixed generic message with no internal code. A pack template keyed by reason code is OPEN, after G1.
- C1 records a T1 to T9 refusal as a Decision Record under A574 and A581, and C2 then tightens the test to exactly one record.
- The Steward drafts a REQ-INT-004 rewording like A312's.

### A681. Settings and contract additions (C1)

- `NOEMA_EXECUTION_EXECUTE_TIMEOUT_MS` and `NOEMA_EXECUTION_ROLLBACK_TIMEOUT_MS` stay required with no code default (fail closed).
- Interim values go in the bench compose only: execute 10000, rollback 5000. The Steward adds an OPEN entry for the Founders.
- The `SLA_EVALUATED` payload schema is approved as an additive contract file, with a migration note and regenerated models. It goes in one small PR for both Founders in the pass with #969.
- EXE-06's design stands. EL gives the independent migration read on 0042.

### A682. Webhook transport

- Mock-case gets a control endpoint that delivers webhooks through the relay path.
- It signs with its own SYNTHETIC key, using the scheme the Tushe spec states. If the scheme is not stated, IL stops and lists it.
- IL owns it, and BO's runner calls it. A resume does not move the simulated clock.
- B14 and B15 to B20 are settled by A649 (abstain the slot). BO regenerates the recordings to match.

### A683. The 19 principals

They are in BO's #962 manifest: `usr_synth001`, `002`, `009`, `015`, `019`, `029`, `030`, `037`, `042`, `045`, `049`, `109`, `117`, `122`, `141`, `150`, `161`, `173`, `178`. IL issues one 15-minute customer token each through `bench_tokens.sh`, with `BENCH_PRINCIPALS="usr_synth001:customer …"`. "Tenant-init seed" meant exactly this.

### A684. G1 critical path: `/readyz` is 503 (IL's stack-check)

- **Not configured:** evidence, Intents, Writes, Candidates, Ownership, production Evidence, Reconciler, Policies, Clocks, Confirmations, Planner, Recorder, explainer, input gateway, confirmation route, worker.
- EL burns these down one PR per gap, and each PR flips one named gap to wired.
- **Order, by what is already open:**
  1. Writes (#935), Candidates (#960 plus the builder), Clocks (#910 plus `LoadPackFile`), Intents.
  2. Reconciler (#949, #958, plus the adapter), Confirmations (expiry from `trust-limits.v2`, capability from the action graph in #963), Planner (the link from #963).
  3. Ownership, Evidence read and seal, Policies, Recorder (write login and sealed facts).
  4. Explainer, input gateway (#919 and #925), confirmation route, worker (#945 and the start site).
- After each merge IL re-dispatches the stack-check. The first 200 closes #692 and unblocks TST-02's smoke job.

## 2. What the Steward did, and where the rulings are silent

- **The day Codex returned (A670, A673): 25 November 2026.** A673 says "from today"; the record is dated 25 Nov 2026. `AGENTS.md` §11 now states the date and the review labels. The plan (v1.29 §4) says only that the Steward records the day, so it needs no change. **The noema copy of AGENTS.md** carries the old paragraph until it is re-pointed (a small pull request after this one merges, with `tools/vendor/repoint_docs.py`, as noema#967 did).
- **Review-gate wording after Codex's return (SR's and Codex's findings on this pull request).** `AGENTS.md` §11 first said "an independent role read stays for migrations only (A463)" after the return date. A673 does not say that; A656 and A657 granted the narrowing only "while Codex is out of usage", and A670 says the Tier 1 text applies again unamended, which includes one independent role review (EL, C1 or C2, not the author). **The clause is removed.** The safer reading (AGENT-20) applies until the Architect says otherwise: from 25 Nov 2026 the Tier 1 gate is the Tier 1 text of §11 and plan §4, with the independent role read. **Question for the Architect:** does the independent role read of every Tier 1 PR apply again from 25 Nov (the safer reading, applied here), or does A656's "migrations only" continue now Codex is back?
- **Open question from SR on "Codex, or SR standing in" after the return.** One reviewer cannot be both the Codex read and the SR READY on the same head without the two gates collapsing into one. SR asks the Architect to state (1) when SR may still stand in for Codex (for example only when Codex has not posted on the head within a period the Architect names; SR will not choose it), and (2) that heads which already carry SR's READY as the stand-in (before 25 Nov) keep it, and that a code push after 25 Nov follows (1). Until it is answered, SR posts no READY described as standing in for Codex on a head pushed after 25 Nov. The Steward records the question; it does not decide it.
- **A673's last sentence ("FE does not adopt that format")** is recorded as given and is **not** put into AGENTS.md: it does not say whether FE keeps another label or is exempt from labelling. The Architect states what FE uses.
- **[OPEN] entries opened (provisional, NON-CANONICAL), as asked:**
  - **OD-P-113** the `reversal_posted` shape and the reversal pair, with the pair's rule text taken from the pack's rule set v1 (the `reversal_conflict` contradiction and rule R3). EL attaches the exact pair and window to the pull request, because the PCK-05 matrix is not on `main`.
  - **OD-P-114** the decline template keyed by reason code (after G1).
  - **OD-P-115** the interim execute and rollback timeouts (10000 and 5000, bench compose only).
  - **OD-P-116** the `SLA_EVALUATED` payload schema. A681 approves it as a contract file but states no members; they are C1's to propose in the pull request.
- **Tushe question list:** item 9 (the `reversal_posted` shape) is added to the draft (`docs/poc/tushe/questions-2026-11-25-env05.md`, still not sent).
- **REQ-INT-004 rewording (A680), drafted like A312's:** PERD **v1.30** (Proposed; v1.29 is not edited) with `CR-2026-11-25-A680-perd-v1.30-int-004-lazy-void`. It says version N+1 voids nothing at admit time and that a decision, grant or confirmation of version N is refused at its next use (step E3), as D8 says for policy. `requirements-index.csv` is regenerated (no requirement added or removed). No SoT passage says a new Intent Object version voids grants at admit time, so no conflict is added to the conflicts register. The Architect and the Founders approve it with this pull request; until then the rulings govern.
- **A675 and A665.** The Steward notes that A556 (the candidate item is the payment-facts source) and A665 (the version token and complete marker) are both kept, as the ruling says. Nothing to reconcile in `docs`.
- **A676, A677, A678, A679, A682, A683, A684:** other owners' work; nothing for the Steward beyond this record. A676's privacy fix is the first HIGH item on #960. A684's list is the G1 critical path; the Steward does not move `tasks.csv` for it.
- **A681 and AGENT-16.** The interim timeout values are the Architect's, set for the bench compose only (AGENT-16 keeps agents from setting them).
- **A674 and the plan.** PCK-05's task row (plan v1.29) is unchanged; the three-pair scope is the ruling's (an approved POC decision ranks above the plan, SoT §0.4).
- **Next free ruling: A685.**
