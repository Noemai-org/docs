# DEC-2026-11-19 · Architect rulings A384 to A388 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 19 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 19 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Five rulings, A384 to A388 (§1): UI-01 on polling, the UI's transport limits, the contracts the UI needs, parallel work and review for the UI, and a CI job for the UI end-to-end tests. |
| **Supersedes** | **A384 changes the order of UI-01's transport:** polling first, SSE as an upgrade after noema#726 (it was not a precondition before either; the ruling states it). **A385 ends the wait on EL** for the UI's transport limits. Otherwise per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 19 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A384 to A388
- Decision: §1
- Rationale and evidence: the Architect's message of 19 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: REQ-UI-001; AGENT-11, AGENT-13, AGENT-15, AGENT-16; PERD §39.2 (the conversation and investigation routes), §40.1 (the UI), §47 (budgets); plan UI-01, UI-02, EDG-02, CON-07
- Supersedes: see the Supersedes row above
- Migration notes: none (`none_option_id` is a contract minor, noema#736, owned by its author)

## 1. The rulings, as given

### A384 (interim): UI-01 on polling.

Build UI-01 on polling now.

- Send with `POST /v1/conversations`.
- Poll `GET /v1/investigations/{id}` while the stage is `understanding` or `working`. Stop at a terminal stage.
- Poll interval: 1 s, as a UI config value.
- SSE: it becomes an upgrade after noema#726. It is not a precondition.

### A385 (interim): Transport limits (no more waiting on EL).

- **Response limit:** the UI derives the maximum size of each response from the contract's own bounds. A test computes it from the schema, and the UI constant must equal it.
- **Enforcement:** it checks `Content-Length` and caps a streamed body before buffering. A larger response is refused.
- **SSE frames:** the same method with `sse-event.v1`, once SSE exists.
- **Reconnect:** after any drop, refetch authoritative state first. Retry 3 times with 1 s, 2 s and 4 s backoff, then show plain-language "connection lost". After SSE exists, resume with `Last-Event-ID` (the chain position).
- **No server text is shown:** nothing from an error body reaches the screen.
- These are UI behaviour values in the one tokens file, not safety thresholds.

### A386 (interim): The contracts FE needs are merged.

`message-request.v1` (noema#743) and `confirmation-answer.v1` (noema#758) are on `main`. `none_option_id` is a contract minor (noema#736). FE codes to the contract now and rebases when noema#736 merges. FE doesn't wait for the route (noema#754).

### A387 (interim): Parallel work and the review rule.

- FE works on several PRs at once. The WIP cap is suspended until G1 passes (A317).
- FE merges `main` at any time and doesn't wait for a read before starting the next item.
- UI PRs are Tier 2: Codex, CI and one Founder, with no independent read (A334).
- Commit the prepared real-investigation Playwright check now as an opt-in test.

### A388 (interim): A CI job for the UI end-to-end tests.

IL adds one that runs Playwright against the stack after stack-check, so FE's live tests have a real core to run on.

## 2. What the Steward notes

- **The wording "A384, build UI-01 on polling now"** is taken as the ruling's first line, as given.
- **A385's values** (the poll interval of A384, the retry counts and backoff) are UI behaviour values that belong in the one tokens file (AGENTS §7); they are not safety thresholds (AGENT-16 does not apply to them, as the ruling says). The Steward adds no value of its own.
- **A388 touches `.github`.** A CI job is a workflow change, which needs a Founder's approval and SR's read (AGENTS §11; plan §4 Tier 2). The Steward does not change that. The ruling gives the job no task ID; the Steward adds no task row without one (plan §19). IL names the task or the Architect says which row carries it.
- **A387 and the WIP cap:** the cap is suspended until G1 passes (A317); nothing here changes that.
- **Rulings still not received:** A358 to A361, A380 to A383, A389 to A392 and A393 to A400 (the list in `DEC-2026-11-19-architect-corrections-a371-a345s4`, §2, is updated by this record). Next free ruling: A401.
