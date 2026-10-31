#!/usr/bin/env python3
"""Check or extract byte-preserved text sources embedded in a research Skill.

This is a data operation, not a proof checker or a program executor. Extraction
requires a new directory. No Session, network, credential or installer is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re


MAX_FILE_BYTES = 8 * 1024 * 1024
MAX_TOTAL_BYTES = 64 * 1024 * 1024


def relative_path(value):
    if not isinstance(value, str) or not value or "\\" in value or "\0" in value:
        raise ValueError("Invalid relative source path")
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in {"", ".", ".."} for p in value.split("/")):
        raise ValueError("Unsafe relative source path")
    return path


def package_file(root, name):
    path = root.joinpath(*relative_path(name).parts)
    if any(p.is_symlink() for p in [path, *path.parents] if p != root.parent):
        raise ValueError("Symlinks are not accepted in source archives")
    if not path.is_file():
        raise ValueError(f"Missing archive file: {name}")
    return path


def checked_sources(package):
    root = Path(package).resolve(strict=True)
    index = json.loads(package_file(root, "references/source-coverage.json").read_text())
    rows = index["supplemental_sources"]["files"]
    if not isinstance(rows, list) or not rows:
        raise ValueError("No supplemental sources")
    result, used_anchors, texts, total = {}, set(), {}, 0
    for row in rows:
        name = str(relative_path(row["path"]))
        if name in result:
            raise ValueError(f"Duplicate source: {name}")
        size = row["bytes"]
        if type(size) is not int or not 0 <= size <= MAX_FILE_BYTES:
            raise ValueError("Invalid source size")
        total += size
        if total > MAX_TOTAL_BYTES:
            raise ValueError("Source archive exceeds size limit")
        embedded = row["embedded"]
        location, anchor = embedded["file"], embedded["anchor"]
        if not isinstance(anchor, str) or not re.fullmatch(r"[a-zA-Z0-9_-]+", anchor):
            raise ValueError("Invalid source anchor")
        if (location, anchor) in used_anchors:
            raise ValueError("Duplicate source anchor")
        used_anchors.add((location, anchor))
        if location not in texts:
            texts[location] = package_file(root, location).read_bytes()
        text = texts[location]
        marker = f'<a id="{anchor}"></a>'.encode()
        if text.count(marker) != 1:
            raise ValueError(f"Missing or ambiguous source anchor: {name}")
        tail = text.split(marker, 1)[1]
        match = re.search(rb"(?m)^(~{4,})[^\r\n]*\n", tail)
        if not match:
            raise ValueError(f"Missing source fence: {name}")
        start = match.end()
        body = tail[start:start + size]
        suffix = tail[start + size:]
        closing = match[1] + b"\n"
        expected = closing if body.endswith(b"\n") or not body else b"\n" + closing
        if not suffix.startswith(expected):
            raise ValueError(f"Source size/fence mismatch: {name}")
        if hashlib.sha256(body).hexdigest() != row["sha256"]:
            raise ValueError(f"Source hash mismatch: {name}")
        body.decode("utf-8")
        result[name] = body
    return result


def extract_sources(package, output):
    sources = checked_sources(package)  # Validate everything before writing.
    output = Path(output)
    # Reject symlinked destinations, including a linked parent.
    if any(p.is_symlink() for p in [output, *output.parents]):
        raise ValueError("Symlinked output destination")
    output.mkdir(parents=True, exist_ok=False)
    for name, body in sources.items():
        path = output.joinpath(*relative_path(name).parts)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as handle:
            handle.write(body)
    return {"files": len(sources), "bytes": sum(map(len, sources.values()))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    parser.add_argument("--extract", type=Path, help="new destination; omit for read-only validation")
    args = parser.parse_args()
    try:
        if args.extract:
            result = extract_sources(args.package, args.extract)
        else:
            sources = checked_sources(args.package)
            result = {"files": len(sources), "bytes": sum(map(len, sources.values()))}
        print(json.dumps({"status": "passed", **result}))
        return 0
    except (OSError, ValueError, KeyError, TypeError, UnicodeError) as exc:
        print(json.dumps({"status": "failed", "error": str(exc)}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
