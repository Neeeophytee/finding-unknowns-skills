---
name: blindspot-pass
description: Surface the user's unknown unknowns before work starts. Use when the user is entering an unfamiliar codebase area, an unfamiliar domain (design, video, infra), or explicitly asks for a "blindspot pass" or to find their "unknown unknowns."
---

# Blindspot pass

The user is about to work in territory they don't know well. Your job is not to do the task yet. Your job is to show them what they don't know they don't know, so their next prompt is better.

## Steps

1. Ask (or infer from context) two things: what they're trying to do, and what their experience level is with this specific area. Their starting point changes everything.
2. Explore the relevant territory yourself: the module, its history, its conventions, prior art in the repo, and (if the domain is external) what practitioners consider table stakes.
3. Report back in four sections:
   - **Landmines** — the mistakes someone new here typically makes, and any repo-specific potholes (deprecated paths, misleading names, half-migrated patterns).
   - **Hidden context** — decisions already made that constrain the work (why the code is shaped this way, invariants that must hold).
   - **What good looks like** — 2-3 examples of the pattern done well, from this repo or elsewhere, so they can calibrate quality.
   - **Questions you should be asking** — the 3-5 questions an expert would ask before starting, with your best guess at each answer.
4. End with a rewritten version of their original request that incorporates what you found, so they can see the difference between their map and the territory.

## Guardrails

- Do not start implementing. This skill ends at understanding.
- Prioritize unknowns that would change the architecture or the approach over trivia.
- If the area turns out to be simpler than the user feared, say so plainly. "You have no significant blindspots here" is a valid and valuable result.
