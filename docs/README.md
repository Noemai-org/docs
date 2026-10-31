# Noema documentation map

## The one authority

[`NOEMA_SOURCE_OF_TRUTH.md`](NOEMA_SOURCE_OF_TRUTH.md) (the **SoT**, v1.10, 31 October 2026, status: canonical) is the single source of truth for what Noema is, what we are building first, why, and how. When anything disagrees with it, the SoT wins until it is formally revised (SoT, "How to use this document").

**Every other active document here is derived and non-normative.** Each one is an index, register, checklist or map that points back to SoT sections. None of them defines Noema, its architecture, its requirements or its states. If any of them disagrees with the SoT, the derived document is wrong and must be fixed.

Do not edit the SoT in place. A change to the SoT is a new SoT version with an entry in its Appendix D, recorded in [`decisions/`](decisions/README.md) and merged through a reviewed pull request (SoT §0.4).

## Which document owns which question

| Question | Owner |
|---|---|
| What is Noema, and what is it not? What is Intent Computing? | SoT §1, §3.1, §12, §57 |
| What is the architecture? What does each power own and what is it forbidden to do? | SoT §13–17 (navigation aid: [`engineering/boundary-map.md`](engineering/boundary-map.md)) |
| What are Mode 1 and Mode 2? | SoT §16 |
| What are the Intent, Trust and Outcome Taxonomies and Vertical Packs? | SoT §15 |
| What are the canonical contracts and objects? | SoT §43 (JSON Schemas go in `/contracts` when written; see [OD-P-01](open-decisions.md#od-p-01)) |
| What state, outcome and status values exist? | SoT §13.1, §35.5, §43 (lookup: [`engineering/state-registry.md`](engineering/state-registry.md)) |
| What are the invariants and security boundaries? | SoT §45, §47 |
| What is the POC, and where is the fence between Noema and the POC? What is the first wedge? | SoT Part VII, §30–40 (brief and checklist: [`poc/README.md`](poc/README.md)) |
| What did we ask Tushe to build for the synthetic environment? | [`poc/tushe/`](poc/tushe/README.md): issued external specification — frozen (SoT §36). Our response and the acceptance worksheet were sent on 13 Oct 2026; the joint session planned for Fri 16 Oct, 18:00 is postponed until Tushe confirms a date; G0 has two halves, G0-T and G0-N (DEC-2026-10-16 E4) |
| What comes after the POC? | SoT Part VIII, §41–42 |
| Which requirement IDs exist, and what is their scope? | SoT (definitions); [`requirements-index.md`](requirements-index.md) (traceability) |
| What does each status tag mean? | SoT §0.2 |
| What rules bind coding agents? | SoT §0.3, §44 (operating instructions: [`../AGENTS.md`](../AGENTS.md)) |
| What is undecided, and how do we decide it? | SoT §46 (register: [`open-decisions.md`](open-decisions.md); process: [`decisions/README.md`](decisions/README.md)) |
| What do terms mean? | SoT Appendix A |
| Where do external numbers come from? | SoT Appendix C and the evidence rules in §0.6 |
| What did the earlier documentation say? | [`archive/`](archive/README.md) (**non-authoritative**) |

## Reading paths

These follow the table in the SoT, "How to use this document".

- **Believers, investors, partners:** SoT Parts I–VI, then Part X, then Part VII.
- **Founding team:** the whole SoT in order. Keep Part IX open while working.
- **Engineers:** SoT Parts III, VII and IX, then Part VIII. Then [`poc/README.md`](poc/README.md), [`engineering/boundary-map.md`](engineering/boundary-map.md) and [`engineering/state-registry.md`](engineering/state-registry.md).
- **Security reviewers and design-partner CTOs:** SoT §13, §34.2, §43, §45 and §47–50.
- **AI coding agents:** [`../AGENTS.md`](../AGENTS.md), then SoT §0.3–0.6 and Part IX (especially §44), then the section a task's requirement ID points to.

## Directory layout

```
docs/
  NOEMA_SOURCE_OF_TRUTH.md     canonical (do not edit in place)
  README.md                    this map
  requirements-index.md        ID → SoT section, scope, verification (derived)
  open-decisions.md            OD-01..16 generated from SoT §46 + provisional OD-P-xx items (NON-CANONICAL)
  engineering/
    boundary-map.md            powers, components, may / must-never, enforcing IDs (derived)
    state-registry.md          every state and status value with its SoT source (derived)
  poc/
    README.md                  POC fence, scope pointers, definition-of-done checklist (derived)
    tushe/                     Issued external specification — frozen
      README.md                index, rules and issue record for the Tushe documents
      Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md
                               Tushe requirements & acceptance spec v1.0 — issued, frozen
      source/                  original v1.0 export, unchanged
      tushe-spec-delta-v1.1.md draft changes v1.0 → v1.1 (superseded by v1.2; never sent)
      tushe-spec-delta-v1.2.md changes v1.0 → v1.2: what was agreed and withdrawn on 13 Oct 2026
      acceptance/              Phase A acceptance: the worksheet as sent, verbatim AT-01..20, the signed report (none yet; the joint session date is to be confirmed by Tushe)
      responses/               Tushe correspondence: received and sent records, with checksums
    perd/                      POC PERD v1.19 (current, Accepted; ranks below the SoT; v1.1 to v1.18 kept unchanged), generated REQ index, conflicts, templates
    execution/                 four-week plan v1.5 (current, Accepted; v1.1 to v1.4 kept unchanged), generated tasks.csv, calendar, templates, daily/gate/release records
      task-cards/              task cards for the tasks added by plans v1.2 to v1.5 and for PLT-01 to PLT-04 (GOV-19, GOV-20, ENV-08 to ENV-14); the index is generated
  security/                    threat model, trust-boundary and threat-to-test maps (from the PERD; Proposed)
  runbooks/                    runbook scaffolds (headings and TODOs only)
  vendors/                     vendor and partner register: what we need from each, where it goes, who chases it
  decisions/
    README.md                  decision-record process and template
    DEC-2026-10-02-sot-v1.2.md the v1.2 amendment record
    DEC-2026-10-06-*.md        architecture and vendor-benchmark records (superseded in part)
    DEC-2026-10-09-deployment-temporal-providers.md
                               two deployables, Temporal, multi-provider (the v1.3 decisions)
    DEC-2026-10-11-poc-perd-v1.1.md
                               adopt the POC PERD (Accepted; re-pointed to the current PERD)
    DEC-2026-10-11-poc-4week-plan.md
                               four-week execution plan and schedule change (Proposed)
  archive/                     NON-AUTHORITATIVE legacy material and the migration report
```

This repository is documentation-first. It contains no application code ([OD-P-01](open-decisions.md#od-p-01)). Noema uses four repositories (SoT §51; [DEC-2026-10-13](decisions/DEC-2026-10-13-code-monorepo.md)):

| Repository | Job | Change |
|---|---|---|
| `docs` | Governing documents: SoT, PERD, plan, decisions, Tushe correspondence | None |
| **`noema`** (new) | All POC code | Created |
| **`benchmark-heldout`** (new, private) | Held-out cases and oracles. Benchmark owner only; no agent access | Created, if GOV-03 has not already created it |
| `brain` | Founder documentation outside the build. Not part of the build's chain of authority | None. Its purpose is now recorded |
| `backend`, `intent-engine` | Superseded by `noema` | Archived read-only, after any code built under the current architecture is moved into `noema` with its history |


## Changing documentation

1. **A change of meaning:** what Noema is, a requirement, a state, a decision or a number. This needs a SoT revision, or a decision record plus an [OPEN] entry until the SoT is revised. Never put it in a derived document first.
2. **A change to a derived document:** this must keep every SoT reference accurate, and must not add requirements, states, IDs or numbers.
3. **New documents:** create one only when it owns a question no existing document owns. Do not create a second definition of anything the SoT already defines.
4. **External numbers:** these appear only if they are in the SoT with a source (AGENT-18, §0.6).
