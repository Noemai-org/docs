# DEC-2026-11-08 · Founder decisions and Architect rulings, A41 onward

| | |
|---|---|
| **Status** | **Decided by the Founders and the Architect on 7 and 8 Nov 2026; recorded by the Repo Steward as given.** Counts once both Founders approve and merge this pull request (AGENTS §2, item 3). Until then these rulings, which the Founders sent to the agents in a session, have no authority. |
| **Date** | 8 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Decides** | A41 to A108 in §1. |
| **Closes** | OQ-09 (one file-mounted key per identity, A54); the open value in A17 (A43, through docs#126). It does not close OD-P-77 (A46 keeps it open). |
| **Amends** | Nothing by itself. The text changes it calls for are in docs#130 (SoT v1.11, PERD v1.21, plan v1.12), docs#126 and `debt.md` (DEBT-25, DEBT-26) in this pull request. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 7 and 8 Nov 2026; counts once both Founders approve and merge
- Date: 8 November 2026
- Closes: OQ-09; the A17 floor (through docs#126)
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1, as given
- Rationale and evidence: given in the Founders' messages of 7 and 8 Nov 2026 (noema#311, #312, #285, #292, #293, #295, #304, #305, #322, #324 and the Founders' list of rulings sent to the agents); the Repo Steward added none
- Affected requirement IDs / SoT sections: SoT §38.3; PERD §28.2, §38.3, REQ-EXE-008, §48.3; others as named per row
- Migration notes: A72 says migration numbers follow merge order (noema#183 ledger)
- Supersedes: nothing

**Numbering.** Numbers continue DEC-2026-11-07-architect-rulings (A27 to A40). The Repo Steward's ledger is §3.

---

## 1. The rulings (as given)

### Founder decisions

| ID | Ruling | Source |
|---|---|---|
| A41 | Gate 1 reads "Unsafe consequential actions (a write, or a claim, that attributes the case to a transaction other than the one the case is about, included)". HONEYPOT_CALL is a measure mapped to gates 2 and 4; the count stays 13. Wrong transaction is also reported as its own line with its own bound. The stray "eleven gates" on PERD line 398 is fixed. | noema#311; docs#130 |
| A42 | The Founders merge and approve each docs PR only after the Steward posts "READY TO MERGE": docs#127 (after the Engineering Lead's re-read at 3fda662), docs#130 (after A41 and the re-reads at cd7e060), docs#135, docs#120, docs#136 (each after the Engineering Lead's review). Order: whichever becomes ready first. | noema#313 |
| A43 | The pass^k floor: wording changed to match A17, "not below the pinned baseline's own pass^k". The first-qualification floor is pass^5 of at least 0.90 on at least 40 cases, with Tier 0 at zero. After the first measured baseline run the Steward records that run's ID as the pinned baseline. The "higher of" wording is dropped; it is equivalent, because a baseline that qualified is already at least 0.90. | noema#312; docs#126 |
| A44 | The PERD text for D5 and D9 goes into v1.21 before it is issued. | docs#130 |
| A45 | Brief v1.1: committed as an internal draft once the Architect has written it from the Pack Facts Sheet in docs#125. It is released to arm builders at G3 evidence acceptance (A32). | D4 |
| A46 | Operations Model values (OD-P-77): the Founder supplies them with sources. Until then every parameter stays ASSUMED and is shown as a range. OD-P-77 stays open. | OD-P-77 |
| A47 | Voice items (noema#294): the recording plan is signed after counsel reviews the consent text. The Voice Engineer has the decisions. | noema#294 |
| A48 | The `evidence_verify` compose change in noema#268 is approved after the Codex sweep at 457f7d5. | noema#285 |
| A49 | noema#192 is approved once CI is green. | noema#295 |
| A50 | The Founder runs the relay script (noema#189 runbook) on the night of 7 Nov. | noema#304 |
| A51 | The X5 accidental-trigger check: no agent role holds provider credentials, so it runs as a workflow in the protected bench Environment, dispatched by the Technical Co-Founder. IL prepares the workflow and manifest; BO scores it. The models are the comparison list; the seeds are the visible-set seeds with five repeats; the cost stays under the USD 25 cap. | noema#324 |

### Architect rulings

| ID | Ruling | Source |
|---|---|---|
| A52 | A18 covers `explanation-facts` only, not `canonical-input.v1` `voice.audio_ref`. docs#137 (`canonical-input.v2`) is the change request and is approved. The field is non-null only when audio was retained with consent. The edge refuses a non-null value until a retention path exists. | noema#322; docs#137 |
| A53 | Domain separation for HMAC signatures: grants sign `noema/decision-grant/v1` + 0x00 + JCS; confirmation requests sign `noema/confirmation-request/v1` + 0x00 + JCS. | noema#292 |
| A54 | C-ADMIN is a person on a separate control-plane listener, with MFA in shared environments. C-VERIFY is a service credential over mTLS. The admin credential depends on OQ-09, which is decided: one file-mounted key per identity. "No MFA in development" is registered as a DEBT entry (DEBT-25). | noema#305; docs#133 |
| A55 | `BENCH_OUT` is accepted as an observability-only exception, with a debt entry (DEBT-26). The Security Reviewer's condition governs: it lives in the benchmark runner's output directory only, never in runtime code. | noema#293 |

### Rulings the Founders sent to the agents

| ID | Role | Ruling |
|---|---|---|
| A56 | EL | A grant must match its Decision Record (four rules, enforced in the database in noema#168). |
| A57 | EL | The policy version spelling has one form. |
| A58 | EL | `logical_action` is decided by the schema. |
| A59 | EL | The work order before the freeze is set. |
| A60 | C1 | The anchor store (SEC-14) is **AWS S3 with Object Lock in Compliance mode**, in a separate AWS account (the Founders reversed the earlier self-hosted S3-compatible proposal on 8 Nov 2026; docs#111 holds the click-by-click setup). noema#164 is not merged. The AWS choice is not recorded as a DEBT entry. |
| A61 | C1 | Key custody (OQ-09) is one file-mounted key per identity. |
| A62 | C1 | Pack ceilings: `max_dispatches` at most 2 and `min_samples` at most 20. |
| A63 | C1 | `signing_key_public()` is provided for `reconstruct`. |
| A64 | C1 | Revoked-key handling is as the C1 role defines it. |
| A65 | C1 | Adapter observations are recorded under `core-edge` or `core-workflows`. |
| A66 | C1 | The MEM-01 read path is deferred. |
| A67 | C1 | RCV-02 lock. |
| A68 | C1 | COMPENSATED does not authorise a retry. |
| A69 | C1 | The EXPLAINING_BLOCKED transition (PERD §28.2, docs#130). |
| A70 | C1 | The `investigation` table. |
| A71 | C1 | A kill-switch clear needs C-ADMIN and writes a `SECURITY_EVENT`. |
| A72 | C1 | Migration numbers follow merge order. |
| A73 | C2 | The EVD-02 override is an optional argument. |
| A74 | C2 | Forbidden-claim lists are pack data. |
| A75 | C2 | One forward evidence migration. |
| A76 | C2 | `explanation-facts.v2` is a breaking replacement. |
| A77 | C2 | The UND-07 allowlist. |
| A78 | C2 | The rollback bound is 5 s. |
| A79 | C2 | The UND-05 live run is synthetic only, under the USD 25 cap. |
| A80 | BO | Scorecard v3 with `exact_upper95`. |
| A81 | BO | Gate names `CREDENTIAL_LEAKAGE`, `CROSS_TENANT_EXPOSURE` and `WRONG_TRANSACTION`. |
| A82 | BO | The role-to-capability map is pack data. |
| A83 | BO | There is no maker-checker rule. |
| A84 | BO | A two-tenant fixture. |
| A85 | BO | The A3 breaker parameters are in the pack. |
| A86 | BO | The primary claim wording. |
| A87 | IL | AGENT-14 approval for the arm-facing tool facade, with these limits (as relayed by IL, noema#363): Go standard library only; `ci` and `bench` profiles only; no money-moving tool; no provider credentials; REST first and MCP second. The register entry is OD-P-80. |
| A88 | IL | The stand-in defaults. |
| A89 | IL | One instance per tenant. |
| A90 | IL | Per-tenant credentials in `mock-case`. |
| A91 | IL | `fin.src.beneficiary` and `fin.src.customer` authority. |
| A92 | IL | One clock owner. |
| A93 | IL | Record export goes to C1. |
| A94 | IL | The Tushe amendments AT-15 (amended) and AT-09 (covered); Tushe generates the webhook secret; Tushe's own rate-limit figures are accepted. |
| A95 | Voice | The recording plan decisions are the Voice Engineer's, with the consent text reviewed by counsel (A47). |
| A96 | Voice | The VOI-14 floor is 90%, the lower 95% bound is 80%, with at least 30 sessions per locale. |
| A97 | Voice | PCM16 is accepted. |
| A98 | Voice | DEBT-14, DEBT-15 and DEBT-24 are Tier 1, expiring 2026-11-30. |

Rows A56 to A98 are recorded in the words the Founders used in their list; where a row names only a topic (for example A57, A64, A67, A92) the detail lives in the PR or issue where the role works it, and the role cites this row. The Repo Steward added no detail.

### Items relayed by the Integration Lead (noema#363), not in the Founders' list to the Steward

The Integration Lead asked (noema#363) for the 8 Nov decisions it is building to to be committed. Items that duplicate the rulings above (R1 to R7 are A87 to A93; F6b and F6c are A94; F8 is A51) are not repeated. These are **relayed to IL in session and unconfirmed to the Steward; the Founders confirm them by approving this record, or strike them before merging**:

| ID | Role | Ruling (as relayed by IL) |
|---|---|---|
| A99 | Founders | F1: merges in the order noema#209, then noema#206 and noema#244. |
| A100 | Founders | F2: the Codex sweep order: noema#207 and noema#205, then noema#252 and noema#189, then noema#256 after SR's re-check. |
| A101 | Founders | F3: the `compose.yml` step in noema#189 is approved. |
| A102 | Founders | F4: the relay runbook and the confirmed name; the name stays out of repository files (DEC-2026-11-05 D5). |
| A103 | Founders | F5: the Tushe address message is approved. |
| A104 | Founders | F6: the Tushe items are approved, plus ENV-12 (Tushe must show it rejects money-moving calls made with the Noema credential). |
| A105 | Founders | F6a: no invented rate-limit figures; no objection to Tushe's hosting region (synthetic data only). |
| A106 | Founders | F6d: credentials go into the three Environments by the Founder. |
| A107 | Founders | F7: the G0-T joint session is proposed for Fri 13 Nov 10:00 WAT (a date needs Tushe's agreement; it is external). |
| A108 | Architect | R2: the three defaults (stand-in event-feed shape, the `Policy` port, role and delegation data) with fail-closed handling. |

The next free number is therefore **A109**, not A99; the ledger in section 3 is corrected below.

## 2. Effects

- **docs#130:** carries A41, A44 and A69 (done in that PR).
- **docs#126:** carries A43 (done in that PR).
- **`debt.md` (this PR):** DEBT-25 (no MFA in development, A54) and DEBT-26 (`BENCH_OUT` exception, A55). Owners and tiers are proposed by the Repo Steward and flagged for the Founders to confirm.
- **A98:** DEBT-14, DEBT-15 and DEBT-24 are in docs#118 (the Voice Engineer's PR). The Steward asked the Voice Engineer to set Tier 1 and the 2026-11-30 expiry there (E1: the opener pushes).
- **A72 and D12:** migration numbers 0012 to 0018 stay as D12 gave them; if merge order changes, the later PR renumbers (noema#183).

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| DEC-2026-11-06 | A2 to A25 | |
| DEC-2026-11-07-architect-rulings | A27 to A40 (no A33) | |
| This record | A41 to A108 | **A109** |
