---
name: progressive-disclosure
description: Split an oversized skill, CLAUDE.md, or spec into an entry file plus files that load only when they're needed.
disable-model-invocation: true
---

# Progressive disclosure

A long instruction file is paid for on every single turn, including the turns that need none of it. The fix is not deletion — the material is real — but placement: keep what every run needs in the entry file, and move what only some runs need behind a pointer that fires when it's relevant. This skill restructures one artifact. To find out which artifacts need it, audit first.

## Steps

1. Read the whole artifact and identify its **branches** — the genuinely different ways a run can go through it. A verification section reached only when the user asks to verify is a branch; a rule that applies every time is not.
2. Sort every section into two piles: needed on every branch, and needed on one. The split is the entire decision, and it is usually less even than it looks — most files are a short universal core wrapped in branch-specific detail.
3. Keep the universal core in the entry file, ordered so the file still reads coherently on its own. An entry file that no longer makes sense without its children has been cut in the wrong place.
4. Move each branch into a sibling file named for what it holds, not for where it came from — `verification.md`, `glossary.md` — so the name alone tells the reader when to open it.
5. Write the pointer with care, because the pointer's wording is what decides whether the material is ever reached. Name the condition and the file together: "when the change touches migrations, read `migrations.md` before planning." A bare link at the bottom of a file is not a pointer.
6. Walk each branch end to end and confirm it still has everything it needs. Then report what moved, what stayed, and the new size of the entry file.

## Guardrails

- Splitting is not deleting. If a section is genuinely dead, say so and remove it outright rather than hiding it in a file nobody opens.
- Never split material that every branch needs. Two files that are always read together are one file with extra steps.
- A pointer that never fires has made the material invisible, which is worse than leaving it inline. When the triggering condition can't be stated crisply, that section stays put.
- Verify that the target harness actually ships sibling files alongside `SKILL.md` before relying on them; installers differ, and a pointer to a file that didn't travel is a broken skill.
- Stop when the entry file is legible. Splitting past that point trades one kind of unreadability for another.
