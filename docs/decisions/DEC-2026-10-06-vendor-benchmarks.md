# DEC-2026-10-06-vendor-benchmarks

- Date: 6 October 2026
- Owner: Founders (Technical Co-founder)
- Decision:
  1. **Understanding/LLM Providers (Closes OD-05):** The Phase A benchmark for Intent extraction on the code-switched suite will compare **Google Gemini (Latest Pro)** against **Anthropic Claude (Latest Sonnet)**.
  2. **Speech Providers (Closes OD-04):** The Phase A benchmark for the voice subset will compare **Intron Health** (fulfilling the African-accent specialization requirement) against **Deepgram** (acting as the low-latency baseline).
- Rationale and evidence:
  - Both Gemini and Claude offer state-of-the-art strict schema adherence (function calling) required by the `instructor` library, while maintaining the necessary nuance for Nigerian code-switched text.
  - Intron Health provides the required regional specialization for the synthetic POC wedge, while Deepgram provides the global benchmark for latency and cost.
- Affected requirement IDs / SoT sections:
  - Closes: OD-04, OD-05.
- Supersedes: The recommended open defaults for OD-04 and OD-05.
