# DEC-2026-11-13 · Voice provider (Intron): draft of the SoT edit, for the Founders

| | |
|---|---|
| **Status** | **DRAFT for the Founders to author or approve. This file edits nothing.** The SoT is changed only by a new version made by the Founders, with an Appendix D entry (AGENTS §11, docs repository). |
| **Date** | 13 November 2026 |
| **Owner** | Founders |
| **Decision record** | [DEC-2026-11-13-voice-provider-intron](DEC-2026-11-13-voice-provider-intron.md) (rulings A179 to A182) |
| **Version number** | A179 says "SoT v1.7". The SoT on `main` is v1.11 and Appendix D already lists v1.7 (16 Oct 2026). The next version is **v1.12**; the Founders confirm the number. |

**Record fields (decisions README template).**

- Status: DRAFT for the Founders; edits nothing
- Date: 13 November 2026
- Closes: nothing
- Owner: Founders
- Decides: nothing; proposes the SoT text for the decision of DEC-2026-11-13-voice-provider-intron
- Decision: none; see the proposed text below
- Rationale and evidence: rulings A179 to A182 of 13 Nov 2026 (the Architect's message, relayed to the Steward)
- Affected requirement IDs / SoT sections: BD-16, OD-04, SoT §35.3, §37, §51 and Appendix D
- Migration notes: none; applies only if the Founders author or approve the SoT edit
- Supersedes: nothing

---

Each block below gives the place in `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.11, line numbers as of 13 Nov 2026), the text now, and the proposed text. The proposed text follows A179 and adds no requirement. Lines 218 and 1134 mention these vendors only as market background and stay unchanged.

## 1. BD-16 (line 101, the decision table)

**Now:** | BD-16 | No single provider dependence. Understanding integrates at least GPT, Gemini and Claude, and speech integrates at least Aethex AI, Indigenius and N-ATLAS, all behind provider-neutral interfaces. Switching providers is configuration plus a benchmark run, never a code change. | §17, §35.3 |

**Proposed:** | BD-16 | No single provider dependence for Understanding: it integrates at least GPT, Gemini and Claude behind provider-neutral interfaces. **Speech has one integrated provider in the POC, Intron Sahara v2.5, behind separate provider-neutral speech-to-text and text-to-speech interfaces; replacing it needs no change to Trust, Execution, Outcome or the Record, and a provider failure degrades safely to text.** Whether to add a second speech provider is a Founder decision at pilot readiness (OD entry). Switching providers is configuration plus a benchmark run, never a code change. | §17, §35.3 |

## 2. The BD-16 decision statement (line 729)

**Now:** **[DECISION — BD-16]** Noema integrates several providers at once rather than one with a theoretical fallback. Understanding runs on GPT (OpenAI), Gemini (Google) and Claude (Anthropic); speech runs on Aethex AI, Indigenius and N-ATLAS. The default provider for each task and locale is whichever performs best on the benchmark, and it can be changed per tenant or locale by configuration. If a provider degrades or becomes unavailable, traffic moves to another without code changes.

**Proposed:** **[DECISION — BD-16]** Understanding runs on several providers at once rather than one with a theoretical fallback: GPT (OpenAI), Gemini (Google) and Claude (Anthropic). The default provider for each task and locale is whichever performs best on the benchmark, and it can be changed per tenant or locale by configuration; if an Understanding provider degrades or becomes unavailable, traffic moves to another without code changes. **For the POC, speech runs on one provider, Intron Sahara v2.5, behind separate provider-neutral speech-to-text and text-to-speech interfaces under `providers/` in the model service. A speech provider failure degrades safely to text: no guessed intent, no unsafe retry, no compromised execution. Aethex AI, Indigenius and N-ATLAS are not integrated in the POC. The Founder decides at pilot readiness, in a new OD entry and from POC evidence, whether to add a second speech provider.**

## 3. §35.3, the speech row (line 1511)

**Now:** | Speech | Aethex AI, Indigenius and N-ATLAS, all behind the provider-neutral speech interface (BD-16) | No single-provider dependence |

**Proposed:** | Speech | Intron Sahara v2.5, behind separate provider-neutral speech-to-text and text-to-speech interfaces (BD-16) | Replacing it changes no Trust, Execution, Outcome or Record code; failure degrades to text |

## 4. §37, "Provider runs" (line 1816)

**Now:** **Provider runs.** Every release run executes the Understanding and voice suites on **every** integrated provider: GPT, Gemini and Claude for Understanding; Aethex AI, Indigenius and N-ATLAS for speech. Results are recorded per provider. The default per task and locale is set from these results. A provider whose results fall below the §38.2 targets is not used as a default until it recovers.

**Proposed:** **Provider runs.** Every release run executes the Understanding and voice suites on **every** integrated provider: GPT, Gemini and Claude for Understanding; Intron Sahara v2.5 for speech (speech-to-text and text-to-speech, with the model IDs pinned and qualified before any gate run). Results are recorded per provider. The default per task and locale is set from these results. A provider whose results fall below the §38.2 targets is not used as a default until it recovers; **a weak speech result is reported as measured, and the gate thresholds do not change.**

## 5. OD-04 (line 2381, §46)

**Now:** | OD-04 | Speech providers | **DECIDED 9 Oct 2026 (DEC-2026-10-09; BD-16).** Aethex AI, Indigenius and N-ATLAS, all integrated behind the provider-neutral speech interface. Default per locale chosen by benchmark (key-slot accuracy, then latency, then cost); switchable by configuration. Each must pass the voice subset and the real-conditions gate (§37.5) before it serves a demo or pilot, and must clear vendor due diligence (data terms, continuity) before handling partner data. | Closed |

**Proposed:** | OD-04 | Speech providers | **DECIDED 9 Oct 2026 (DEC-2026-10-09; BD-16); CHANGED 13 Nov 2026 (DEC-2026-11-13-voice-provider-intron).** Intron Sahara v2.5 is the sole integrated speech provider for the POC, behind separate provider-neutral speech-to-text and text-to-speech interfaces; Aethex AI, Indigenius and N-ATLAS are not integrated in the POC. It must pass the voice subset and the real-conditions gate (§37.5) before it serves a demo or pilot. **No real speaker's audio or transcript goes to Intron until the Founder commits written data terms** (retention, zero data retention, no training, sub-processors, hosting region, deletion timeline, incident notice); until then only synthetic audio. Whether to add a second provider is a Founder decision at pilot readiness. | Closed |

## 6. §51, the `/providers` layout (line 2575)

**Now:**     /providers          GPT, Gemini, Claude; Aethex AI, Indigenius, N-ATLAS adapters

**Proposed:**     /providers          GPT, Gemini, Claude; Intron Sahara v2.5 adapters (speech-to-text, text-to-speech)

## 7. Appendix D entry (new first row of the table)

| 1.12 | 13 Nov 2026 | **Voice provider (DEC-2026-11-13-voice-provider-intron; rulings A179 to A182).** Why: the Founder decided that Intron Sahara v2.5 is the sole integrated speech provider for the POC. What changed: BD-16 (§ decisions table and the decision statement), §35.3 (speech row), §37 ("Provider runs"), OD-04 (§46) and the §51 `/providers` layout now name Intron and say that a speech provider failure degrades safely to text; a second provider is a Founder decision at pilot readiness, from POC evidence. Aethex AI, Indigenius and N-ATLAS are no longer integrated in the POC. No gate threshold changes. Data terms: no real speaker's audio or transcript goes to Intron until the Founder commits written terms. |

The Founders may also want the front-matter version line and the "Governing source" lines of the PERD and the plan to name the new version; those are separate new-version files (PERD v1.24 is drafted in this pull request).
