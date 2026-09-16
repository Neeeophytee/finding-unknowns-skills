#!/usr/bin/env python3
"""Build the FlowStacks OSS hub and individual project pages without hosting side effects."""
import html
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.validate import read_skill

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://oss.flowstacks.xyz"
e = html.escape


def load_projects():
    projects = json.loads((ROOT / "site/projects.json").read_text())
    slugs = set()
    for p in projects:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", p["slug"]) or p["slug"] in slugs:
            raise ValueError("invalid or duplicate project slug")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", p["repo"]):
            raise ValueError("invalid GitHub repository")
        slugs.add(p["slug"])
    return sorted(projects, key=lambda p: (-p["stars"], p["name"].casefold()))


def star_badge(p):
    repo = e(p["repo"])
    return f'<a class="star-badge" href="https://github.com/{repo}/stargazers" aria-label="GitHub stars for {e(p["name"])}"><img src="https://img.shields.io/github/stars/{repo}?style=flat&amp;label=GitHub%20stars&amp;color=7b4b2a" alt="GitHub stars for {e(p["name"])}" height="20" loading="lazy"></a>'


def card(p):
    owner = p["repo"].split("/")[0]
    return f'''<article class="project-card"><div class="card-top"><span class="category">{e(p['category'])}</span><span class="license">{e(p['license'])}</span></div><h3><a href="/{p['slug']}">{e(p['name'])}</a></h3><p>{e(p['description'])}</p>{star_badge(p)}<div class="card-bottom"><a class="text-link" href="/{p['slug']}">Explore project →</a><a class="button star-it" href="https://github.com/{e(p['repo'])}" aria-label="Star {e(p['name'])} on GitHub">☆ Star it</a></div></article>'''


def catalog(projects):
    return '''<section class="wrap hero"><p class="eyebrow">The FlowStacks open-source collection</p><h1>Open work.<br><span class="accent">Built to be useful.</span></h1><p class="intro">Tools, skills, and public evidence for people building with AI. Explore the projects we maintain, understand what each one does, and take a closer look at the source.</p><div class="hero-actions"><a class="button" href="#projects">Explore the projects ↓</a><a class="button secondary" href="https://flowstacks.xyz">Visit FlowStacks ↗</a></div></section>''' + f'''<section id="projects" class="wrap section"><div class="section-top"><div><p class="eyebrow">The directory</p><h2>Find your next starting point.</h2></div><p class="note">{len(projects)} maintained projects · Most stars first</p></div><div class="projects">{''.join(card(p) for p in projects)}</div><p class="note">Licenses are listed individually. “Not declared” identifies a public repository without a declared reuse license; it is not a claim of open-source licensing.</p></section>''' + '''<section id="about" class="wrap section about"><div><p class="eyebrow">Why we share the work</p><h2>Useful ideas deserve something you can inspect.</h2><p>These projects make a workflow, an assumption, or a piece of evidence easier to examine. Each project page links to its source, explains where it helps, and makes its limits visible.</p><p>Maintained by <a href="https://github.com/Neeeophytee">Neeeophytee</a> and <a href="https://github.com/smukh">smukh</a>, alongside FlowStacks.</p></div><div><p class="eyebrow">Make it better</p><h2>Bring a problem worth solving.</h2><p>Found a broken example, a missing case, or a useful improvement? Start with the relevant repository’s contribution guidance or issues. Keep reports specific and remove private information.</p><p>This hub presents the collection. Each repository remains the source of truth for its license, installation steps, and maintenance history.</p></div></section>'''


def skill_catalog():
    rows = []
    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        data = read_skill(path)
        kind = "Maintainer-designed extension" if data['name'] in {'assumption-test', 'test-blindspots'} else "Essay-derived workflow"
        body = path.read_text().split('---', 2)[2].strip()
        rows.append(f'<article class="skill"><div><h3>{e(data["name"])}</h3><small>{kind}</small></div><div><p>{e(data["description"])}</p><details><summary>Read the skill</summary><pre>{e(body)}</pre></details></div></article>')
    return '<section class="wrap section"><p class="eyebrow">The skills</p><h2>Thirteen ways to make uncertainty useful.</h2><div class="skills">'+''.join(rows)+'</div></section>'


