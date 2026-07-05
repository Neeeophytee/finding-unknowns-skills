---
name: reference-hunt
description: Use existing source code as the specification when the user can't describe what they want in words. Use when the user points at a library, module, folder, or site and says "like this," even if it's in a different language or stack.
---

# Reference hunt

Some requirements are too intricate or too tacit to write down, but working code somewhere already embodies them. The best reference is not a screenshot or a description — it's source. Read it like a spec, then reimplement the semantics, not the syntax.

## Steps

1. Get the reference: a repo path, a vendored folder, a library name, or a site whose underlying code can be read. Ask what specifically to extract from it — behavior, structure, visual system, API shape — so you don't imitate the wrong dimension.
2. Read the reference and produce a **semantics summary** before writing any code:
   - the behaviors and guarantees it implements (timing, ordering, error handling, edge cases),
   - the decisions that look deliberate versus incidental,
   - anything that won't translate to the target language or stack, with a proposed equivalent.
3. Have the user confirm the semantics summary. This is the moment misreadings get caught cheaply.
4. Reimplement in the target stack: same semantics, native idioms. Do not transliterate line by line, and do not copy code verbatim from references whose license doesn't allow it — note the license if it's unclear.
5. Close the loop: list each behavior from the summary and where the new implementation honors it, plus any place you consciously diverged and why.

## Guardrails

- The reference defines *what*; the target codebase's conventions define *how*.
- If the reference itself turns out to be buggy or inconsistent, surface that instead of faithfully reproducing the bug.
- Respect licenses: extracting semantics is fine; copying incompatible code is not.
