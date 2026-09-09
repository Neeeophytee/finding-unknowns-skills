# FlowStacks OSS hosting

## Live deployment — 2026-09-09

- Vercel team: `neophytes-projects-242f42c6` (the same team as FlowStacks).
- Separate project: `flowstacks-oss`.
- Public hub: https://oss.flowstacks.xyz
- Finding Unknowns page: https://oss.flowstacks.xyz/finding-unknowns-skills
- Custom domain: https://oss.flowstacks.xyz
- Production deployment: `dpl_FjRSySVSGjQ897piARkfVa7Mw2tM`.

All nine pages and the shared CSS/icon returned HTTP 200 without authentication. Private deployment configuration paths returned 404. The page uses FlowStacks’ cream/chocolate palette, Fraunces headings, Geist body type, and existing logomark.

## Custom domain and main-site links

`oss.flowstacks.xyz` is live with HTTPS. Authoritative DNS is hosted by Hostinger (`hermes.dns-parking.com` and `artemis.dns-parking.com`). FlowStacks desktop navigation, mobile navigation, and footer now link to this custom domain.

Cards are sorted by the star-count snapshot recorded in `site/projects.json` on September 9, 2026. Star badges refresh independently; ordering changes when those recorded counts are refreshed and the site is rebuilt. Each card links directly to its repository through “Star it.” Each project page links to its contribution guide, or GitHub’s repository contribution page when no guide exists.

## Source and rebuild

`site/projects.json` is the reviewed eight-project catalog. `scripts/build_site.py` generates the directory, one page per project, the sitemap, and static deployment configuration into ignored `site/dist/`. The Finding Unknowns skill listing comes directly from its unchanged SKILL.md files.

```bash
python scripts/build_site.py
```

Use the development Python environment from CONTRIBUTING.md. Vercel serves clean URLs; a generic local static server may require the `.html` suffix on project-page URLs. No website code runs inside installed skills.

The deployment is a direct static upload, not an automatic Git integration. Website source is maintained in this repository; publishing it to GitHub does not automatically redeploy Vercel. The separate license-detection correction was already pushed and GitHub now reports MIT.

## License labels

Finding Unknowns, Agent Stylebooks, AI Cost-Cutter Skills, and Accessibility Agent Skills are labeled MIT. Awesome AI Workflows is CC0-1.0; AI Watermarks Reality Check is AGPL-3.0. MCP Stateless Conformance and Agent Arena Skill have no declared license in the checked files and are clearly labeled as public repositories with no declared reuse license.

## OSS program scope

Apply for Finding Unknowns using its dedicated page and repository. Explain that the site also lists other projects; do not assume that credits awarded for one project cover unrelated pages. Confirm the permitted shared-hosting scope with Vercel before using program credits.
