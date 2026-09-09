#!/usr/bin/env python3
"""Validate repository packaging and local documentation without running agents."""

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys instead of silently taking the last value."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key in result:
            raise ValueError(f"duplicate or non-string YAML key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def read_skill(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", text, re.S)
    if not match:
        raise ValueError("missing YAML frontmatter")
    data = yaml.load(match[1], Loader=UniqueLoader)
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    name = data.get("name")
    if not isinstance(name, str) or len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("invalid skill name")
    if name != path.parent.name:
        raise ValueError("name must match directory")
    description = data.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        raise ValueError("description must be 1–1024 characters")
    for key in ("license", "allowed-tools", "compatibility"):
        if key in data and (not isinstance(data[key], str) or not data[key].strip()):
            raise ValueError(f"{key} must be a non-empty string")
    if len(data.get("compatibility", "")) > 500:
        raise ValueError("compatibility exceeds 500 characters")
    if "metadata" in data and (not isinstance(data["metadata"], dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in data["metadata"].items())):
        raise ValueError("metadata must map strings to strings")
    # Preserve the existing Claude-specific extension; do not pretend every client honors it.
    if "disable-model-invocation" in data and not isinstance(data["disable-model-invocation"], bool):
        raise ValueError("disable-model-invocation must be boolean")
    headings = re.findall(r"^## (.+)$", match[2], re.M)
    if not headings or headings[-1] != "Guardrails":
        raise ValueError("last section must be ## Guardrails")
    return data


def local_links(path):
    # This repo uses inline Markdown links. Ignore examples inside fenced code blocks.
    text = re.sub(r"^```.*?^```[^\n]*$", "", path.read_text(encoding="utf-8"), flags=re.M | re.S)
    for target in re.findall(r"\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", text):
        parsed = urlsplit(target.strip("<>"))
        if not parsed.scheme and not parsed.netloc and parsed.path:
            yield unquote(parsed.path)


def validate(root):
    errors = []
    skills = {}
    for directory in sorted((root / "skills").iterdir()):
        if not directory.is_dir() or directory.is_symlink():
            errors.append(f"skills/{directory.name}: expected a real skill directory")
            continue
        if sorted(p.name for p in directory.iterdir()) != ["SKILL.md"]:
            errors.append(f"skills/{directory.name}: keep the single-file packaging convention")
        try:
            skills[directory.name] = read_skill(directory / "SKILL.md")
        except (ValueError, OSError, yaml.YAMLError) as exc:
            errors.append(f"skills/{directory.name}: {exc}")
    if not skills:
        errors.append("no valid skills found")
    manifests = []
    for relative in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
        try:
            manifests.append(json.loads((root / relative).read_text()))
        except (OSError, ValueError) as exc:
            errors.append(f"{relative}: {exc}")
    if len(manifests) == 2:
        claude, codex = manifests
        for field in ("name", "version", "description", "license"):
            if not claude.get(field) or claude.get(field) != codex.get(field):
                errors.append(f"plugin manifests must agree on {field}")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(claude.get("version", ""))):
            errors.append("plugin version must be X.Y.Z")
        expected = {f"./skills/{name}" for name in skills}
        entries = claude.get("skills", [])
        if not isinstance(entries, list) or not all(isinstance(x, str) for x in entries) or set(entries) != expected or len(entries) != len(expected):
            errors.append("Claude ship gate must list each skill exactly once")
        if codex.get("skills") != "./skills/":
            errors.append("Codex skills path must remain ./skills/")
        description = claude.get("description", "")
        if not isinstance(description, str) or not description.startswith(f"{len(skills)} skills "):
            errors.append("plugin description skill count is stale")
        elif any(name.replace("-", " ") not in description for name in skills):
            errors.append("plugin description must enumerate every skill")
    for relative, marketplace_name in ((".claude-plugin/marketplace.json", "finding-unknowns-skills"), (".agents/plugins/marketplace.json", "finding-unknowns")):
        try:
            marketplace = json.loads((root / relative).read_text())
            plugins = marketplace.get("plugins", [])
            if marketplace.get("name") != marketplace_name or len(plugins) != 1 or plugins[0].get("name") != "finding-unknowns" or plugins[0].get("source") != "./":
                errors.append(f"{relative}: preserve marketplace identity and local source")
            if "version" in marketplace or any("version" in p for p in plugins):
                errors.append(f"{relative}: versions belong in plugin manifests")
        except (OSError, ValueError, AttributeError, TypeError) as exc:
            errors.append(f"{relative}: {exc}")
    for relative in ("README.md", "EXAMPLES.md", "CONTRIBUTING.md", "LICENSE", "CHANGELOG.md", "COMPATIBILITY.md", "ROADMAP.md"):
        if not (root / relative).is_file():
            errors.append(f"missing {relative}")
    if (root / "AGENTS.md").read_bytes() != (root / "CLAUDE.md").read_bytes():
        errors.append("AGENTS.md and CLAUDE.md must be byte-identical")
    readme = (root / "README.md").read_text()
    if not re.search(rf"\*\*{len(skills)} installable skills\b", readme):
        errors.append("README headline skill count is stale")
    examples = (root / "EXAMPLES.md").read_text()
    for name in skills:
        if f"skills/{name}/SKILL.md" not in readme:
            errors.append(f"README missing skill link: {name}")
        if not re.search(rf"^## {re.escape(name)}$", examples, re.M):
            errors.append(f"EXAMPLES missing invocation: {name}")
    docs = list(root.glob("*.md")) + list((root / "skills").glob("*/SKILL.md"))
    docs += list((root / "docs").rglob("*.md")) + list((root / "evals").rglob("*.md"))
    for path in docs:
        if path.name in {"FUTURE-EXTENSIONS.md", "implementation-notes.md"}:
            continue
        for target in local_links(path):
            if not (path.parent / target).exists():
                errors.append(f"{path.relative_to(root)}: broken local link {target}")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--release", action="store_true", help="also reject an unfinished conduct reporting contact")
    args = parser.parse_args()
    failures = validate(args.root)
    if args.release:
        conduct = args.root / "CODE_OF_CONDUCT.md"
        if not conduct.is_file() or "[INSERT CONTACT METHOD]" in conduct.read_text() or "Draft:" in conduct.read_text():
            failures.append("finalize the Code of Conduct and its private reporting contact before release")
    for failure in failures:
        print(f"ERROR: {failure}")
    if failures:
        raise SystemExit(1)
    print(f"PASS: {len(list((args.root / 'skills').glob('*/SKILL.md')))} skills; packaging, manifests, documentation, and local file links")
