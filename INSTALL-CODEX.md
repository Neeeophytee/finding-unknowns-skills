# Finding-unknowns on OpenAI Codex

These skills run on Codex natively — they're the same Agent-Skills-standard `SKILL.md` files Claude Code uses, no conversion. You have two routes: install the whole set as a **plugin**, or install individual skills.

> Verified on **Codex CLI v0.143.0**: the plugin installs at version 1.3.0 and all 11 skills load into the model-visible prompt (`codex debug prompt-input`). Receipts below.

## Route A — as a plugin (all 11 skills)

```bash
codex plugin marketplace add Neeeophytee/finding-unknowns-skills   # or /plugin marketplace add in-session
codex plugin add finding-unknowns@finding-unknowns                 # or /plugin install finding-unknowns@finding-unknowns
# restart Codex / reload plugins
```

The skills become available as `$blindspot-pass`, `$context-audit`, and so on — Codex invokes skills by `$name` mention or through the `/skills` picker. There is no `/blindspot-pass` slash command as in Claude Code.

This route reads two Codex-specific manifests in the repo:
- `.codex-plugin/plugin.json` — mirrors `.claude-plugin/plugin.json`, but declares `"skills": "./skills/"` (the whole directory) rather than an explicit array.
- `.agents/plugins/marketplace.json` — the Codex marketplace catalog, `"source": "./"`.

## Route B — skills only (no plugin machinery)

Any Agent-Skills installer works, because `skills/*/SKILL.md` is the open standard:

```bash
npx skills add Neeeophytee/finding-unknowns-skills     # detects Codex, installs into your agent dirs
```

Skills land in `~/.agents/skills/<name>/` (some Codex versions still read the legacy `~/.codex/skills/`; both are honoured).

## The Codex difference to know

Codex **ignores `disable-model-invocation`.** In Claude Code that flag makes `progressive-disclosure` user-invoked only, costing nothing in the context window until you type it. On Codex the skill and its description load into the model-visible prompt like any other — verified on v0.143.0. Treat it as a normal model-invoked skill here.

## Passive-guidance version

If you'd rather have the approach as always-on guidance than as commands, copy [`guidance/finding-unknowns.md`](guidance/finding-unknowns.md) into your project root as `AGENTS.md` — Codex reads it before doing any work.

## Honest status of the Codex route

- **Verified on v0.143.0:** plugin marketplace add + plugin add + all 11 skills in the model-visible prompt; `npx skills add` discovery of all 11.
- The `$name` invocation and `/skills` picker behaviour is per Codex's documented model; the prompt-load itself is what was measured here.

(Paths per the [Codex skills docs](https://developers.openai.com/codex/skills).)
