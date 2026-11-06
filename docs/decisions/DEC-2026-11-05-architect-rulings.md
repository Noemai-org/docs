# DEC-2026-11-05 · Architect's rulings of 5 November 2026

| | |
|---|---|
| **Status** | Proposed for the Founders. The Architect gave these rulings in a work order of 5 November 2026 and asked for them to be committed as one record. An instruction given in a session is not authoritative until committed (AGENTS §2, item 3). They count once both Founders approve and merge this pull request. |
| **Date** | 5 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | OD-P-74 (D2). Nothing else. |
| **Amends** | None. No SoT, PERD or plan text changes. D1 and D5 are for the next PERD version where they touch PERD text; until then this record governs. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Proposed; counts once both Founders approve and merge this pull request
- Date: 5 November 2026
- Closes: OD-P-74
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: the Architect's work order of 5 November 2026 (relayed to the Repo Steward). This record adds no rationale the Architect did not give.
- Affected requirement IDs / SoT sections: per row
- Migration notes: per row; no merged migration or frozen record is edited
- Supersedes: None

---

## 1. The rulings

| ID | Ruling | Tasks and sources it touches |
|---|---|---|
| D1 | **Policy-version rule.** A grant binds to the exact `policy_id` and version it was decided under. Versions are compared only within the same `policy_id`. At execution, if the active version of that `policy_id` differs from the grant's, the executor refuses and returns the case to Trust. The executor never picks the newest version across different policy IDs. | TRU-05 (noema#163); Execution revalidation (INV-03, INV-17); REQ-TRU-004 |
| D2 | **OD-P-74 is adopted as canonical. The claim list and role list in this row are superseded by D7 (ruling A1); read D7, not this row, for the claims, the roles and the issuer.** The recorded default of OD-P-74 in `docs/open-decisions.md` (added by docs#107) becomes the decision: the claims `sub`, `aud`, `exp`, `iat`, `tenant_id` and `roles`; the roles `customer`, `operator` and `approver` (any other value rejects the token); `alg` `ES256` only and a `kid` naming a configured P-256 public key; the maximum token lifetime of the configured value. The NON-CANONICAL label is removed from the entry, which is closed by this record. The recorded text names no issuer claim value, so none is adopted here. The text is to be checked by the Security Reviewer and by Codex, and their findings go back to the Architect (see §3). | EDG-01; REQ-SEC-001, REQ-API-004, REQ-API-002; INV-12 |
| D3 | **Migration numbering.** The first pull request to merge keeps its migration number. The second renumbers its migration when it merges `main` in. | `services/core/migrations` in `noema`; AGENTS §11 (forward-only migrations) |
| D4 | **Production anchor retention is 365 days, in Compliance mode.** | REQ-AUD-007 (external anchoring of chain heads); DEC-2026-10-31-proof-depth-and-completeness D19 |
| D5 | **`RELAY_PULL_TOKEN` lives only in the Environment named in docs#108, and it is a read-only pull of queued inbound events.** Its exact scope is marked **"verify when the relay is deployed"**: until then the scope is stated, not verified. | ENV-13 (webhook relay); docs#108 (GitHub Environments checklist); AGENTS §10 |
| D6 | **Pack postconditions for the beneficiary and account capabilities come from the source that covers them (noema#104).** `lookup_beneficiary` takes its postcondition from `fin.src.beneficiary` (`beneficiary_list_and_aliases`). `lookup_account` takes an ownership-only postcondition from `fin.src.customer`. Neither declares a balance or state postcondition, because no source covers them and `core_ledger` is authoritative only for `debit_posted_or_reversed`. The descriptors in noema#148 re-point the same way. The account state and balance gap is filed as DEBT-12 (Tier 1) and is added to the open Tushe requests as proposed R14. | PCK-04 (noema#104, noema#148); REQ-OUT-001; `docs/poc/execution/debt.md` DEBT-12; `docs/poc/tushe/tushe-spec-delta-v1.3-draft.md` |
| D7 | **The identity contract (ruling A1 of 6 Nov 2026; supersedes the claim list and role list of D2).** Issuer: the string `noema-poc-idp`, exact match. Claims, all required: `sub`, `aud`, `exp`, `iat`, `iss`, `tenant_id`, `roles`. `roles` holds exactly one value from `customer`, `ops`, `approver`, `audit`; zero values, several values or an unknown value is refused. `alg` is `ES256` only. The maximum token lifetime is 15 minutes. Deny by default. No identity claim is ever read from a request body. The signature is verified against a configured key. The tenant claim is mandatory. The Security Reviewer's nine gaps on OD-P-74 (comment on docs#112, 5 Nov 2026) become requirements; none contradicts an invariant. They are listed in §2, D7. | EDG-01 (noema#156); REQ-SEC-001, REQ-SEC-006, REQ-API-004, REQ-API-002; INV-12, INV-21, DEBT-04 |
| D8 | **Alerts and the production anchor.** Pushover is the primary alert channel and ntfy the fallback, each in its own GitHub Environment named `alerts`. The production anchor bucket keeps objects for 365 days in Compliance mode (as D4). | DEBT-02; REQ-AUD-007; docs#111 (anchor click-script) |

## 2. Notes for the people who act on these rulings

- **D1.** The check compares a grant's `policy_id` and version with the active version of the same `policy_id` only. Two different policy IDs are never ranked against each other. A mismatch is a refusal that returns the case to Trust; it is not a retry (AGENT-08).
- **D2.** The label change is made in this pull request, in the OD-P-74 entry of `docs/open-decisions.md`. The code in `services/core/edge/session` (noema#156) already implements the recorded default.
- **D3.** A renumbering moves the second migration only; it never edits the first one after merge.
- **D4.** "Compliance mode" is stated as the Architect gave it. No retention number or mode is changed for non-production anchors.
- **D5.** The Environment holding the token is the one docs#108 names. This record does not name it again, and no hostname or domain appears in any repository file; the relay's address lives only in a GitHub Environment variable.
- **D6.** A balance or account-state postcondition is not declared until a source covers it. `core_ledger` is authoritative only for `debit_posted_or_reversed`. The request to Tushe is a draft, not sent; sending is for the Founders.
- **D7.** The issuer string and the role list are now written down (ruling A1). Where D2 lists the roles `customer`, `operator`, `approver` and no issuer, D7 governs: the role `operator` becomes `ops`, `audit` is added, and `iss` is a required claim. noema#156 as built has no `iss` and accepts a list of roles, so it changes. The Security Reviewer's nine gaps become these requirements, each with a test:
  1. One role per token, so no token carries `customer` with `approver` (self-approval); a token with zero or several roles is refused.
  2. The issuer is `noema-poc-idp`, exact match; a missing or different `iss` is refused. The signature against a configured key remains the second anchor.
  3. A token with header `none`, `jwk`, `jku`, `x5u`, `x5c` or `crit`, or a `kid` outside the configured set, is refused. The curve is P-256, and a signature that is not exactly 64 bytes (R and S) is refused.
  4. A token whose `iat` is later than now plus a stated skew is refused, and so is a token whose `exp` is not after its `iat` or whose `exp - iat` is above 15 minutes (a per-token check, not only the configured maximum). The maximum lifetime must be set, non-zero and at or below 15 minutes, or the service does not start. The clock is injected (INV-21). No `nbf` is required. The clock-skew leeway on `exp` and `iat` is 60 s, pack data, tested on the simulated clock (ruling A21 of 6 Nov 2026).
  5. `tenant_id` must equal the tenant of the database login the request runs on (DEBT-04); a mismatch is refused and tested across tenants. The IdP's signature is the only proof that `sub` belongs to that tenant, which is acceptable for the synthetic IdP.
  6. `aud` is one string; an array form is refused. `sub` is non-empty and length-bounded. A value read from a request body is never a principal.
  7. An `ops` token acts within its own `tenant_id` only, until a decision says otherwise (REQ-SEC-006).
  8. There is no `jti`, so a stolen token works until `exp`. This is a named residual risk at the 15-minute lifetime.
  9. The "[REC] 15 minutes" wording is replaced by the ceiling of 15 minutes in item 4.
  Three further points come from the Security Reviewer's check of D7 (comment on docs#112, 6 Nov 2026). Items 10 and 11 are now ruling A20 of 6 Nov 2026 (DEC-2026-11-06-architect-rulings); item 12 is housekeeping:
  10. An `audit` token acts within its own `tenant_id` only, as `ops` does in item 7, and reads only through tenant-bound Record read functions.
  11. Neither an `ops` token nor an `audit` token has a path to a Record writer; only service emitters write the Record (DEBT-07, EDG-01 writers).
  12. The D2 row points to D7, so no implementer reads the old list.
- **D8.** "Each in its own Environment (alerts)" is recorded as the Architect gave it. Where the two Environments are created is in docs#111. The recipient of the human alert (DEBT-02) is not decided by this record.

## 3. Review asked for D2

The Security Reviewer and Codex check the OD-P-74 text (claims, roles, algorithm, key identification, lifetime) against INV-12 and PERD REQ-SEC-001. Their findings go to the Architect, not to this record's author.
