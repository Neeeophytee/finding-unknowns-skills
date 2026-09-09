# Release checklist — 1.4.0 candidate

This is a local preparation checklist, not authorization to publish.

## Verify the candidate

- Run `python scripts/validate.py` and `python -m unittest discover -s tests -v` in the development environment.
- Run the bundled skill-creator validator for each new skill when available.
- Review the new skill triggers and the evaluation cases. Packaging checks do not replace behavioral trials.
- Confirm the original eleven skill hashes match `tests/fixtures/legacy-skills.json`.
- Confirm both plugin manifests say 1.4.0 and the Claude ship gate includes every skill exactly once.
- Review the dated compatibility receipts and any untested routes.
- Confirm the approved private reporting address `coc@flowstacks.xyz` is monitored.
- Run `python scripts/validate.py --release` to catch an unresolved conduct contact.
- Build the local documentation page with `python scripts/build_site.py`.

## After explicit publication authorization

- Wait for the maintainer to review the complete diff and switch to their own GitHub account.
- Verify the authenticated GitHub account, destination repository, and Git commit identity before any commit or push. Do not log out or change accounts on the maintainer’s behalf.
- Review the full diff, finalize the changelog date, and commit only the approved files.
- Create an annotated `v1.4.0` tag only if that tag does not already exist.
- Push the approved commit and tag, then create a published GitHub Release with release notes from the finalized changelog. A tag alone is not completion.
- Set up the dedicated Vercel OSS project using [the hosting notes](HOSTING.md), then verify the deployed page.
- Recheck links to new files after GitHub publication.
- Capture application-day metrics and finalize [the application draft](OSS-APPLICATION.md).

Do not add AI-attribution trailers. Do not claim an unreleased local candidate is available through the public GitHub install command.
