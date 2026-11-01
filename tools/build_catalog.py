#!/usr/bin/env python3
"""Build the source index and a path, size and mode inventory."""

from __future__ import annotations

import argparse
import hashlib
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
        dirs[:] = sorted(d for d in dirs if d != ".git")
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


def file_record(path: Path, root: Path, *, content_hashes: bool = False) -> dict:
    if not content_hashes:
        stat = path.lstat()
        return {
            "path": path.relative_to(root).as_posix(),
            "size": len(os.fsencode(os.readlink(path))) if path.is_symlink() else stat.st_size,
            "mode": "120000" if path.is_symlink() else
                    ("100755" if stat.st_mode & 0o111 else "100644"),
        }
    if path.is_symlink():
        data = os.fsencode(os.readlink(path))
        size = len(data)
        sha256 = hashlib.sha256(data).hexdigest()
        blob = hashlib.sha1(f"blob {size}\0".encode() + data).hexdigest()
        mode = "120000"
    else:
        size = path.stat().st_size
        sha = hashlib.sha256()
        git = hashlib.sha1(f"blob {size}\0".encode())
        with path.open("rb") as stream:
            for data in iter(lambda: stream.read(1024 * 1024), b""):
                sha.update(data)
                git.update(data)
        sha256, blob = sha.hexdigest(), git.hexdigest()
        mode = "100755" if path.stat().st_mode & 0o111 else "100644"
    return {
        "path": path.relative_to(root).as_posix(),
        "size": size,
        "sha256": sha256,
        "git_blob_sha": blob,
        "mode": mode,
    }


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
              "The original archive references remain recorded separately.", "",
              "| Archive | Extracted files | Extraction |", "| --- | ---: | --- |"]
    for item in sorted(packages, key=lambda x: (x["expanded_path"], x["archive"])):
        number = "shared" if item.get("duplicate") else str(item.get("files", ""))
        lines.append(f"| {link(item['archive'])} | {number} | {link(item['expanded_path'])} |")
    lines += ["", "## Maintenance", "",
              "Regenerate this index and the path, size and mode inventory with "
              "python3 tools/build_catalog.py. Normal updates do not read or hash file contents.",
              "",
              "Git records revisions of the maintained mathematical text. Original-source "
              "metadata is retained for checking a particular archived version when needed.",
              ""]
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
