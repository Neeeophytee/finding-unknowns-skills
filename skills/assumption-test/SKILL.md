---
name: assumption-test
description: Test a consequential technical assumption with a small, falsifiable experiment before committing to an approach. Use when a plan depends on uncertain runtime, integration, or data behavior that inspection alone cannot establish. Not for preference interviews or routine implementation.
---

# Assumption test

A plausible assumption can survive every planning conversation and still fail on contact with the system. Turn the consequential uncertainty into a question an experiment can answer.

## Steps

1. Read the request, relevant code, and existing evidence. If inspection already settles the question, cite that evidence and stop; do not manufacture an experiment. If several assumptions remain, select the one whose failure would most change the approach.
2. State the assumption as an observable prediction. Define what would refute it, what would support it within the tested scope, and what would leave it inconclusive. Set those criteria before observing the result.
3. Design the smallest discriminating experiment. Use an isolated fixture or test environment, the real component under question where available, and a bounded number of operations. Name what the setup cannot represent; a mock's behavior is not evidence about its provider.
4. Run the experiment within the user's authorized scope. Preserve the command, relevant inputs, actual output, and environment details needed to reproduce it. If a tool or dependency is unavailable, report the experiment as unrun or inconclusive, with the missing prerequisite.
5. Close with the assumption, method, observation, verdict (**supported within scope**, **refuted**, or **inconclusive**), and the planning decision this evidence changes. Recommend the next discriminating check only if it could change that decision. Keep temporary code separate from the production implementation.

## Guardrails

- One successful trial does not establish a universal claim. State the tested conditions and remaining uncertainty, particularly for concurrency and performance.
- Do not use production writes, real payments, destructive operations, or newly incurred costs without authorization. An experiment does not grant additional permissions.
- Distinguish the component failing from the experiment failing to run. Never turn missing access or a broken fixture into a verdict about the system.
- Do not fix the implementation or broaden into a build unless the user requested it. The deliverable is evidence that informs a decision.
