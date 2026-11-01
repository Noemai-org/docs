# SEC-14: the write-once store for chain-head anchors, evaluation

Date: 2026-11-01
Task: SEC-14 (owner SR; human owner: a founder). Requirement: REQ-AUD-007 (D19 of DEC-2026-10-31-proof-depth-and-completeness). Feeds: REC-07.
Status: **Recommendation for founder approval under AGENT-14. Nothing is adopted, built or run.** This is a docs-only evaluation. Facts I could not read from a primary source are marked **NOT VERIFIED**.
Non-normative: the SoT, the PERD and the decision records govern. The word is **tamper-evident**; nothing here makes the Record tamper-proof or immutable.

## 1. What the requirement asks

REQ-AUD-007: chain heads are anchored on a schedule and at every benchmark-run boundary to a **separately controlled write-once store**; the core holds a **write-only credential**; the store's **retention cannot be shortened by any account**. The chain verifier proves the live chain matches every anchor. A missed anchor raises an alert and is retried; a mismatch is a security event and stops release evidence. Tests required: a rewrite-detection test and an anchor-outage test. The store is a new datastore (AGENT-14).

Why it exists: without an external anchor an administrator could rewrite a whole chain consistently (REQ-AUD-007 rationale). So the anchor must be out of reach of the people and credentials that can rewrite the database.

## 2. Two findings that change the question

**2.1 The named leading candidate is not viable as named.** The D19 text names "an S3-compatible store with object lock in compliance mode, such as MinIO". The upstream `minio/minio` repository was **archived by its owner on 25 Apr 2026**; its README says "THIS REPOSITORY IS NO LONGER MAINTAINED", that the community edition is "distributed as source code only", and that pre-compiled binaries are no longer provided; older binaries "will not receive updates" (read on 1 Nov 2026 from <https://github.com/minio/minio>). A web search reports that Docker Hub images were removed and that a Quay mirror's `latest` points to a September 2025 build; that is a secondary source and **NOT VERIFIED**. Adopting an archived AGPL project that gets no security fixes as the component that guards our evidence is not acceptable. Compose could pull a stale image or build from archived source; neither gives us fixes.

**2.2 "Separately controlled" cannot be shown in Compose.** Whoever runs our Compose stack controls every container, volume and the host. An object-lock store in the same Compose file protects against API-level actions (a stolen core credential, a compromised core process that tries to delete or shorten) but **not against the operator**: a person with the Docker socket or the volume can delete the data under the store's API. D19's own justification is the administrator, so the in-Compose store demonstrates the mechanism and the write-only credential, and does not meet "separately controlled". Meeting it needs the store under a different owner than the database: a second founder's account, or a different host or cloud account with its own credentials. This must be said in every report; "anchored" in Compose is a test of the mechanism.

## 3. Candidates

Read on 1 Nov 2026 from each project's repository (shallow clones at the commits named) unless marked otherwise.

| | Upstream MinIO | pgsty/silo (fork of MinIO) | SeaweedFS | RustFS | A cloud object store with Object Lock |
|---|---|---|---|---|---|
| Version read | archived (README) | tag `RELEASE.2026-10-26T00-00-00Z`; HEAD `0cfca29` (1 Nov 2026) | tag 4.51 (25 Oct 2026); HEAD `a7a6482` (1 Nov 2026) | Cargo version 1.0.2; tag `1.0.4-preview.1`; HEAD `e494dc2` (1 Nov 2026) | not read: `docs.aws.amazon.com` is not reachable from this session, so every statement about a cloud service is **NOT VERIFIED** |
| Licence | AGPL-3.0 | AGPL-3.0-or-later (README; DCO, no CLA) | Apache-2.0 (LICENSE, README) | Apache-2.0 (README) | commercial service terms |
| Maintenance | none; read-only | releases every one to two months (stated); changelog current to 26 Oct 2026 | active (releases within the last week) | active (7,517 commits), but a `preview` tag is the latest I found and the README puts some features in a "Preview" tier | vendor-run |
| COMPLIANCE mode in code | `RetCompliance` exists, but unmaintained | `RetCompliance` and `ErrObjectLocked` paths present (`internal/bucket/object/lock/lock.go`, `cmd/bucket-object-lock.go`); inherited from MinIO, behaviour not run | S3 handler `setObjectRetention` refuses a mode change or an earlier retain-until date under COMPLIANCE (`weed/s3api/s3api_object_retention.go`); delete guard returns `ErrComplianceModeActive` for COMPLIANCE regardless of any bypass | README table says "Object Lock (WORM) ✅"; COMPLIANCE vs GOVERNANCE not confirmed in what I read (an e2e object-lock test directory exists) | claims compliance mode; **NOT VERIFIED** here |
| Supply chain | no binaries | README: checksums, SPDX SBOMs, Sigstore-signed manifests, build attestations (claimed; **NOT VERIFIED** by me) | releases on GitHub; signing **NOT VERIFIED** | Docker image `rustfs/rustfs`; signing **NOT VERIFIED** | n/a |
| Fit for this requirement | no | possible, after a spike | possible, after a spike | not yet | the only option that can be genuinely separate |

Not evaluated in depth: Ceph RGW (supports S3 Object Lock but is a large cluster to run for the POC); Garage (I did not find evidence it implements Object Lock; **NOT VERIFIED**). A different mechanism, not an S3 store, is also possible: submitting each chain head to an independent timestamping or transparency-log service, so a hash exists that we cannot rewrite. I did not evaluate that class and name it so the founders know the option exists.

## 4. The control we need to prove, whatever the store

These are what the spike must show, and are the acceptance tests for REQ-AUD-007's controls (the chain-matching test is REC-07's).

