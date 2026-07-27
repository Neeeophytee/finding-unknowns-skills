# Repo notes

This repo ships agent skills distilled from two Thariq Shihipar essays. It is a Claude Code plugin, its own single-plugin marketplace, and a plain `SKILL.md` collection installable into Codex, Kimi, and Cursor. Everything below is a gotcha about maintaining it — none of it ships to users.

## What ships, and the gate that decides

`.claude-plugin/plugin.json`'s `skills` array is the ship gate. A skill directory that exists under `skills/` but is missing from that array **does not reach plugin users**, even though `npx skills add` and manual `cp -r` installs will still pick it up. Add every new skill to the array in the same commit that creates it, and use the array (not a separate folder) to hold anything not ready to ship.

`plugin.json`'s `version` is what tells already-installed users an update exists — bump it whenever a skill changes. `marketplace.json` carries no version field.

## Files that must be edited together

- `CLAUDE.md` and `AGENTS.md` are byte-identical. Edit both, or `diff` fails.
- The skill count is hardcoded in `README.md` (4 places) and in `plugin.json`'s `description`, which also enumerates every skill by name.
- Two of those README lines are **verification claims**, not prose. Find-and-replacing the number in them turns a verified claim into an unverified one. Re-run both and edit to what you observed:

```
npx skills@latest add /path/to/this/repo --list      # read-only; accepts a local path
```

```
mkdir -p /tmp/t/.agents/skills && cd /tmp/t && git init -q .
cp -r /path/to/this/repo/skills/* .agents/skills/
codex debug prompt-input                              # every skill name + description must appear
```

The Codex check needs a git repo and a project-level `.agents/skills/`; it resolves from the nearest `.git` root, so a bare temp directory silently finds nothing.

## Shipped guidance is not this file

`guidance/finding-unknowns.md` is the passive-guidance version users drop into their own project as `CLAUDE.md` or `AGENTS.md`. It used to live at this path, which made one filename mean two opposite things. Keep them separate: general methodology goes in `guidance/`, repo-specific gotchas go here.

## Skill conventions

Skills are flat: `skills/<name>/SKILL.md`, one file each, no subdirectories. Single-file skills install identically on all five supported agents; sibling files are only verified to travel on Claude Code.

Every skill ends in a `## Guardrails` section. That is deliberate house style — keep it.

`progressive-disclosure` is user-invoked (`disable-model-invocation: true`), so its description is human-facing: a one-line summary with no "Use when…" trigger phrasing. Model-invoked skills need the trigger phrasing; check which kind you're writing before copying a description's shape.

**The flag is Claude Code-only.** Verified on Codex CLI v0.143.0: Codex ignores `disable-model-invocation` and still loads the skill and its description into the model-visible prompt. So a user-invoked skill costs nothing in Claude Code but behaves as model-invoked everywhere else — and its human-facing description is weaker trigger text on those agents. Any README claim about context savings must name Claude Code specifically. Codex's own lever is a per-skill `agents/openai.yaml` with `policy.allow_implicit_invocation: false`; adopting it would mean giving up the one-file-per-skill rule above, so it's a deliberate trade, not a default.

## Don't bucket yet

Keep `skills/` flat until roughly 20 skills. Introducing `skills/<bucket>/<name>/` breaks the three `cp -r finding-unknowns-skills/skills/* …` commands in the README — they would copy bucket directories, and `~/.agents/skills/<bucket>/SKILL.md` does not exist, so every skill silently fails to load on Codex, Kimi, and manual installs. When buckets do land: change those globs to `skills/*/*`, check whether Vercel's CLI needs its `--full-depth` flag to see nested skills, and re-verify all five install paths in the same commit. The `skills` array in `plugin.json` already carries explicit paths, so the plugin install survives nesting unchanged — that is the reason it exists.
