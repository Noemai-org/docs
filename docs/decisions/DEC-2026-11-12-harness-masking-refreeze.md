# DEC-2026-11-12 · Harness masking re-freeze: the digit-run floor goes from 8 to 4 (ruling A162)

| | |
|---|---|
| **Status** | **Proposed by the Principal Architect's ruling A162 (12 Nov 2026). The Founder said in the session of 12 Nov 2026 that they approve it, with the two conditions in §2** (frozen values, D10). The Repo Steward records that statement here; it is not an approval until a Founder who did not author this pull request merges it (A111; AGENTS §2, item 3). |
| **Date** | 12 November 2026 |
| **Owner** | Founder (the approval); Benchmark Owner (the re-freeze in `noema`); Principal Architect (the ruling) |
| **Decides** | The two harness configurations are re-frozen without the masking key, and the harness reads the shared `masking-limits.v1`, whose floor is 4. |
| **Closes** | EL's finding that the harness still masks at 8. |
| **Supersedes** | The frozen value `masking.account_run_min_digits: 8` in `benchmark/decisions/harness-gpt-6-luna.json` and `benchmark/decisions/harness-gpt-6.1-terra.json`, and the SHA-256 hashes of those two files in `benchmark/decisions/2026-10-27-model-selection.md`, from the moment the new freeze record in `noema` is merged. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Proposed; the Founder's in-session approval of 12 Nov 2026 is recorded here and counts on merge by a non-author Founder (A111) (frozen values)
- Date: 12 November 2026
- Closes: EL's finding on the harness masking floor
- Owner: Founder; Benchmark Owner; Principal Architect
- Decides: the harness masking floor is 4 and comes from `masking-limits.v1`
- Decision: §1
- Rationale and evidence: ruling A162; the PERD explanation and error-body criteria (maximum unmasked digit run 4) and A154; EL's reading of the two harness configs
- Affected requirement IDs / SoT sections: PERD §44.2; AGENT-13, AGENT-28; INV-22
- Migration notes: the two config files and their hashes change in `noema` (§3); no run has used the old values
- Supersedes: see the Supersedes row above

---

## 1. The decision

The prompts the harness sends to a model are an outward surface. The PERD wins over the earlier harness value: the floor is **4**, not 8 (A162; A154).

1. `benchmark/decisions/harness-gpt-6-luna.json` and `harness-gpt-6.1-terra.json` are re-frozen **without** the `masking` key.
2. The harness reads the masking floor from the shared `masking-limits.v1`, the one constant shared by the core and the model service (A154).
3. A new freeze record in `noema` (`benchmark/decisions/`) carries the new hashes of the two files.
4. **The same record names the path and the SHA-256 of `masking-limits.v1`** (the file that noema#468 adds; it is not on `main` yet) at the commit the re-freeze covers. The masking value is no longer pinned inside the two hashed configs, so without this hash a later run has no frozen proof of the floor. The re-freeze is not complete until the record carries it.

## 2. Why it is safe

Tightening masking is safer: a shorter unmasked run exposes less. **No comparison-arm run has taken place** (no arm runs before G3, A118), so no comparison result was produced under the old value and none has to be redone. **Earlier live calls are not comparison results but did use the old value:** the pilot of the 27 Oct freeze, the cancelled run mentioned on noema#342, and any UND-05 qualification call made before the re-freeze merges. Those results stay labelled as made under `account_run_min_digits: 8` and are not mixed with results under the new floor. A live call made after this record is approved should wait for the re-freeze to merge.

## 3. What this record does not do

- It does not change any file in `noema`. The Benchmark Owner makes the two config edits, computes the new SHA-256 hashes of the two configs and of `masking-limits.v1` and merges the new freeze record; the benchmark tests that check the hashes fail until the new record is merged (`benchmark/decisions/README.md`).
- It does not touch the corpus, the scoring code, the gates or the retry policy of the 27 Oct freeze.

## 4. What would invalidate it

A requirement that the harness mask at a different floor than the product (for example, to keep the prompts comparable with a run made under 8). No such run exists.
