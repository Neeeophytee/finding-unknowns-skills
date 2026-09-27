# Compatibility and verification

Version 1.5.0 adds `regression-proof`. The September 8 receipts below cover 1.4.0; the September 27 receipts cover 1.5.0.

The collection uses flat, single-file Agent Skills. Installation discovery, invocation, and behavioral quality are separate claims. This matrix describes observed checks, not a promise that every agent interprets every instruction identically.

## Local candidate checks — 1.5.0, 2026-09-27

- The cached `skills@1.7.0` CLI entrypoint, invoked directly with Node (`add /absolute/path/to/repo --list`), discovers all 14 names and descriptions on Node 24.19.0. No skills were installed by this preview.
- Codex CLI 0.143.0: isolated directory and plugin routes expose all 14 names and descriptions in `debug prompt-input`. Each route used a separate temporary configuration and Git repository.
- Both manifests are 1.5.0; the Claude manifest lists all 14 directories. All 13 pre-existing skill files are byte-identical to the starting checkout.
- This is local discovery evidence, not live skills.sh indexing, invocation, or behavioral improvement. Hermes, Claude Code, Cursor, and Kimi were not re-tested for this candidate; their prior receipts below cover 1.4.0 only.

## Pre-release checks — 2026-09-08

| Client / route | Version | Observed result | Limit |
|---|---|---|---|
| Codex directory skills | 0.143.0 | All 13 names and descriptions in `debug prompt-input` | Discovery, not behavioral testing |
| Codex plugin | 0.143.0 | Local marketplace installed candidate 1.4.0; all 13 names and descriptions in prompt | Isolated configuration; no real config changes |
| Hermes `external_dirs` | 0.15.1 | All 13 skills listed as `enabled` | Other surfaces and invocation not exercised |
| Claude Code plugin | Not available locally | Explicit manifest lists all 13; validated structurally | Live install/invocation not re-tested |
| Cursor | Not available locally | Standard packaging retained | CLI discovery is not a Cursor invocation test |
| Kimi | Not available locally | Existing skill format and documented paths retained | Live discovery/invocation not re-tested |

`skills@1.5.25 --list` discovered all 13 names and descriptions on 2026-09-08. The run exited successfully on Node 20.20.2 but emitted an engine warning: that CLI requires Node >=22.20.0. This is an observed discovery result on an unsupported runtime, not a supported-runtime certification. Recheck on a supported Node version before release. See [Codex details](INSTALL-CODEX.md) and [Hermes details](INSTALL-HERMES.md) for historical context and installation commands.

## Reproduce without changing personal configuration

Run `npx skills@latest add /absolute/path/to/this/repo --list` and record the resolved CLI version and names. This previews discovery; it does not install skills.

For client checks, create fresh temporary directories and a temporary Git repository. For the directory route, copy `skills/*` into that repository's `.agents/skills/`, then run `codex debug prompt-input` with its working directory set to the temporary repository. Supply an isolated `CODEX_HOME` to that child process.

For the plugin route, use a different empty `CODEX_HOME` and a Git repository **without** a `.agents/skills/` copy. Run:

```text
codex plugin marketplace add /absolute/path/to/this/repo
codex plugin add finding-unknowns@finding-unknowns
codex debug prompt-input
```

Keeping the routes separate prevents directory-installed skills from disguising a broken plugin installation. Check every name and description, not just a count.

For Hermes, supply an isolated `HERMES_HOME` containing a `config.yaml` with `skills.external_dirs` pointing to this repo's `skills` directory. Run `hermes skills list` and check that each name has `enabled` status. Do not use `hermes plugins install`.

Never include full personal prompts or configuration in published receipts. Record versions, route, names, statuses, and limitations only.

## Invocation flag

The original `progressive-disclosure` file is unchanged. Its `disable-model-invocation: true` flag is a Claude-specific control; Codex 0.143.0 still exposes its name and description. Hermes flag behavior remains unverified. Do not generalize Claude-specific context savings to other agents.
