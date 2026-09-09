# Finding-Unknowns Skills

[![GitHub stars](https://img.shields.io/github/stars/Neeeophytee/finding-unknowns-skills?style=flat)](https://github.com/Neeeophytee/finding-unknowns-skills/stargazers)
[![skills.sh installs](https://skills.sh/b/neeeophytee/finding-unknowns-skills)](https://skills.sh/neeeophytee/finding-unknowns-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Validate skills](https://github.com/Neeeophytee/finding-unknowns-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/Neeeophytee/finding-unknowns-skills/actions/workflows/validate.yml)

**13 installable skills that help your coding agent find what you don't know — before it gets expensive to fix.**

The map is not the territory. Your prompt is a map; the codebase and the real world are the territory. The gap between them is your *unknowns*, and with strong models the quality of the work is bottlenecked by how well you clarify them. The original eight task-level skills turn that idea, from [Thariq Shihipar's](https://thariqs.github.io/html-effectiveness/unknowns/) essay *A Field Guide to Fable: Finding Your Unknowns*, into commands you can run in Claude Code, OpenAI Codex, Kimi Code CLI (Kimi K3), or any agent that reads the [agentskills.io](https://agentskills.io) SKILL.md format.

Another three come from his follow-up, [*The new rules of context engineering for Claude 5 generation models*](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models), which works one layer up: not the unknowns in a single prompt, but the ones baked into the context every prompt inherits.

> Community project. Eleven skills distilled, with attribution, from public essays by Thariq Shihipar (Anthropic, Claude Code team), plus two maintainer-designed extensions. **Not an official Anthropic repository.**

The contribution here is the reusable instruction design: focused triggers, concrete deliverables, scope boundaries, portable packaging, and documented checks. The new extensions take the workflow from identifying unknowns to testing them. [Examples](EXAMPLES.md) · [Compatibility](COMPATIBILITY.md) · [Contributing](CONTRIBUTING.md) · [Roadmap](ROADMAP.md)

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

### Two extensions for evidence

These are maintainer-designed additions, informed by established testing practices. The original eleven skill files are unchanged in the 1.4.0 candidate.

| Skill | Phase | One line |
|---|---|---|
| [`assumption-test`](skills/assumption-test/SKILL.md) | Before | Turn a consequential technical assumption into a bounded, falsifiable experiment |
| [`test-blindspots`](skills/test-blindspots/SKILL.md) | During / after | Investigate what passing tests do not establish, with focused probes and reproducible evidence |

The additions have packaging and discovery checks. [Evaluation protocol and fixtures](evals/README.md).

## Install

**One command, any agent (recommended):** Vercel's `skills` CLI auto-detects your coding agent (Claude Code, Cursor, Codex, Copilot, Gemini, and more) and installs the skills into the right place for each:

```
npx skills add Neeeophytee/finding-unknowns-skills
```

Add `--list` to preview the 13 skills first, or `--skill blindspot-pass` to install just one. (Discoverable on [skills.sh](https://skills.sh).)

**As a Claude Code plugin (all 13 skills):**

```
/plugin marketplace add Neeeophytee/finding-unknowns-skills
/plugin install finding-unknowns@finding-unknowns-skills
```

**Manually (pick the skills you want):** copy any `skills/<name>/` folder into your project's `.claude/skills/` directory (or `~/.claude/skills/` for all projects).

**The one-file version:** if you'd rather have the whole approach as passive guidance instead of commands, copy [`guidance/finding-unknowns.md`](guidance/finding-unknowns.md) into your project root as `CLAUDE.md` (Claude Code) or `AGENTS.md` (Codex and other AGENTS.md-reading agents), or append it to your existing one.

> Moved in v1.2.0: this file used to be the repo's own `CLAUDE.md`. Root `CLAUDE.md`/`AGENTS.md` now hold gotchas for maintaining *this* repo, which is what those files are for — general methodology in a file meant for repo-specific context is exactly the pattern `context-audit` flags.

### Use in Cursor

The `npx skills add Neeeophytee/finding-unknowns-skills` command above detects Cursor and installs the skills into `~/.cursor/skills/` for you — no manual step. (Historical receipt: at v1.2.0, `skills@1.5.20 --list` discovered eleven skills and descriptions. Current discovery results are recorded in [COMPATIBILITY.md](COMPATIBILITY.md); CLI discovery alone does not verify Cursor invocation.)

### Use in OpenAI Codex

The skills use the same `SKILL.md` format Codex reads natively, so no conversion is needed. Either run `npx skills add Neeeophytee/finding-unknowns-skills` (it detects Codex), or copy them into a Codex skill location:

```
git clone https://github.com/Neeeophytee/finding-unknowns-skills
cp -r finding-unknowns-skills/skills/* ~/.agents/skills/        # all projects
# or, per project:  cp -r finding-unknowns-skills/skills/* your-repo/.agents/skills/
```

Prefer a managed bundle? Codex also installs the whole set as a **plugin**:

```
codex plugin marketplace add Neeeophytee/finding-unknowns-skills
codex plugin add finding-unknowns@finding-unknowns
```

Codex detects skill changes automatically. For the passive-guidance version, copy [`guidance/finding-unknowns.md`](guidance/finding-unknowns.md) into your project root as `AGENTS.md` — Codex reads it before doing any work. Re-tested on 2026-09-08 with Codex CLI v0.143.0 against the local v1.4.0 candidate: both routes load all 13 skills into the model-visible prompt (verify with `codex debug prompt-input`). Codex does not honour `disable-model-invocation`, so `progressive-disclosure` is model-reachable there. Full details and receipts: [INSTALL-CODEX.md](INSTALL-CODEX.md). (Paths per the [Codex skills docs](https://developers.openai.com/codex/skills).)

### Use in Hermes Agent

These are *skills*, not a Python plugin, so install them via Hermes's skills system, **not** `hermes plugins install`. Clone the repo and point Hermes at it in `~/.hermes/config.yaml`:

```yaml
skills:
  external_dirs:
    - ~/finding-unknowns-skills/skills
```

Re-tested on 2026-09-08 with Hermes Agent v0.15.1 against the local v1.4.0 candidate: all 13 skills show `enabled` in `hermes skills list`. Other Hermes surfaces were not exercised in this check. Single-skill installs and full receipts: [INSTALL-HERMES.md](INSTALL-HERMES.md).

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
- An approach depends on behavior you have not established → `assumption-test`
- Passing tests may miss an important boundary → `test-blindspots`
- Ready to build → `implementation-plan`, then keep `implementation-notes` running
- Built → `pitch-packager` for buy-in, `change-quiz` before you merge
- Your agent ignores its own instructions, or your CLAUDE.md has grown past reading → `context-audit`
- You're building a tool, MCP server, or script an agent will call → `agent-interface-design`
- One skill or spec got too long to keep loading in full → `/progressive-disclosure` (type it; it won't fire on its own)

## Invoking a skill on each agent

Same skills, different invocation syntax per agent. The model reaches them on its own from the descriptions; this is how *you* trigger one by hand:

| Agent | How you invoke a skill | Install |
|---|---|---|
| Claude Code | `/context-audit` (slash command) | plugin or `npx skills add` |
| OpenAI Codex | `$context-audit`, or the `/skills` picker | [plugin or skills](INSTALL-CODEX.md) |
| Hermes Agent | `/context-audit` (slash command) | [`skills.external_dirs`](INSTALL-HERMES.md) |
| Cursor / Kimi K3 | agent's own skills UI / `SKILL.md` autodiscovery | `npx skills add` |

`progressive-disclosure` is user-invoked in Claude Code only — elsewhere it behaves as a normal model-invoked skill (see the per-agent notes above).

See [EXAMPLES.md](EXAMPLES.md) for real prompts.

## Credit

The original eleven skills draw on two essays by Thariq Shihipar:

- *A Field Guide to Fable: Finding Your Unknowns* — the unknowns framing and the eight task-level skills. [Essay and companion artifacts](https://thariqs.github.io/html-effectiveness/unknowns/). Coverage: [The Decoder](https://the-decoder.com/anthropic-developer-shares-prompting-tips-for-fable-5-that-focus-on-finding-your-own-blind-spots-first/).
- *[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)* — the three context-level skills: rules give way to judgement, examples to interface design, upfront loading to progressive disclosure.

This repo distills them into the SKILL.md format with original instruction text. Read the essays for the full reasoning, including the Fable 5 launch-video story that motivates the first.

The two maintainer-designed extensions are not attributed to those essays. `assumption-test` applies falsifiable experiments to uncertain technical decisions; [consumer-driven contract testing](https://docs.pact.io/) is one relevant precedent. `test-blindspots` applies [exploratory testing](https://martinfowler.com/bliki/ExploratoryTesting.html) to the gap between passing assertions and intended behavior. The instruction flows are new to this collection; the underlying testing methods are established practice.

## Community

Read [CONTRIBUTING.md](CONTRIBUTING.md) to propose a skill or report a problem. Community participation follows our [Code of Conduct](CODE_OF_CONDUCT.md). [CHANGELOG.md](CHANGELOG.md) records releases and the current candidate.

## License

[MIT](LICENSE) for the skill text in this repo. Sources and method attribution are documented above. The Code of Conduct retains its own Contributor Covenant attribution.

---

<sub>Maintained alongside [awesome-ai-workflows](https://github.com/Neeeophytee/awesome-ai-workflows), a list of AI workflows re-checked by CI, and [FlowStacks](https://flowstacks.xyz), where each recipe carries a machine-verified badge. If this repo is useful, a star helps the next person find it.</sub>
