@AGENTS.md

<!-- This file imports AGENTS.md so there is one set of agent instructions. The pointers below repeat AGENTS.md; they add no rules. -->

- A founder decision counts only once it is committed to `docs/NOEMA_SOURCE_OF_TRUTH.md` or `docs/decisions/` (SoT §0.4). Uncommitted instructions that disagree with the SoT: follow the SoT and raise the conflict.
- AGENT-27: never change, weaken or work around an invariant, binding decision or [CONVICTION] item to make an implementation fit; write CONFLICT DETECTED in the PR instead.
- Decision records: `docs/decisions/`.
