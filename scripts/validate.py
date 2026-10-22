#!/usr/bin/env python3
"""Offline checks for this skill's metadata, installation and local references."""

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently changing skill metadata."""


def unique_mapping(loader, node):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str) or key in mapping:
            raise ValueError(f"Non-string or duplicate YAML key: {key!r}")
        mapping[key] = loader.construct_object(value_node)
    return mapping


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def validate(root, *, installed=False):
    root = Path(root).resolve()
    errors = []
    try:
        text = (root / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
        if not match:
            return ["SKILL.md: missing YAML frontmatter (UTF-8 without BOM required)"]
        meta = yaml.load(match[1], Loader=UniqueLoader)
        if not isinstance(meta, dict):
            return ["SKILL.md: frontmatter must be a mapping"]
        name = meta.get("name")
        if (not isinstance(name, str) or not 1 <= len(name) <= 64
                or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)):
            errors.append("SKILL.md: invalid name")
        elif installed and root.name != name:
            errors.append(f"Installation directory must be named {name}")
        description = meta.get("description")
        if (not isinstance(description, str) or not description.strip()
                or len(description) > 1024):
            errors.append("SKILL.md: description must contain 1-1024 characters")
        allowed = {"name", "description", "license", "version", "updated", "compatibility", "metadata", "allowed-tools"}
        if set(meta) - allowed:
            errors.append(f"SKILL.md: unknown fields {sorted(set(meta) - allowed)}")
        for key, limit in (("license", None), ("compatibility", 500), ("allowed-tools", None)):
            if key in meta and (not isinstance(meta[key], str)
                                or (limit and len(meta[key]) > limit)):
                errors.append(f"SKILL.md: invalid {key}")
        if "metadata" in meta and (not isinstance(meta["metadata"], dict) or any(
                not isinstance(k, str) or not isinstance(v, str)
                for k, v in meta["metadata"].items())):
            errors.append("SKILL.md: metadata must map strings to strings")
        if meta.get("license") == "MIT" and not (root / "LICENSE").is_file():
            errors.append("MIT license declared but LICENSE is missing")
        if not text[match.end():].strip():
            errors.append("SKILL.md: instructions are empty")

        ui_path = root / "agents" / "openai.yaml"
        if ui_path.exists():
            ui = yaml.load(ui_path.read_text(encoding="utf-8"), Loader=UniqueLoader)
            interface = ui.get("interface") if isinstance(ui, dict) else None
            if not isinstance(interface, dict):
                errors.append("agents/openai.yaml: interface must be a mapping")
            else:
                for key in ("display_name", "short_description", "default_prompt"):
                    if not isinstance(interface.get(key), str) or not interface[key].strip():
                        errors.append(f"agents/openai.yaml: missing {key}")
                if isinstance(name, str) and f"${name}" not in str(interface.get("default_prompt", "")):
                    errors.append("agents/openai.yaml: prompt must mention the skill")

        # Check this repo's inline Markdown links, including Chinese/percent-encoded filenames.
        docs = [root / "SKILL.md", root / "README.md", root / "tests" / "README.md"]
        docs += sorted((root / "references").glob("**/*.md"))
        for doc in docs:
            if not doc.is_file():
                continue
            for target in re.findall(r"\]\(([^\s)]+)\)", doc.read_text(encoding="utf-8")):
                url = urlsplit(target.strip("<>"))
                if url.scheme or url.netloc or not url.path:
                    continue
                path = (doc.parent / unquote(url.path)).resolve()
                if not path.is_relative_to(root) or not path.exists():
                    errors.append(f"{doc.relative_to(root)}: broken/local escaping link {target}")
    except (OSError, UnicodeError, yaml.YAMLError, ValueError) as exc:
        errors.append(f"Cannot validate skill: {exc}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--installed", action="store_true", help="also check folder/name match")
    args = parser.parse_args()
    errors = validate(args.path, installed=args.installed)
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print("PASS: metadata, local references and requested installation checks (offline only)")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
