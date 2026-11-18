# DEC-2026-11-18 · Architect rulings A306 to A312 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 18 Nov 2026, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 18 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Seven rulings, A306 to A312 (§1). |
| **Closes** | The per-step policy gap of noema#572 (A306), the P2 of noema#675 (A307), the digit-vector questions of noema#709 (A308), the task IDs of A299 and A297 (A309), IL's bench slice and Temporal TLS (A310), the numbers of noema#679 (A311) and the PERD wording of TRU-08 (A312). |
| **Supersedes** | **A309** replaces the PLT-08 split of **A299**. **A310** narrows **A296**. Otherwise per ruling, in §1. |
| **Amends** | The plan (v1.23: EXE-10 added, PLT-08's owner changed, REQ-TRU-005's title) and, as a Proposed draft, the PERD (v1.25: the policy-publication wording). Nothing in the SoT: see the conflict in §2. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 18 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A306 to A312
- Decision: §1
- Rationale and evidence: the Architect's message of 18 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-22, INV-26; AGENT-16, AGENT-29; REQ-TRU-005, REQ-TRU-010, REQ-EXE-008, REQ-OPS-002, REQ-VER-005; PERD §23.1, §23.4, §27.1 (E4); SoT §0.4
- Migration notes: none for contracts. Plan v1.23 adds one task and changes one owner; `tasks.csv` regenerated
- Supersedes: see the Supersedes row above

## 1. The rulings, exactly as given

| Ruling | Text | Supersedes or changes |
|---|---|---|
| **A306** (interim) | **Policy per step (noema#572).** PERD §23.1 says each write step is evaluated as its own action decision. Merge #572 as it stands. The gap is an early-refusal gap, not an authority gap, because execution revalidates at dispatch (E4, `POLICY_SUPERSEDED`). C1 does the per-step policy evaluation in the very next Trust pull request, before the G1 run. The wording in the comment and README says exactly what the code does until then. The budget default is accepted: ask for every capability in the set and escalate `DISPATCH_BUDGET_EXHAUSTED`. EL's Dispatches adapter answers a limit of at least 1 for reads. | Applies **A297** (TRU-10: an action decision is the per-write-step decision) and the budget reason code of **A254**. No plan row: the per-step evaluation is "the very next Trust PR" of C1 (§2). |
| **A307** (interim) | **noema#675.** Codex's remaining P2 is a recompute for every manifest entry. It affects speed only. It is a tracked follow-up (A287). | Applies **A287**. |
| **A308** (interim) | **noema#709 (digit vectors).** The Record guard joins U+001C to U+001F too. We mask more, never less. The money exemption applies in every consumer through the one shared function, including `record/reconstruct` Mask and `assemble.py`. Keeping the prefix at any three capitals is accepted. Reading `currencies.json` is low-priority debt. | Extends **A259** (the wide separator set) and **A279** (the money exemption). Opens DEBT-47 (the Steward's proposal). |
| **A309** (interim) | **Task IDs.** PLT-08 stays the outbox. Its owner becomes C2. The callback half already exists as OUT-05, so there is no split. The kill-switch listener becomes a new row EXE-10, owner C1, needing EXE-06. The Steward registers both. | **Replaces** the split of **A299** (08a and 08b): there is no split. Registers **EXE-10** and changes PLT-08's owner in plan v1.23. |
| **A310** (interim) | **IL and the bench.** IL proceeds with the transition-log and event-feed slice, using fixtures built from delta v1.3's field list and marked SYNTHETIC. Temporal TLS without client authentication is accepted for the bench. The internal-frontend split is DEBT-46 (IL and EL), due before G3. | Narrows **A296** (Temporal TLS in the bench profile) to TLS without client authentication. Opens DEBT-46. |
| **A311** (interim) | **UI-05 numbers (noema#679).** The digit rule exists to protect the customer overlay. The benchmark inspector is operator-only and shows aggregates only (INV-22). It uses its own scan with the no-case-id rule instead, and shows exact numbers as given. | Applies **A298** (UI-05 shows the numbers exactly as `scorecard-view` gives them). No change to **A259**'s overlay scan. |
| **A312** (interim) | **TRU-08 PERD wording.** Yes, the Steward drafts PERD v1.25 to reword the eager-void text to D8's lazy void, as one change request. | Answers the question of CR-2026-11-17-D8-tru08-row. Drafted as PERD v1.25 (Proposed) by CR-2026-11-18-A312-perd-v1.25-lazy-void; see the conflict in §2. |

## 2. What the Steward did where the rulings are silent

- **A309 registered.** Plan v1.23 (CR-2026-11-18-A309-exe10-plt08-owner): **EXE-10**, the tenant kill-switch listener (owner C1; REQ-EXE-008 and REQ-OPS-002 as EXE-06; Needs EXE-06; the date of EXE-06; joined to the G2 review row GOV-11 Needs). The ruling gave the owner and the Need, not the done-when, REQs or date: those are the Steward's smallest defaults and C1 or the Architect may correct them. **PLT-08's owner is C2.** There is no PLT-08a or PLT-08b: A309 replaces the split of A299. OUT-05 already holds the callback half.
- **A312: PERD v1.25 drafted, with a conflict the Steward cannot settle.** The draft rewords the policy-publication text (§23.4 and REQ-TRU-005; §54 item 12, a sacred safety invariant, is left as written: only the Founders restate it) to D8's lazy void: publication sets the version ACTIVE and appends `POLICY_PUBLISHED`; a grant of a superseded version is voided at execution (E4, `POLICY_SUPERSEDED`). **But SoT INV-26 says "Publishing a new policy version voids every outstanding, unspent Decision Grant governed by an earlier version"**, and OD-09 and US-20 read the same way (US-08 says the grant is void when Execution revalidates, which a lazy void satisfies). D8 outranks it (SoT §0.4, item 1: the latest recorded founder decision) and says "no document change", but the SoT text is the Founders' to restate (a new SoT version with an Appendix D entry; AGENTS §11). The CR carries the CONFLICT DETECTED block, and `conflicts-register.md` lists it as SOT-C-32 (Open). **v1.25 is Proposed and takes effect only with the SoT edit that restates INV-26**, as v1.24 does for A179; until then v1.23 governs. The safer reading meanwhile (AGENT-20) is the one the code already follows: no grant of a superseded version is ever spent.
- **A308 low-priority debt.** The ruling names no number or owner. DEBT-47 is the Steward's proposal (owner C1, the owner of the shared digit definition), Tier 3.
- **A306's next Trust PR.** C1's per-step policy evaluation has no plan row; "the very next Trust PR, before the G1 run" is the ruling's own scope. The Steward does not invent a row.
- **A307.** A tracked follow-up under A287; no debt entry, because a speed-only recompute is not a shortcut. Say if the Architect wants one.
- **A310 and A311 are recorded as given.** DEBT-46 is in the debt register (IL and EL, before G3).
- **Next free ruling: A313.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A305 | |
| This record | A306 to A312 | **A313** |
