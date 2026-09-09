# Examples

Invocation prompts for each skill. Adapt freely — the skill does the structuring; your context does the steering. Giving Claude your starting point (what you know, what you've tried, your experience level) is the highest-leverage line in every one of these.

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

## context-audit

> My CLAUDE.md is 400 lines and Claude still ignores half of it. Audit everything that reaches the model — CLAUDE.md, the skills, the hooks — and give me a cut list with the contradictions first.

> Before we add another rule: read our agent instructions the way the model receives them and tell me which lines actually change behavior and which are just expensive.

## agent-interface-design

> I'm writing an MCP server for our deploy tooling. Design the tool signatures so the agent can't call them wrong, instead of me writing three paragraphs of usage notes per tool.

> Claude keeps passing the wrong thing to this script. Don't add documentation — look at the interface and tell me what's badly named or too loosely typed.

## progressive-disclosure

> /progressive-disclosure — our code-review skill is 300 lines and most runs need about 40 of them. Split it so the rest loads only when it's relevant.

## assumption-test

> Before committing to this integration, test the assumption that replaying a webhook cannot create a duplicate order. Use only the local fixture.

## test-blindspots

> The permissions tests pass. Tenant isolation is required even for administrators. Find important behavior these tests do not establish, using the local fixture.

## Worked examples with reproducible observations

These are deterministic teaching examples, not agent benchmark results or production incidents. The fixtures deliberately contain flaws. Run `python3 -m unittest discover -s evals/fixtures -p 'test_baseline.py' -v`, then `python3 evals/reproduce.py` from the repository root. See [the evaluation protocol](evals/README.md).

### An assumption changes the implementation plan

- **Problem:** The webhook handler accepts an event, but the plan assumes repeated delivery creates only one order.
- **Invocation:** Use `assumption-test` with the prompt above and [the handler fixture](evals/fixtures/webhooks.py).
- **Prediction before the probe:** Two deliveries of the same event ID should leave one order.
- **Observed output:** `Same event delivered twice: 2 orders (desired: 1)`.
- **Verdict and decision:** Refuted for this local handler. The plan needs an idempotency mechanism before treating retries as safe. This sequential probe does not establish behavior under concurrent delivery or provider retries.

### Passing tests leave a boundary untested

- **Problem:** Four baseline tests pass, including same-tenant admin access. Cross-tenant isolation is a stated requirement.
- **Invocation:** Use `test-blindspots` with the prompt above and [the permissions fixture](evals/fixtures/permissions.py).
- **Probe:** An administrator in tenant A requests a document belonging to tenant B.
- **Observed output:** `Tenant A admin can read tenant B document: True (desired: False)`.
- **Finding and decision:** The baseline misses tenant isolation. Preserve this input as a regression case; correct the permission boundary before claiming the tests establish isolation. No production code is changed by the example.

## Illustrative outputs for the original skills

These abbreviated examples show the kind of decision each skill helps make. They are illustrations, not measured runs.

| Skill | Problem / invocation | Example output and resulting decision |
|---|---|---|
| blindspot-pass | New to auth; use the auth prompt above | Identifies account linking as a hidden constraint; the next request specifies how existing accounts should link |
| brainstorm-prototypes | Unsure about dashboard layout; request four variants | Reactions favor dense comparisons; the spec prioritizes comparison over individual detail cards |
| interview-me | Spec leaves deletion ambiguous; request an interview | A question establishes recoverable deletion; the data model must preserve a recovery window |
| reference-hunt | Need the reference rate limiter's semantics | Extracts retry timing and cancellation rules; those rules become acceptance criteria |
| implementation-plan | Ready to build; request a reviewable plan | Puts identifier choice and its migration cost first; reviewer resolves it before wiring begins |
| implementation-notes | An integration differs from the plan | Records the fallback, why it was chosen, and how to reverse it; review includes the deviation |
| pitch-packager | Need approval for a finished prototype | Leads with the demo and states an unsupported case; reviewer can assess the actual scope |
| change-quiz | Maintainer has not understood a large change | A prediction question reveals confusion about retries; review returns to that behavior before merge |
| context-audit | Conflicting project instructions | Quotes both rules and proposes a focused diff; reviewer resolves the contradiction |
| agent-interface-design | Agent misuses a tool's status parameter | Proposes an enum based on observed misuse and caller inventory; maintainer reviews compatibility |
| progressive-disclosure | A large spec carries rarely used sections | Proposes a small entry file and linked detail; reviewer checks that critical constraints remain reachable |
