---
name: change-quiz
description: After a working session, produce a report on what changed plus a quiz the user must pass before merging. Use when the user asks "what did we actually do," wants to review a large change, or invokes a quiz before merge.
---

# Change quiz

After a long session the agent has often done more than the user realizes, and a diff only shows surface. Behavior lives in how the change interacts with existing code paths. The user should merge only what they can pass a quiz on.

## Steps

1. Build the report first, in four short sections:
   - **Context** — what problem this session set out to solve.
   - **What changed** — grouped by intent (feature, fix, refactor), not by file.
   - **How it interacts** — the existing code paths the change touches, and what now behaves differently even in files the diff doesn't show.
   - **Intuition** — the 2-3 mental-model updates the user should walk away with ("retries are now idempotent because X").
2. For long sessions, offer the report as a single self-contained HTML page with the quiz at the bottom — it reads better than a wall of markdown.
3. Then the quiz: 5-8 questions targeting what would bite an unaware maintainer.
   - Mix recall ("what happens to in-flight jobs during deploy now?") with prediction ("if someone calls X with a stale token, what do they see?").
   - Weight questions toward deviations, edge cases, and interaction effects — not trivia about names.
4. Grade honestly, one round at a time. For each miss, explain the right answer AND flag it: a miss is either a gap in the user's model or a sign the change is too clever — say which.
5. Pass = merge-ready. Fail = point back to the specific report sections to reread, then offer a fresh variant quiz. Do not soften the bar; the whole point is that unread changes don't ship.

## Guardrails

- The quiz covers the change and its blast radius, not general knowledge.
- If the user can't pass after two rounds, the recommendation is to simplify the change or split it, not to keep quizzing.
- Never mark the user correct out of politeness. A false pass defeats the skill.
