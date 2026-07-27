---
name: context-audit
description: Audit the instructions an agent already carries — CLAUDE.md, AGENTS.md, skills, tool descriptions — for contradictions, over-constraint, and duplication, then propose a cut list. Use when an agent ignores its own instructions, when a CLAUDE.md has grown bloated, or when the user asks to audit or rightsize their agent context.
---

# Context audit

A prompt is written for one task; context is reused across every task, so it can never be as specific. That gap is where instructions rot: rules written for a worst case that no longer happens, guidance duplicated across three layers, two layers quietly telling the model opposite things. The model can resolve all of it — by spending thinking budget on it before it starts your actual work. This skill finds what to delete.

## Steps

1. Inventory every layer that reaches the model: root and nested `CLAUDE.md`/`AGENTS.md`, each skill's description and body, hooks, tool and MCP server descriptions, and any harness prompt the user controls. Report each layer's size. The layer the user forgot they wrote is usually the loudest one.
2. Read them together, the way the model receives them — not one file at a time. Contradictions only exist between layers.
3. Classify every instruction as one of five things:
   - **Conflict** — two layers pulling opposite ways ("document as appropriate" against "never add comments"). Quote both sides verbatim. These are the most expensive finding and go first.
   - **Duplicate** — the same instruction in two places. Keep the copy nearest the point of use; behavior of a tool belongs in that tool's description, not in the global preamble.
   - **Obvious** — restates what the file tree, the language, or the surrounding code already shows.
   - **Judgement-now** — a blanket rule written to prevent a worst case, wrong for some real subset of requests, and the kind of call a current model makes well on its own.
   - **Gotcha** — non-obvious, specific to this repo, load-bearing. This is what should survive; most repos are mostly the other four.
4. Propose the cut as a diff: conflicts resolved first, then duplicates, then the rest. For anything that is worth keeping but only sometimes needed, propose relocating it into a skill or a linked file loaded on demand rather than deleting it.
5. Close with before/after line counts and the single deletion you are least confident about, named explicitly so a human decides that one.

## Guardrails

- Propose, don't apply. The user approves every deletion.
- A rule that reads as over-constraint is sometimes scar tissue from a real incident. Anything naming a specific failure gets asked about, not cut.
- Judge instructions by whether they change behavior, not by whether they sound wise. A line the model already follows by default costs tokens to say nothing.
- If the harness ships its own rightsizing command, this runs alongside it, not instead of it.
- An audit that deletes a real invariant costs far more than the tokens it saved. When a line's purpose is unclear, that ambiguity is the finding — report it rather than guessing.
