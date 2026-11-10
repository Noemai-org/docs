# Founder click-script: the AWS anchor store and the alert channel

Date: 2026-11-05 · Owner: Security Reviewer · Status: draft for the Founder (rewritten click by click on 8 Nov 2026 by the Repo Steward at the Founder's request; the store is AWS S3 Object Lock, Compliance mode, per ruling A60) · Derived and non-normative. The choices below (AWS only; S3 Object Lock in a separate AWS account; put-only writer; 365-day Compliance retention; Pushover with ntfy as fallback) are Founder rulings given in work orders. Under AGENTS.md section 2 a ruling binds only once it is committed, and the Steward is committing them. **Steps marked must not be run until that record is merged**; this file will then link it. The AWS choice is recorded as ruling A60 in docs#140 (once that record merges, this file links it). Steps 1 to 40 prepare and test the TEST bucket and carry no such mark; step 41 (production) waits for the same record.

**Every AWS and Pushover fact below is UNVERIFIED** (vendor sites were unreachable when this was written; names of screens and settings come from memory and may have moved). The click-through and the CI test (`anchor-aws`, noema) verify them. If a screen differs, do what its label means and tell me which step moved. **Never paste a secret into chat, a PR or a file.** Replace `BUCKET`, `ACCT` and `REGION` yourself.

## A. The anchor account and the test bucket (AWS)

**Decision (Founders, 8 Nov 2026; recorded as ruling A60 in docs#140): the anchor store is AWS S3 with Object Lock in Compliance mode, in a separate AWS account.** Everything below follows it. Click by click: each numbered line is one action; text in **bold** is the exact label to click or the value to type. If a screen is labelled differently, do what the label means and tell the Security Reviewer which step moved (all screen names are UNVERIFIED).

**A1. Create the account (about 15 minutes).**
1. Open a browser window in a private/incognito tab. Go to **aws.amazon.com**.
2. Click **Create an AWS Account** (top right).
3. **Root user email address:** an address you control and that is not the production account's (a Gmail plus-address such as `yourname+noema-anchor@gmail.com` may work; if AWS refuses the `+`, create a new address). **AWS account name:** `noema-anchor`. Click **Verify email address**, type the code from your email, click **Verify**.
4. **Root user password:** choose a long unique password in your password manager. Click **Continue**.
5. Contact information: choose **Personal** or **Business** as is true; fill the form; tick the agreement; click **Continue**.
6. Billing information: enter a card you own. Click **Verify and Continue**. Complete any card check your bank asks for.
7. Identity verification: choose **Text message (SMS)**, enter your phone, enter the code. Click **Continue**.
8. Support plan: choose **Basic support - Free**. Click **Complete sign up**. Wait for the "account is activated" email (can take a few minutes).

**A2. Protect the root user.**
9. Go to **console.aws.amazon.com**, choose **Root user**, sign in with the email and password.
10. Top right, click your account name > **Security credentials**.
11. Under **Multi-factor authentication (MFA)**, click **Assign MFA device**. Name it `root-mfa`, choose **Authenticator app**, click **Next**, scan the QR code with an authenticator app, type two consecutive codes, click **Add MFA**.
12. On the same page, check that **Access keys** is empty. **Do not create a root access key.**
13. Top right, account name > **Billing and Cost Management** > left menu **Budgets** > **Create budget** > **Use a template** > **Monthly cost budget**; amount **10** (USD); your email; click **Create budget**.

**A3. Pick the region.**
14. Top right, click the region name and choose **Europe (Ireland) eu-west-1** (recommendation). Write the code `eu-west-1` down as `REGION`. Use this same region every time below.

**A4. Create the test bucket.**
15. In the search bar type **S3** and open **S3**. Click **Create bucket**.
16. **Bucket type:** General purpose. **Bucket name:** `noema-anchor-ci-` followed by six random characters (for example `noema-anchor-ci-k4x9q2`). Write the full name down as `BUCKET`. **AWS Region:** confirm it shows `eu-west-1`.
17. **Object Ownership:** **ACLs disabled (recommended)**.
18. **Block Public Access settings:** leave **Block all public access** ticked.
19. **Bucket Versioning:** choose **Enable**.
20. **Default encryption:** **Server-side encryption with Amazon S3 managed keys (SSE-S3)**.
21. Expand **Advanced settings**. Under **Object Lock** choose **Enable**. Tick the box that says you understand Object Lock may need versioning and cannot be disabled once enabled. Click **Create bucket**.
22. Click the bucket name > **Properties** tab > scroll to **Object Lock** > **Edit**. Under **Default retention** choose **Enable**; **Default retention mode:** **Compliance**; **Retention period:** **1 Days**. Tick the acknowledgement. Click **Save changes**. (This 1-day period is for the TEST bucket only; the production period is in step 41.)
23. **Clean-up rule (test bucket only).** Bucket > **Management** tab > **Create lifecycle rule**. **Rule name:** `expire-test-objects`. Scope: **Apply to all objects in the bucket** (tick the acknowledgement). Actions: tick **Expire current versions of objects**, **Permanently delete noncurrent versions of objects**, **Delete expired object delete markers**. Days after object creation: **2**. Days after objects become noncurrent: **2**. Click **Create rule**.

**A5. Create the two limited users.**
24. Search **IAM**, open it. Left menu **Users** > **Create user**. **User name:** `anchor-ci-writer`. Leave **Provide user access to the AWS Management Console** UNticked. Click **Next** > **Next** (no groups) > **Create user**.
25. Click `anchor-ci-writer` > **Permissions** tab > **Add permissions** > **Create inline policy** > the **JSON** tab. Paste, replacing `BUCKET` with your bucket name:
   ```json
   {"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":"s3:PutObject","Resource":"arn:aws:s3:::BUCKET/ci-probe/*"}]}
   ```
   Click **Next**, **Policy name** `anchor-ci-put-only`, click **Create policy**.
26. Same user > **Security credentials** tab > **Create access key** > **Application running outside AWS** > **Next** > **Create access key**. **Keep this page open**: copy the **Access key ID** and **Secret access key** straight into your password manager. (You cannot see the secret again.) Click **Done**.
27. Back to **Users** > **Create user** > `anchor-ci-verifier`, no console access > **Create user**.
28. Click `anchor-ci-verifier` > **Add permissions** > **Create inline policy** > **JSON**. Paste, replacing `BUCKET`:
   ```json
   {"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":["s3:ListBucket","s3:ListBucketVersions","s3:GetBucketObjectLockConfiguration","s3:GetBucketVersioning"],"Resource":"arn:aws:s3:::BUCKET"},{"Effect":"Allow","Action":["s3:GetObject","s3:GetObjectVersion","s3:GetObjectRetention"],"Resource":"arn:aws:s3:::BUCKET/*"}]}
   ```
   **Policy name** `anchor-ci-read-only`, **Create policy**. (It is read-only; it exists because the put-only writer cannot list, and the test must prove the object stays listed.)
29. Same user > **Security credentials** > **Create access key** > **Application running outside AWS** > create it, copy both values into the password manager.

**A6. Add the bucket policy.**
30. Find your 12-digit **Account ID**: top right account name > the number shown (call it `ACCT`).
31. S3 > your bucket > **Permissions** tab > **Bucket policy** > **Edit**. Paste, replacing `ACCT` and `BUCKET` everywhere:
```json
{"Version":"2012-10-17","Statement":[
 {"Sid":"DenyPlainHttp","Effect":"Deny","Principal":"*","Action":"s3:*","Resource":["arn:aws:s3:::BUCKET","arn:aws:s3:::BUCKET/*"],"Condition":{"Bool":{"aws:SecureTransport":"false"}}},
 {"Sid":"WriterCannotRemoveOrShorten","Effect":"Deny","Principal":{"AWS":"arn:aws:iam::ACCT:user/anchor-ci-writer"},
  "Action":["s3:DeleteObject","s3:DeleteObjectVersion","s3:PutObjectRetention","s3:PutObjectLegalHold","s3:BypassGovernanceRetention","s3:PutBucketObjectLockConfiguration","s3:PutBucketVersioning","s3:PutBucketPolicy","s3:PutLifecycleConfiguration"],
  "Resource":["arn:aws:s3:::BUCKET","arn:aws:s3:::BUCKET/*"]},
 {"Sid":"WriterMayOnlyCreate","Effect":"Deny","Principal":{"AWS":"arn:aws:iam::ACCT:user/anchor-ci-writer"},"Action":"s3:PutObject","Resource":"arn:aws:s3:::BUCKET/*","Condition":{"Null":{"s3:if-none-match":"true"}}}]}
```
   (The `s3:if-none-match` condition key is UNVERIFIED. If AWS rejects the policy with a message about that key, tell the Security Reviewer; the test row W3 will show it.) Click **Save changes**.

## B. The CI Environment (GitHub)

**B1. Create the Environment `anchor-store`.**
32. Open the `noema` repository on github.com > **Settings** > left menu **Environments** > **New environment**. **Name:** `anchor-store`. Click **Configure environment**.
33. Tick **Required reviewers**, type your GitHub username, click **Save protection rules**.
34. Untick **Allow administrators to bypass configured protection rules** if it is ticked.
35. **Deployment branches and tags:** choose **Selected branches and tags** > **Add deployment branch or tag rule** > type `main` > **Add rule**.

**B2. Add the values (never paste them in chat, a PR or a file).**
36. In the same Environment, **Add environment secret** four times: `ANCHOR_WRITER_KEY_ID`, `ANCHOR_WRITER_SECRET` (step 26), `ANCHOR_VERIFIER_KEY_ID`, `ANCHOR_VERIFIER_SECRET` (step 29).
37. **Add environment variable** twice: `ANCHOR_BUCKET` = your `BUCKET`; `ANCHOR_REGION` = `eu-west-1`. Do not add these at repository level.

**B3. Run the proof (after the PR with the `anchor-aws` workflow is merged).**
38. `noema` > **Actions** tab > left list **anchor-aws** > **Run workflow** > branch `main` > **Run workflow**.
39. Open the run > **Review deployments** > tick `anchor-store` > **Approve and deploy**.
40. Expected: every row PASS and the last line `anchoring: PASS (0 failed rows)`. Copy the run link. Any FAIL row tells us which AWS fact was wrong.

## C. The alert channel

C1. **Pushover.** Create an account at pushover.net, install the app on your phone, note your **User Key**. Create an Application/API Token named `noema-alerts`; note the **API Token**. For the fallback, choose a long random ntfy topic name (the name is the secret) and subscribe to it in the ntfy app.
C2. **Environment `alerts`.** Same settings as steps 32 to 35 (`main` only, you as reviewer, no admin bypass). Secrets: `PUSHOVER_USER_KEY`, `PUSHOVER_APP_TOKEN`, `NTFY_TOPIC`.

## D. Production and hand-back

41. **Production bucket (only after step 40 passes and docs#140 is merged).** Repeat steps 15 to 22 and 24 to 31 with the names `noema-anchor-prod-<six random characters>`, `anchor-prod-writer` and `anchor-prod-verifier`. In step 22 set **Default retention** to **Enable**, mode **Compliance**, **Retention period: 365 Days** (ruled by the Founders). **Skip step 23** (no clean-up rule on the production bucket). Compliance retention cannot be shortened or removed during that period, by anyone, including the account root. Put the **writer** key only in the core's file-mounted secret store (one key per identity, OQ-09), never in GitHub; the verifier key goes in the `anchor-store` Environment only. **The production prefix is `anchors/` (the Security Reviewer names it for the REC-07 handover): in step 25 and in every bucket-policy resource line that names `ci-probe`, write `anchors` instead, so the production writer can write exactly under `anchors/` and nowhere else.**
42. **Tell the Security Reviewer** "done", the account ID, `REGION`, the bucket names (not keys), and the run link from step 40.

## E. Two notes for the hand-back (added by the Repo Steward, 8 Nov 2026)

- **The alert channel (section C) is a separate decision** (DEBT-02: who is alerted when a receipt signature fails) and is **not needed for REC-07**. Do steps 1 to 42 first; section C can wait.
- **What the core reads (the REC-07 handover).** After step 42 the Security Reviewer gives the Core Engineer 1 role three values and no secret: the **production bucket name**, the **region** (`eu-west-1`), and the **writer's access key id** location (the core's file-mounted secret store, one key per identity, OQ-09). The writer's secret is never sent; it is placed in the file-mounted store by the Founder.

**Do not mix the buckets.** The recording bucket for the voice study (noema#201, Founder decision F3) is a different bucket in the Founder's own AWS account, without Object Lock, with its own credential readable by the two Founders only. It is never created in the `noema-anchor` account (whose buckets are Compliance-locked), never uses the `anchor-store` Environment, and never uses either anchor key.
