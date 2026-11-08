# Change request: CR-2026-11-08-VOI-canonical-input-audio-ref · a nullable `voice.audio_ref` in the canonical input (canonical-input.v2)

> **Status: PROPOSAL for review. It is not approved and authorises no work.** Drafted 8 Nov 2026 by the Core Engineer 2 role agent, as the Engineering Lead asked in noema relay issue #321. The Architect's answer to noema relay issue #322 (does ruling A18 already cover this?) decides whether this request is needed at all; if A18 is read to cover it, withdraw this file.

- **Change ID:** CR-2026-11-08-VOI-canonical-input-audio-ref
- **Requester:** Core Engineer 2 (C2), proposer; relay issues noema#296 (Voice needs C2) and noema#321 (C2 needs EL).
- **REQ IDs affected:** REQ-INP-001 (the canonical input; its voice keys), REQ-VOI-001 (voice compiles to the same canonical input), REQ-VOI-004 (raw audio handling); plan tasks VOI-02, UND-02. SoT: INV-12 (unchanged), AGENT-13, POC-NFR-07, AGENT-15 (the contract-change steps).
- **Governing text:** PERD v1.20 §19.3 (REQ-INP-001 field table: `voice`: provider_id, model_version, utterance_confidence, token_confidences[], is_final, audio_ref), §35 (REQ-VOI-004: "Runtime raw audio is held in memory for transcription only, then discarded"; stored under `raw_ref` only if the case is disputed and consent is recorded; `AUDIO_RETAINED{consent_ref}` only when retained), DEC-2026-11-06-architect-rulings A18 (nullable `voice.audio_ref` in the explanation-facts bump, "C2 defines both"; no contract named for the canonical input).

## Behaviour before

`contracts/schemas/canonical-input.v1.json` requires `voice.audio_ref` as a string of at least one character. Runtime raw audio is discarded after transcription (REQ-VOI-004), so the Voice builder (noema#193, `FinalUtterance`) has no reference to put there; the only way to satisfy the contract today is to invent one. noema#270 (the Input Gateway) therefore requires all six voice keys, as the contract does. A18's nullable `voice.audio_ref` exists only in `explanation-facts.v2` (noema#211), where it is the reference to the stored audio of the *spoken answer*; it is a different field.

## Behaviour after

A new `canonical-input.v2.json` (no tag, A12; `<name>.v<major>.json`, AGENT-15). The only change is `voice.audio_ref`: `string | null`, required (the key is always present).

- **Non-null** (`rec_…`, the `raw_ref`) **only when audio was retained with consent**, that is, an `AUDIO_RETAINED{consent_ref}` Record event exists for it.
- **Null when the audio was discarded after transcription**, which is the default.
- A non-null `audio_ref` with no retained-audio consent record is invalid. JSON Schema cannot state that (the event lives in the Record), so core's edge refuses it at runtime and a test pins it; the schema carries the shape and the pattern (`^[a-z]+_[A-Za-z0-9_]{2,64}$`, as in `explanation-facts.v2`).
- Everything else in the canonical input is unchanged. The Gateway (noema#270) accepts `null` for `audio_ref` and still requires the key and the other five voice keys; Voice's builder emits `null` unless a retained-audio record exists.

## Safety and security impact

None on the Tier 0 gates, the invariants or the threat model, with one reason each. The change *removes* a pressure to fabricate a reference (a made-up value in a contract field would be a false provenance claim), makes "no audio kept" the visible default (AGENT-13, POC-NFR-07), and adds no field that can carry raw audio. Identity still comes only from the session (INV-12). The runtime check that a non-null reference has a consent record strengthens REQ-VOI-004's acceptance criterion ("retained audio objects without a consent reference = 0") on the input path. Risk: a consumer that assumes `audio_ref` is always a string; the regenerated models make that a compile-time change in Go and a validation change in Python.

## Tests added or changed

New or changed, none weakened or deleted: fixtures for `canonical-input.v2` (voice with `audio_ref: null` positive; voice with a `rec_…` reference positive; a missing key negative; `audio_ref` of a non-reference string negative); the contract tests that read `contracts/fixtures`; a Gateway test that `null` is accepted and a missing key refused (noema#270); a core-edge test that a non-null reference with no `AUDIO_RETAINED{consent_ref}` event is refused (the Record is read, so it is a database test, not a mock); the Voice builder test that discarded audio yields `null`. Regeneration gives Go and Pydantic models; `codegen-diff` stays green.

## Schedule and dependency impact

Blocks Voice building the canonical voice input from `FinalUtterance` (noema#193, relay issue #296) and the Gateway's voice branch becoming final. No gate moves. The bump should land with noema#211 or after it in the same merge window, since both change a contract and both need both Founders (the contracts workflow). Consumers change together: the Gateway (noema#270), Voice's builder, and core's `INPUT_RECEIVED` handling.

## SoT or PERD text changes

PERD: yes, one cell. The §19.3 field table lists `audio_ref` among the voice keys without saying it can be absent of audio; it needs the words "null when the audio was discarded". The PERD is never edited in place, so this rides the next PERD version (the v1.21 draft is docs#130) with a decision record, in one pull request with the register regeneration (AGENT-29). SoT: no.

## Decision owner

The Architect decides, with the Security Reviewer and both Founders (a P0 contract, AGENT-15), as the Engineering Lead set out in noema#321. The Engineering Lead reviews. The requester does not approve its own change.

## Decision record

Not yet written. If approved: `docs/decisions/DEC-2026-11-…-canonical-input-v2.md`, with the PERD cell, the migration note and the affected requirement IDs above.

## Migration and rollback

Apply: add `canonical-input.v2.json` and its fixtures; regenerate the Go and Pydantic models (`tools/codegen`); move the Gateway, Voice's builder and core's edge to v2 in one change; keep `canonical-input.v1.json` in place until every producer and consumer has moved (a producer on v1 keeps working because v2 only widens a field). Rollback: point the consumers back at v1 (no data migration; the Record stores the canonical input's hash, not its schema version) and remove v2. A v1 document that already exists stays valid.
