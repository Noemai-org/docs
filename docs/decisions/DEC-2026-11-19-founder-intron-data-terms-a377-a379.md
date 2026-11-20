# DEC-2026-11-19 · Founder decision: Intron's email of 18 Nov is the POC data terms (A377 to A379)

| | |
|---|---|
| **Status** | **Founder decision**, given to the Repo Steward on 19 Nov 2026 and committed here by the Steward. It counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 19 November 2026 |
| **Owner** | Founders |
| **Decides** | The data terms for the POC (A377), Voice's live calls and baseline (A378), and consent and retention for recordings (A379). |
| **Closes** | OD-P-89 (Intron's written data terms). Noema#294's Founder item on the recording plan; noema#201's hold. |
| **Supersedes** | **A180's "written terms before real audio"**, which A377 replaces. Whatever else says a DPA, written terms, counsel or a consent form must come first for Intron or for recordings of people outside the team: OD-P-89's default; VOI-05's consent form, counsel and signature elements (plan v1.25, below); the Intron row and the DPA rule of `docs/vendors/README.md`. |
| **Amends** | The plan (VOI-05, by `CR-2026-11-19-A379-voi-05-recording-plan`, plan v1.25); `docs/open-decisions.md` (OD-P-89 closed); `docs/vendors/README.md`; noema#294 and noema#201 (comments, below). Nothing in the SoT. |
| **Authority order applied** | Latest recorded founder decision (SoT §0.4, item 1) → SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Founder decision; counts on merge by a non-author Founder (A111)
- Date: 19 November 2026
- Owner: Founders
- Decides: A377, A378, A379 and the instructions in §2
- Decision: §1 and §2
- Rationale and evidence: the Founder's instruction to the Steward of 19 Nov 2026; Intron's email of 18 Nov 2026 (not stored in the repository; its commitments are as the Founder states them in A377)
- Affected requirement IDs / SoT sections: REQ-VOI-001, REQ-VOI-004; AGENT-18; PERD R-18; SoT §50.2; AGENTS §10; VOI-05, VOI-06, VOI-16; GOV-25 (its provider due diligence for Intron)
- Supersedes: see the Supersedes row above
- Migration notes: plan v1.25 changes the VOI-05 row only; no contract, schema or code change

## 1. The decisions, exactly as the Founder worded them

**A377:** Intron's email of 18 Nov commits to zero data retention by default (configurable upward), no training on customer data, SOC 2 Type I / ISO 27001 / NDPR certification, and the DPA alongside a commercial agreement. That email is accepted as the data terms for the POC and replaces A180's "written terms before real audio". A DPA is no longer a precondition for any work, including real-speaker audio. The Founder holds Intron to those commitments in writing.

**A378:** Voice's live calls start as soon as the key arrives; the baseline run starts on synthetic audio and recordings of consenting team members; #201 is no longer held on the DPA; counsel is not needed on any of these and blocks nothing.

**A379:** consent forms are no longer required for recordings of people outside the team (amend VOI-05); the Integrator account's retention is set to zero days; REQ-VOI-004 still applies (raw audio never in the repo or CI artifacts, only in the bench Environment's private store, deleted per the plan); synthetic audio stays labelled; the USD 500 custom voice per language is declined for the POC.

## 2. The Founder's instructions to the Steward, and what was done

1. **A Founder decision record for 19 Nov:** this file.
2. **Amend VOI-05 by change request:** `CR-2026-11-19-A379-voi-05-recording-plan` and plan v1.25 (the VOI-05 row only). The consent form and the counsel and signature elements are removed. Speaker mix, accents, noise conditions, devices, retention zero and raw-audio handling stay.
3. **Update issue #294** (noema): a comment and an edited body say what A377 to A379 change. Items 3 and 4 of its Needs list (the correctness floor and the devices and SIMs) are not touched by this decision and stay with the Founder.
4. **#201 is no longer held** (noema#201, the VOI-05 draft): a comment says so. The draft's own text (its consent section and its decisions in its section 8) is Voice's to bring in line with A379 in that pull request; the Steward does not edit another agent's pull request.
5. **No document may claim regulatory compliance** (AGENTS §10; SoT §50.2). Intron's certifications are Intron's own statements, quoted as that and never as Noema's. Nothing in this record says Noema or Intron complies with any regime.
6. **OD-P-89 is closed** in `docs/open-decisions.md`, with the Intron statements kept as Intron's.

## 3. What the Steward notes

- **What stays as it was:** REQ-VOI-004 (raw audio never in the repository or in CI artifacts; only in the bench Environment's private store; deleted per the plan), the SYNTHETIC label on synthetic audio (AGENT-25), masking before any provider call (AGENTS §10), and PERD R-18's rule that no customer or partner data goes to a provider whose data terms are not approved: here the Founder has approved Intron's terms for the POC (A377). The terms of any other provider are not covered.
- **GOV-25** (partner data schedule and provider due diligence, "approved with counsel", plan v1.24) and **GOV-26** (counsel review of any regulatory wording) are not changed by this record: A378 says counsel blocks nothing "on any of these" (the Intron terms, the recordings, the baseline), and these two rows are about partner data and external regulatory claims. The Founder or the Architect says if they change.
- **VOI-06 and VOI-08 and the demo pre-flight** also say "consent" or "consent forms in hand" (plan v1.24 rows VOI-06, VOI-08 and the pre-flight list). A379 says to amend VOI-05 and says consent forms are no longer required for people outside the team; it does not name those rows, so the Steward does not change them. The demo's pre-flight line and VOI-06's "annotations and consent" are open for the Architect or the Founder to name.
- **The key:** A378 says live calls start when the key arrives. No key name is decided (`docs/vendors/README.md`). The Steward does not touch it.
- **The USD 500 custom voice per language is declined** (A379); nothing in the repository depends on it.
- **No number or certification here is Noema's claim.** Everything in A377 about Intron is Intron's statement, accepted by the Founders as the POC data terms; it is not verified by the Steward.
