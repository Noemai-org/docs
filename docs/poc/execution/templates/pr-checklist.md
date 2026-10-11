# PR checklist

<!-- Paste into the PR description and tick each line only on evidence. Source: plan §13.1 (NOEMA_POC_4WEEK_PLAN_v1.1.md lines 794–804), verbatim. -->

**PR checklist (CI enforces what it can; the reviewer checks the rest).**

- [ ] Task ID, REQ IDs and SoT IDs in the PR; changes only inside the card's allowlist.
- [ ] Tests written first, including failure paths.
- [ ] Unit, contract, property and relevant benchmark tests green; lint, boundaries, clock and money rules, codegen, secret and PII scans green.
- [ ] Record events and reconstruction asserted for any consequential behaviour.
- [ ] No model call in Trust, Execution or Outcome; no path from a model to an adapter.
- [ ] No new capability without its registry entry, policy, verification predicate and recovery definition.
- [ ] Any bug found has its regression case; any shortcut is in the debt register with owner, risk and removal condition.
- [ ] SoT and PERD conflict check done; decisions and registers in sync.
- [ ] The reviewer verified behaviour from evidence, not from the author's description.

A task is Done only when every line of the task definition of done (plan §13.1) is also true.
