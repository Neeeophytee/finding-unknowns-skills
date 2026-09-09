#!/usr/bin/env python3
"""Build the static OSS page from the shipped skills; no hosting side effects."""

import html
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.validate import read_skill

ROOT = Path(__file__).resolve().parents[1]
ORDER = ["blindspot-pass", "brainstorm-prototypes", "interview-me", "reference-hunt", "implementation-plan", "implementation-notes", "pitch-packager", "change-quiz", "context-audit", "agent-interface-design", "progressive-disclosure", "assumption-test", "test-blindspots"]


def build():
    paths = {p.parent.name: p for p in (ROOT / "skills").glob("*/SKILL.md")}
    names = [name for name in ORDER if name in paths] + sorted(set(paths) - set(ORDER))
    cards = []
    for name in names:
        path = paths[name]
        data = read_skill(path)
        origin = "Maintainer-designed extension" if name in {"assumption-test", "test-blindspots"} else "Essay-derived workflow"
        body = path.read_text().split("---", 2)[2].strip()
        cards.append(f'<article class="skill" id="{html.escape(name)}"><div><h3>{html.escape(name)}</h3><span class="origin">{origin}</span></div><div><p>{html.escape(data["description"])}</p><details><summary>Read the skill</summary><pre>{html.escape(body)}</pre></details></div></article>')
    manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    page = (ROOT / "site/index.html").read_text()
    for key, value in {"count": str(len(names)), "version": html.escape(manifest["version"]), "skills": "\n".join(cards)}.items():
        page = page.replace("{{" + key + "}}", value)
    if "{{" in page:
        raise ValueError("unresolved site template token")
    output = ROOT / "site/dist"
    output.mkdir(exist_ok=True)
    (output / "index.html").write_text(page)
    shutil.copy2(ROOT / "site/styles.css", output / "styles.css")
    print(f"Built {len(names)} skill entries into {output}")


if __name__ == "__main__":
    build()
