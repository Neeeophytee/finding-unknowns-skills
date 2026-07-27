# Finding-Unknowns Skills

**11 installable skills that make Claude help you find what you don't know — before it gets expensive to fix.**

The map is not the territory. Your prompt is a map; the codebase and the real world are the territory. The gap between them is your *unknowns*, and with strong models the quality of the work is bottlenecked by how well you clarify them. These skills turn that idea, from [Thariq Shihipar's](https://thariqs.github.io/html-effectiveness/unknowns/) essay *A Field Guide to Fable: Finding Your Unknowns*, into commands you can run in Claude Code, OpenAI Codex, Kimi Code CLI (Kimi K3), or any agent that reads the [agentskills.io](https://agentskills.io) SKILL.md format.

Three of them come from his follow-up, [*The new rules of context engineering for Claude 5 generation models*](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models), which works one layer up: not the unknowns in a single prompt, but the ones baked into the context every prompt inherits.

> Community project. Distilled, with attribution, from public essays by Thariq Shihipar (Anthropic, Claude Code team). **Not an official Anthropic repository.**

## The idea in one table

|  | **Known** | **Unknown** |
|---|---|---|
| **Known** | What's in your prompt | What you know you haven't figured out |
| **Unknown** | So obvious you'd never write it down, but you'd recognize it on sight | What you haven't considered at all |

Every skill below is a cheap way to move something out of the bottom row before implementation makes it expensive.

## The skills

| Skill | Phase | One line |
|---|---|---|
| [`blindspot-pass`](skills/blindspot-pass/SKILL.md) | Before | Surface your unknown unknowns in an unfamiliar area, then help you prompt better |
| [`brainstorm-prototypes`](skills/brainstorm-prototypes/SKILL.md) | Before | Throwaway variations you can react to, for taste you can't verbalize |
| [`interview-me`](skills/interview-me/SKILL.md) | Before | One question at a time, architecture-changing questions first |
| [`reference-hunt`](skills/reference-hunt/SKILL.md) | Before | Use working source code as the spec, even across languages |
| [`implementation-plan`](skills/implementation-plan/SKILL.md) | Before | A plan that leads with the decisions you're most likely to change |
| [`implementation-notes`](skills/implementation-notes/SKILL.md) | During | Log every deviation from the plan so the next attempt learns from this one |
| [`pitch-packager`](skills/pitch-packager/SKILL.md) | After | Bundle spec + prototype + notes into a buy-in doc for reviewers |
| [`change-quiz`](skills/change-quiz/SKILL.md) | After | A comprehension quiz you must pass before you merge |

### And three for the context itself

The eight above work on one task at a time. These three work on the instructions your agent carries into *every* task — the layer where Anthropic deleted 80% of Claude Code's system prompt with no measurable loss.

| Skill | One line |
|---|---|
| [`context-audit`](skills/context-audit/SKILL.md) | Find the contradictions, duplicates, and dead rules in your CLAUDE.md and skills, and cut them |
| [`agent-interface-design`](skills/agent-interface-design/SKILL.md) | Design tools an agent can't misuse, so you don't have to document them |
| [`progressive-disclosure`](skills/progressive-disclosure/SKILL.md) | Split an oversized skill or spec into an entry file plus files loaded only when needed |

`progressive-disclosure` ships with `disable-model-invocation: true`. **In Claude Code** that makes it user-invoked only — it stays out of the model's reach and costs nothing in your context window until you type its name. **Codex ignores the flag** (verified on v0.143: the skill and its description still load into the model-visible prompt), so treat it as a normal model-invoked skill there.

## Install

**One command, any agent (recommended):** Vercel's `skills` CLI auto-detects your coding agent (Claude Code, Cursor, Codex, Copilot, Gemini, and more) and installs the skills into the right place for each:

```
npx skills add Neeeophytee/finding-unknowns-skills
```

Add `--list` to preview the 11 skills first, or `--skill blindspot-pass` to install just one. (Discoverable on [skills.sh](https://skills.sh).)

**As a Claude Code plugin (all 11 skills):**

```
/plugin marketplace add Neeeophytee/finding-unknowns-skills
/plugin install finding-unknowns@finding-unknowns-skills
```

**Manually (pick the skills you want):** copy any `skills/<name>/` folder into your project's `.claude/skills/` directory (or `~/.claude/skills/` for all projects).

**The one-file version:** if you'd rather have the whole approach as passive guidance instead of commands, copy [`guidance/finding-unknowns.md`](guidance/finding-unknowns.md) into your project root as `CLAUDE.md` (Claude Code) or `AGENTS.md` (Codex and other AGENTS.md-reading agents), or append it to your existing one.

> Moved in v1.2.0: this file used to be the repo's own `CLAUDE.md`. Root `CLAUDE.md`/`AGENTS.md` now hold gotchas for maintaining *this* repo, which is what those files are for — general methodology in a file meant for repo-specific context is exactly the pattern `context-audit` flags.

### Use in Cursor

The `npx skills add Neeeophytee/finding-unknowns-skills` command above detects Cursor and installs the skills into `~/.cursor/skills/` for you — no manual step. (Re-verified at v1.2.0 with `skills@1.5.20`: the CLI discovers all 11 skills in this repo, and their descriptions, via `--list`.)

### Use in OpenAI Codex

The skills use the same `SKILL.md` format Codex reads natively, so no conversion is needed. Either run `npx skills add Neeeophytee/finding-unknowns-skills` (it detects Codex), or copy them into a Codex skill location:

```
git clone https://github.com/Neeeophytee/finding-unknowns-skills
cp -r finding-unknowns-skills/skills/* ~/.agents/skills/        # all projects
# or, per project:  cp -r finding-unknowns-skills/skills/* your-repo/.agents/skills/
```

Codex detects skill changes automatically. For the passive-guidance version, copy [`guidance/finding-unknowns.md`](guidance/finding-unknowns.md) into your project root as `AGENTS.md` — Codex reads it before doing any work. Re-tested with Codex CLI v0.143.0 at v1.2.0: all 11 skills and their descriptions load into the model-visible prompt (verify yourself with `codex debug prompt-input`). Note that Codex does not honour `disable-model-invocation`, so `progressive-disclosure` is model-reachable there. (Paths per the [Codex skills docs](https://developers.openai.com/codex/skills).)

### Use in Kimi Code CLI (Kimi K3)

Kimi Code CLI auto-discovers SKILL.md skills at startup and injects their names and trigger descriptions into the system prompt — the same mechanism as Claude Code and Codex. Its search paths include `~/.claude/skills/`, `~/.codex/skills/`, and `~/.agents/skills/`, so **if you already installed these skills for Claude Code, Codex, or via `npx skills add`, Kimi K3 sees them with zero extra steps.** Fresh install into Kimi's own location:

```
git clone https://github.com/Neeeophytee/finding-unknowns-skills
cp -r finding-unknowns-skills/skills/* ~/.kimi/skills/           # all projects
# or, per project:  cp -r finding-unknowns-skills/skills/* your-repo/.kimi/skills/
```

Project-level paths (`.kimi/skills/`, `.claude/skills/`, `.codex/skills/`, `.agents/skills/`) resolve from the nearest `.git` root; add custom locations with `--skills-dir` or `extra_skill_dirs`. (Paths per the [Kimi Code CLI skills docs](https://moonshotai.github.io/kimi-cli/en/customization/skills.html).)

## When to reach for which

- New to a part of the codebase, or a whole domain → `blindspot-pass`
- You'll know it when you see it (design, UX, tone) → `brainstorm-prototypes`
- You've brainstormed but ambiguity remains → `interview-me`
- You can't describe it, but some code somewhere does it right → `reference-hunt`
- Ready to build → `implementation-plan`, then keep `implementation-notes` running
- Built → `pitch-packager` for buy-in, `change-quiz` before you merge
- Your agent ignores its own instructions, or your CLAUDE.md has grown past reading → `context-audit`
- You're building a tool, MCP server, or script an agent will call → `agent-interface-design`
- One skill or spec got too long to keep loading in full → `/progressive-disclosure` (type it; it won't fire on its own)

See [EXAMPLES.md](EXAMPLES.md) for real prompts.

## Credit

The techniques come from two essays by Thariq Shihipar:

- *A Field Guide to Fable: Finding Your Unknowns* — the unknowns framing and the eight task-level skills. [Essay and companion artifacts](https://thariqs.github.io/html-effectiveness/unknowns/). Coverage: [The Decoder](https://the-decoder.com/anthropic-developer-shares-prompting-tips-for-fable-5-that-focus-on-finding-your-own-blind-spots-first/).
- *[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)* — the three context-level skills: rules give way to judgement, examples to interface design, upfront loading to progressive disclosure.

This repo distills them into the SKILL.md format with original instruction text. Read the essays for the full reasoning, including the Fable 5 launch-video story that motivates the first.

## License

[MIT](LICENSE) for the skill text in this repo. The underlying techniques belong to their author; attribution above.

---

<sub>Maintained alongside [awesome-ai-workflows](https://github.com/Neeeophytee/awesome-ai-workflows), a list of AI workflows re-checked by CI, and [FlowStacks](https://flowstacks.xyz), where each recipe carries a machine-verified badge. If this repo is useful, a star helps the next person find it.</sub>
