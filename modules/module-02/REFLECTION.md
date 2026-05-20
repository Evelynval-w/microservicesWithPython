# Module 2 — Reflection

**Team name**: _______________
**Branch**: `module-02/<team-name>`
**Submitted**: before Module 3 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

You built a service with distinct layers: models, schemas, repository, service, and routes — each with a single responsibility.

**Why not just put everything in one file and call it done?**

Think about what happens six months later when someone new joins the team, or when you need to swap SQLite for PostgreSQL. What does the layered structure protect you from?

> *Your answer:*

--- putting everything in opne file is file at first but then it gets messy as time goes on... for instance if a new person joins he has to go through gaint line of  code which can be so daunting

---or if we swap db's then it gets really messy.. having each file with their own function is better.

## 2. Your choice

Each service owns its data exclusively — no other service is allowed to touch its database directly.

**Pick one entity your service owns (e.g. `User`, `Game`). What would go wrong if another service could write to that table directly?**

Give a concrete scenario, not a general principle.

> *Your answer:*

--- if the game-service has access to
write into the users table directly...
then things can go wrong fast.

say there's a bug in the game-service
and it accidentally sets a user's
is_active to false after a game ends

now that user can't log in anymore


## 3. The tradeoff

You now have models, schemas, a repository, a service, and routes — five layers for what is essentially a CRUD service.

**For a system this small, what is the cost of all this structure?**

And at what point does the complexity start to pay off? Where is the tipping point?

> *Your answer:*

--- for me, i beleive that for a small crud service like this one ... these 5 layered structure is an overkill...
it starts paying off when we have real business rules, when alot of people ar collaborating

*Keep this file. You will refer back to it during the oral presentation.*
