# OSS page hosting

The page is prepared locally; no site registration, deployment, or domain change has been performed. It uses static HTML and CSS, with its catalog generated from the actual skills. The skill packages themselves gain no website runtime dependency.

## Local preview

In the development Python environment:

```bash
python scripts/build_site.py
python -m http.server 8765 --bind 127.0.0.1 --directory site/dist
```

The generated output is ignored by Git. Source files are in `site/` and `scripts/build_site.py`.

## Intended Vercel deployment

After publication authorization, use a separate Vercel project for the OSS page. Build the static output using the development dependencies and `python scripts/build_site.py`, then publish only `site/dist`. If the selected Vercel build environment lacks Python, generate this output in CI and deploy it as a static directory. Verify the chosen setup before documenting it as working.

Do not attach the commercial application, credentials, or billing resources to this project. Domain routing for `flowstacks.xyz/open-source/finding-unknowns-skills` needs review in the actual FlowStacks project; this repository does not change that routing. A dedicated subdomain is another option if routing would otherwise require changes to the commercial app.

## Before making the page public

- Publish the approved repository release first: the page's GitHub links and install command target the public default branch.
- Confirm the Code of Conduct reporting address is monitored.
- Review the copy that identifies this as a local candidate; update it only to the actual published state.
- Verify the deployed page and navigation on the chosen host. No live-hosting compatibility is claimed from a local build.
- Add adoption metrics only after capturing current source evidence. None are hardcoded into the page.