def project_page(p, projects):
    github = 'https://github.com/'+p['repo']
    owner = p['repo'].split('/')[0]
    start = f'<pre>{e(p["command"])}</pre><p class="note">Check the repository for current runtime requirements and agent-specific installation options.</p>' if p['command'] else '<p>Start with the repository’s README for the workflow, setup, and current usage instructions.</p>'
    license_link = f'<a href="{github}/blob/main/LICENSE">Read the license ↗</a>' if p['license'] != 'Not declared' else 'No reuse license declared in the repository checked.'
    body = f'''<div class="wrap breadcrumb"><a href="/">All projects</a> / {e(p['name'])}</div><section class="wrap project-hero"><p class="eyebrow">{e(p['category'])}</p><h1>{e(p['name'])}</h1><p class="intro">{e(p['tagline'])} {e(p['description'])}</p><div class="project-meta"><span class="license">{e(p['license'])}</span>{star_badge(p)}<span>Maintained by <a href="https://github.com/{e(owner)}">{e(owner)}</a></span></div><div class="hero-actions"><a class="button" href="{github}">View on GitHub ↗</a><a class="button secondary" href="#get-started">Get started ↓</a><a class="button secondary" href="{e(p['contribute_url'])}">Contribute ↗</a></div></section><section class="wrap section detail-grid"><div><p class="eyebrow">Where it helps</p><h2>A useful fit for your next task.</h2><p>{e(p['audience'])}</p><ul class="feature-list">{''.join('<li>'+e(x)+'</li>' for x in p['features'])}</ul><p class="example-label">An example request</p><blockquote class="example">{e(p['example'])}</blockquote><p><strong>What you get:</strong> {e(p['outcome'])}</p></div><aside class="panel" id="get-started"><h2>Get started</h2>{start}<p><a href="{github}#readme">Read the documentation ↗</a></p><div class="source-note"><p class="eyebrow">License &amp; scope</p><p>{license_link}</p><p class="note">{e(p['limits'])}</p></div></aside></section>'''
    if p['slug'] == 'finding-unknowns-skills':
        body += '<section id="community" class="wrap section"><p class="eyebrow">Community &amp; coverage</p><h2>Explore community perspectives.</h2><ul class="feature-list"><li><a href="https://skillproof.dev/skills/blindspot-pass">SkillProof</a> — review of blindspot-pass, one skill in the collection.</li><li><a href="https://x.com/aiedge_/status/2076456586546131031">AI Edge</a> — project walkthrough and installation overview.</li><li><a href="https://swipe.md/issues/sketch-an-app-with-ai#blindspot-pass">Swipe</a> — editorial feature on blindspot-pass.</li><li><a href="https://zenn.dev/shintaroamaike/articles/672de8598dd268">Zenn</a> — Japanese-language article discussing the community implementation.</li><li><a href="https://github.com/VoltAgent/awesome-agent-skills">VoltAgent</a> — inclusion in its curated agent-skills collection.</li></ul><p class="note">Coverage may describe earlier releases. Reviews of individual skills do not establish results for the entire collection.</p></section>'
        body += skill_catalog()
        body += f'<section class="wrap section"><p class="eyebrow">Evidence and attribution</p><h2>Know what was checked.</h2><p>The original eleven skill files are unchanged in v1.4.0. Codex and Hermes discovery checks, reproducible fixtures, and their limits are documented in the repository.</p><p><a href="{github}/blob/main/COMPATIBILITY.md">Compatibility</a> · <a href="{github}/blob/main/EXAMPLES.md">Examples</a> · <a href="{github}/blob/main/NOTICE.md">Attribution</a> · <a href="{github}/blob/main/CODE_OF_CONDUCT.md">Code of Conduct</a></p></section>'
    body += '<section class="wrap section source-note"><p class="eyebrow">Keep exploring</p><h2>More from the collection.</h2><div class="other-projects">'+''.join(f'<a href="/{q["slug"]}">{e(q["name"])}</a>' for q in projects if q['slug'] != p['slug'])+'</div></section>'
    return body


def build(output=None):
    output = Path(output) if output else ROOT / 'site/dist'
    output.mkdir(parents=True, exist_ok=True)
    projects = load_projects()
    template = (ROOT / 'site/index.html').read_text()
    pages = [('', 'Open tools & public projects', f'Explore {len(projects)} maintained projects in the FlowStacks open-source collection, with source links, installation guidance, and individual licenses.', catalog(projects))]
    pages += [(p['slug'], p['name'], p['description'], project_page(p, projects)) for p in projects]
    for slug, title, description, body in pages:
        page = template
        for key, value in {'title':e(title), 'description':e(description), 'canonical':e(ORIGIN+('/'+slug if slug else '/')), 'body':body}.items():
            page = page.replace('{{'+key+'}}', value)
        if '{{' in page:
            raise ValueError('unresolved template token')
        # Flat HTML files pair with Vercel cleanUrls and an extensionless local preview.
        (output / (slug+'.html' if slug else 'index.html')).write_text(page)
    for file in ['styles.css', 'icon.svg']:
        shutil.copy2(ROOT / 'site' / file, output / file)
    (output / 'vercel.json').write_text(json.dumps({'version':2,'cleanUrls':True,'trailingSlash':False},indent=2)+'\n')
    (output / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+ORIGIN+'/sitemap.xml\n')
    urls=[ORIGIN+('/'+slug if slug else '/') for slug, *_ in pages]
    (output / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+e(url)+'</loc></url>' for url in urls)+'</urlset>')
    print(f'Built {len(pages)} pages into {output}')
    return output


if __name__ == '__main__':
    build()
