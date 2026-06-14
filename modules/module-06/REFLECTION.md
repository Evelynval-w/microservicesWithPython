# Module 6 — Reflection

**Team name**: _______________
**Branch**: `module-06/<team-name>`
**Submitted**: before Module 7 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

The gateway now validates every JWT before forwarding a request. Individual services no longer need to check identity themselves.

**What does centralising authentication at the gateway buy you?** What would the alternative look like — if every service validated tokens on its own?

Think about what happens when you need to rotate the secret key, or add a new service to the system.

> *Your answer:*

--- this means there's one place that says yes or no. Everything past the gateway can assume the caller is already authenticated. which makes the architecture simpler compared to the services validating tokens itself,, this compute(operational) cost of this one is cheaper and also less duplicating.

if I want to rotate the secret key, I update one config and restart the gateway. If every service did its own validation, I'd be redeploying six services.
Adding a new service is the same story: instead of just registering it in the gateway's routes, I'd be copy-pasting the JWT logic into yet another codebase and hoping I don't introduce a subtle bug.

## 2. Your choice

When activity-service calls user-service internally, it uses a Machine-to-Machine (M2M) token — not a user's token.

**Why can't it just reuse the user's token that arrived in the original request?**

What would break, or what door would you accidentally leave open, if services passed user tokens between themselves?

> *Your answer:*

--- Reusing the user's token would mean their identity gets passed around into background calls they never agreed to, and if activity-service ever got compromised, an attacker would have a real user token to replay everywhere. It also breaks the audit trail, user-service would see "this user called me" when really it was another service acting on their behalf, and you lose the ability to tell user traffic from internal traffic. 

## 3. The tradeoff

The gateway and the auth-service share the same `SECRET_KEY` to verify tokens without making a network call on every request.

**What is the security risk of sharing this key?** What happens if it leaks?

And what would the alternative look like — verifying tokens by calling auth-service on every request instead? What does that cost you?

> *Your answer:*

--- the tradeoff -- if the secret leaks, the whole system is open.
Anyone with the key can mint a token claiming to be any user with any role, and the gateway and every service will happily believe it, because the signature checks out.

*Keep this file. You will refer back to it during the oral presentation.*
