# DEC-2026-11-04 · Architect's rulings of 4 November 2026

| | |
|---|---|
| **Status** | Proposed for the Founders. The Architect gave these rulings in a work order of 4 November 2026 and asked for them to be committed as one record. An instruction given in a session is not authoritative until committed (AGENTS §2, item 3). They count once both Founders approve and merge this pull request. |
| **Date** | 4 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None. Opens DEBT-06 (Tier 1) in the debt register, in this pull request. |
| **Amends** | None. No SoT text changes. PERD and plan wording that these rulings touch changes only in a new PERD or plan version, by its own pull request. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Proposed; counts once both Founders approve and merge this pull request
- Date: 4 November 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: the Architect's work order of 4 November 2026 (relayed to the Repo Steward). Where a ruling cites a task, PERD section or record, it is named in the row. This record adds no rationale the Architect did not give.
- Affected requirement IDs / SoT sections: per row
- Migration notes: per row; no row edits a frozen record or a merged migration
- Supersedes: None

---

## 1. The rulings

| ID | Ruling | Tasks and sources it touches |
|---|---|---|
| R1 (a) | **A lone CONFIRM keeps `NO_PERMITTING_RULE` and the result marker.** A CONFIRM rule without a PERMIT rule does not permit; the decision carries `NO_PERMITTING_RULE` and the result marker, as built. | Trust rule evaluation (TRU tasks); PCK-04 |
| R2 (b) | **`log_complaint_reference` gets a PERMIT rule with exactly the CONFIRM rule's predicates.** No predicate is added, dropped or loosened. | PCK-04 pack rules |
| R3 (c) | **PCK-02 is split.** The mechanism is built now. Enforcement moves to EXP-04. PCK-04 needs the mechanism only. Template format: one JSON file per locale at `packs/fintech/templates/<locale>.json`, keyed `<outcome_id>/<classification>`. Locales: `en-NG`, `pcm`, `yo`, `ha`, `ig`. | PCK-02, PCK-04, EXP-04 |
| R4 (d) | **The PCK-04 descriptor key is the id declared in the pack. The source is the evidence response named by the descriptor's declared source.** | PCK-04 |
| R5 (e) | **DEBT-03 is accepted, with the `session_user` check.** Receipt authenticity fails closed: `NOT_CHECKED` never yields `ACHIEVED`. | DEBT-01, DEBT-03, REC-08; INV-04 |
| R6 (f) | **The OpenTelemetry Go dependency is approved under AGENT-14.** It is pinned, and no exporter is included. | OBS tasks; PERD §36.1 (OpenTelemetry) |
| R7 (g) | **`init.sh` creates all roles. No migration needs `CREATE ROLE`.** | PLT-06, migrations |
| R8 (h) | **The tenant-table isolation gap is DEBT-06, Tier 1, closed before G3.** It covers the tables other than the Record functions that DEBT-04 covers. | DEBT-04, DEBT-06, SEC-08, REQ-SEC-004 |
| R9 (i) | **`record_insert_t` binds the writing power.** | REC-08, DEBT-03 |
| R10 (j) | **G1 story tests live in `execution/e2e` and `adapters/outcome_e2e`.** | G1; EXE and OUT tasks |
| R11 (k) | **SEC-14: the credential is put-only.** | SEC-14 |
| R12 (l) | **GitHub Environments `tushe-runtime`, `tushe-fixture` and `tushe-admin` are main-only, with the Founder as required reviewer.** | ENV tasks; OD-16, REQ-AGT-004 |
| R13 (m) | **The ENV-05 pause is lifted. G0-T acceptance is Tushe's final written response by Wed 11 Nov 2026.** | ENV-05, ENV-07, ENV-12; G0-T |
| R14 (n) | **The TEN-02 Trust half merges as partial.** It is not recorded as TEN-02 done. | ENV-14, TEN-02 |

## 2. Notes for the people who act on this record

- **R3.** The pack format is data, not code (SoT §51). The template files are synthetic and labelled as such (AGENT-25).
- **R5.** "Fails closed" is the existing rule of INV-07 and INV-04 applied to the receipt check: a missing or unchecked authenticity result is never success.
- **R6.** The dependency list is exact: the OpenTelemetry Go API and SDK modules the core already needs, pinned in `services/core/go.mod`, with no exporter module. A later exporter needs its own AGENT-14 entry.
- **R8.** DEBT-06 is filed in `docs/poc/execution/debt.md` by this pull request as Tier 1, not Tier 0, by the Architect's ruling. G3 requires it closed.
- **R12.** Environment protection settings are changed by the Founder in GitHub; no agent changes them (AGENTS §11).
- **R13.** The date is "no later than". No Phase B result counts before G0 passes (plan §3).
- **Sequence.** Any PERD text these rulings need goes in the next PERD version (docs#96 is v1.20); any plan row change goes in plan v1.11 or its successor. Neither is done here.
