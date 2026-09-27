---
name: regression-proof
description: Fix a reported bug with a regression test that demonstrably fails on the original behavior and passes after the fix. Use when implementing a bug fix or checking whether a proposed fix actually addresses a reported failure. Not a general coverage audit or new-feature workflow.
---

# Regression proof

A passing test is evidence for a fix only if it can distinguish the broken behavior from the intended behavior.

## Steps

1. Establish the reported failure, expected behavior, and authorized scope from the request, relevant code, and existing tests. Record the starting state, including uncommitted changes. Run the relevant baseline and reproduce the bug before editing when possible; distinguish a product failure from a broken test environment.
2. Add the smallest regression test that exercises the real failing path and asserts the required outcome. Run it against the original behavior and verify that it fails for the reported reason, not an import error, missing dependency, or unrelated failure. Reuse an existing test if it already demonstrates this.
3. Trace the cause and make a scoped fix when implementation is authorized. For review-only requests, assess the proposed fix without silently changing production code. Preserve the evidence from the original failure.
4. Run the same regression test against the fixed behavior. If the fix existed before the test, compare with the original implementation in an isolated copy or worktree that preserves the relevant starting state. Do not reset the user's working tree. If an equivalent comparison cannot be made, report that limitation rather than claiming a verified before/after result.
5. Check the neighboring behavior most likely to be affected. Where an incomplete fix could pass the reproducer, add a discriminating case. Use reference comparisons, bounded randomized checks, or performance measurements only when the failure mechanism warrants them; record seeds and conditions needed to reproduce results.
6. Finish with the cause, fix or review finding, commands and observed before/after outcomes, adjacent checks, and remaining uncertainty. If the bug cannot be reproduced or expected behavior is unresolved, say what evidence is missing and avoid a speculative fix. Stop once the scoped claim is supported and relevant checks pass.

## Guardrails

- Never weaken assertions, change expected behavior merely to make a test pass, or mock away the boundary responsible for the bug.
- Preserve existing tests and unrelated user changes. Keep comparison artifacts isolated; do not use destructive checkout or reset operations to recreate the original failure.
- A missing dependency or unavailable original version is a verification limitation, not proof of correctness. Keep pre-existing failures separate from regressions caused by the fix.
- Keep execution within the task's authorization. A local reproducer does not authorize production writes, external side effects, or an unrelated refactor.
- A regression test establishes the tested behavior, not the absence of all bugs. This skill does not change the host's reasoning-effort setting.
