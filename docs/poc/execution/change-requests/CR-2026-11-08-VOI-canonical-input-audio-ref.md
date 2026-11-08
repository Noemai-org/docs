# Change request: CR-2026-11-08-VOI-canonical-input-audio-ref · a nullable `voice.audio_ref` in the canonical input (canonical-input.v2)

> **Status: APPROVED IN PRINCIPLE by the Architect (decision A1, 8 Nov 2026); the Security Reviewer's review and both Founders' approval are still owed.** It authorises no work until those two are recorded. The Architect answered relay issue #322: ruling A18 does **not** cover `canonical-input.v1`, and this change request is approved as the way to change it. It stays separate from noema#211. No tag (A12). Drafted 8 Nov 2026 by the Core Engineer 2 role agent, as the Engineering Lead asked in noema relay issue #321.

- **Change ID:** CR-2026-11-08-VOI-canonical-input-audio-ref
- **Requester:** Core Engineer 2 (C2), proposer; relay issues noema#296 (Voice needs C2) and noema#321 (C2 needs EL).
- **REQ IDs affected:** REQ-INP-001 (the canonical input; its voice keys), REQ-VOI-001 (voice compiles to the same canonical input), REQ-VOI-004 (raw audio handling); plan tasks VOI-02, UND-02. SoT: INV-12 (unchanged), AGENT-13, POC-NFR-07, AGENT-15 (the contract-change steps).
- **Governing text:** PERD v1.20 §19.3 (REQ-INP-001 field table: `voice`: provider_id, model_version, utterance_confidence, token_confidences[], is_final, audio_ref), §35 (REQ-VOI-004: "Runtime raw audio is held in memory for transcription only, then discarded"; stored under `raw_ref` only if the case is disputed and consent is recorded; `AUDIO_RETAINED{consent_ref}` only when retained), DEC-2026-11-06-architect-rulings A18 (nullable `voice.audio_ref` in the explanation-facts bump, "C2 defines both"; no contract named for the canonical input).

## Behaviour before

