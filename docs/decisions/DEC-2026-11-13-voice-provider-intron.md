# DEC-2026-11-13 · Voice provider: Intron Sahara v2.5 is the sole integrated speech provider in the POC (rulings A179 to A182)

| | |
|---|---|
| **Status** | **Proposed. Founder decision of 13 Nov 2026, relayed by the Principal Architect to the Repo Steward; recorded by the Repo Steward, subject to the SoT process.** It counts as recorded when a Founder who did not author this pull request merges it (A111; AGENTS §2, item 3). **A179 takes effect only with the SoT version that adopts it** (the next SoT version after v1.11; see §2, "The version number"). Until then the SoT, the PERD v1.23 and the plan v1.18 govern and no one builds against this record. |
| **Date** | 13 November 2026 |
| **Owner** | Founders (the decision and the SoT edit); Principal Architect (the rulings) |
| **Decides** | Four rulings, A179 to A182 (§1). |
| **Closes** | Nothing yet. OD-04 and BD-16 are closed or changed only when the SoT is edited. Opens OD-P-87 to OD-P-91 (§2). |
| **Supersedes** | **From the date the SoT edit takes effect:** the speech half of BD-16 (SoT lines 101 and 729), SoT §35.3 (line 1511), §37 "Provider runs" (line 1816), OD-04 (line 2381), the `/providers` layout (line 2575), item 4 of `DEC-2026-10-09-deployment-temporal-providers`, REQ-VOI-002 and the speech rows of PERD v1.23 (lines 494, 979, 3904, 3954, 4050, 6219), and the AGENTS §6 row "Aethex AI, Indigenius and N-ATLAS behind `providers/`". Nothing is superseded before then. |
| **Amends** | Drafts only: the SoT (see `DEC-2026-11-13-voice-provider-intron-sot-draft`, which does not edit the SoT), PERD v1.24 (new file, Proposed), and a change request for six plan tasks. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Proposed; Founder decision of 13 Nov 2026 relayed by the Architect; counts on merge by a non-author Founder (A111); effective only with the SoT edit
- Date: 13 November 2026
- Closes: nothing yet; opens OD-P-87 to OD-P-91
- Owner: Founders; Principal Architect
- Decides: A179 to A182
- Decision: §1
- Rationale and evidence: the Architect's message of 13 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: BD-16, OD-04, SoT §35.3, §37, §51 (`/providers`), INV-29; REQ-VOI-002, REQ-VOI-003; plan tasks PRE-04, VOI-01, VOI-04, VOI-10, BEN-23, UND-13; GOV-25, VOI-05, VOI-14, VOI-16
- Migration notes: none for code. A new SoT version and PERD v1.24; the plan follows by change request ([CR-2026-11-13-A179-intron-voice-provider](../poc/execution/change-requests/CR-2026-11-13-A179-intron-voice-provider.md)); the `noema` copies of `AGENTS.md` and `CLAUDE.md` are re-pointed after the merge (REQ-OPS-005)
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A179** | **Intron Sahara v2.5 is the sole integrated STT and TTS provider for the POC.** STT and TTS have separate provider-neutral interfaces under `providers/` in the model service; Intron is implemented behind them. Replacing Intron requires no change to Trust, Execution, Outcome or the Record. Provider failure degrades safely to text: no guessed intent, no unsafe retry, no compromised execution. Aethex AI, Indigenius and N-ATLAS are not integrated in the POC. This changes BD-16, OD-04 and the SoT lines above; it takes effect only with SoT v1.7. The Founder decides in a new OD entry, at pilot readiness, whether to add a second provider, using POC evidence: the G5 voice gate result, the field report (VOI-14), the latency lab report (VOI-16), Intron's answer on capacity, the data-terms outcome (GOV-25), and failure drills. The gate thresholds already in the pack and plan decide; agents set none. | The speech half of BD-16 and OD-04 (SoT), once the SoT edit takes effect. Does not reinterpret BD-16 (see §2). |
| **A180** | **No real speaker's audio or transcript goes to Intron until the Founder commits written terms:** retention, zero data retention, no training, sub-processors, hosting region, deletion timeline, incident notice. The VOI-05 consent form names Intron. Until then only synthetic audio. "Zero data retention" is an unverified claim until it is in writing. | Nothing. It applies PERD R-18 and AGENTS §10 (no partner data until each provider's data terms are approved) to Intron by name. |
| **A181** | **Spoken amounts, account identifiers and transaction references are never trusted:** they enter through canonical input and the schema gate; partial transcripts never set a slot; a missing confidence counts as low. "Insufficient confidence" is Founder or pack data. A spoken "yes" is never a confirmation; only the signed card submit is. TTS speaks only the core's masked answer text, never progress text or an execution claim the core did not send. Intron's documented 10 to 100 character TTS chunking is done by the adapter. | Nothing. It restates INV-02, INV-04 and A154 for the voice path. |
| **A182** | **Intron's STT and TTS model IDs are pinned and qualified (UND-13) before any gate run.** BEN-23 becomes "Intron on the voice subset": per-locale key-slot accuracy, latency and cost, with pacing for the documented rate limits. G5 thresholds do not change. A weak result is reported as measured. | The plan row BEN-23 ("Aethex AI, Indigenius and N-ATLAS on the voice subset"), once the plan version that applies it is written. |

