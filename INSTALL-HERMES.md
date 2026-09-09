# Finding-unknowns on Hermes Agent

These skills run on Nous Research's [Hermes Agent](https://hermes-agent.nousresearch.com) with no conversion — they're plain Agent-Skills-standard `SKILL.md` files, and unlike some skill packs there is **no engine, no scripts, and no hooks** to wire up. Installation is one config block.

> Re-verified on 2026-09-08 with **Hermes Agent v0.15.1** against the local 1.4.0 candidate: all 13 skills show `enabled` in `hermes skills list`, using an isolated temporary configuration. See [COMPATIBILITY.md](COMPATIBILITY.md).

## Install — point Hermes at the skills

Do **not** use `hermes plugins install` for this repo. That command is for Python plugins (it looks for `plugin.yaml` / `__init__.py`) and will warn that this repo "may not be a valid Hermes plugin" — correct, because these are *skills*, not a plugin.

**1 · Clone:**

```bash
git clone https://github.com/Neeeophytee/finding-unknowns-skills ~/finding-unknowns-skills
```

**2 · Register the skills directory** — add to `~/.hermes/config.yaml` under the `skills:` section (create the section if it isn't there):

```yaml
skills:
  external_dirs:
    - ~/finding-unknowns-skills/skills
```

That's the whole install. The skills join the agent's skill index. The current check verifies CLI listing; it does not exercise every Hermes surface or invocation. Pull the repo to update; no re-register needed.

## Alternatively — single skills, no clone

Hermes can install one skill straight from GitHub by `owner/repo/skill`:

```bash
hermes skills install Neeeophytee/finding-unknowns-skills/context-audit
hermes skills install Neeeophytee/finding-unknowns-skills/blindspot-pass
```

Use this when you only want a couple of them. The `external_dirs` route above is better for the whole set, because a `git pull` keeps every skill current in one step.

## Invocation

Hermes exposes each skill both by name for the model and as a slash command for you:

| Skill | You type | Model reaches it when… |
|---|---|---|
| `context-audit` | `/context-audit` | you ask to audit or rightsize agent instructions |
| `blindspot-pass` | `/blindspot-pass` | you enter an unfamiliar area |
| `progressive-disclosure` | `/progressive-disclosure` | you ask by name (it ships user-invoked) |

`progressive-disclosure` carries `disable-model-invocation: true`. Whether Hermes honours that flag was not verified here; on Codex the equivalent flag is ignored, so treat the skill as model-reachable on Hermes unless you confirm otherwise.

## Honest status of the Hermes route

- **Current candidate, verified on v0.15.1:** `external_dirs` registration — all 13 skills show `enabled`.
- **Historical v1.3.0 receipt:** all eleven skills showed `enabled` in the earlier check.
- **Not verified:** the single-skill `hermes skills install owner/repo/skill` path (documented from `--help`, not run end-to-end), and whether Hermes honours `disable-model-invocation`.
- engram's Hermes notes reference v0.18.2; behaviour on newer Hermes may differ from what was tested here.
