# Threat-to-test map (POC)

Tracks whether each threat in [`threat-model.md`](threat-model.md) (PERD §42) has a passing test. Proposed with the PERD ([DEC-2026-10-11-poc-perd-v1.1](../decisions/DEC-2026-10-11-poc-perd-v1.1.md)).

- **Control (REQ IDs):** only the REQ IDs that the PERD §42 row itself names. Where §42 names none, the cell is a TODO; do not fill it by inference.
- **Test / benchmark case:** copied verbatim from the `Test` column of PERD §42.
- **Status:** `Not started` until a test exists and runs in CI or the benchmark. Change it only with a link to the passing run.

| TM | Control (REQ IDs) | Test / benchmark case | Status |
|---|---|---|---|
| TM-01 | TODO(SR, SEC-01): §42 names no REQ for this control | EC-U05, EC-X01 | Not started |
| TM-02 | TODO(SR, SEC-01): §42 names no REQ for this control | EC-X05, EC-X08, EC-X10 | Not started |
| TM-03 | TODO(SR, SEC-01): §42 names no REQ for this control | US-09, EC-X02..X04 | Not started |
| TM-04 | TODO(SR, SEC-01): §42 names no REQ for this control | EC-X13 | Not started |
| TM-05 | TODO(SR, SEC-01): §42 names no REQ for this control | EC-U03 | Not started |
| TM-06 | TODO(SR, SEC-01): §42 names no REQ for this control | EC-X08 | Not started |
| TM-07 | TODO(SR, SEC-01): §42 names no REQ for this control | EC-X07, PUS-07 | Not started |
| TM-08 | TODO(SR, SEC-01): §42 names no REQ for this control | US-05, US-06 | Not started |
| TM-09 | TODO(SR, SEC-01): §42 names no REQ for this control | Tamper test | Not started |
| TM-10 | REQ-AUD-005 | REQ-AUD-005 | Not started |
| TM-11 | REQ-SEC-003 | REQ-SEC-003 | Not started |
| TM-12 | TODO(SR, SEC-01): §42 names no REQ for this control | US-07 | Not started |
| TM-13 | TODO(SR, SEC-01): §42 names no REQ for this control | US-19, US-20 | Not started |
| TM-14 | TODO(SR, SEC-01): §42 names no REQ for this control | Authorisation-matrix test | Not started |
| TM-15 | REQ-ENV-002 | REQ-ENV-002 | Not started |
| TM-16 | TODO(SR, SEC-01): §42 names no REQ for this control | CI scan | Not started |
| TM-17 | TODO(SR, SEC-01): §42 names no REQ for this control | EC-X09 | Not started |
| TM-18 | TODO(SR, SEC-01): §42 names no REQ for this control | EC-E08 | Not started |
| TM-19 | REQ-EXP-002 | REQ-EXP-002 corpus | Not started |
| TM-20 | TODO(SR, SEC-01): §42 names no REQ for this control | INV-05 test | Not started |
| TM-21 | TODO(SR, SEC-01): §42 names no REQ for this control | EC-X08 variant | Not started |
| TM-22 | REQ-API-006 | REQ-API-006 | Not started |
| TM-23 | TODO(SR, SEC-01): §42 names no REQ for this control | EC-X16 | Not started |
| TM-24 | TODO(SR, SEC-01): §42 names no REQ for this control | EC-X17 | Not started |
| TM-25 | REQ-SEC-009 | SSRF test set | Not started |
| TM-26 | TODO(SR, SEC-01): §42 names no REQ for this control | Permission matrix; evil-provider run | Not started |
| TM-27 | TODO(SR, SEC-01): §42 names no REQ for this control | US-19, EC-K01 | Not started |

## Proposed additions, pending review

These threats come from [DEC-2026-10-12](../decisions/DEC-2026-10-12-tushe-environment-scope.md) and are not in PERD §42, so they carry provisional IDs (`PA-`) until a PERD revision adds them to the threat model. Each control is the REQ named; each test is that REQ's acceptance criterion (PERD v1.2).

| ID | Threat | Control (REQ IDs) | Test / benchmark case | Status |
|---|---|---|---|---|
| PA-01 | The Tushe administrator credential leaks into the runtime | REQ-ENV-002 | A call by any runtime identity to a Tushe `/partner/...` route or to the `mock-case` truth endpoint SHALL be refused. | Not started |
| PA-02 | A core engineer alters `mock-case` or the hostility proxy (separation of duties) | REQ-ENV-008 | It SHALL be built and maintained by someone who does not build services/core, and its fault plans SHALL be owned by the benchmark owner. | Not started |
| PA-03 | The system under test sees Tushe test account numbers | REQ-ENV-005 | Every proxy fault family SHALL reproduce from a scenario and seed; the same Tushe number SHALL always map to the same synthetic number; no `9999` test-number pattern SHALL appear in any response delivered to a system under test. | Not started |
| PA-05 | Forged, replayed or flooding webhook deliveries at the public receiver | REQ-API-008, REQ-SEC-002 | EC-X17 plus a rate-limit case | Not started |
| PA-04 | Tushe changes sandbox behaviour without notice | TODO(SR, SEC-01): no REQ names this control; see PERD v1.2 R-22 and plan v1.2 SR-20 | TODO(SR, SEC-01) | Not started |
| PA-06 | CI secret reachable by another service's workflow | REQ-SEC-005 | Canary (PLT-02): a workflow that references another area's environment fails CI; a secret defined at repository level fails CI | Not started |
| PA-07 | Service image contains the other service's code or configuration | REQ-SEC-002 | Canary (PLT-02): a cross-service file planted in an image fails CI | Not started |

Owner: Security reviewer (SR), a role held by the Founder and the Technical Co-Founder (DEC-2026-10-16 E2).
