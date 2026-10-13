# PLT-01: settings the engineering lead applies by hand

Prepared 13 Oct 2026 for task [PLT-01](PLT-01.md) from [DEC-2026-10-13](../../../decisions/DEC-2026-10-13-code-monorepo.md) R3 and R4. **An agent never changes repository settings.** Each line is ticked by the engineering lead (EL), with the date.

| Done | Setting | Detail (from the DEC) |
|---|---|---|
| [ ] | The `noema` repository exists | Private, created by a founder before PLT-01 starts |
| [ ] | GitHub Environment `core-ci` | Holds: Tushe read-only key; test database and grant-signing test keys. Used only by core workflows |
| [ ] | GitHub Environment `model-ci` | Holds: model and speech provider keys. Used only by model-service workflows |
| [ ] | GitHub Environment `bench` | Holds: Tushe administrator and fixture credentials; `mock-case` truth access. Used only by benchmark workflows |
| [ ] | Required reviewers on `bench` | The benchmark owner |
| [ ] | No repository-level secrets | The repository's Actions secrets list is empty |
| [ ] | Branch protection on `main` | Required checks (TODO(EL): the check names, once PLT-02 defines them); required CODEOWNER review; no force-push |
| [ ] | `.github/CODEOWNERS` is active | The DEC R4 paths, committed by PLT-01 |

Evidence: TODO(EL): who applied each setting, and when.
