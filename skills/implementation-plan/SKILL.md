---
name: implementation-plan
description: Write an implementation plan that leads with the decisions the user is most likely to change, and buries the mechanical work at the bottom. Use when planning is requested before a build, especially after brainstorming or an interview.
---

# Implementation plan

A plan's job is not to prove you thought of everything. It's to put the reversible-but-expensive decisions in front of the user while changing them is still free. Order the plan by likelihood-of-tweaking, not by build order.

## Steps

1. Open with a three-line summary: what is being built, the approach chosen, and the single riskiest assumption.
2. **Section 1 — Decisions you'll probably want to tweak.** Data model changes, new type interfaces, API shapes, anything user-facing. For each: the choice made, one alternative considered, and what changing it later would cost.
3. **Section 2 — Known unknowns and how the plan absorbs them.** Where ambiguity remains, state the default that will be taken and the signal that would trigger a pivot. A plan that admits its unknowns survives contact with the territory; one that doesn't just breaks quietly.
4. **Section 3 — The mechanical work.** Refactors, wiring, migrations, tests. Compress this; the user trusts you here and reviewing it is a waste of their attention.
5. End with the review request: the 2-4 specific items you want a yes/no or a pick on before starting.
6. If the plan is more than a screenful or the user prefers visual artifacts, offer it as a single self-contained HTML page — sections collapsible, tweakable decisions pinned to the top.

## Guardrails

- If a genuinely better approach appears mid-planning, present the pivot as its own decision — don't silently re-plan.
- Keep it reviewable in minutes. A plan too long to read gets skimmed, and skimmed plans hide bad decisions.
- The plan should leave room for improvisation during implementation; over-specified plans fail exactly where the territory disagrees with the map.
