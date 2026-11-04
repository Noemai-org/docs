# PERD v1.21 amendment text: the three gaps found by SEC-01

Date: 2026-11-03. Author: Security Reviewer (SEC-01). Status: **Draft text for the Engineering Lead to record as a decision and the Repo Steward to apply** (Architect, 3 Nov 2026: yes, amend; the draft is due Mon 9 Nov). It edits nothing: PERD v1.19 and the plan are unchanged until a decision record and a new version file adopt it (AGENT-29). Requirement IDs and status tags are kept as the PERD writes them.

Basis: the threat-to-test map ([`threat-to-test-map.md`](threat-to-test-map.md)) names three mitigations that PERD §42 or the risk register states and no requirement carries: GAP-1 (TM-14), GAP-2 (TM-09), GAP-3 (PA-04). Each amendment below gives the v1.19 text and the text that replaces it, the test, the threat row it closes, and the effect on other documents. Text marked `[REC]` follows the PERD convention for items not yet adopted.

**Relation to v1.20.** The signing design (DEC-2026-11-01, docs#80) amends REQ-AUD-006, REQ-SEC-005, REQ-EXE-004, §32.1, §36.1, §38.2, §41.1. Nothing below edits those. The only shared requirement is REQ-SEC-001, which both leave untouched except for the one sentence added in 1.2.

## 1. GAP-1: admin MFA (TM-14, "Insider misuse")

**Why it is a gap.** PERD §42 TM-14 lists "Admin MFA" as the mitigation and PERD §41.1 says the control plane has "a separate admin credential, MFA-protected in shared environments". No requirement carries it, so REQ-SEC-006's acceptance criteria and tests cannot fail if MFA is absent.

**1.1 REQ-SEC-006, "Requirement", after the third bullet.**

> before: (three bullets: admin credential and API; no data-plane identity; no model.)
>
> after (added bullet): In a shared environment, the admin credential is accepted only on a session that carries a second factor: the synthetic IdP issues an admin-role token with an `amr` claim that includes `mfa`, and the admin API refuses any other admin token [REC]. In a local development environment the second factor is not required, and the environment says so in every admin response header `X-Noema-Env`.

**1.2 REQ-SEC-001, "Requirement", appended sentence.**

> after (added): For the admin role the IdP issues the `amr` claim and issues an admin token only after a second factor from a fixed synthetic test authenticator, so that the check of REQ-SEC-006 can be tested without a real person [REC].

**1.3 REQ-SEC-006, "Audit".**

> before: Control-plane events go to the Record.
>
> after: Control-plane events go to the Record, with the `amr` claim of the credential that made the call. A refused admin call without the second factor appends `SECURITY_EVENT{reason: MFA_REQUIRED}`.

**1.4 REQ-SEC-006, "Acceptance criteria" and "Tests".**

> after (added to acceptance): In a shared environment, an admin call made with an admin-role token that lacks `mfa` in `amr` SHALL be refused with a typed error and recorded; the same call with the second factor SHALL succeed.
>
> after (added to tests): Authorisation matrix extended with a row for "admin token without MFA"; a test per admin endpoint of PERD §39.4.

**Closes:** TM-14 (control now REQ-SEC-006; test: the authorisation-matrix row). **Effects:** the synthetic IdP (ENV/EDG tasks) issues `amr`; the task that builds the admin API adds the check. **Decision for the founders:** whether MFA belongs to the POC. §41.1 already says so; with no scope cut I recommend yes.

## 2. GAP-2: the policy checksum is verified at load (TM-09, "Policy tampering")

**Why it is a gap.** PERD §42 TM-09 lists "Admin-only publish; checksum; Record event" and detection "Checksum mismatch on load". PERD §38.2 gives `policy_version` a `checksum` column. REQ-TRU-004 validates the rules' contents and REQ-TRU-005 voids grants on publication; neither says the loader recomputes and checks the checksum, so a policy row edited directly in the database is not required to be detected. (For packs the check is stated: REQ-SEC-007, and the pack requirement's "the loader verifies the checksum".)

**2.1 REQ-TRU-004, "Requirement".**

