# DEC-2026-11-16 · The Founder's direction on Intron (A241)

| | |
|---|---|
| **Status** | **Interim.** The Founder's direction of 16 Nov 2026 on Intron's reply, relayed to the Repo Steward, who records it (ruling number **A241**). Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 16 November 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Decides** | The way the Intron work proceeds (§1). |
| **Closes** | Nothing. It refines how **A179 to A182** are applied. |
| **Supersedes** | Nothing committed. It sets the working posture for OD-P-87 to OD-P-91 (§2). |
| **Amends** | `docs/open-decisions.md` (vendor statements added to OD-P-89, OD-P-90 and OD-P-91; no decision in them changes). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 16 November 2026
- Closes: nothing
- Owner: Founder; Technical Co-Founder
- Decides: A241
- Decision: §1
- Rationale and evidence: the Founder's direction of 16 Nov 2026 and Intron's email of 13 Nov 2026 (two messages), relayed to the Steward
- Affected requirement IDs / SoT sections: AGENT-16, AGENT-18, AGENT-27; REQ-VOI-001, REQ-VOI-003; SoT BD-16, OD-04; PERD R-18; GOV-25; VOI-16
- Migration notes: none
- Supersedes: nothing committed

---

## 1. The direction, exactly as given

**A241 (interim; the Founder's direction): proceed fast, proportionately.**

1. Intron integration starts now with synthetic audio.
2. Requirements fall in three classes: **blocks engineering work**; **restricts real speaker data** (A180, DPA); **blocks production**. Vendor uncertainties are notes, not decisions, unless they block code or real data.
3. The only latency target is **VOI-16** (under 1.8 s end to end).
4. No new thresholds or governance decisions without a specific technical, security, legal or architectural reason.

## 2. What the Steward did

- **Vendor statements are recorded, marked unverified.** Intron's email of 13 Nov 2026 (and its follow-up on streaming latency, 14 minutes later) is recorded in OD-P-89 (data terms), OD-P-90 (rate limits and capacity) and OD-P-91 (per-token confidence) as **vendor statements, unverified until the DPA is signed and, for performance figures, until measured**. They are notes, not decisions, and set no threshold. Names, telephone numbers and calendar links in the email are not copied. Prices are recorded only as Intron's statement (AGENT-18).
- **OD-P-91 is not answered by the email.** It says nothing about a confidence for each token. The entry stays open on that point; the default (a missing confidence counts as low) already blocks no engineering work.
- **The three classes, applied to Intron's statements (a proposal; the Founder corrects it).**

| Class | What Intron's email puts in it |
|---|---|
| **Blocks engineering work** | Nothing in the email. Engineering starts on synthetic audio (A241, point 1) with the Integrator account's free test minutes. One thing to watch: the real-time streaming endpoints are said to go live "in the next few weeks"; until they do, a streaming pipeline can be built and tested on synthetic audio and the voice simulation library (VOI-17), but not measured against Intron's streaming endpoints. That is a note, not a block. |
| **Restricts real speaker data (A180, the DPA)** | The Data Processing Agreement (signed together with the commercial agreement); retention (the customer sets it, new accounts start at zero); no training on customer audio (stated); processing in AWS Ireland; the certifications Intron states (SOC 2 Type I, ISO 27001, NDPR). All are claims until the DPA and its evidence are in hand. Until then only synthetic audio goes to Intron (A180, OD-P-89). |
| **Blocks production** | The DPA; the concurrency (3 sessions by default, raisable once peak concurrency and volumes are known); rate limits (set in the same step); the pricing and volume tier. |

- **VOI-16 is the only latency target.** Plan task VOI-16 states it: end of speech to first spoken word on the clean path, against the under 1.8 s target, by stage. Intron's quoted figures (partial transcripts about 1.7 s, P95 3 s; final transcript P95 8 s on a 5-minute stream) are **its statements, not targets**, and are not compared to VOI-16 until measured on the streaming endpoints. The Steward notes, without deciding, that the 8-second final-transcript figure and the 1.8 s target measure different things; the lab report (VOI-16) is where they meet.
- **Intron's questions to us** (use case and split, peak concurrent sessions and hours, latency target, text-to-speech volume, a call) are for the Founder or the Voice Engineer to answer. They set no threshold (point 4).
- **The Steward's reading of point 1, for the Founder to confirm.** OD-P-87 says no one builds against A179 until the SoT edit that adopts it (v1.12) merges (AGENT-20, AGENT-27). The Founder's direction is the latest recorded founder decision (SoT §0.4); on merge of this record it allows Intron adapter work **on synthetic audio** to start without waiting for v1.12. The SoT edit itself still follows: the Steward does not edit the SoT, and the v1.12 branch is refreshed for the Founder to open as a pull request.
- **No new threshold, task row or governance decision is added** by this record (point 4).
