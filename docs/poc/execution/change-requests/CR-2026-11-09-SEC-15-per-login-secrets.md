# Change request: CR-2026-11-09-SEC-15-per-login-secrets

- Change ID: CR-2026-11-09-SEC-15-per-login-secrets
- Requester: Core Engineer 1 (C1), through noema issue #385; drafted by the Repo Steward. **The Principal Architect decided it; the plan row and `tasks.csv` row are added in plan v1.14 in the same change set.**
- Status: **Approved by the Principal Architect on 9 Nov 2026 (ruling A112, DEC-2026-11-09-sec-15-per-login-secrets)**, in the answer to noema#385, relayed to the Repo Steward by the Founder.
- REQ IDs affected: REQ-SEC-004 (tenant isolation), REQ-SEC-005 (key management); INV-12, INV-29. Plan tasks: a new task, **SEC-15**; the register entry DEBT-13 names it.
- Behaviour before: only the emitter logins have their own file-mounted secret (ruling A4, noema#181). The tenant logins and the power logins share one password. DEBT-13 records this as Tier 1, due before G3 evidence, with no task to remove it.
- Behaviour after: every tenant login and power login has a distinct file-mounted secret, created by `secrets_local.sh`, read by `init.sh` and `provision-tenants.sh`, mounted by Compose; two shell tests prove that tenant A's secret cannot authenticate as tenant B's role and that no two logins share a secret.
- Safety and security impact: closes the shared-secret exposure of DEBT-13. It touches bootstrap scripts only: no migration, no contract change, no dependency, no role. It does not touch a Tier 0 gate.
- Tests added or changed: the failing-first tests listed on the card (cross-tenant authentication refused; no shared secret; a login without its own secret refused at bootstrap).
- Schedule and dependency impact: **new task SEC-15** · owner C1 · reviewer SR · EL accountable · Needs EXE-08 · starts as soon as the migration stack is merged, never in front of noema#181 · due before G3 evidence (Tue 1 Dec). It counts toward the driving founder's WIP when started.
- SoT or PERD text changes: no.
- Decision owner: Principal Architect (the ruling); the Founders merge the record.
- Decision record: [DEC-2026-11-09-sec-15-per-login-secrets](../../../decisions/DEC-2026-11-09-sec-15-per-login-secrets.md).
- Migration and rollback: none; revert the scripts to return to the shared secret.