> before: §23.4. The policy loader validates rules with the predicate type checker, and rejects unknown fields, unknown capability IDs and missing `evaluation_time`.
>
> after: §23.4. The policy loader validates rules with the predicate type checker, and rejects unknown fields, unknown capability IDs and missing `evaluation_time`. At publication the checksum is stored as `SHA-256(JCS(rules_json))`; the loader recomputes it on every load and refuses a version whose stored checksum differs [REC].

**2.2 REQ-TRU-004, "Failure behaviour".**

> before: If loading fails, the previous ACTIVE version stays in force. If none exists, all writes are refused.
>
> after: If loading fails, including a checksum mismatch, the previous ACTIVE version stays in force. If none exists, all writes are refused. A checksum mismatch appends `SECURITY_EVENT{reason: POLICY_CHECKSUM_MISMATCH, policy_id, version}`.

**2.3 REQ-TRU-004, "Acceptance criteria" and "Tests".**

> after (added to acceptance): A policy row whose `rules_json` is changed directly in the database after publication SHALL be detected at the next load, SHALL NOT be in force, and SHALL leave the previous ACTIVE version in force.
>
> after (added to tests): The "Tamper test" of PERD §42 TM-09, written failing first: publish a version, edit its `rules_json` as a database superuser, reload, and assert the three results above.

**Closes:** TM-09 (control REQ-TRU-004; test: the tamper test). **Effects:** none on contracts; a test and the loader check. **Residual risk to state:** a database superuser can edit both the rules and the checksum. That is the migration-role limit of DEC-2026-11-01 §7.2 and is detected by anchoring (REQ-AUD-007), not prevented; this amendment makes the *accidental or partial* edit detectable at load.

## 3. GAP-3: the Tushe sandbox version is recorded in every run (PA-04, "Tushe changes behaviour without notice")

**Why it is a gap.** The control is the risk-register mitigation R-22 ("record the sandbox version in every run manifest"; detection: "a nightly failure with an unchanged commit; the sandbox version on responses changes"). No requirement carries it, so a run manifest without the version is not a defect.

**3.1 REQ-BEN-008, "Requirement", the third bullet.**

> before: the Tushe version, scenario-pack version, seed set, fault configuration and oracle version (the oracle itself stays private);
>
> after: the Tushe version, scenario-pack version, seed set, fault configuration and oracle version (the oracle itself stays private); **and the Tushe sandbox version as reported on the responses of that run** (R-22), every distinct value observed, with the first and last response time of each;

**3.2 REQ-BEN-004, "Acceptance criteria", appended.**

> after (added): Every report SHALL state the Tushe sandbox version(s) observed in the run. A run in which no sandbox version was observed SHALL be marked `VERSION_UNKNOWN` and SHALL NOT be used as release evidence.

**3.3 REQ-ENV-004, "Requirement", appended sentence.**

> after (added): The fault trace records the Tushe sandbox version of each response that it covers. A nightly failure on an unchanged commit, with a sandbox version that differs from the previous run's, is classified `TUSHE_CHANGE` and handled under the Tushe defect rule of the plan (§18), not as a regression of Noema.

**Closes:** PA-04 (control REQ-BEN-004, REQ-BEN-008, REQ-ENV-004; test: a run without a version is rejected; a changed version is classified). **Depends on:** Tushe actually reporting a version on its responses (R-22 asked for it; whether it does is a fact to confirm with the Integration Lead before the amendment is relied on; unknown today). If Tushe does not, the amendment reads "the sandbox version as obtained from `<the source the Integration Lead confirms>`".

## 4. Changes to other documents when this is adopted

| Document | Change |
|---|---|
| `threat-to-test-map.md` | TM-14, TM-09 and PA-04 take the new control REQs; GAP-1, GAP-2 and GAP-3 are removed from "Gaps found by SEC-01" |
| Requirements index | no new REQ IDs; REQ-SEC-006, REQ-SEC-001, REQ-TRU-004, REQ-BEN-004, REQ-BEN-008 and REQ-ENV-004 change text only (`requirements-index.csv` is regenerated by `perd_index.py`) |
| Plan | no task is added: the checks belong to the tasks that already cite these REQs; their "done when" gains the new tests (a change request, plan §19) |

## 5. What I need

The Engineering Lead records the decision (adopt, adopt with changes, or declare a gap not a POC control) and the Repo Steward applies it as PERD v1.21 with the regenerated indexes. I will update the threat-to-test map in the same change set once the text is adopted.
