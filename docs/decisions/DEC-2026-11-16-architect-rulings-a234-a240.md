# DEC-2026-11-16 · Architect rulings A234 to A240 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect on 16 Nov 2026, relayed to the Repo Steward, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). **A237 and A238 point to "§3" of the Architect's message, which the Steward was not given; they are recorded as given and their content is not invented.** |
| **Date** | 16 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge, and the actions A240 names) |
| **Decides** | Seven rulings, A234 to A240 (§1). Each states what it supersedes. |
| **Closes** | The public route shape of noema#601 (A234); the reading of G0-N item N10 on noema#590 (A235); the payload limit of noema#606 (A236); noema#611 (A237); the axe approval (A238); the concurrency groups of noema#569 and noema#577 (A239); the consequences of Tushe's addendum of 15 Nov for the harness (A240). |
| **Supersedes** | Per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 16 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A234 to A240
- Decision: §1
- Rationale and evidence: the Architect's message of 16 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-07, INV-22; AGENT-14, AGENT-16, AGENT-29; REQ-API-001, REQ-ENV-005, REQ-ENV-007, REQ-API-008; PERD §32.3, §39.2; SoT §0.4
- Migration notes: none by this record
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A234** (interim) | **noema#601.** Take EL's alternative 1. The route answers the PERD shape plus `correlation_id`. `investigation_id` is `inv_` plus the ULID of the input's core-minted correlation ID, so a retry gets the same value (A168). `conversation_ref` uses the same ULID with its contract prefix (EL checks PERD §32.3 and `common.v1`). `state` is `understanding`. | Nothing committed. It chooses between the alternatives EL put on noema#601 and applies **A168** (a retry gets the same value). |
| **A235** (interim) | **noema#590 (G0-N N10).** Unavailability on the ten switch cases plus the case-creation timeouts satisfy the fault family. A generated switch-timeout case becomes a registered follow-up for BO. It is not a gate condition. | Nothing committed. It fixes the reading of the fault-family line of G0-N item N10 that noema#590 argues. |
| **A236** (interim) | `NOEMA_PAYLOAD_MAX_BYTES` is 262144 in the bench profile, provisional (noema#606). | Nothing committed. It supplies a limit (AGENT-16: agents set no limit; this ruling does). |
| **A237** (interim) | **noema#611 as in §3.** | Nothing is recorded: the content is in "§3", which the Steward was not given. |
| **A238** (interim) | **The axe approval as in §3.** | Nothing is recorded: the content is in "§3", which the Steward was not given. |
| **A239** (interim) | The single-flight concurrency groups on noema#569 and noema#577 are accepted: `cancel-in-progress` for PR events only, run ID for the others. | Nothing committed. |
| **A240** (interim) | **Tushe consequences.**<br>• IL adds stale, reordered and drift faults to the hostility proxy (AT-07).<br>• Duplicate uses Tushe's replay endpoint. Timeout uses our receiver holding the response past 12 seconds.<br>• You create the read-only key `noema-harness-readonly` with the eight scopes. You register the webhook relay and rotate its secret (partner dashboard, MFA). Put the values in the bench Environment only, never in the runtime or model environments (INV-22). | Nothing committed. It applies Tushe's addendum of 15 Nov 2026 (committed in its own pull request) to the harness and names the Founder's actions. |

## 2. What the Steward did where the rulings are silent

- **A237 and A238 are recorded without their content.** The Architect's message refers to "§3" for both and the Steward was not given it. **The Architect is asked to post §3 on noema#183**; the Steward records it in a note on this record. For A238 (the "axe" approval, a dependency approval under AGENT-14) the package name, version and use are needed; none is invented here, and no [OPEN] entry is filed until they are given.
- **A240's "you" is the Founder.** The actions (create the read-only key, register the webhook relay, rotate the secret on the partner dashboard with MFA) are the Founder's, not the Steward's and not an agent's: no agent holds Tushe credentials (DEC-2026-10-16 E2). **No key, secret or address value is written in any repository file;** the values go in the bench Environment only (INV-22; DEC-2026-11-05, D5).
- **The eight scopes** are those Tushe's addendum lists for `noema-harness-readonly`: `events:read`, `audit:read`, `accounts:read`, `customers:read`, `cards:read`, `bills:read`, `compliance:read`, `group_savings:read`.
- **A235's "registered follow-up for BO".** The Steward proposes it as a debt entry (a generated switch-timeout case is not produced; owner BO; not a gate condition), numbered in the next debt pull request. If the Architect prefers a task row, plan v1.22 carries it.
- **A236 is bench only and provisional;** a production value would go through an [OPEN] entry (AGENT-02).
- **Next free ruling: A241.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A222 (merged); A223 to A228 in docs#182 and A229 to A233 in docs#185 (open when this record was written) | |
| This record | A234 to A240 | **A241** |
