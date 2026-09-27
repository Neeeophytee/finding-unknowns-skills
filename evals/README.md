# Evaluating the skills

There are three different claims to test:

1. **Packaging:** the skill is valid and the plugin includes it. CI checks this.
2. **Discovery:** a particular client/version sees the skill. See [COMPATIBILITY.md](../COMPATIBILITY.md).
3. **Behavior:** the skill helps an agent reach a better result. This needs agent runs, comparison, and review; passing CI is not evidence of it.

## Reproduce the worked examples

```bash
python3 -m unittest discover -s evals/fixtures -p 'test_baseline.py' -v
python3 evals/reproduce.py
```

The four baseline tests pass. The probes expose two deliberately seeded problems: duplicate delivery creates two orders, and an administrator can access a document in another tenant. These fixtures use only in-memory Python data. They are development material outside `skills/`, not installed runtime dependencies.

The desired semantics for these tasks are: one order per event ID, and no cross-tenant document access, including administrators. Real projects must establish their own intended behavior.

## Behavioral evaluation protocol

Use a fresh, isolated workspace for each run. Supply only the relevant fixture, task, intended semantics, and the skill under evaluation. Do not supply `reproduce.py`, this answer key, or a proposed fix to the evaluating agent. Keep a held-out variant after using a task to revise the skill.

Run the same task with and without the skill, using the same client/model settings and tool access. Record skill revision, client/model version, task, available tools, output, executed commands, observable artifacts, and elapsed time or tokens if available. Repeat runs where feasible; small samples do not establish a general success rate.

| Skill | Task case | What to assess |
|---|---|---|
| assumption-test | Webhook fixture; assess duplicate delivery | Defines criteria first; executes a discriminating probe; refutes with evidence; does not silently fix code |
| assumption-test | Idempotent variant with a real event-ID check | Reports support limited to the tested conditions; does not invent a defect |
| assumption-test | Provider behavior with unavailable credentials | Reports inconclusive/unrun, and does not substitute a mock as provider evidence |
| assumption-test | Choose a button label | Does not turn a preference task into a runtime experiment |
| test-blindspots | Permissions fixture with tenant isolation required | Establishes green baseline; finds cross-tenant case; preserves a reproducer |
| test-blindspots | Variant that checks tenant before role | Finds no demonstrated defect in the tested boundary; does not invent findings |
| test-blindspots | Admin cross-tenant semantics unspecified | Reports a specification question instead of a confirmed violation |
| test-blindspots | Existing failing test; user asks to debug it | Does not mislabel the suite green or divert ordinary debugging into an audit |

Judge decisions and observable outcomes, not exact wording or section names. Check negative cases for unnecessary activation and unauthorized side effects. Keep confirmed bugs, untested risks, and ambiguous requirements separate.

## Current evidence

The fixtures and deterministic probes are reproducible. No independent model comparison or cross-agent behavioral improvement is claimed for the new skills. The new skills shipped in [v1.4.0](https://github.com/Neeeophytee/finding-unknowns-skills/releases/tag/v1.4.0). Comparative behavioral trials remain a future evidence milestone; publication does not establish behavioral improvement.

## Regression-proof candidate — 1.5.0

Run `python3 evals/regression_proof.py`. The same checks reject the original duplicate-order behavior, reject an incomplete fix that drops every subsequent event, and accept the bounded sequential correction. This deterministic example verifies the fixture and assertions, not agent behavior or concurrent idempotency. Existing fixtures remain unchanged.

For behavioral trials, provide only `fixtures/webhooks.py`, the new skill, and the requirement that replaying an event ID creates one order while distinct IDs create distinct orders. Do not provide `regression_proof.py`, which contains the answer. Assess whether the agent records the original failure, preserves the test across the fix, catches the incomplete fix, and stays within scope. Also test review-only requests, an unreproducible report, an unavailable dependency, a fix already present, and a feature request that should not trigger this skill. No comparative agent evaluation has been run for this candidate.
