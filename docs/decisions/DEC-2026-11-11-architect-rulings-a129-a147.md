# DEC-2026-11-11 · Architect rulings A129 and A135 to A147, and the Founder's decision on the UND-05 live run (noema#338)

| | |
|---|---|
| **Status** | **Decided by the Principal Architect on 10 and 11 Nov 2026; A143 approved by the Founder on 11 Nov 2026; the UND-05 decision is the Founder's. All relayed to the Repo Steward and recorded by the Repo Steward.** Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 11 November 2026 |
| **Owner** | Principal Architect (A129, A135 to A147); Founder (A143 approval, §3); Founder and Technical Co-Founder (the merge) |
| **Decides** | Fourteen rulings (§1) and the Founder's UND-05 decision (§3). Each states what it supersedes. |
| **Closes** | The pending rows A129, A135 and A136 of `DEC-2026-11-10-architect-block-f-a129-a136` (their text is in §1 here). The question on noema#338. |
| **Supersedes** | Per ruling, in §1. In short: A141 supersedes A113's strict ascending order, A34 and A72; A143 supersedes A123 and the two-review rule in plan §4. |
| **Amends** | New plan version `docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v1.16.md` (A143; v1.15 stays unchanged); the three pending rows of the Block F record point here. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 10 and 11 Nov 2026; counts once a Founder who did not author this pull request approves and merges
- Date: 11 November 2026
- Closes: the pending rows of the Block F record; the question on noema#338
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A129, A135 to A147; the UND-05 decision
- Decision: §1 and §3
- Rationale and evidence: the Architect's message of 11 Nov 2026 relayed by the Founder; the Founder's message of 11 Nov 2026 relayed by the Architect
- Affected requirement IDs / SoT sections: REQ-AGT-001, REQ-OPS-004, REQ-SEC-004; INV-12, INV-29; AGENT-14, AGENT-15, AGENT-29; SoT §0.4
- Migration notes: A141 and A145 change how migrations merge; no migration is added by this record
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A129** | A hotfix that restores a red `main` needs only green CI and one independent reproduction; Codex after the merge. | Narrows **A14** (Codex before merge on code PRs) and the order of gates of **A128** (reviewer READY before the merge), for that one case only. |
| **A135** | The stand-in client sends the tenant from the session (INV-12); the stand-in refuses a mismatch; the client refuses a response for another tenant; if a contract change is needed, stop and raise it. | Nothing. It applies INV-12 to the stand-in. |
| **A136** | New tenant tables get RLS plus FORCE in their own migration (A6). | Nothing. It applies **A6** and adds "in their own migration". |
| **A137** | Codex gives all P1 and P2 findings on a PR in one pass; later passes verify fixes only. | Nothing. It refines **A134** and the Codex rules of **A29**. |
| **A138** | Generated Pydantic patterns are fully anchored (`\A...\Z` or fullmatch). | Nothing. |
| **A139** | The relay's Caddy runs as root in its container with `cap-drop ALL`, only `NET_BIND_SERVICE`, `no-new-privileges` and a read-only root filesystem (DEBT-29, Tier 2). | Nothing. The shortcut is registered as DEBT-29 (docs#155). |
| **A140** | noema#417's 1 MiB payload bound stays; tighten when real sizes are known. | Nothing. |
| **A141** | Merge in dependency order only: a child after its parent; noema#229 before #233 and #263; noema#234 before #263 and #272. | **A113's strict ascending merge order, A34 and A72.** A113's acceptance of the migration-number gap stands. |
| **A142** | Stack merge: if each PR has its gates at its own diff and the top PR's branch contains each parent's current head, the Founder merges the top PR once and the lower PRs close as "included". | Nothing. It builds on **A124** (a stacked child's own commit range). |
| **A143** | **Gates by tier.** **Tier 1** (trust, execution, outcome, record, migrations, identity): Codex READY + SR READY + one independent role review (EL, C1 or C2, not the author) + CI + one Founder approval. **Tier 2** (contracts, packs, benchmark, voice, docs): Codex where A14 applies + one independent reviewer READY (SR counts) + CI + one Founder approval; `.github` and `deploy` still need SR. Founder approved on 11 Nov. Write plan v1.16. | **A123** and **the two-review rule in plan §4** (and its restatement in the definition of done). Where **PERD §71.2** states the same two-review rule, this ruling prevails by the order of authority (SoT §0.4); the PERD text is not edited here. |
| **A144** | Branch protection plus auto-merge (Founder action): required checks, one approval, code-owner review; the Founder approves and enables auto-merge on a PR whose gates are met. | Nothing. Until the Founder enables it, `pr-base-guard` and `main-merge-audit` stay the enforcement (AGENTS §11). |
| **A145** | No PR edits `migrations/README.md` or other shared tables; the ledger lives on noema#183. | Nothing committed. It ends the practice of each migration PR adding a row to `services/core/migrations/README.md`. |
| **A146** | **G1 slice.** Composition root `cmd/core/compose.go` owned by EL; packages: EL (STM-01, EDG-01 3c), C1 (EDG-01 3b, EXE-05, REC-03), C2 (UND-02, UND-04, evidence call site, OUT-01, EXP-01), IL (ENV-04 wiring), BO (BEN-29, BEN-05). | Nothing. The plan's task rows are not changed here; a clash with a row's owner goes to a change request (plan §19). |
| **A147** | No agent waits for a review; after `READY FOR CODEX` it starts its next task. | Nothing. It bears on **A133**. |

**Note on the word "Tier".** A143's Tier 1 and Tier 2 are **review-gate tiers**. They are not the debt tiers of `debt.md` (DEBT-29 is a Tier 2 debt) and not the Tier 0 safety gates of plan §1.1.

## 2. What the Steward did where the rulings are silent

- **A143 and the plan.** Plan v1.16 changes only the two places that state the two-review rule: the "Accountability rule" in §4 and item 7 of the definition of done. It adds the tier gates as given. No task, gate, date or requirement changes; the task count stays 265.
- **A143 and the other texts.** `AGENTS.md` §11 ("P0-path PRs need two human reviews") and PERD §71.2 still carry the older wording. The Steward does not edit them here: `AGENTS.md` is vendored into `noema`, and changing it re-points that copy. The Steward asks the Architect whether to correct `AGENTS.md` §11 in a follow-up.
- **A139 and DEBT-29.** The register row is in docs#155 (open); this record is the ruling's text.
- **A141 and the ledger.** The migration ledger on noema#183 is rebuilt in dependency order; migration numbers are unchanged.
- **A142.** Closing the lower PRs "as included" is the Founders' and owners' step; the Steward does not close another role's PR.
- **A146.** Recorded as given; it names no dates.

## 3. The Founder's decision on the UND-05 live run (noema#338), as relayed

Relayed by the Architect from the Founder's message of 11 Nov 2026. **Owner: the Founder.** Secret **names** only; no value is written anywhere.

> "OPENAI_API_KEY is set in bench-live. ANTHROPIC_API_KEY and GOOGLE_API_KEY are not set. USD 5 hard stop approved for UND-05."

- The Environment `bench-live` holds `OPENAI_API_KEY` only. `ANTHROPIC_API_KEY` and `GOOGLE_API_KEY` are not set and stay out until a later reviewed workflow change adds them (SR's custody plan on noema#338).
- The UND-05 live run has a **USD 5 hard stop**, inside the USD 25 total live-run cap of A79. Data is synthetic only, with account data masked before any provider call (F7).
- It supersedes nothing. It is the approval and the confirmation that SR and C2 asked for on noema#338.

## 4. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| DEC-2026-11-08-rulings-a41-onward | A41 to A108 | |
| A109 to A112 | REC-09, control-plane callers, one non-author Founder approval, DEBT-13 and SEC-15 | |
| A113 to A128 | the three sync records and the A127 and A128 record (merged) | |
| DEC-2026-11-10-architect-block-f-a129-a136 (merged) | A130 to A134 text; A129, A135, A136 pending | |
| This record | A129, A135 to A147 | **A148** |
