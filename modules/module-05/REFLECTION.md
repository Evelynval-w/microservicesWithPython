# Module 5 — Reflection

**Team name**: _______________
**Branch**: `module-05/<team-name>`
**Submitted**: before Module 6 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

The game-service now has two models for the same data: SQLite for writes, Redis for reads. They store the same games in two different shapes.

**Why go through the trouble of maintaining two representations of the same data?**

Think about what kind of queries each model is optimised for, and what would happen if you tried to use the write model for high-traffic read operations.

> *Your answer:*
 If I tried to serve every /summary request from SQLite, the writes would start fighting the reads for connections, query plans would get heavier, and the read latency would creep up under load. Redis is good because we can use redis cache to store datas that are read often.. this also helps with latency 

## 2. Your choice

The logging-service checks GDPR consent before recording any activity. If a user has not opted in, the log is silently dropped.

**What does this consent check force you to accept about your data?** It is incomplete by design — some activities will never be recorded.

From a system design perspective: where is the right place to enforce this rule — in the logging-service, in the activity-service, or at the gateway? Why?

> *Your answer:*
The consent check forces me to accept that the log is not a complete history of what happened — it's a complete history of what users let me record, according to the gdpr compliance of the zone.  If someone never opts in, their actions still occurred, but my logs will never know it. I can't reason about "all activity"; I can only reason about "all consented activity.

## 3. The tradeoff

With CQRS, your write model and read model can drift out of sync — a game is updated in SQLite but the Redis projection still shows the old data.

**In what scenario does this inconsistency matter to the user? In what scenario is it completely acceptable?**

Is there a class of applications where eventual consistency is never acceptable? What are they?

> *Your answer:*

--- it matters to the users if thy can't see their writes,, like if their updated their profile picture or info,, It's completely fine when the user has no reference point for what "fresh" should look like — browsing the catalogue, looking at someone else's profile... generally it depends on the app and the architecture.. if we are handling money like banking systems, trading or inventory, medical records stale reads could lead to many problems.

*Keep this file. You will refer back to it during the oral presentation.*
