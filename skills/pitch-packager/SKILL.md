---
name: pitch-packager
description: Package a finished piece of work (spec, prototype, implementation notes) into a single document that gets reviewers to understanding and approval fast. Use when the user needs buy-in, a review, or a shareable summary of what was built and why.
---

# Pitch packager

Reviewers start with the same unknowns the builder started with, plus one more: whether the builder accounted for the failure points an expert would probe. A good pitch doc kills both in one read.

## Steps

1. Collect the artifacts: the spec or plan, the prototype or demo, the implementation notes, and the diff. Ask for a demo recording or screenshots if any user-facing behavior changed — lead with that.
2. Structure the document in reading order for a skeptic:
   - **The demo** — what it looks like working, first. A GIF or screenshot beats prose.
   - **The problem and the bet** — two paragraphs max: what this solves and the approach chosen over the alternatives.
   - **What an expert would ask** — the 3-5 hard questions a reviewer in this domain would raise (edge cases, scale, failure modes, migration), each answered honestly, including "not handled, here's why that's acceptable for now."
   - **Deviations from plan** — lifted straight from implementation-notes, because surprises found in review cost trust.
   - **What's NOT in this change** — scope fences, so the review doesn't sprawl.
3. Keep it one page. Link out to the spec, notes, and diff rather than inlining them.
4. Match the medium to the venue: a Slack-pasteable doc, a PR description, or a standalone HTML page — ask which if unclear.

## Guardrails

- Never oversell: a pitch that hides a known weakness converts one approval into a permanent credibility loss.
- The "what an expert would ask" section is the heart. If it's easy to write, the questions aren't hard enough.
- If the work isn't actually ready, the honest pitch is a status update, and saying so is part of this skill.