`contracts/schemas/canonical-input.v1.json` requires `voice.audio_ref` as a string of at least one character. Runtime raw audio is discarded after transcription (REQ-VOI-004), so the Voice builder (noema#193, `FinalUtterance`) has no reference to put there; the only way to satisfy the contract today is to invent one. noema#270 (the Input Gateway) therefore requires all six voice keys, as the contract does. A18's nullable `voice.audio_ref` exists only in `explanation-facts.v2` (noema#211), where it is the reference to the stored audio of the *spoken answer*; it is a different field.

## Behaviour after

A new `canonical-input.v2.json` (no tag, A12; `<name>.v<major>.json`, AGENT-15). The only change is `voice.audio_ref`: `string | null`, required (the key is always present).

- **Non-null** (a `raw_ref`, `raw_<id>`) **only when audio was retained with consent**, that is, an `AUDIO_RETAINED{consent_ref}` Record event exists for it (the check is bound as set out below).
- **Null when the audio was discarded after transcription**, which is the default. **`null` means "discarded", nothing else:** it is never "retention not asked about", and no consumer may read a null as consent or as a claim that audio was retained (Security Reviewer, note 5).
- **No retention path exists in the POC today** (the voice pipeline, noema#193, keeps audio in memory for the call only and closes it), so Voice's builder emits `null` in every case until one is built. A future retention path must decide *while the audio is still in memory*: after the call it is gone, so "disputed later" can only mean "retained at the time, on a consent flag". This request does not imply, and does not authorise, retaining audio after the fact. (Voice Engineer's fact, docs#137 comment.)
- **Until a retention path exists, the edge refuses any non-null `audio_ref`** (the Architect's decision A1, matching the Engineering Lead's ruling). A non-null reference is valid only when audio was retained with consent, that is, an `AUDIO_RETAINED{consent_ref}` event exists for it; JSON Schema cannot state that (the event lives in the Record), so core's edge checks it and a test pins it. The schema carries the shape and a tight pattern, `^raw_[0-9A-Za-z]{2,32}$`: one fixed prefix, no underscore after it and at most 32 characters, the same shape as the other ID types in `common.v1.json` (a ULID is 26). It is deliberately **not** `rec_`: `rec_<id>` is the ReconciliationId (`common.v1.json`), and a `raw_ref` must not be mistakable for it. The pattern leaves no room to carry encoded audio or a secret in a field the Record hashes (Security Reviewer, blocking finding 3).
- **The edge check is tenant- and session-bound** (Security Reviewer, blocking finding 1; INV-12). "An `AUDIO_RETAINED{consent_ref}` event exists for it" means an event **in the caller's tenant** (the login's), **for this principal's session**, and **for exactly this `audio_ref`**. A reference that exists only in another tenant, or only for another session, is refused with the **same response, byte for byte,** as a reference that exists nowhere: no existence oracle (REQ-API-002). A cross-tenant test pins both.
- **The same rule applies to `canonical-input.v1`** (Security Reviewer, blocking finding 2). v1 requires a non-empty string, which is exactly the pressure to fabricate a reference; the edge applies "a non-null `audio_ref` is refused unless that bound consent event exists" to **both versions**. Because v1 cannot express `null`, **every v1 voice input is refused at the edge** until its producer moves to v2; that is intended. A v1 voice input with an invented `raw_` value is a negative test.
- Everything else in the canonical input is unchanged. The Gateway (noema#270) accepts `null` for `audio_ref` and still requires the key and the other five voice keys; Voice's builder emits `null` unless a retained-audio record exists.

## Safety and security impact

None on the Tier 0 gates, the invariants or the threat model, with one reason each. The change *removes* a pressure to fabricate a reference (a made-up value in a contract field would be a false provenance claim), makes "no audio kept" the visible default (AGENT-13, POC-NFR-07), and adds no field that can carry raw audio. Identity still comes only from the session (INV-12). The runtime check that a non-null reference has a consent record strengthens REQ-VOI-004's acceptance criterion ("retained audio objects without a consent reference = 0") on the input path. Risk: a consumer that assumes `audio_ref` is always a string; the regenerated models make that a compile-time change in Go and a validation change in Python.

## Tests added or changed

New or changed, none weakened or deleted: fixtures for `canonical-input.v2` (voice with `audio_ref: null` positive; voice with a `raw_…` reference positive, valid only against the schema, since the consent event is the edge's business; a missing key negative; negatives for a base64 blob, a value over 32 characters after the prefix, a `rec_` prefix and any other prefix). The existing valid fixture `voice_request.json` carries `rec_raw_01J9X3`, which the tightened pattern rejects: it is replaced by a v2 fixture with a `raw_` value, and the v1 fixture stays as the v1 fixture; the contract tests that read `contracts/fixtures`; a Gateway test that `null` is accepted and a missing key refused (noema#270); core-edge tests that a non-null reference with no `AUDIO_RETAINED{consent_ref}` event is refused, that an event in **another tenant** or for **another session** gives a refusal byte-identical to "exists nowhere", and that a **v1** voice input with an invented `raw_` value is refused (the Record is read, so these are database tests, not mocks). **Failing-first order:** the refusal tests are written and red **before** the Gateway accepts `null`, so the loosening cannot land without the refusal; the Voice builder test that discarded audio yields `null`. Regeneration gives Go and Pydantic models; `codegen-diff` stays green.

## Schedule and dependency impact

Blocks Voice building the canonical voice input from `FinalUtterance` (noema#193, relay issue #296) and the Gateway's voice branch becoming final. No gate moves. The bump should land with noema#211 or after it in the same merge window, since both change a contract and both need both Founders (the contracts workflow). Consumers change together: the Gateway (noema#270), Voice's builder, and core's `INPUT_RECEIVED` handling.

## SoT or PERD text changes

PERD: yes, one cell. The §19.3 field table lists `audio_ref` among the voice keys without saying it can be absent of audio; it needs the words "null when the audio was discarded". The PERD is never edited in place, so this rides the next PERD version (the v1.21 draft is docs#130) with a decision record, in one pull request with the register regeneration (AGENT-29). SoT: no.

## Decision owner

The Architect decided (A1, 8 Nov 2026: approved). The Security Reviewer reviews it and both Founders approve it (a P0 contract, AGENT-15), as the Engineering Lead set out in noema#321. The Engineering Lead reviews. The requester does not approve its own change.

## Decision record

Not yet written. If approved: `docs/decisions/DEC-2026-11-…-canonical-input-v2.md`, with the PERD cell, the migration note and the affected requirement IDs above.

## Migration and rollback

Apply: add `canonical-input.v2.json` and its fixtures; regenerate the Go and Pydantic models (`tools/codegen`); move the Gateway, Voice's builder and core's edge to v2 in one change; keep `canonical-input.v1.json` in place as a document that still validates against its schema until every producer and consumer has moved; **the edge, however, refuses any v1 voice input that carries a non-null `audio_ref`, which is all of them** (v1 cannot express `null`), so producers must move to v2 in the same change. Rollback: point the consumers back at v1 (no data migration; the Record stores the canonical input's hash, not its schema version), remove v2, and note that v1 voice inputs are then refused until a retention path or a reversal of A1 exists. A stored v1 document stays readable.
