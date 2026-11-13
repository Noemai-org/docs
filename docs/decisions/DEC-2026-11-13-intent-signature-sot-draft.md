# DEC-2026-11-13 · The intent signature: draft of the SoT edit (v1.13), for the Founders

| | |
|---|---|
| **Status** | **DRAFT for the Founders to author or approve. This file edits nothing.** The SoT is changed only by a new version made by the Founders, with an Appendix D entry (AGENTS §11, docs repository). Interim ruling A189; counts as recorded once a Founder who did not author this pull request merges it (A111). |
| **Date** | 13 November 2026 |
| **Owner** | Founders |
| **Ruling** | A189 (interim), in [DEC-2026-11-13-architect-rulings-a183-a192](DEC-2026-11-13-architect-rulings-a183-a192.md); A177 stays interim until this edit. |
| **Version number** | **v1.13.** The Intron change (rulings A179 to A182) is v1.12 and is a separate pull request (docs#168). This draft is applied after v1.12. |

**Record fields (decisions README template).**

- Status: DRAFT for the Founders; edits nothing
- Date: 13 November 2026
- Closes: nothing (OD-P-86 closes when the SoT edit takes effect)
- Owner: Founders
- Decides: nothing; proposes the SoT text for ruling A189
- Decision: none; see the proposed text below
- Rationale and evidence: ruling A189 of 13 Nov 2026 (the Architect's message, relayed to the Steward); OD-P-86
- Affected requirement IDs / SoT sections: SoT §7 (the Intent Object and its signature), §36 diagram, §43.1, Appendix A glossary, Appendix D; INV-29, AGENT-02
- Migration notes: none; applies only if the Founders author or approve the SoT edit. PERD §20.1 ("an HMAC over ...") changes in a later PERD version by a new file (not drafted here)
- Supersedes: nothing

---

## The conflict this resolves

SoT §7 says the Intent Object is "signed by Understanding", and the Trust row lists "Schema and signature of the Intent Object" among Trust's checks. Ruling A189 says what the POC does instead: **Trust checks that the recomputed `intent_hash` equals the hash in the signed `INTENT_ADMITTED` event**, read through the admission reader (tenant, principal and correlation bound). The model service never signs (INV-29). Until the SoT changes, the conflict stays open as OD-P-86 and G1 evidence says "signatures verified: no".

Line numbers are those of `docs/NOEMA_SOURCE_OF_TRUTH.md` v1.11 on 13 Nov 2026 (they move with v1.12; the Founders apply the blocks by their text).

## 1. §7, the Trust "Checks" cell (line 449)

**Now:** Schema and signature of the Intent Object; freshness of evidence

**Proposed:** Schema of the Intent Object; that the recomputed `intent_hash` equals the hash in the signed `INTENT_ADMITTED` event; freshness of evidence

## 2. §7, the first artifact (line 458)

**Now:** 1. **Intent Object**, signed by Understanding. Says what was asked, in structured form, with every ambiguity flagged. It is a *proposal*.

**Proposed:** 1. **Intent Object**, produced by Understanding and admitted by the core. Says what was asked, in structured form, with every ambiguity flagged. It is a *proposal*. The core computes its `intent_hash` after the schema gate, and the Record signs the `INTENT_ADMITTED` event that carries that hash; Trust checks the recomputed hash against the signed event. The model service never signs.

## 3. The pipeline diagram (line 1481)

**Now:** `Intent Object (signed)`

**Proposed:** `Intent Object (hashed and admitted)`

## 4. §43.1, the Intent Object example (line 2070) and the note under it

**Now:** the example ends with `"sig": { "key_id": "und-2026-10", "value": "..." }`.

**Proposed:** the example keeps its shape, and a sentence is added under it: "In the POC the `sig` member is an unsigned marker. The signature that counts is the Record's signature on the `INTENT_ADMITTED` event, which carries the `intent_hash` (ruling A189)." The Founders decide whether the example's `sig` value is shown as an unsigned marker or the member is removed in a later contract version.

## 5. Appendix A, the glossary (line 2787)

**Now:** | **Intent Object** | The structured, signed proposal produced by Understanding. |

**Proposed:** | **Intent Object** | The structured proposal produced by Understanding and admitted by the core; its hash is signed by the Record in the `INTENT_ADMITTED` event. |

## 6. Appendix D entry (new first row, after the v1.12 row)

| 1.13 | 13 Nov 2026 | **The intent signature (DEC-2026-11-13-architect-rulings-a183-a192, ruling A189).** Why: the POC cannot have Understanding sign the Intent Object (the model service never signs, INV-29, and no signing domain exists for it), so SoT §7 and the build differed (OD-P-86). What changed: §7 (the Trust checks cell and the first artifact), the pipeline diagram, the §43.1 note and the glossary now say that Trust checks the recomputed `intent_hash` against the hash in the signed `INTENT_ADMITTED` event, and that the Intent Object's own `sig` is an unsigned marker in the POC. No gate threshold changes. |
