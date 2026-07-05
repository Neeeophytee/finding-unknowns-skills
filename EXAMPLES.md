# Example prompts

Real prompts for each skill. Adapt freely — the skill does the structuring; your context does the steering. Giving Claude your starting point (what you know, what you've tried, your experience level) is the highest-leverage line in every one of these.

## blindspot-pass

> I need to add a new auth provider but I've never touched the auth modules in this codebase. Do a blindspot pass: find my unknown unknowns and help me prompt you better.

> I have to color grade this video and I don't actually know what color grading is. Teach me my unknown unknowns so I can tell good from bad before we start.

## brainstorm-prototypes

> I want a dashboard for this data but I don't know what's possible and I have no visual taste. One HTML page, four wildly different design directions, fake data. I'll react.

> Users churn right after onboarding. Search the codebase and brainstorm ten interventions from cheapest to most ambitious. I'll tell you which resonate.

> Before you wire anything up: mock the new editor toolbar in a single HTML file. I want to react to the layout before you touch the real app.

## interview-me

> The spec is attached. Interview me one question at a time about anything ambiguous, and prioritize questions where my answer would change the architecture.

> I've approved the brainstorm direction. Before you plan, interview me — but only about things you can't answer from the codebase.

## reference-hunt

> The Rust crate in vendor/rate-limiter implements exactly the backoff behavior I want. Read it and reimplement the same semantics in our TypeScript API client.

> I love how this site's pricing table is built. Read the underlying code, not the screenshot, and give me a semantics summary before you build ours.

## implementation-plan

> Write the implementation plan, but lead with what I'm most likely to tweak: data model changes, new type interfaces, anything user-facing. Bury the mechanical refactoring at the bottom — I trust you there.

## implementation-notes

> Keep an implementation-notes.md as you build. If an edge case forces you off the plan, take the conservative option, log it under Deviations, and keep going. Only stop for irreversible calls.

## pitch-packager

> Package the prototype, the spec, and the implementation notes into one doc I can drop in Slack for buy-in. Lead with the demo GIF, and include the questions a staff engineer would ask, answered honestly.

## change-quiz

> That was a long session. Give me a report on the changes — context, intuition, what interacts with what — and a quiz at the bottom that I must pass before we merge. Don't go easy.
