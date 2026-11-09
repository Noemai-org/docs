# DEC-2026-11-09 · Ruling on noema#385: DEBT-13 does not block noema#181; new task SEC-15 (ruling A112)

| | |
|---|---|
| **Status** | **Decided by the Principal Architect on 9 Nov 2026 (the answer to noema#385), relayed to the Repo Steward by the Founder; recorded by the Repo Steward.** Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 9 November 2026 |
| **Owner** | Principal Architect (the ruling); Founder and Technical Co-Founder (the merge) |
| **Decides** | Whether the registered DEBT-13 blocks noema#181, and adds task SEC-15 to the plan. |
| **Closes** | The question on noema#385 (C1 closes the issue). The change request [CR-2026-11-09-SEC-15-per-login-secrets](../poc/execution/change-requests/CR-2026-11-09-SEC-15-per-login-secrets.md) (its Status is Approved). |
| **Supersedes** | **Nothing.** Ruling A4 (DEC-2026-11-06) stands: DEBT-13 stays Tier 1, due before G3 evidence; this record adds the task that removes it and names its builder. |
| **Amends** | New plan version `docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v1.14.md` (v1.13 and earlier stay unchanged), the regenerated `tasks.csv`, the card `task-cards/SEC-15.md`, and the DEBT-13 row of `docs/poc/execution/debt.md`. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Decided 9 Nov 2026; counts once a Founder who did not author this pull request approves and merges
- Date: 9 November 2026
- Closes: CR-2026-11-09-SEC-15-per-login-secrets
- Owner: Principal Architect; Founder and Technical Co-Founder
- Decides: DEBT-13 does not block noema#181; new task SEC-15
- Decision: ruling A112 in §1
- Rationale and evidence: the Principal Architect's answer on noema#385 (9 Nov 2026), relayed by the Founder to the Repo Steward; C1's question and recommendation on noema#385; the Security Reviewer's finding F1 on noema#181 at c8d6c35
- Affected requirement IDs / SoT sections: REQ-SEC-004, REQ-SEC-005; INV-12, INV-29
- Migration notes: none; SEC-15 adds no migration
- Supersedes: nothing

---

## 1. The ruling

| ID | Ruling |
|---|---|
| **A112** | **DEBT-13 does not block noema#181.** noema#181 merges with DEBT-13 open (Tier 1, due before G3 evidence). C1 adds one line to noema#181: "DEBT-13 stays open; tenant and power logins still share a password until SEC-15." The Security Reviewer re-checks noema#181 at the final head for the **emitter-login half of ruling A4 only** and posts READY or numbered findings, with finding F1 recorded as DEBT-13. **New task SEC-15**: owner C1, reviewer SR, EL accountable; a distinct file-mounted secret per tenant login and power login, in `init.sh`, `provision-tenants.sh`, `secrets_local.sh`, the Compose wiring and the two shell tests; no migration. Failing test first: tenant A's secret cannot authenticate as tenant B's role, and no two logins share a secret. SEC-15 starts as soon as the migration stack is merged and is **not** put in front of noema#181. DEBT-13 is updated to name SEC-15 and C1 as builder. |

## 2. What the Steward chose where the ruling is silent

- **Date and gate.** The ruling gave none. SEC-15 is placed in the Tuesday 1 December group (G3) because DEBT-13 is due before G3 evidence and the plan dates a task by the gate that needs it (plan §3). C1 starts earlier, the moment the stack is on `main` (DEC-2026-11-03 D4: nobody waits for a date). The date moves only by change request (plan §19).
- **Needs.** The plan row lists EXE-08, C1's migration task. The start condition "after the migration stack is merged" is stated on the card, because the stack spans several tasks (EDG-01, TRU-05, EXE-08, TRU-08, REC-05, REC-08, EVD-03, MEM-01).
- **Requirements and priority.** REQ-SEC-004 (tenant isolation) and REQ-SEC-005 (key management), both P0, so the card is P0. EL or the Architect corrects them if another requirement is meant.
- **Files.** The card's allowlist names `deploy/compose/postgres/init.sh`, `provision-tenants.sh`, `test_init.sh`, `deploy/compose/secrets_local.sh`, `deploy/compose/test_secrets_local.sh` (added by noema#181) and the secrets wiring in `docker-compose.yml`. These are the files the ruling names, found in the repository.
- **DEBT-13.** The owner stays EL, as registered; the row now names SEC-15 and C1 as builder. The tier, the closure test and the due point are unchanged.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| DEC-2026-11-08-rulings-a41-onward | A41 to A108 | |
| A109, A110, A111 | REC-09, control-plane callers, one non-author Founder approval | |
| This record | A112 | **A113** |
