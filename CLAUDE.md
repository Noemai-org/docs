@AGENTS.md

<!-- This file imports AGENTS.md so there is one set of agent instructions. The pointers below repeat AGENTS.md; they add no rules. -->

- A founder decision counts only once it is committed to `docs/NOEMA_SOURCE_OF_TRUTH.md` or `docs/decisions/` (SoT §0.4). Uncommitted instructions that disagree with the SoT: follow the SoT and raise the conflict.
- AGENT-27: never change, weaken or work around an invariant, binding decision or [CONVICTION] item to make an implementation fit; write CONFLICT DETECTED in the PR instead.
- AGENT-29: a change that opens, decides or closes a decision includes, in the same pull request, the decision record in `docs/decisions/`, the matching SoT edit and the regenerated register.
- Never hand-edit the generated register section in `docs/open-decisions.md`; run `python3 tools/check_docs_consistency.py --write`.
- Run `python3 tools/check_docs_consistency.py --check` before every push.
- Decision records: `docs/decisions/`.
- **Issued external documents are frozen.** Files marked "frozen record" (for example the Tushe specification in `docs/poc/tushe/`) must never be edited. Propose changes in a delta file next to them, and do not put internal strategy, benchmark details or hidden test material in any document meant for an external partner.
