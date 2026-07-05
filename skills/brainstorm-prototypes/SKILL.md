---
name: brainstorm-prototypes
description: Generate several genuinely different throwaway variations (designs, approaches, drafts) for the user to react to. Use when the user can only recognize what they want by seeing it — visual design, UX flows, naming, tone — or asks to brainstorm or prototype before building.
---

# Brainstorm and prototypes

The user has unknown knowns: criteria they can't verbalize but will recognize on sight. Finding those during prototyping is cheap; finding them mid-implementation is expensive, because small spec changes can mean drastically different code. Give them things to react to.

## Steps

1. Establish scope first: what is being decided (layout? approach? data model? tone?) and what is explicitly out of scope. One decision per round.
2. Produce 3-5 variations that are **wildly different, not shades of the same idea**. If two variations would get the same reaction, replace one.
3. Make them cheap and disposable:
   - Visual/UX → a single self-contained HTML file with fake data, no backend, no state.
   - Approaches → a one-screen sketch of each: the idea, what it optimizes for, its sharpest tradeoff.
   - Ranked lists → order from cheapest to most ambitious so the user can draw their line.
4. Label each variation with the belief it bets on ("this one assumes density beats whitespace"), so the user's reaction reveals the underlying criterion, not just a preference.
5. Collect reactions, then verbalize what was learned: "you consistently rejected X, which suggests the real requirement is Y." That sentence is the deliverable — it becomes part of the spec.

## Guardrails

- Nothing produced here is production code. Say so, and don't wire prototypes into the real app.
- Do not converge early to the variation you'd pick. The point is spanning the space.
- If the user reacts to none of them, that's signal too: the decision space was framed wrong. Reframe and rerun rather than generating more of the same.
