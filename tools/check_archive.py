#!/usr/bin/env python3
"""Check source locations and inventory; optionally verify historical archive digests."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path, PurePosixPath

# Verification must not create a new, unlisted __pycache__ directory.
sys.dont_write_bytecode = True
from build_catalog import file_record, read_records, repository_files


def safe_path(root: Path, relative: str) -> Path:
    value = PurePosixPath(relative)
    if value.is_absolute() or ".." in value.parts or not value.parts or ".git" in value.parts:
        raise ValueError(f"Invalid repository path: {relative!r}")
    path = root.joinpath(*value.parts)
    if not path.resolve().is_relative_to(root):
        raise ValueError(f"Path leaves repository: {relative!r}")
    return path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--full", action="store_true", help="Also check every file against catalog/files.json.")
    parser.add_argument("--content", action="store_true", help="Also read bytes and check historical digests.")
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    checked: dict[str, tuple[int, str]] = {}

    def verify(relative: str, expected_size: int | None, expected_sha: str | None, origin: str) -> None:
        try:
            path = safe_path(root, relative)
            if path.is_symlink() or not path.is_file():
                raise ValueError("missing regular file")
            if relative not in checked:
                checked[relative] = (path.stat().st_size, sha256(path) if args.content and expected_sha else "")
            size, digest = checked[relative]
            if expected_size is not None and size != expected_size:
                errors.append(f"{origin}: {relative}: bytes {size}, expected {expected_size}")
            if args.content and expected_sha and digest != expected_sha:
                errors.append(f"{origin}: {relative}: SHA256 mismatch")
        except (OSError, ValueError) as error:
            errors.append(f"{origin}: {relative}: {error}")

    try:
        sources = read_records(root / "catalog/sources.json")
        members = read_records(root / "catalog/archive_members.json")
        packages = read_records(root / "catalog/packages.json")
        for item in sources:
            verify(item["repository_path"], item["bytes"], item["sha256"], "sources.json")
        for item in members:
            verify(item["path"], item["bytes"], item["sha256"], "archive_members.json")
        for item in packages:
            verify(item["archive"], None, item["sha256"], "packages.json")
            extracted = safe_path(root, item["expanded_path"])
            if not extracted.is_dir():
                errors.append(f"packages.json: missing extraction {item['expanded_path']}")
            elif not item.get("duplicate") and "files" in item:
                count = sum(1 for path in extracted.rglob("*") if path.is_file())
                if count != item["files"]:
                    errors.append(f"packages.json: {item['expanded_path']}: {count} files, expected {item['files']}")

        server_map = root / "catalog/server_sources.json"
        if server_map.exists():
            for item in read_records(server_map):
                verify(item["repository_path"], item["bytes"], None, "server_sources.json")

        if args.full:
            inventory = read_records(root / "catalog/files.json")
            indexed = {item["path"]: item for item in inventory}
            if len(indexed) != len(inventory):
                errors.append("files.json: duplicate paths")
            actual = {path.relative_to(root).as_posix(): path for path in repository_files(root)}
            for relative in sorted(indexed.keys() - actual.keys()):
                errors.append(f"files.json: missing {relative}")
            for relative in sorted(actual.keys() - indexed.keys()):
                errors.append(f"files.json: unlisted {relative}")
            for relative in sorted(indexed.keys() & actual.keys()):
                observed = file_record(actual[relative], root)
                for field in ("size", "mode"):
                    if observed[field] != indexed[relative][field]:
                        errors.append(f"files.json: {relative}: {field} mismatch")
    except (OSError, ValueError, KeyError, TypeError) as error:
        errors.append(f"Manifest error: {error}")

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        print(f"FAILED: {len(errors)} issue(s).")
        return 1
    print(f"OK: {len(sources):,} source records, {len(members):,} member records, {len(packages):,} package records.")
    print(f"Checked {len(checked):,} distinct source locations.")
    if args.full:
        print(f"Verified complete catalog: {len(inventory):,} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
