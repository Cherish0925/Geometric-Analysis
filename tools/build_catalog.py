#!/usr/bin/env python3
"""Build the source index and file inventory without rereading file contents."""

from __future__ import annotations

import argparse
import json
import os
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote


def read_records(path: Path) -> list[dict]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list):
        raise ValueError(f"Expected a JSON array: {path}")
    return value


def repository_files(root: Path):
    """Yield tracked-content candidates, including symlinks but never .git."""
    for directory, dirs, names in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in {".git", "__pycache__"})
        for name in list(dirs):
            path = Path(directory) / name
            if path.is_symlink():
                dirs.remove(name)
                yield path
        for name in sorted(names):
            path = Path(directory) / name
            relative = path.relative_to(root).as_posix()
            if name == ".git" or relative == "catalog/files.json":
                continue
            yield path


def file_record(path: Path, root: Path) -> dict:
    if path.is_symlink():
        size = len(os.fsencode(os.readlink(path)))
        mode = "120000"
    else:
        size = path.stat().st_size
        mode = "100755" if path.stat().st_mode & 0o111 else "100644"
    return {"path": path.relative_to(root).as_posix(), "size": size, "mode": mode}


def label(text: str) -> str:
    return str(text).replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]").replace("|", "\\|").replace("\n", " ")


def link(path: str, title: str | None = None) -> str:
    return f"[{label(title or path)}]({quote('../' + path, safe='/')})"


def write_source_index(root: Path, sources: list[dict], packages: list[dict]) -> None:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in sources:
        grouped[str(item.get("created_at", "undated"))[:10]].append(item)
    lines = [
        "# Source and package index",
        "",
        "This index links every source entry and extracted package recorded in the archive manifests. "
        "Dates are source creation dates; they are not independent dates of mathematical discovery.",
        "",
        f"- Source entries: **{len(sources):,}**.",
        f"- Package records: **{len(packages):,}**.",
        "- [Source metadata](sources.json), [package metadata](packages.json), "
        "[archive member records](archive_members.json), and [complete file inventory](files.json).",
        "",
        "Server research is indexed separately in [server_sources.json](server_sources.json), "
        "with mathematical navigation in [the server collection](../research/server/README.md).",
        "",
        "## Original sources",
        "",
    ]
    for date in sorted(grouped):
        lines += [f"### {date}", "", "| Source | Bytes | Materialization |", "| --- | ---: | --- |"]
        for item in sorted(grouped[date], key=lambda x: (x.get("created_at", ""), x["repository_path"])):
            lines.append(
                f"| {link(item['repository_path'], item.get('name'))} "
                f"| {item['bytes']:,} | {label(item.get('materialization', ''))} |"
            )
        lines.append("")
    lines += ["## Extracted packages", "", "Identical archives share an extracted directory. "
              "The original archive paths and their hashes remain recorded separately.", "",
              "| Archive | Extracted files | Extraction |", "| --- | ---: | --- |"]
    for item in sorted(packages, key=lambda x: (x["expanded_path"], x["archive"])):
        number = "shared" if item.get("duplicate") else str(item.get("files", ""))
        lines.append(f"| {link(item['archive'])} | {number} | {link(item['expanded_path'])} |")
    lines += ["", "## Maintaining the catalog", "",
              "`python3 tools/build_catalog.py` refreshes this index and the path/size inventory. "
              "Git records content versions; normal catalog maintenance does not hash the source collection.", "",
              "`python3 tools/check_archive.py --full` checks source locations, sizes, and the inventory. "
              "The original archive digests remain in their historical metadata and can be checked "
              "explicitly with `--content` when byte verification is needed.", "",
              "`python3 tools/server_sources.py materialize sessions/S1003A01 /tmp/S1003A01` "
              "reconstructs a scientific source tree from the deduplicated server map. "
              "Use an empty output directory. Other collection names are listed in that map.", ""]
    (root / "catalog" / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    sources = read_records(root / "catalog/sources.json")
    packages = read_records(root / "catalog/packages.json")
    write_source_index(root, sources, packages)
    records = sorted((file_record(path, root) for path in repository_files(root)), key=lambda x: x["path"])
    output = root / "catalog/files.json"
    output.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Catalogued {len(records):,} files, {sum(row['size'] for row in records):,} bytes.")
    print("Wrote catalog/README.md and catalog/files.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