| ID | Check | Pass means |
|---|---|---|
| A1 | The store builds or pulls from a pinned, checksum-verified source and runs in Compose | digest or checksum pinned; no unchecked download |
| A2 | Bucket created with Object Lock enabled and a default COMPLIANCE retention; objects written with a retain-until date | the object cannot be deleted before that date |
| A3 | The core's credential is write-only: a policy allowing `PutObject` (and nothing that reads, lists, deletes, or changes retention, legal hold or the bucket) | with that credential, `DeleteObject`, `DeleteObjectVersion`, `PutObjectRetention` (shorter), `PutObjectLegalHold`, `PutBucketObjectLockConfiguration`, `PutBucketVersioning`, `GetObject` and `ListBucket` all fail; a second `PutObject` to the same key is refused or creates a new version, never an overwrite of the first |
| A4 | The store's own administrator credential (root) cannot shorten or remove a COMPLIANCE retention through the API | every attempt refused |
| A5 | The verifier has a separate read credential, which cannot write | anchors are readable by it and not by the core |
| A6 | Anchor outage: the store is down or slow | the anchor attempt fails visibly, raises the alert path, is retried, and a missed anchor is never reported as anchored |
| A7 | Clock: retain-until dates come from the store's clock or a clock the core cannot move back | an anchor cannot be written with a past retention date |

What the spike cannot show, and what the report must keep saying: a person with the host or volume can still destroy data under the API (section 2.2); the anchor proves a chain head existed by a time, not that the Record's contents are true.

## 5. Recommendation

1. **Do not adopt upstream MinIO.** Remove it as the "leading candidate".
2. **Approve a time-boxed spike (checks A1 to A7) on SeaweedFS first, and on pgsty/silo second**, run in CI as test infrastructure only, the way the pgsodium spike was run. Choose SeaweedFS first because it is Apache-2.0, actively released, and I read its COMPLIANCE enforcement in the S3 layer. Its filer and volume servers expose other interfaces; whether they let an S3 administrator bypass retention is **NOT VERIFIED** and is the first thing the spike must test (A4 through every interface the Compose service publishes). Silo is the fallback because it keeps the MinIO behaviour that the D19 text assumed, but it is AGPL, a community fork of an archived project, and its supply-chain claims are not yet checked.
3. **Decide separation now, not at the end.** For D19 to hold, someone other than the operator of the database must own the store. The founders should decide who: a second founder's own host, or a cloud object store in an account the first founder cannot administer. The Compose store then becomes the test double for the same interface, and the REC-07 code speaks plain S3 so either works.
4. **Until that is decided, state the limit** wherever anchoring is described: "anchored to a write-once store in the same trust domain" is not the same as "separately controlled".

If neither self-hosted candidate passes A1 to A7, the fallback is the external-account route in point 3 only, which needs the founders' account and the vendor's terms (outside this evaluation).

## 6. Escalation (charter section 6 format)

**Decision required (AGENT-14: a new datastore; section 6 items 3 and 6: a security boundary and a new dependency).**

**Problem.** D19's leading candidate (upstream MinIO) is archived and unmaintained as of 25 Apr 2026, and a store inside our Compose stack does not meet "separately controlled" (sections 2.1 and 2.2).

| | A. Spike SeaweedFS, then Silo; separate ownership by a second founder's host (recommended) | B. Cloud object store with Object Lock in an account the database operator cannot administer | C. Defer REC-07 and say the Record is only writer-authenticated |
|---|---|---|---|
| Effort | spike about a day per candidate, plus REC-07 | account, policy and a vendor review; needs a real account (the POC otherwise uses synthetic data only; the anchor is a hash) | none now |
| Risk | self-hosted store maintenance; AGPL for Silo; the host belongs to a founder | an external dependency and cost; vendor terms and data location to be reviewed; not verifiable by me from this session | a rewritten whole chain is undetected: REQ-AUD-007's reason for existing |
| Impact | REC-07 on S3, with a test double in Compose | same interface; no new software to run | G3 evidence for REQ-AUD-007 is missing |
| Maintenance | we update a pinned store | none for us | none |

**Recommendation.** A, with the ownership decision taken first. B is the only way to be sure no one on the team can touch the store, and the S3 interface keeps both open.

**Questions for the founders.** (1) May I run the SEC-14 spike on SeaweedFS and Silo as test infrastructure (no adoption)? (2) Who owns the store: a second founder's host, or a cloud account? (3) Is the POC's "separately controlled" satisfied for the demo by a store in Compose, with the limit stated, or must it be separate before G3?

## 7. Not covered

- Which fields an anchor carries: the chain head hash, the sequence number, the run boundary and a signature (REC-07 with GOV-28). No customer data is anchored.
- The anchor schedule and its cost.
- Cloud-provider verification: I could not read any cloud vendor's documentation from this session (`docs.aws.amazon.com` is outside the session's allowed network domains; add it to read it).
- Performance, backups, and upgrade behaviour of any candidate.

## 8. Sources read (1 Nov 2026)

- <https://github.com/minio/minio> (README: archived 25 Apr 2026, unmaintained, source only).
- <https://github.com/pgsty/silo> at `0cfca29`: `README.md`, `CHANGELOG.md`, `SECURITY.md`, `internal/bucket/object/lock/lock.go`, `cmd/bucket-object-lock.go`.
- <https://github.com/seaweedfs/seaweedfs> at `a7a6482`: `README.md`, `LICENSE`, `weed/s3api/s3api_object_retention.go`.
- <https://github.com/rustfs/rustfs> at `e494dc2`: `README.md`, `Cargo.toml`, `crates/e2e_test/src/object_lock/`.
- Requirement text: PERD v1.19 REQ-AUD-007; D19 of DEC-2026-10-31-proof-depth-and-completeness; SoT §46 OD-06.
