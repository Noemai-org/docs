# Founder click-script: the AWS anchor store and the alert channel

Date: 2026-11-05 · Owner: Security Reviewer · Status: draft for the Founder · Derived and non-normative. Decisions (Founder, 5 Nov 2026): AWS only; S3 Object Lock in a separate AWS account; put-only writer; Pushover with ntfy as fallback; `RELAY_PULL_TOKEN` in its own `main`-only Environment, pull access only.

**Every AWS and Pushover fact below is UNVERIFIED** (vendor sites were unreachable when this was written; names of screens and settings come from memory and may have moved). The click-through and the CI test (`anchor-aws`, noema) verify them. If a screen differs, do what its label means and tell me which step moved. **Never paste a secret into chat, a PR or a file.** Replace `BUCKET`, `ACCT` and `REGION` yourself.

## A. The anchor account and the test bucket (AWS)

1. **New account.** Go to aws.amazon.com, create an account named `noema-anchor`, with an email you control and that is not the production account's. Gmail plus-addressing may work (`yourname+noema-anchor@gmail.com`); if AWS refuses the `+`, make a new Gmail address. Use a card you own.
2. **Protect the root.** Sign in as root, turn on MFA (an authenticator app), do not create root access keys. In Billing, create a budget alert at $10/month.
3. **Region.** Pick one region and use it everywhere: recommendation `eu-west-1`. Write it down as `REGION`.
4. **Test bucket.** S3 > Create bucket: name `noema-anchor-ci-<six random characters>` (`BUCKET`), your `REGION`, ACLs disabled, **Block all public access ON**, **Bucket Versioning: Enable**, default encryption SSE-S3, and under Advanced settings **Object Lock: Enable**. After creation: Properties > Object Lock > Edit > **default retention ON, mode Compliance, 1 day** (the CI bucket only; the production bucket gets the period you choose in step 14).
5. **Clean-up rule (test bucket only).** Management > Lifecycle rule on the whole bucket: expire current versions after 2 days, permanently delete noncurrent versions after 2 days, remove expired delete markers. (Compliance retention blocks early deletion; this removes the test objects after it ends.)
6. **Writer user.** IAM > Users > Create `anchor-ci-writer`, no console access. Add an inline policy: Allow **only** `s3:PutObject` on `arn:aws:s3:::BUCKET/ci-probe/*`. Create an access key (use case: application outside AWS). Keep the two values for step 10.
7. **Verifier user.** Create `anchor-ci-verifier`, no console access. Inline policy: Allow `s3:ListBucket`, `s3:ListBucketVersions`, `s3:GetObject`, `s3:GetObjectVersion`, `s3:GetObjectRetention`, `s3:GetBucketObjectLockConfiguration`, `s3:GetBucketVersioning` on the bucket and `BUCKET/*`. Create an access key. (It is read-only; it exists because the put-only writer cannot list, and the test must prove the object stays listed.)
8. **Bucket policy.** S3 > BUCKET > Permissions > Bucket policy, paste, replace `ACCT` (your 12-digit account ID) and `BUCKET`:
```json
{"Version":"2012-10-17","Statement":[
 {"Sid":"DenyPlainHttp","Effect":"Deny","Principal":"*","Action":"s3:*","Resource":["arn:aws:s3:::BUCKET","arn:aws:s3:::BUCKET/*"],"Condition":{"Bool":{"aws:SecureTransport":"false"}}},
 {"Sid":"WriterCannotRemoveOrShorten","Effect":"Deny","Principal":{"AWS":"arn:aws:iam::ACCT:user/anchor-ci-writer"},
  "Action":["s3:DeleteObject","s3:DeleteObjectVersion","s3:PutObjectRetention","s3:PutObjectLegalHold","s3:BypassGovernanceRetention","s3:PutBucketObjectLockConfiguration","s3:PutBucketVersioning","s3:PutBucketPolicy","s3:PutLifecycleConfiguration"],
  "Resource":["arn:aws:s3:::BUCKET","arn:aws:s3:::BUCKET/*"]},
 {"Sid":"WriterMayOnlyCreate","Effect":"Deny","Principal":{"AWS":"arn:aws:iam::ACCT:user/anchor-ci-writer"},"Action":"s3:PutObject","Resource":"arn:aws:s3:::BUCKET/*","Condition":{"Null":{"s3:if-none-match":"true"}}}]}
```
(The `s3:if-none-match` condition key is UNVERIFIED. If AWS rejects it, tell me; the test row W3 will show it.)

## B. The CI Environment (GitHub)

9. **Environment `anchor-store`.** noema > Settings > Environments > New: name `anchor-store`; Deployment branches: **Selected branches: `main` only**; Required reviewers: you; **Allow administrators to bypass: off**.
10. **Add to `anchor-store`.** Secrets: `ANCHOR_WRITER_KEY_ID`, `ANCHOR_WRITER_SECRET` (step 6), `ANCHOR_VERIFIER_KEY_ID`, `ANCHOR_VERIFIER_SECRET` (step 7). Variables: `ANCHOR_BUCKET` (`BUCKET`), `ANCHOR_REGION` (`REGION`). No repository-level copies.
11. **Run the proof.** After the PR with `anchor-aws` is merged: Actions > anchor-aws > Run workflow (branch `main`), approve the deployment. Expected: every row PASS and the last line `anchoring: PASS (0 failed rows)`. Send me the run link. Any FAIL row tells us which AWS fact was wrong.

## C. The alert channel

12. **Pushover.** Create an account at pushover.net, install the app on your phone, note your **User Key**. Create an Application/API Token named `noema-alerts`; note the **API Token**. For the fallback, choose a long random ntfy topic name (the name is the secret) and subscribe to it in the ntfy app.
13. **Environment `alerts`.** Same settings as step 9 (`main` only, you as reviewer, no admin bypass). Secrets: `PUSHOVER_USER_KEY`, `PUSHOVER_APP_TOKEN`, `NTFY_TOPIC`.

## D. Production and hand-back

14. **Production bucket (after step 11 passes).** Repeat steps 4 and 6 to 8 with names `noema-anchor-prod-<random>`, `anchor-prod-writer`, `anchor-prod-verifier`; set default retention to the period you decide (recommendation: 365 days, Compliance; **this cannot be shortened or undone for that period, so decide deliberately**; unverified cost: negligible at this size, inside the $10 bound). Skip step 5. Put the **writer** key only in the core's file-mounted secret store, never in GitHub; the verifier key goes to the verification job's secret the same way.
15. **Tell me** "done", the account ID, `REGION`, the bucket names (not keys), and the run link from step 11.

`RELAY_PULL_TOKEN`: create the Environment `relay-pull` the same way (main only, you as reviewer); the Integration Lead adds the secret.