The Architect's instruction to the Steward, which this pull request follows: prepare **one** pull request (AGENT-29) holding the decision record, a draft of the SoT edit for the Founders to author or approve (the SoT is not edited in place), PERD v1.24 as a new file, the AGENTS §6 row, a change request for PRE-04, VOI-01, VOI-04, VOI-10, BEN-23 and UND-13, the OD entries and the regenerated register; use A179 to A182 as given; next free ruling A183; post a CONFLICT block in the pull request with the BD-16 quotes.

## 2. What the Steward did where the rulings are silent, and what needs a decision

- **The conflict, stated, not resolved.** BD-16 says "No single provider dependence", with "speech integrates at least Aethex AI, Indigenius and N-ATLAS" (SoT line 101), and SoT line 729 says "speech runs on Aethex AI, Indigenius and N-ATLAS". A179 makes Intron the only integrated speech provider. The Steward did not reinterpret BD-16, as the Architect instructed. The pull request carries a CONFLICT DETECTED block with the quotes (PERD REQ-AGT-003). What stays true meanwhile is the SoT text (AGENT-20: the safer reading is the committed document), so **no one builds against A179 until the SoT edit is approved.**
- **The version number.** A179 says it takes effect "only with SoT v1.7". The SoT on `main` is **v1.11** (Appendix D lists v1.7 as 16 Oct 2026, money in minor units). The next SoT version is therefore v1.12. The Steward wrote "the next SoT version after v1.11 (v1.12)" in the drafts and asks the Architect or the Founders to confirm the number. This is a conflict between the ruling's text and the SoT, listed in the CONFLICT block.
- **What is drafted, not edited.** `DEC-2026-11-13-voice-provider-intron-sot-draft` holds the exact replacement text for each SoT place and an Appendix D entry, for the Founders to author or approve. The SoT file is untouched. PERD v1.24 is a new file marked Proposed; v1.23 stays unchanged. No plan version is written: the change request carries the six task changes until the SoT edit is approved (plan §19).
- **AGENTS §6.** The Steward changed the row to say it is a rule from the SoT edit onward, and keeps the current rule in the same row until then, so AGENTS.md does not override the SoT (AGENTS §2, item 9).
- **Derived documents.** `docs/vendors/README.md` gets an Intron row marked "pending the SoT edit". `docs/engineering/boundary-map.md` and the register's OD-04 row follow the SoT and are not touched here; the OD-04 row is generated from SoT §46.
- **Open decisions filed (AGENT-02).** OD-P-87 (the SoT edit for BD-16 and OD-04), OD-P-88 (a second speech provider at pilot readiness), OD-P-89 (Intron's data terms, A180), OD-P-90 (Intron's rate limits and capacity), OD-P-91 (per-token confidence). Each carries the default from the rulings and invents no figure. OD-P numbers 83 and 84 stay with BO and FE (A171).
- **What the Steward did not do.** It did not contact Intron, did not set any threshold, TTL or confidence limit (A181 says those are Founder or pack data), did not name interface identifiers, and did not approve any retention claim.
- **Numbering.** Next free ruling: **A183**. docs#166 (plan v1.18, EDG-02) is open and independent.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records (merged) | A41 to A178 | |
| This record | A179 to A182 | **A183** |
