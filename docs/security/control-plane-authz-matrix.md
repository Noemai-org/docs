# Control-plane authorization matrix (SEC-04, ADV-14)

7 Nov 2026 · Security Reviewer · Status: **Proposed. A test specification, not authority.** It follows the route names of OD-P-79 (docs#133, Founder decision D14) and the identity contract of REQ-SEC-001 (rulings A1, A20, A21). **Do not merge before docs#133.** No route in it is built; the matrix is written first so that the control exists before the code that must satisfy it (SEC rows, failing first). It adds no requirement: the PERD §39.4 and SEC-04's done-when decide.

SEC-04: policy publish, kill switch and key rotation only through ops APIs with an operator identity; runtime identities cannot call them. Done when the authorization matrix test passes (ADV-14).

## 1. Credential classes (the columns)

A cell is a *credential class*, not only a session role. Session tokens are the four roles of A1; the control plane needs two classes that A1 does not define (finding 1 on docs#133).

| Class | What it is | Defined? |
|---|---|---|
| C1 `customer` | session token, one role `customer`, tenant T | A1 |
| C2 `approver` | session token, role `approver`, tenant T | A1 |
| C3 `ops-own` / C4 `ops-other` | session token, role `ops`, acting on its own tenant T / on tenant U | A1, D7 item 7 |
| C5 `audit-own` / C6 `audit-other` | session token, role `audit`, own tenant / another tenant | A1, A20 |
| C7 `administrator` | a person on the control plane (PERD §39.4 "admin"); credential and MFA are OQ-09 | **no** |
| C8 `verifier` | the verification service identity (D5) | **no** |
| C9 `benchmark-owner` | separate credentials and network (PERD §39.4) | PERD only |
| C10 `service-login` | a runtime database login (`trust_rw`, `execution_rw`, ... ) presented to HTTP | n/a: must never be accepted |
| D1 to D8 `defective` | no token; expired past the leeway; signed by another key; wrong audience; wrong issuer; zero roles; two roles (`ops` + `approver`); a token for tenant T with `ops` presented for tenant U's resource | A1 |

C7 and C8 cannot be tested with real tokens until the Architect rules how they authenticate (OD-P-79 finding 1). Their rows are written now and marked **PENDING-CREDENTIAL**; the test fails loudly for them, it does not skip.

## 2. Routes (the rows) and who may call them

`A` = allowed (2xx); `-` = refused with the **not-found shape** (`404 NOT_FOUND_OR_NOT_AUTHORIZED`, retryable false, the same body as a route that does not exist, REQ-API-002); `P` = refused with `403 PERMISSION_DENIED` (only where the caller is known to be allowed to learn the route exists); `401` = `UNAUTHENTICATED` / `SESSION_INVALID`.

| # | Route | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | D1 to D8 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `POST /v1/admin/tenants/{t}/kill-switch:set` | - | - | - | - | - | - | A | A | - | 401 |
| 2 | `POST /v1/admin/tenants/{t}/kill-switch:clear` | - | - | - | - | - | - | A | **P** | - | 401 |
| 3 | `GET /v1/admin/tenants/{t}/kill-switch` | - | - | A (t = T) | - | A (t = T) | - | A | - | - | 401 |
| 4 | `POST /v1/admin/policies/{id}/versions` | - | - | - | - | - | - | A | - | - | 401 |
| 5 | `POST /v1/admin/policies/{id}/versions/{v}:publish` | - | - | - | - | - | - | A | - | - | 401 |
| 6 | `POST /v1/admin/packs:load` | - | - | - | - | - | - | A | - | - | 401 |
| 7 | `PUT /v1/admin/tenants/{t}/callback` | - | - | - | - | - | - | A | - | - | 401 |
| 8 | `GET /v1/ops/debt`, `GET /v1/ops/alerts` | - | - | A | - | - | - | - | - | - | 401 |
| 9 | `GET /v1/investigations/{id}/panel` | - | - | A | - | A | - | - | - | - | 401 |
| 10 | `GET /v1/reconstructions/{cid}` | - | - | **PERD: -** | - | A | - | - | - | - | 401 |
| 11 | `GET /v1/record/verify?tenant_id=` | - | - | **PERD: -** | - | A (= T) | - | - | - | - | 401 |
| 12 | `GET /v1/outcomes/{verdict_id}` | own principal only | - | A | - | A | - | - | - | - | 401 |
| 13 | `POST /v1/benchmark/runs` | - | - | - | - | - | - | - | - | A, **only on the benchmark listener** | 401 |

Rows 10 and 11 follow PERD §39.4 (audit only). OD-P-79 gives them to ops as well (finding 3 on docs#133); the matrix keeps the PERD reading until the OD records the widening.

## 3. Rules every cell must satisfy

1. **Deny by default.** A route with no allowed class refuses everyone; a gate with no roles refuses everyone (`RequireRole` in noema#198 already does).
2. **Not-found shape, identical.** For every `-` cell the status, the error code, the `retryable` flag and the body shape equal those of a route that does not exist (compare against `GET /v1/admin/does-not-exist`). Only the correlation id and the timing class may differ. This is what stops a caller from mapping the control plane.
3. **The handler never runs on a refusal.** Each test counts handler invocations and Record appends and asserts 0 for every refused cell, and asserts exactly one `KILL_SWITCH_CHANGED`, `POLICY_PUBLISHED`, `PACK_LOADED` etc. for every allowed write cell, with the caller as actor.
4. **Tenant.** C3 and C5 act on their own tenant only; the same call for another tenant (C4, C6) is the not-found shape. A tenant in the path or query is a selector, never an authority: it must equal the token's tenant or be refused (INV-12, D7 item 7).
5. **Row 2.** The verification identity gets `403 PERMISSION_DENIED` on `:clear` (it may know the route), and every other refused class gets the not-found shape. After a refused `:clear` the switch is unchanged. A person's `:clear` succeeds and records the person.
6. **Row 13.** The route is not served by the runtime core in any runtime profile (dev, ci, bench, demo): the same call returns the not-found shape. It is reachable only on the benchmark listener, and only with C9.
7. **Key rotation has no route** in the POC (D3a: an operator step and `key_register`, `key_retire`, `key_revoke` at deploy). The test asserts that no route matches `rotate` or `key`, and that no runtime database role can execute the three key functions. If the Architect adds a route, it joins this table before it is built.
8. **Defective tokens (D1 to D8)** are refused on every row before routing reaches a handler, with `401` and a body that carries no reason beyond the code (A1: one rejection).
9. **A service-login credential (C10) presented over HTTP is refused** on every row: a database login is not an identity on the control plane.

## 4. How it is tested

- One table-driven test per row over the real router, with the real verifier and synthetic tokens (noema#156/#198 give `mint`, `Middleware`, `RequireRole`, `CheckTenant`). The grid above is the data; the test builds every (class, route) pair and asserts the cell, so a new route fails the test until its row is written.
- A completeness check: every route the router registers under `/v1/admin`, `/v1/ops` or `/v1/benchmark` appears in the table; a route that appears in the router and not in the table fails. This is the part that makes a forgotten route a failure.
- C7 and C8 rows fail loudly until their credential classes exist; they are not skipped.
- Mutation check when the router exists: remove each gate in turn (the role gate, the tenant check, the not-found shaping, the `:clear` restriction); each removal must turn a cell red.
- The database half of D5 (the verifier may set and never clear) is already a failing-first test on noema#190.

## 5. Open questions (named, not decided here)

1. **C7 and C8 authentication** (OD-P-79 finding 1): the Architect rules the credential classes. Recommended: a separate control-plane listener and credentials, `administrator` distinct from the verification service identity; no fifth session role.
2. **Rows 10 and 11:** keep audit only (PERD §39.4), or widen to ops (OD-P-79)?
3. **Key rotation:** confirm there is no API in the POC (rule 7).
4. **`POLICY_VERSION_NOT_NEWER`** (row 5): the new error code is an AGENT-15 change to `errors.v1.json`; the matrix asserts `409` with that code once it exists.
