# DEC-2026-11-16 · Tushe's addendum of 15 Nov 2026 is committed; OD-P-67 is closed

| | |
|---|---|
| **Status** | **Interim.** Recorded by the Repo Steward on the Architect's and the Founder's order of 16 Nov 2026 (A240 and the order to commit the addendum and close OD-P-67). Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 16 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Decides** | (1) Tushe's addendum is committed as a frozen correspondence record. (2) OD-P-67 is closed (§2). |
| **Closes** | OD-P-67: whether Tushe supplies the webhook signing secret. |
| **Supersedes** | The minimum safe default of OD-P-67 ("the relay-generated secret, synthetic, local only") is replaced by the rule in §2. |
| **Amends** | `docs/open-decisions.md` (the status line of OD-P-67 only), `docs/poc/tushe/responses/README.md` and `tools/frozen-files.sha256`. No SoT, PERD or plan text. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 16 November 2026
- Closes: OD-P-67
- Owner: Founder; Technical Co-Founder
- Decides: §1 and §2
- Decision: §1 and §2
- Rationale and evidence: Tushe's addendum of 15 Nov 2026 (`docs/poc/tushe/responses/2026-11-15-tushe-addendum-to-reply-of-10-nov.pdf`, SHA-256 `a2ce867534ef5d230ab07a62485b6fa59e75356736aca1712825b39be00ceaa4`), section 6; ruling A240
- Affected requirement IDs / SoT sections: REQ-API-008, REQ-ENV-005, REQ-ENV-007; INV-22; SoT §0.4
- Migration notes: none
- Supersedes: see the Supersedes row above

---

## 1. The addendum is committed

- **The file.** The PDF is committed unchanged under `docs/poc/tushe/responses/` and listed in the frozen-files list with its SHA-256 (DEC-2026-10-16 E9, E10). It is Tushe's statement, signed by Tushe's cofounder, dated 15 Nov 2026.
- **What it says, in the Steward's words and without opinion.** Tushe audited its M-items against its codebase and says nothing it listed is a missing capability. It corrects five points:
  - **M-13 (faults):** duplicate delivery and timeout are Tushe's and work today (the replay route re-delivers the same message; holding a response past Tushe's 12-second delivery timeout is recorded as a distinct timeout outcome). Stale, reordered and drift faults belong to Noema's harness proxy, and Tushe declines to build them into the platform.
  - **M-01:** a read-only programmatic credential already exists as a partner API key with read-only scopes (the addendum lists eight: `events:read`, `audit:read`, `accounts:read`, `customers:read`, `cards:read`, `bills:read`, `compliance:read`, `group_savings:read`); Tushe is not building a machine credential into the administration surface, and a named person is no longer required.
  - **M-02:** the payout transition log exists; "state at a point in time" is a client-side fold of the transitions up to a timestamp. Correlation and causation are on the event feed, not on the transition row (a two-call join).
  - **AT-05 and AT-17:** recovery from the event feed and an export built from API reads are called standard practice; Tushe asks nothing to be confirmed.
  - **D7 (webhook relay address):** it is self-serve: Noema registers the address, chooses the subscriptions, sends a test and rotates the signing secret through Tushe's own routes.
  - **Still outstanding from Tushe:** M-06, M-07, M-16 and M-17, "being sent by Wednesday 18 November".
- **What the commit does not do.**
  - **It does not make the addendum govern endpoint semantics.** What governs them is the list in `docs/poc/tushe/README.md` (DEC-2026-10-16 E10): the specification, Tushe's response of 7 Oct, DEC-2026-10-12, delta v1.2 and the signed worksheet. The addendum names routes and a credential that no governing document names yet. **No adapter or test is built on those routes from this record;** the adoption goes through a delta file (a v1.3 of the delta already exists as a draft) and the Founders' or the Architect's order.
  - **It is not observed behaviour.** Noema has seen none of it work (AGENTS §2, item 4). Acceptance is the joint session and the signed record, not this note.
  - **The reply of 10 Nov is not committed.** The addendum corrects "our reply of 10 November"; that file was not supplied to the Steward. Its row in the correspondence list says so. The Founder supplies the PDF as received.

## 2. OD-P-67 is closed

- **The question.** Whether Tushe gives Noema the webhook signing secret, or Noema generates it and gives it to Tushe (OD-P-67; Block E, E4; noema#48).
- **The answer, as far as the documents give it.** Tushe's addendum (section 6) says the webhook endpoint is self-serve and names `rotate-secret` as "your signing secret, yours to rotate". Ruling A240 says the Founder registers the webhook relay and rotates its secret on the partner dashboard (with MFA) and puts the values in the bench Environment only, never in the runtime or model environments (INV-22). **So the secret is the one Tushe's endpoint registration carries, rotated by Noema's Founder; the relay holds only that value, in its own Environment (execution reset E6; DEC-2026-11-05 D5), and no value is written in any repository file.**
- **What the documents do not say in so many words.** Who generates the first value is not stated by the addendum; the rule above does not depend on it, because the relay holds whatever value the registered endpoint carries and the Founder rotates it. If Tushe's route behaves otherwise when the Founder registers the endpoint, that is reported on noema#48 and reopens this entry.
- **The owner** of the secret in the vendor register (`docs/vendors/README.md`, row "Webhook signing secret") stays the Founder.
- **The minimum safe default of OD-P-67** (the relay-generated secret, synthetic, local only) is replaced by the rule above once the Founder registers the endpoint; until then the relay runs on its synthetic local secret and nothing real is configured.
