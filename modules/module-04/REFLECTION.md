# Module 4 — Reflection

**Team name**: _______________ makuo
**Branch**: `module-04/makuo`
**Submitted**: before Module 5 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

In Module 3, services called each other directly over HTTP. Now activity-service drops a message into a broker and moves on — it never waits for a reply.

**What does the activity-service gain by not waiting? And what does the notification-service gain by consuming at its own pace?**

Think about what happens under load, or when notification-service is temporarily down.

> *Your answer:*
> activity-service doesn't have to wait for notification-service to do anything. It just drops the message in the queue and moves on, so the POST returns fast no matter what notification-service is doing.
> And if notification-service is down for a minute, the messages wait in the queue until it's back up. Nothing gets lost just because one side is slow or broken.



---

## 2. Your choice

In Module 3 you already knew how to call another service directly over HTTP — you did it for user validation and game enrichment.

**Why not use the same approach for notifications? What does introducing a broker give you that a direct HTTP call doesn't?**

Think about what happens if notification-service is slow, or crashes mid-message.

> *Your answer:*
>  If I'd called notification-service directly over HTTP like I do for users and games, then every time someone logged an activity, they'd have to wait for the notification to actually be created before getting their answer. If notification-service is slow, the user feels it

---

## 3. The tradeoff

With synchronous REST, you get an immediate answer: success or failure. With async messaging, the activity is saved and the message is sent — but you have no idea if the notification was ever delivered.

**How would a user know if their notification was never sent? How would you know as a developer?**

What visibility do you lose when you go async?

> *Your answer:*
>  Before, the POST told me right away if it worked. Now it just says the activity was saved, and I have no clue if the notification actually went out. To check, I had to dig through three places: the RabbitMQ UI, the notification-service logs, and the notifications list. You get speed and resilience, but you lose the simple yes-or-no answer.

---

*Keep this file. You will refer back to it during the oral presentation.*
