# Release checklist — 1.5.0

## Verify

- Run `python scripts/validate.py --release` and `python -m unittest discover -s tests -v`.
- Validate the new skill's frontmatter and single-file structure.
- Confirm all thirteen prior skills match `tests/fixtures/pre-1.5.0-skills.json`.
- Confirm both plugin manifests say 1.5.0 and the Claude manifest lists all fourteen skills exactly once.
- Run `python evals/regression_proof.py` and `python scripts/build_site.py`.
- Review the dated discovery receipts in [COMPATIBILITY.md](../COMPATIBILITY.md); discovery checks do not establish behavioral improvement.

## Publish

- Review the complete release diff and confirm the repository, authenticated account, and commit identity.
- Commit only release files; exclude local notes, credentials, generated output, and unrelated work.
- Finalize the changelog date, create an annotated `v1.5.0` tag, and push the commit and tag.
- Create a published GitHub Release with the changelog highlights. A tag alone is not a release.
- Check CI and public installation discovery after publication.

## skills.sh

- Before publication, `npx skills@latest add /absolute/path/to/repo --list` must discover all fourteen skills.
- After publication, run `npx skills@latest add Neeeophytee/finding-unknowns-skills --list` and verify `regression-proof` is present.
- Verify a genuine install with `--skill regression-proof` in an isolated project and check the [listing](https://skills.sh/neeeophytee/finding-unknowns-skills/regression-proof).
- The [skills.sh FAQ](https://skills.sh/docs/faq) describes listing through installation telemetry. Do not equate local discovery with public indexing, or repeat installs to inflate counts. Record the observed result; indexing may be delayed.
