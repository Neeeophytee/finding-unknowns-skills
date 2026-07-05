---
name: implementation-notes
description: Keep a running implementation-notes.md during a build, logging every deviation from the plan and every discovered edge case. Use whenever implementing against an agreed plan or spec, especially in long autonomous sessions.
---

# Implementation notes

No amount of planning removes every unknown; some only appear once the code is open. When the territory disagrees with the plan, don't stop and don't silently improvise — take the conservative option, write it down, and keep going. The notes file is how the next attempt learns from this one.

## Steps

1. At the start of the build, create `implementation-notes.md` with three headings: **Deviations**, **Discovered edge cases**, **Questions for review**.
2. Whenever reality forces a choice the plan didn't cover:
   - pick the conservative option (the one that's easiest to reverse),
   - log it under Deviations: what the plan said, what was done instead, why, and what it would take to revisit,
   - continue working. Do not block on the user for reversible decisions.
3. Log edge cases as they're found, even ones handled cleanly — they are exactly the unknowns the next plan should account for.
4. Anything irreversible or scope-changing goes under Questions for review AND stops the work at a safe checkpoint. Deviating conservatively is fine; deviating expensively needs a human.
5. At the end, append a five-line summary: deviations count, the one most likely to be revisited, edge cases found, and what the next session should read first. Reference the file in the handoff or PR.

## Guardrails

- The notes file is temporary working memory, not documentation. Keep entries to 2-3 lines each.
- Never let the notes drift from reality — an unlogged deviation is worse than no notes at all, because the file claims completeness.
- "Conservative" means reversible, not necessarily simple.
