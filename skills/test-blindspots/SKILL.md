---
name: test-blindspots
description: Find consequential behavior that a passing test suite does not establish, using focused exploratory checks. Use when the user asks what green tests miss or wants confidence in test coverage for a specific change. Not a general code review, routine test run, or debugging workflow for an already failing test.
---

# Test blindspots

Passing tests establish their assertions under their setup. The gap to investigate is where the implementation and its tests share the same untested assumption.

## Steps

1. Establish the intended behavior and scope from the request, specification, changed code, callers, and relevant tests. Run the relevant baseline when possible. If it is already failing, report that limitation rather than describing it as green.
2. Compare important behavior with what the tests actually assert. Look for a concrete gap: a mock replacing the boundary being claimed, an untested transition, a missing consumer expectation, or an invariant only exercised on the happy path. Choose by consequence and evidence, not by a generic checklist or coverage percentage.
3. For each selected gap, state the question and design a small exploratory probe that can distinguish correct from incorrect behavior. Use existing tooling and isolated data. Prefer the actual component over a mock when the mock is the source of uncertainty.
4. Execute the bounded probes within scope. Record observed behavior and the requirement it contradicts. If intended behavior is unclear, report a specification question; if execution is unavailable, report an untested risk. Neither is a confirmed defect.
5. For a confirmed failure, preserve a minimal reproducer. Add a focused regression test when test edits are within the task's scope; verify that it fails for the intended reason. Report any deliberately failing reproducer separately from the baseline. Do not silently repair production code.
6. Finish with confirmed defects first, then consequential untested risks or specification questions, the evidence for each, and what was not examined. Finding no consequential gap is a valid result.

## Guardrails

- Do not equate low coverage with a defect, or green tests with exhaustive correctness. A hypothetical scenario alone is not a finding.
- Preserve existing tests and assertions. Do not weaken a test, expand the refactor, or install an unrelated testing framework to produce a result.
- Keep probes away from production data and external side effects unless explicitly authorized. State when a local fixture cannot represent the real boundary.
- Keep this proportional to the change. Stop when further exploration is unlikely to alter the user's decision.
