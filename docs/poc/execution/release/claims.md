# External claims: rules and register

Date: 2026-11-03 · Task: GOV-29 (rules), GOV-15 (the wording itself) · Status: **DRAFT for the Founders' approval**

This file is the `claims.md` of the release evidence bundle (plan §13.4; REQ-BEN-008): the exact external claim wording the results permit. It is a **rules scaffold now and a register after the release run**. It adds no requirement and defines nothing the SoT defines: the positioning is SoT §25.5, the publication rules are SoT §38.8 and plan §14, and where this file seems to differ, they win.

**Permitted claims today: none.** No release run exists, so no number can be claimed. Nothing below is a claim.

## 1. Positioning

The only positioning used in any external or demo material is the four statements of **SoT §25.5**, cited by number: (1) enterprise identity and access management is consumed, never replaced; (2) Noema's own policy is typed, versioned data in deterministic code, with other policy engines consumed as evidence; (3) where permission-based safety stops, Noema starts; (4) task benchmarks measure whether an agent can complete the task, Noema's measures whether it is safe to let it. Use the SoT's wording when quoting. Plan §14 repeats the rule for demo material.

## 2. Rules for every number (SoT §38.8, plan §14)

| Rule | What it means in practice |
|---|---|
| Full distribution | Never cherry-pick. Show every family and every run, including failures and where an arm wins. |
| n | Every number states the number of cases it rests on. |
| Method | How the cases were generated (generator version, seed, layer), which are hidden-oracle, which are held-out, and the conditions exercised. |
| Bound | Zero failures in n cases is stated as a bound, not as zero: about 3/n at 95% confidence (the rule of three). SoT §38.8's own example: zero unsafe actions in 300 cases supports "below about 1% on this tested population". |
| Confidence interval | Every rate carries one. |
| Consistency | Model-dependent cases report pass^k (k = 5) beside the single-run result. |
| Synthetic | The environment, data and clocks are synthetic and are labelled so in every external use. |
| No ROI | No ROI or savings figure without a partner's measured baseline (PERD §69, G7). |
| Voice | Shown live on a real phone only if the voice gate passes (SoT §37.5, G5); otherwise in text. |
| Demo | Runs from the benchmarked engine; nothing scripted, edited or replayed from video. |
| Public benchmark | Outcomes are evaluated against the final state of the systems; pass^k is reported; the harness and public cases are open; the held-out set stays private (OD-16). |

## 3. Words we do not use

"Tamper-proof" and "immutable" (the Record is **tamper-evident**, writer-authenticated and externally anchored once REC-08 and REC-07 land; DEC-2026-10-31 D20), "compliant", "certified" and any named regulatory regime as a claim (counsel reviews the exact wording first, GOV-26; SoT §50.2 lists what Noema is designed for, not what it has achieved), "guaranteed", "zero risk", "proven in production", and any [HYPOTHESIS] stated as fact, [TARGET] stated as achieved, or [ILLUSTRATIVE] stated as a plan (SoT §0.2, §0.6).

## 4. How a claim gets in

1. The release run (BEN-26) and its bundle (BEN-27) exist, with the run ID and commit SHA.
2. The claim is written in the register below, from the bundle only, never from memory or a daily note.
3. The Founder and the benchmark owner approve the wording (GOV-15). Counsel reviews it first if it is regulatory (GOV-26).
4. The G7 review checks every line against the bundle (G7 checklist: every external number has n, method, bound and CI; clocks labelled SYNTHETIC; no ROI claim).

## 5. Register (empty until the release run)

| # | Claim wording (exact) | Number | n | How the cases were generated | Conditions exercised | Bound and CI | Run ID and SHA | Bundle file | Approved by (FND, B) | Counsel (if regulatory) | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| — | _none yet_ | | | | | | | | | | |
