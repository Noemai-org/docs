# Task card: SEC-15

Plan v1.14 task SEC-15 (added by ruling A112 of [DEC-2026-11-09-sec-15-per-login-secrets](../../../decisions/DEC-2026-11-09-sec-15-per-login-secrets.md); dated Tue 1 Dec (G3) by the Repo Steward, because DEBT-13 is due before G3 evidence and the Principal Architect gave no date). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Owner C1, reviewer SR, EL accountable. Written by the Repo Steward on 9 Nov 2026 from the Architect's ruling on noema#385; the owner reviews it before work starts.

```
SEC-15 · Per-login secrets: a distinct file-mounted secret for every tenant login and power login (the removal of DEBT-13)
Priority: P0 (REQ-SEC-004 and REQ-SEC-005 are P0)
Requirement IDs: REQ-SEC-004, REQ-SEC-005; SoT IDs: INV-12 (identity from the session only), INV-29 (credential separation); rulings A4 (DEC-2026-11-06) and A112
Rationale: today every tenant login and power login shares one password (`noema_tenant_login_password`), so one leaked secret authenticates as any tenant's power role. Ruling A4 gave each emitter its own secret (noema#181) and registered the rest as DEBT-13, Tier 1, due before G3 evidence. The Security Reviewer's finding F1 on noema#181 is that debt, recorded under DEBT-13.
Start condition (ruling A112): start as soon as the migration stack is merged. NEVER put this task in front of noema#181. The stack is the migration PRs of the ledger on noema#183 (EDG-01, TRU-05, EXE-08, TRU-08, REC-05, REC-08, EVD-03 and MEM-01 work). The plan row's Needs lists EXE-08 only, because the stack spans several tasks; this paragraph is the binding start condition.
Modules touched (allowlist): deploy/compose/postgres/init.sh, deploy/compose/postgres/provision-tenants.sh, deploy/compose/postgres/test_init.sh, deploy/compose/secrets_local.sh, deploy/compose/test_secrets_local.sh (added by noema#181), the secrets wiring in deploy/compose/docker-compose.yml, status/SEC-15.md
  ← nothing else may change. No migration, no contract change, no new dependency, no new role. A change to `.github/` or CODEOWNERS is outside this card.
Contracts: none changed. Bump required? N
Inputs/outputs: one file-mounted secret per tenant login and one per power login, created by `secrets_local.sh`, read by `init.sh` and `provision-tenants.sh`, mounted by Compose; no two logins read the same file; `.env.example` lists names only.
Tests to write FIRST (AGENT-11), each seen failing:
  - tenant A's secret cannot authenticate as tenant B's role;
  - no two logins share a secret (the closure test of DEBT-13: each login connects only with its own secret);
  - a login created without its own secret file is refused at bootstrap.
Faults to exercise (AGENT-12): a missing secret file; two logins pointed at the same file; a tenant added after bootstrap.
Record events to assert: none written; the tests connect to the database and assert authentication outcomes.
Dependencies: the migration stack merged (start condition above); noema#181 merged (it adds `test_secrets_local.sh` and the emitter logins).
Review: SR (reviewer-role READY at the final head); EL accountable; plan section 4 two human reviews apply. One approval from a Founder who did not author the PR (A111).
Out of scope: any migration; any change to the emitter logins; the secrets manager decision for shared environments (OQ-09); a change to a threshold, TTL or budget.
Definition of done: tests green; DEBT-13 closed by EL with the evidence, or kept open with the gap named; docs updated; PR answers the SoT section 52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (PERD section 71.3)
```

Owner: C1. Reviewer: SR. EL accountable. Needs: EXE-08, and the start condition above. Dated Tue 1 Dec (plan v1.14); due before G3 evidence.
