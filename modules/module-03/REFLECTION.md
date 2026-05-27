# Module 3 — Reflection

**Team name**: makuo
**Branch**: `module-03
**Submitted**: before Module 4 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

All client requests now go through the gateway. No client ever calls a service directly.

**Why does that single entry point exist? What would the client's life look like without it?**

Think about what the client would need to know and manage if it talked to each service on its own port.

> *Your answer:* the gateway give the client one address to talk to, the whole point is that even if we change port it wont break cos the frontend doesnt talk directly to the backend...but without it the frontend has to remember every port. so yeah the services are in the middle.. they are the ones we can change and move around how ever we want 

---

## 2. Your choice

The activity-service makes two outbound calls: one to validate the user (with retry logic), one to fetch game data (with a null fallback if it fails).

**Why are these two calls treated differently? Why does one retry and the other just give up gracefully?**

What is the consequence for the user in each case if the downstream service is unavailable?

> *Your answer:* cos one is for validating the user and its very essential so i retry once in case its due to network...whereever for fetching the game from the game service if it fails no issue.

---

## 3. The tradeoff

Every time a client creates an activity, three services are involved synchronously. They all have to be running, healthy, and fast.

**What is the systemic risk of chaining synchronous calls like this?**

What happens to the user experience if the slowest service in the chain takes 3 seconds to respond?

> *Your answer:* When you chain three services synchronously, the response is only as fast as the slowest one. If one of them takes 3 seconds to reply, the whole request takes 3 seconds, even if the other two are instant. sync can look simple but they are fragile

---

*Keep this file. You will refer back to it during the oral presentation.*
