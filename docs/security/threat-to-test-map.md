# Threat-to-test map (POC)

Tracks, for each threat in [`threat-model.md`](threat-model.md) (PERD §42), its control requirements, its test, the plan tasks that build or verify the control, and whether a passing test exists. Opened by SEC-01 against PERD v1.19.

How the cells were filled (SEC-01, 2 Nov 2026):

- **Control (REQ IDs):** chosen by the Security Reviewer by reading each PERD v1.19 requirement against the **Mitigation** column of §42. A REQ without a mark was checked against its requirement text. A REQ marked **†** was chosen from its title and is checked against its text when its test is written. Where §42 states a mitigation that no REQ carries, the cell says **GAP** and the note names it. A gap is not filled by inference.
- **Test / benchmark case:** copied verbatim from the `Test` column of PERD §42.
- **Plan tasks:** every task in `tasks.csv` whose `req_ids` cite a control REQ. It is a pointer to where the control is built and verified, not a claim that the task is done.
- **Status:** `Not started` until a test for the threat exists and passes in CI or the benchmark; change it only with a link to the passing run. `Partially mitigated` names a residual risk in the note, and stays until the evidence closes it.

| TM | Control (REQ IDs) | Test / benchmark case | Plan tasks | Status | Note |
|---|---|---|---|---|---|
| TM-01 | REQ-API-004, REQ-TRU-003†, REQ-TRU-012†, REQ-SEC-008, REQ-SEC-004† | EC-U05, EC-X01 | PLT-06, EDG-01, TRU-04, TRU-11, SEC-08 | Not started |  |
| TM-02 | REQ-INT-001†, REQ-INP-002†, REQ-CAP-001†, REQ-CAP-002†, REQ-INT-005† | EC-X05, EC-X08, EC-X10 | ENV-11, PCK-01, UND-04, UND-05, PCK-02, EXE-01, PCK-03, UND-07, SEC-06 | Not started |  |
| TM-03 | REQ-CTX-007, REQ-INT-001†, REQ-CAP-002† | US-09, EC-X02..X04 | EVD-06, UND-04, EXE-01, UND-07, SEC-06 | Not started |  |
| TM-04 | REQ-CAP-001†, REQ-AG-001†, REQ-SEC-007, REQ-CTX-008 | EC-X13 | PLT-02, SEC-01, ENV-11, PCK-01, EVD-05, PCK-02, PCK-03, SEC-06, SEC-07, REL-01, PCK-04 | Not started |  |
| TM-05 | REQ-API-004, REQ-TRU-009, REQ-SEC-001 | EC-U03 | EDG-01, TRU-07 | Not started |  |
| TM-06 | REQ-INP-002†, REQ-SEC-006, REQ-SEC-001 | EC-X08 | EDG-01, UND-04, SEC-04 | Not started |  |
| TM-07 | REQ-EXE-001†, REQ-INP-003, REQ-API-003, REQ-EXE-006† | EC-X07, PUS-07 | EDG-01, EXE-02 | Not started |  |
| TM-08 | REQ-EXE-002†, REQ-RCV-002†, REQ-RCV-003, REQ-EXE-005†, REQ-EXE-006† | US-05, US-06 | CON-04, EXE-02, EXE-03, OUT-01, RCV-02 | Not started |  |
| TM-09 | REQ-TRU-004, REQ-TRU-005, REQ-SEC-006, REQ-AUD-001†, REQ-DATA-001 | Tamper test | PLT-06, REC-01, TRU-03, REC-06, TRU-08, SEC-04 | Not started | **GAP-2.** The policy table has a `checksum` column (PERD §38.2), but no REQ says the loader verifies it for policy rows (REQ-TRU-004 validates rule contents; the checksum check is stated only for packs, REQ-SEC-007). The 'detected; not in force' behaviour has no requirement to test against. |
| TM-10 | REQ-AUD-001†, REQ-AUD-005†, REQ-AUD-006†, REQ-AUD-007† | REQ-AUD-005 | REC-01, REC-06, REC-05, SEC-14, REC-07, SEC-12, GOV-28, EXE-07, EXE-08, SEC-13, REC-08 | Not started | Writers are not yet authenticated (DEBT-03); anchoring is REQ-AUD-007 (SEC-14 evaluated the store, REC-07 builds it). Wording stays tamper-evident. |
| TM-11 | REQ-SEC-003†, REQ-DATA-003† | REQ-SEC-003 | REC-02, SEC-03, SEC-07, DATA-01 | Not started |  |
| TM-12 | REQ-AMB-002, REQ-CTX-006, REQ-TRU-003†, REQ-AMB-001† | US-07 | EVD-04, TRU-01, TRU-04, AMB-01, UND-11 | Not started |  |
| TM-13 | REQ-EXE-003, REQ-TRU-005, REQ-CTX-003 | US-19, US-20 | EVD-02, EXE-02, TRU-08, EXE-05 | Not started |  |
| TM-14 | REQ-SEC-006, REQ-AUD-001†, REQ-AUD-004† | Authorisation-matrix test | REC-01, REC-02, REC-06, SEC-04 | Not started | **GAP-1.** 'Admin MFA' is stated only in the PERD §41.1 identity table ('a separate admin credential, MFA-protected in shared environments'). No REQ carries it, so no test is planned. REQ-SEC-006 requires the admin credential and API, not MFA. |
| TM-15 | REQ-ENV-002†, REQ-OPS-001†, REQ-SEC-002 | REQ-ENV-002 | PLT-01, GOV-20, PLT-03, PLT-04, UND-01, BEN-03, SEC-02, ENV-13, ENV-14, ENV-07, SEC-11 | Not started |  |
| TM-16 | REQ-BEN-003†, REQ-AGT-004†, REQ-TST-006† | CI scan | GOV-03, PLT-03, BEN-28, BEN-11, TST-04, BEN-19, BEN-26 | Not started |  |
| TM-17 | REQ-API-005, REQ-SEC-002, REQ-SEC-005, REQ-TRU-009, REQ-INT-001†, REQ-AUD-006† | EC-X09 | PLT-01, GOV-20, PLT-03, PLT-05, UND-01, UND-04, SEC-02, TRU-05, ENV-13, TRU-07, SEC-09, SEC-12, GOV-28, EXE-07, EXE-08, SEC-13, REC-08 | Partially mitigated | **Partially mitigated.** mTLS and HMAC cover the model-to-core hop and grants. The internal receipt and Record-event objects are not yet authenticated against a stolen database credential: DEBT-01 (Tier 0, open) and DEBT-03. Closure needs REQ-AUD-006 evidenced by SEC-13 after EXE-08 and REC-08 (design: docs#80, Proposed; extension: SEC-12). |
| TM-18 | REQ-CAP-003, REQ-RCV-003, REQ-RCV-001†, REQ-NFR-002†, REQ-TST-009† | EC-E08 | TRU-02, RCV-01, CAP-01, RCV-02, SEC-10, TST-06 | Not started |  |
| TM-19 | REQ-EXP-001†, REQ-EXP-002† | REQ-EXP-002 corpus | EXP-01, EXP-02, EXP-03, BEN-14 | Not started |  |
| TM-20 | REQ-CAP-002†, REQ-CAP-001†, REQ-PLN-001, REQ-AG-001† | INV-05 test | ENV-11, PCK-01, PCK-02, EXE-01, PLN-01, PCK-03, UND-07, SEC-06, PCK-04 | Not started |  |
| TM-21 | REQ-VOI-001†, REQ-INP-002†, REQ-TRU-009, REQ-VOI-004 | EC-X08 variant | VOI-02, UND-04, VOI-05, TRU-07, VOI-06, VOI-07, VOI-09, DATA-01, VOI-16, VOI-15 | Not started |  |
| TM-22 | REQ-API-006, REQ-VER-005 | REQ-API-006 | PLT-08, OUT-05 | Not started |  |
| TM-23 | REQ-CTX-001, REQ-CTX-002, REQ-CTX-003, REQ-CTX-008 | EC-X16 | EVD-01, EVD-02, EVD-05 | Not started | Source, `authority_class`, `payload_hash` and `read_at` are fields of SoT §43.5 that REQ-CTX-001 requires. |
| TM-24 | REQ-API-008, REQ-INP-003, REQ-CTX-008 | EC-X17 | EDG-01, EVD-05, ENV-10, ENV-13, OUT-04 | Not started |  |
| TM-25 | REQ-SEC-009† | SSRF test set | SEC-05 | Not started |  |
| TM-26 | REQ-DATA-001, REQ-SEC-004†, REQ-SEC-005, REQ-SEC-002, REQ-EXE-001†, REQ-AUD-001†, REQ-AUD-006† | Permission matrix; evil-provider run | PLT-01, GOV-20, PLT-03, PLT-05, PLT-06, REC-01, UND-01, SEC-02, TRU-05, ENV-13, REC-06, EXE-02, SEC-08, SEC-09, SEC-12, GOV-28, EXE-07, EXE-08, SEC-13, REC-08 | Not started |  |
| TM-27 | REQ-EXE-004†, REQ-EXE-003, REQ-CTX-003 | US-19, EC-K01 | EVD-02, EXE-02, EXE-04, EXE-05, GOV-28, EXE-08 | Not started |  |

## Gaps found by SEC-01

Each is a mitigation stated in §42 or the risk register that no requirement carries, so nothing tests it. None is filled here; each needs a founder decision on the PERD text (AGENT-02, AGENT-29).

| ID | Threat | What is missing | Smallest safe fix (a proposal) |
|---|---|---|---|
| GAP-1 | TM-14 | Admin MFA appears in PERD §41.1 only; no REQ and no test | Add to REQ-SEC-006: the admin credential in a shared environment requires a second factor from the synthetic IdP; test: an admin call without it is refused |
| GAP-2 | TM-09 | No REQ says the loader verifies a policy row's `checksum` and refuses a mismatch | Add to REQ-TRU-005 or REQ-TRU-004: the loader recomputes the checksum and refuses to activate a policy that does not match; test: the tamper test of §42 |
| GAP-3 | PA-04 | The sandbox-version control (R-22) is a risk-register item, not a requirement | Add to the run-manifest requirement (REQ-BEN-004 or REQ-BEN-008): record the Tushe sandbox version in every run; test: a run without it fails |

## Proposed additions, pending review

These threats come from [DEC-2026-10-12](../decisions/DEC-2026-10-12-tushe-environment-scope.md) and are not in PERD §42, so they carry provisional IDs (`PA-`) until a PERD revision adds them to the threat model. Each control is the REQ named; each test is that REQ's acceptance criterion (PERD v1.2).

| ID | Threat | Control (REQ IDs) | Test / benchmark case | Status |
|---|---|---|---|---|
| PA-01 | The Tushe administrator credential leaks into the runtime | REQ-ENV-002 | A call by any runtime identity to a Tushe `/partner/...` route or to the `mock-case` truth endpoint SHALL be refused. | Not started |
| PA-02 | A core engineer alters `mock-case` or the hostility proxy (separation of duties) | REQ-ENV-008 | It SHALL be built and maintained by someone who does not build services/core, and its fault plans SHALL be owned by the benchmark owner. | Not started |
| PA-03 | The system under test sees Tushe test account numbers | REQ-ENV-005 | Every proxy fault family SHALL reproduce from a scenario and seed; the same Tushe number SHALL always map to the same synthetic number; no `9999` test-number pattern SHALL appear in any response delivered to a system under test. | Not started |
| PA-05 | Forged, replayed or flooding webhook deliveries at the public receiver | REQ-API-008, REQ-SEC-002 | EC-X17 plus a rate-limit case | Not started |
| PA-04 | Tushe changes sandbox behaviour without notice | **GAP-3.** No REQ names this control; it is the risk-register mitigation R-22 (record the sandbox version in every run manifest; a nightly failure on an unchanged commit detects it). REQ-ENV-004 and REQ-ENV-007 make faults and acceptance reproducible but say nothing about the sandbox version | Nightly run on an unchanged commit; sandbox version in the run manifest (R-22) | Not started |
| PA-06 | CI secret reachable by another service's workflow | REQ-SEC-005 | Canary (PLT-02): a workflow that references another area's environment fails CI; a secret defined at repository level fails CI | Not started |
| PA-07 | Service image contains the other service's code or configuration | REQ-SEC-002 | Canary (PLT-02): a cross-service file planted in an image fails CI | Not started |

Owner: Security reviewer (SR), a role held by the Founder and the Technical Co-Founder (DEC-2026-10-16 E2).
