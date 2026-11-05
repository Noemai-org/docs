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
| D2 | **OD-P-74 is adopted as canonical.** The recorded default of OD-P-74 in `docs/open-decisions.md` (added by docs#107) becomes the decision: the claims `sub`, `aud`, `exp`, `iat`, `tenant_id` and `roles`; the roles `customer`, `operator` and `approver` (any other value rejects the token); `alg` `ES256` only and a `kid` naming a configured P-256 public key; the maximum token lifetime of the configured value. The NON-CANONICAL label is removed from the entry, which is closed by this record. The recorded text names no issuer claim value, so none is adopted here. The text is to be checked by the Security Reviewer and by Codex, and their findings go back to the Architect (see §3). | EDG-01; REQ-SEC-001, REQ-API-004, REQ-API-002; INV-12 |
| D3 | **Migration numbering.** The first pull request to merge keeps its migration number. The second renumbers its migration when it merges `main` in. | `services/core/migrations` in `noema`; AGENTS §11 (forward-only migrations) |
| D4 | **Production anchor retention is 365 days, in Compliance mode.** | REQ-AUD-007 (external anchoring of chain heads); DEC-2026-10-31-proof-depth-and-completeness D19 |
| D5 | **`RELAY_PULL_TOKEN` lives only in the Environment named in docs#108, and it is a read-only pull of queued inbound events.** Its exact scope is marked **"verify when the relay is deployed"**: until then the scope is stated, not verified. | ENV-13 (webhook relay); docs#108 (GitHub Environments checklist); AGENTS §10 |

## 2. Notes for the people who act on these rulings

- **D1.** The check compares a grant's `policy_id` and version with the active version of the same `policy_id` only. Two different policy IDs are never ranked against each other. A mismatch is a refusal that returns the case to Trust; it is not a retry (AGENT-08).
- **D2.** The label change is made in this pull request, in the OD-P-74 entry of `docs/open-decisions.md`. The code in `services/core/edge/session` (noema#156) already implements the recorded default.
- **D3.** A renumbering moves the second migration only; it never edits the first one after merge.
- **D4.** "Compliance mode" is stated as the Architect gave it. No retention number or mode is changed for non-production anchors.
- **D5.** The Environment holding the token is the one docs#108 names. This record does not name it again, and no hostname or domain appears in any repository file; the relay's address lives only in a GitHub Environment variable.

## 3. Review asked for D2

The Security Reviewer and Codex check the OD-P-74 text (claims, roles, algorithm, key identification, lifetime) against INV-12 and PERD REQ-SEC-001. Their findings go to the Architect, not to this record's author.
