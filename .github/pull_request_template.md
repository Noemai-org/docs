## Summary

<!-- What changes and why. -->

## Requirement IDs touched

<!-- SoT IDs and, for POC build work, PERD REQ IDs (see docs/poc/perd/requirements-index.csv). For example BD-16, INV-29, OD-05 (AGENT-01). -->

## Plan task ID(s)

<!-- e.g. EXE-02 (see docs/poc/execution/tasks.csv) -->

## Checklist

For POC build work, also complete the PR checklist in `docs/poc/execution/templates/pr-checklist.md`.

- [ ] If this opens, decides or closes a decision: the decision record, the SoT edit and the regenerated register are all in this PR (AGENT-29).
- [ ] Requirement IDs touched are listed.
- [ ] `python3 tools/check_docs_consistency.py --check` passes.
- [ ] No frozen file changed, or the change is intended and its hash is updated.
- [ ] The SoT version and change log are updated if the SoT changed.
