# Contributing

Start with an issue describing a real situation where an existing skill falls short. Include the request, the relevant context, what the agent did, and what would have been more useful. Remove secrets and private project information from examples.

## Proposing a skill

A new skill should resolve a distinct kind of uncertainty. Explain its trigger, the decision it helps the user make, its observable deliverable, and why an existing skill cannot cover it with a small improvement. More skills is not a goal on its own.

Use `skills/<lowercase-hyphenated-name>/SKILL.md`, with YAML `name` and `description`, concise instructions, and a final `## Guardrails` section. Keep each skill self-contained in one file. This is our portability convention, not a limitation of the Agent Skills standard. Model-invoked descriptions should explain when to use the skill and avoid attracting unrelated requests.

Attribute the source of adapted methods and distinguish your instruction design from that source. Write original text or ensure copied material has a compatible license and attribution. Contributions to skill text are under this repository's MIT license.

## Quality bar

Include a realistic invocation and a worked example. Label illustrative outcomes as illustrative; do not present them as measured agent results. For behavioral evidence, retain the task, model/client version, environment, output, scoring criteria, and limitations. See [the evaluation protocol](evals/README.md).

Skills must preserve the user's scope, available tools, and authorization. Do not add mandatory infrastructure, production side effects, or automatic dependencies on other skills. Missing evidence should remain missing evidence.

## Local checks

Use Python 3.10 or newer in a virtual environment:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
```

These checks validate packaging and fixtures, not model quality or every client. Re-run relevant installation checks from [COMPATIBILITY.md](COMPATIBILITY.md) in temporary directories. Never overwrite a maintainer's agent configuration to test installation.

## Pull requests

- Explain the problem, before/after behavior, evidence, and limitations.
- Add every new skill to `.claude-plugin/plugin.json` in the same change; keep the Codex directory declaration intact.
- Update both plugin versions together when preparing a release. Keep marketplace identities stable.
- Update README counts, skill links, examples, and attribution. Re-run checks before changing a verification claim; preserve older receipts as historical.
- Keep `AGENTS.md` and `CLAUDE.md` identical when changing maintainer guidance.
- The legacy snapshot test preserves the eleven 1.3.0 skills for this additive release. Future intentional changes require explicit review of both the skill diff and its snapshot update.

CI should pass before merge. Maintainers review usefulness and behavioral scope separately from formatting. Do not add AI-attribution trailers to commits, pull requests, or releases.
