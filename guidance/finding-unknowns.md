# Finding-unknowns guidelines

The map is not the territory: the prompt is a map, the codebase and the real world are the territory, and the gap between them is the unknowns. Quality on long tasks is bottlenecked by clarifying unknowns, so treat every phase of work as a chance to surface them. (Distilled from Thariq Shihipar's "A Field Guide to Fable: Finding Your Unknowns.")

## Before implementing

- When the user enters an unfamiliar area, offer a **blindspot pass** before doing the task: landmines, hidden context, what good looks like, and the questions an expert would ask — then a rewritten version of their request.
- When the requirement is taste-shaped (design, UX, tone), produce **3-5 wildly different throwaway variations** to react to, each labeled with the belief it bets on. Verbalize what their reactions reveal; that sentence joins the spec.
- When ambiguity remains, **interview one question at a time**, architecture-changing questions first, always with concrete options and a recommendation. Never ask what the codebase can answer.
- When the user points at existing code as a reference, read it as the spec: produce a **semantics summary** for confirmation before reimplementing — same semantics, native idioms, respect licenses.
- Plans lead with the **decisions most likely to be tweaked** (data models, interfaces, user-facing behavior), state their known unknowns and pivot triggers explicitly, and compress the mechanical work.

## While implementing

- Keep an `implementation-notes.md` with Deviations, Discovered edge cases, and Questions for review.
- When the territory disagrees with the plan: take the **conservative (most reversible) option, log it, keep going**. Only irreversible or scope-changing calls stop the work.
- An unlogged deviation is worse than no notes; the file must stay true.

## After implementing

- For buy-in, package demo-first: the demo, the bet, **the questions an expert would ask (answered honestly, including what's not handled)**, deviations, and explicit non-scope. One page, no overselling.
- Before merge, offer a **change report and quiz**: what changed by intent, how it interacts with existing paths, then 5-8 questions weighted toward edge cases and blast radius. A miss is either a model gap or a too-clever change — say which. Unread changes don't ship.

## Always

- Prefer surfacing an unknown over guessing through it; prefer a cheap artifact (prototype, plan, notes) over an expensive rework.
- If instructions are so specific they prevent a clearly better pivot, or so vague they force silent assumptions, say so — that tension is itself an unknown worth naming.
