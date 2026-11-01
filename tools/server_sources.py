#!/usr/bin/env python3
"""Import scientific source trees once, or reconstruct a tree from the source map.

Input manifests are local JSON arrays of {source, target, role}. Source is a
local filename; target normally starts with research/server/. An explicit
collection/source_path pair also allows recovered originals in archive/.
Absolute host paths are
not written to the repository. Identical bytes reuse an existing repository
file. A source tree can therefore be reconstructed without storing duplicates.
"""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
from collections import defaultdict
from pathlib import Path


def read(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else []


def source_identity(target: str) -> tuple[str, str]:
    parts = Path(target).parts
    if parts[:2] != ("research", "server") or ".." in parts:
        raise ValueError(f"Expected a research/server/ destination: {target}")
    # Session trees are independent; Codex's project and historical worktrees
    # are kept together so their relative references can be reconstructed.
    length = 4 if parts[2] == "sessions" else 3
    return "/".join(parts[2:length]), "/".join(parts[length:])


def import_sources(root: Path, manifests: list[Path]) -> None:
    catalog = root / "catalog/server_sources.json"
    records = read(catalog)
    known = {(r["collection"], r["source_path"]): r for r in records}
    by_size: dict[int, list[Path]] = defaultdict(list)
    for directory in (root / "archive", root / "research"):
        for path in sorted(directory.rglob("*")):
            if path.is_file() and not path.is_symlink():
                by_size[path.stat().st_size].append(path)
    copied = reused = 0
    for manifest in manifests:
        for item in json.loads(manifest.read_text(encoding="utf-8")):
            source = Path(item["source"])
            target = item["target"]
            if item.get("collection") and item.get("source_path"):
                collection, relative = item["collection"], item["source_path"]
                if Path(target).is_absolute() or ".." in Path(target).parts:
                    raise ValueError(f"Expected a repository-relative target: {target}")
            else:
                collection, relative = source_identity(target)
            size = source.stat().st_size
            candidates = by_size[size]
            # Same-named sources are the usual aliases; no digest pass is needed.
            candidates = sorted(candidates, key=lambda p: p.name != source.name)
            match = next((p for p in candidates if filecmp.cmp(source, p, shallow=False)), None)
            if match is None:
                match = root / target
                if match.exists():
                    raise ValueError(f"Different content already occupies {target}")
                match.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, match)
                by_size[size].append(match)
                copied += 1
            else:
                reused += 1
            record = {
                "collection": collection,
                "source_path": relative,
                "repository_path": match.relative_to(root).as_posix(),
                "bytes": size,
                "role": item.get("role", "research source"),
            }
            known[collection, relative] = record
    records = sorted(known.values(), key=lambda r: (r["collection"], r["source_path"]))
    catalog.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Imported {copied} files; reused {reused} existing files; {len(records)} source locations.")


def materialize(root: Path, collection: str, destination: Path) -> None:
    records = [r for r in read(root / "catalog/server_sources.json") if r["collection"] == collection]
    if not records:
        raise ValueError(f"Unknown collection: {collection}")
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("Use an empty destination to reconstruct a source tree.")
    destination.mkdir(parents=True, exist_ok=True)
    for item in records:
        target = destination / item["source_path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(root / item["repository_path"], target)
    print(f"Reconstructed {len(records)} source files in {destination}.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    sub = parser.add_subparsers(dest="command", required=True)
    imp = sub.add_parser("import", help="Import manifests prepared on the source server")
    imp.add_argument("manifests", nargs="+", type=Path)
    restore = sub.add_parser("materialize", help="Reconstruct a collection for reading or computation")
    restore.add_argument("collection")
    restore.add_argument("destination", type=Path)
    args = parser.parse_args()
    if args.command == "import":
        import_sources(args.root.resolve(), args.manifests)
    else:
        materialize(args.root.resolve(), args.collection, args.destination)


if __name__ == "__main__":
    main()
