# DEC-2026-11-06 · Architect's rulings of 6 November 2026 (A2 to A25)

| | |
|---|---|
| **Status** | Proposed for the Founders. The Architect gave these rulings in a work order of 6 November 2026 and asked for them to be committed as one record. An instruction given in a session is not authoritative until committed (AGENTS §2, item 3). They count once both Founders approve and merge this pull request. A2 also has a condition (§3). |
| **Date** | 6 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | OD-P-72 (A2, on its condition). Nothing else. |
| **Amends** | None. No SoT, PERD or plan text changes. Where a ruling touches PERD text, it is for the next PERD version; until then this record governs. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Proposed; counts once both Founders approve and merge this pull request
- Date: 6 November 2026
- Closes: OD-P-72 (on the condition in §3)
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: the Architect's work order of 6 November 2026 (relayed to the Repo Steward). This record adds no rationale the Architect did not give.
- Affected requirement IDs / SoT sections: per row
- Migration notes: per row; no merged migration or frozen record is edited
- Supersedes: None

The identity contract (A1) is recorded as D7 of DEC-2026-11-05-architect-rulings (docs#112, not yet merged), not here. A7 (the Steward is the single writer of `tasks.csv` status) is the AGENTS §9 amendment in docs#116, not repeated here. A21 and A20 also settle points of D7; D7 governs where it and D2 differ.

---

## 1. The rulings

| ID | Ruling | Tasks and sources it touches |
|---|---|---|
| A2 | **OD-P-72 is approved: pgsodium.** GOV-28 (the W1 signing design, [DEC-2026-11-01-receipt-and-record-signing](DEC-2026-11-01-receipt-and-record-signing.md)) moves from Proposed to Accepted. The condition: the Security Reviewer first comments that it independently validated the 66 of 66 spike. noema#94 and noema#90 stay held. | GOV-28; OD-P-72; DEBT-01; DEBT-03; SEC-12 |
| A3 | **Circuit-breaker and dispatch-budget values live in pack data.** Breaker: `MinSamples` 20, `Cooldown` 30 s on the simulated clock, 1 half-open probe. Dispatch budget: 2, per key `tenant_id` + `correlation_id` + `capability` + `target_ref`, counting `DISPATCH_ATTEMPTED` events. | CAP-01 (noema#182); EXE-02; AGENT-16; INV-07 |
| A4 | **Each emitter login gets its own file-mounted secret.** A new Tier 1 debt, DEBT-13, covers extending the same to the tenant logins and the power logins before G3 evidence. | EXE-08; DEBT-07; DEBT-13; AGENTS §10 |
| A5 | **The Decision Record is signed with HMAC-SHA256 over JCS, using the grant keys and a domain label.** `decision-record.v2` adds `intent_id`, `correlation_id` and `policy_id@version`. | TRU-05 (noema#163, noema#168); REQ-TRU-004; AGENT-15 |
| A6 | **All tenant tables get tenant-bound writes plus row-level security with FORCE, as in noema#167.** The Engineering Lead owns `decision_record` and `decision_grant`. Core Engineer 1 owns the Execution and Record tables and hardens the Record functions with a schema-qualified `tenant_login` and `set search_path`. This is done before G3 evidence. DEBT-06 closes only when the Security Reviewer's row-security tests pass on `main`. | DEBT-04; DEBT-06; REQ-SEC-004; SEC-08 |
| A8 | **EXP-01 templates live in the pack**, as data, en-NG only. The code that renders them is in `services/core/explanation/`. | EXP-01 (docs#113); INV-14; AGENT-04 |
| A9 | **`voice/` may import `providers.speech`.** | VOI tasks; INV-29; AGENT-05 |
| A10 | **The Integration Lead owns the stand-in and the Tushe adapters** (ENV-04, ENV-05), built on the PERD §34.4 shapes. The Tushe route mapping follows Tushe's response. | ENV-04; ENV-05; ENV-12 |
| A11 | **The relay's TLS terminator is Caddy,** with HTTP-01 on ports 80 and 443 and no DNS plugin. | ENV-13; AGENT-14 |
| A12 | **`contracts-v1.0.0` is not tagged yet.** The tag will mean the frozen contract files at the G1 SHA, each schema keeping its own version. It is tagged after CON-04 and CON-06 are Done. | CON-04; CON-06; PERD M1 |
| A13 | **Decision Record v2 signing form** (refines A5). The signed bytes are the label `noema/decision-record/v2`, a `0x00` byte, then the JCS bytes. Bound fields: `intent_id`, `correlation_id`, `policy_id@version`, `issued_at`, `expires_at` (simulated clock) and `key_id`. A record missing any of them is invalid. | TRU-05 (noema#163, noema#168); A5; REQ-TRU-004 |
| A14 | **Review rule.** Codex review is required for code pull requests touching `services/`, `migrations/`, `contracts/`, `.github/` or `deploy/`. Docs-only and data-only pull requests need green CI at the final head plus a reviewer-role READY stated in the pull request body. | AGENTS §11; plan §13.1 |
| A15 | **Benchmark roles are the four A1 roles only.** `ops_agent` becomes `ops`; `viewer` becomes `customer` (acting) or `audit` (read-only). | BEN tasks; A1 |
| A16 | **Core Engineer 2 is the independent validator of the pgsodium spike.** C2 reads the harness, runs a fresh `workflow_dispatch`, and posts the result on docs#117. The pgsodium test is a dedicated workflow job with a pinned image digest, not a docker call in a Go test helper. | A2; OD-P-72; SEC-12; noema#106 |
| A17 | **UND-13 qualification records.** Schema `qualification-record.v1.json` in `contracts/` (AGENT-15 steps and a CODEOWNERS line); records in `benchmark/qualification/records/`; the pass^k bar is pack data, set by a decision record. Interim QUALIFIED means Tier 0 zero, a complete run, drift PASS and pass^k not below baseline. A first qualification waits for a Founder-set floor. | UND-13; AGENT-15 |
| A18 | **EXP-01 templates are keyed by (outcome_class, locale);** `template_id` is an output. One contract bump carries the explanation-facts shape and a nullable `voice.audio_ref` (C2 defines both). No tag (A12). | EXP-01; A8; AGENT-15 |
| A19 | **The POC phone sends PCM16 at 16 kHz.** Opus gets a document-only AGENT-14 draft. | VOI tasks; AGENT-14 |
| A20 | **`audit` reads only through tenant-bound Record read functions.** `ops` and `audit` have no path to Record writers (service emitters only). Where D2 and D7 conflict, D7 governs. | EDG-01; DEBT-04; DEBT-07; D7 |
| A21 | **Clock-skew leeway on `exp` and `iat` is 60 s,** pack data, tested on the simulated clock. This sets the value D7 left open. | EDG-01; D7; INV-21 |
| A22 | **The Integration Lead adds a per-start generation to `GET /control/v1/requests`,** with a test. | ENV-09; noema#170 |
| A23 | **Docs merge order:** docs#116, docs#114, docs#112, docs#117, docs#115. docs#112 gets `main` merged in (no rebase), with the D1 to D8 text byte-identical. | OPS-09 |
| A24 | **Rollback after a cancelled context is bounded:** `context.WithTimeout(context.WithoutCancel(ctx), N)`, with `N` from configuration and a test that a hung rollback times out. It applies to noema#172 and everything stacked on it. | EVD-01 (noema#172, #174, #176); AGENTS §7 (a context deadline on every call) |
| A25 | **A review finding of the form "tests could not run locally" is not a defect.** The CI check runs at the final head are the test evidence. Codex reads the check runs. | AGENTS §8; plan §12 |

## 2. Notes for the people who act on these rulings

- **A2.** The record does not edit DEC-2026-11-01. GOV-28 counts as Accepted from the merge of this record, and only once the condition holds. The W1 record asks the Repo Steward to apply the PERD v1.20 text of §12 the day it is accepted; that is a separate pull request.
- **A3.** The values are pack data, not code constants (AGENT-16: agents do not set thresholds). Changing one is a pack change reviewed by the Founders. "Simulated clock" means the injected clock (INV-21), never wall time.
- **A4.** DEBT-13 is filed in `docs/poc/execution/debt.md` by this pull request, Tier 1, with the Engineering Lead as owner. DEBT-12 is filed by DEC-2026-11-05 (docs#112); DEBT-13 keeps the next number.
- **A5.** `decision-record.v2` is a contract change: it needs a version bump, a migration note and regenerated models (AGENT-15), and needs both Founders. The HMAC key is the grant key; the domain label keeps a Decision Record signature from verifying as a grant signature. The label's value is not set here.
- **A6.** noema#167 is the model for the row-security pattern. The work order names the Security Reviewer's pull request as `#184`; noema#184 is closed ("DRAFT, NOT FOR MERGE", SEC-08), so DEBT-06's closure evidence needs a live pull request. This record does not assume one.
- **A8.** The templates are data that Understanding and Explanation read; no template text sits in code. The question of where they live (EXP-01 task card, Q1) is answered by this ruling.
- **A9.** This is the one speech import `voice/` may have. Provider credentials still live only in the model service.
- **A10.** The endpoint semantics of the Tushe adapters are not inferred; they follow Tushe's final written response (DEC-2026-11-04-architect-rulings R13).
- **A11.** Caddy is a new component. This record is the approval AGENT-14 asks for, and OD-P-76 in `docs/open-decisions.md` is the entry it asks for; the Compose and relay changes go through their own pull requests.
- **A12.** Tagging is for the Founders. The Repo Steward names the SHA when CON-04 and CON-06 are Done.
- **A13 to A25.** These are given as written in the Architect's standing updates of 6 November 2026. A13 refines A5 and does not replace it. A14 changes how this record's own pull request is judged: docs-only and data-only pull requests need a reviewer-role READY in the body; the Repo Steward has not given itself one and states below when a reviewer role has. A16 names who gives A2's independent validation; A2's condition is otherwise unchanged (§3). A20 and A21 settle two points D7 left to the Architect, and the D7 note in docs#115 is updated to match. A22 is the Integration Lead's work on noema#170. A24 and A25 were added at 14:00 WAT and apply to code pull requests, not to this record. The `N` of A24 is configuration the author of noema#172 sets and states in the PR; no value is set here.

## 3. Condition on A2

A2 is not in force until an independent validator has confirmed the 66 of 66 result. A16 names Core Engineer 2 as that validator and asks for the result on docs#117. (The Security Reviewer built the spike and has said, on docs#117, that it cannot give this validation.) Until that comment exists, GOV-28 stays Proposed and OD-P-72 stays open. Merging this record without the comment is a Founders' call and should say so.
