# Finding-Unknowns Skills

**8 installable skills that make Claude help you find what you don't know — before it gets expensive to fix.**

The map is not the territory. Your prompt is a map; the codebase and the real world are the territory. The gap between them is your *unknowns*, and with strong models the quality of the work is bottlenecked by how well you clarify them. These skills turn that idea, from [Thariq Shihipar's](https://thariqs.github.io/html-effectiveness/unknowns/) essay *A Field Guide to Fable: Finding Your Unknowns*, into commands you can run in Claude Code, OpenAI Codex, or any agent that reads the [agentskills.io](https://agentskills.io) SKILL.md format.

> Community project. Distilled, with attribution, from a public essay by Thariq Shihipar (Anthropic, Claude Code team). **Not an official Anthropic repository.**

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

## Install

**As a Claude Code plugin (all 8 skills):**

```
/plugin marketplace add Neeeophytee/finding-unknowns-skills
/plugin install finding-unknowns@finding-unknowns-skills
```

**Manually (pick the skills you want):** copy any `skills/<name>/` folder into your project's `.claude/skills/` directory (or `~/.claude/skills/` for all projects).

**The one-file version:** if you'd rather have the whole approach as passive guidance instead of commands, drop [`CLAUDE.md`](CLAUDE.md) (Claude Code) or [`AGENTS.md`](AGENTS.md) (Codex and other AGENTS.md-reading agents) into your project root, or append it to your existing one.

### Use in OpenAI Codex

The skills use the same `SKILL.md` format Codex reads natively, so no conversion is needed. Copy them into one of Codex's skill locations:

```
git clone https://github.com/Neeeophytee/finding-unknowns-skills
cp -r finding-unknowns-skills/skills/* ~/.agents/skills/        # all projects
# or, per project:  cp -r finding-unknowns-skills/skills/* your-repo/.agents/skills/
```

Codex detects skill changes automatically. For the passive-guidance version, drop [`AGENTS.md`](AGENTS.md) into your project root — Codex reads it before doing any work. (Paths per the [Codex skills docs](https://developers.openai.com/codex/skills).)

## When to reach for which

- New to a part of the codebase, or a whole domain → `blindspot-pass`
- You'll know it when you see it (design, UX, tone) → `brainstorm-prototypes`
- You've brainstormed but ambiguity remains → `interview-me`
- You can't describe it, but some code somewhere does it right → `reference-hunt`
- Ready to build → `implementation-plan`, then keep `implementation-notes` running
- Built → `pitch-packager` for buy-in, `change-quiz` before you merge

See [EXAMPLES.md](EXAMPLES.md) for real prompts.

## Credit

The techniques and the unknowns framing come from Thariq Shihipar's essay and his [companion artifacts](https://thariqs.github.io/html-effectiveness/unknowns/). This repo distills them into the SKILL.md format with original instruction text; read the essay for the full reasoning and the Fable 5 launch-video story that motivates it. Coverage: [The Decoder](https://the-decoder.com/anthropic-developer-shares-prompting-tips-for-fable-5-that-focus-on-finding-your-own-blind-spots-first/).

## License

[MIT](LICENSE) for the skill text in this repo. The underlying techniques belong to their author; attribution above.

---

<sub>Maintained alongside [awesome-ai-workflows](https://github.com/Neeeophytee/awesome-ai-workflows), a list of AI workflows re-checked by CI, and [FlowStacks](https://flowstacks.xyz), where each recipe carries a machine-verified badge. If this repo is useful, a star helps the next person find it.</sub>
