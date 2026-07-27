---
name: agent-interface-design
description: Design tools, scripts, and CLIs that an agent will call, so the interface teaches its own use instead of a wall of prose and examples. Use when building an MCP server or tool definition, writing an agent-facing script, or when an agent keeps misusing a tool it already has.
---

# Agent interface design

Examples teach one path and quietly fence off the others: shown three ways to call a tool, a model tends to produce those three. A well-designed interface teaches the whole space at once. The parameters say what is possible, the description says what is expected, and there is very little left to write.

## Steps

1. Find out how the tool is actually being misused before redesigning it. Read transcripts, logs, or the user's complaint. Misuse is an interface symptom first and a documentation symptom second, and the fix is usually a rename or a type, not a paragraph.
2. Push meaning into the parameters:
   - Enumerate instead of accepting free text. A status of `pending | in_progress | completed` teaches the whole state machine without a sentence of prose.
   - Name for intent rather than implementation, so the right call is the one that reads correctly.
   - Make invalid states unrepresentable wherever the type system allows it. A parameter that cannot express a mistake needs no warning about that mistake.
3. Put behavioral instruction in the tool's own description, at the point of use, and only there. The same guidance restated in a global preamble is how a codebase grows contradictions.
4. Treat the urge to add a usage example as a diagnostic: it usually means a parameter is underspecified. Fix the interface first. Keep an example only for a format that genuinely cannot be guessed, such as a bespoke query syntax.
5. Decide what is resident and what is discoverable. Tools needed on most turns belong in context; tools needed rarely should be findable on demand so they cost nothing until they're wanted.
6. Finish by naming the mistake the design still permits, and say whether it is cheap enough to live with or needs an explicit guardrail.

## Guardrails

- A description that has to explain what a parameter means is a parameter that needs a better name.
- Irreversible and high-stakes operations are the exception to all of the above: there, explicit constraint and confirmation beat elegance.
- Never redesign a signature without first finding every existing caller.
- Terseness is not the goal; expressiveness is. Cutting a description that carried real behavior is a worse outcome than a description that ran long.
