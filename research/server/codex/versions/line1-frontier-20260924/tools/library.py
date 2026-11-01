#!/usr/bin/env python3
"""Local source lookup and byte-preservation checks for the Yau26 library."""
import argparse
from collections import defaultdict
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, quote
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for part in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(part)
    return h.hexdigest()

def records():
    for manifest in sorted((ROOT / "catalog").glob("sources-*.jsonl")):
        with manifest.open() as stream:
            for line in stream:
                yield json.loads(line)

def index():
    groups = defaultdict(list)
    for row in records():
        groups[row["sha256"]].append(row)
    with (ROOT / "catalog/content-index.jsonl").open("w") as out:
        for digest, rows in sorted(groups.items()):
            out.write(json.dumps({"sha256": digest, "bytes": rows[0]["bytes"],
                "copies": [{"source": r["source"], "path": r["archive"],
                            "category": r["category"]} for r in rows]}, ensure_ascii=False) + "\n")
    zips, members, errors = 0, 0, []
    with (ROOT / "catalog/archive-members.jsonl").open("w") as out:
        for digest, rows in sorted(groups.items()):
            path = ROOT / rows[0]["archive"]
            if path.suffix.lower() != ".zip":
                continue
            zips += 1
            try:
                with zipfile.ZipFile(path) as archive:
                    bad = archive.testzip()
                    if bad:
                        errors.append({"archive": str(path.relative_to(ROOT)), "bad_member": bad})
                    for info in archive.infolist():
                        if info.is_dir():
                            continue
                        members += 1
                        out.write(json.dumps({"archive_sha256": digest,
                            "archive": path.relative_to(ROOT).as_posix(),
                            "member": info.filename, "bytes": info.file_size,
                            "crc32": format(info.CRC, "08x")}, ensure_ascii=False) + "\n")
            except (OSError, zipfile.BadZipFile, RuntimeError) as error:
                errors.append({"archive": str(path.relative_to(ROOT)), "error": str(error)})
    summaries = [json.loads(p.read_text()) for p in sorted((ROOT / "catalog").glob("snapshot-*.json"))]
    lines = ["# Original source archive", "", "Original bytes are preserved here; no archived source is edited or executed by the importer.",
        "These are historical sources, not a parallel set of current theorem statements. Read the",
        "[claim/correction map](../navigation/CLAIMS_AND_CORRECTIONS.md) before reusing old assertions.", "",
        "## Source trees", "", "| Snapshot / source | Files | Category |", "| --- | ---: | --- |"]
    for snapshot in summaries:
        for item in snapshot["roots"]:
            path = "sources/" + snapshot["snapshot"] + "/" + item["id"]
            lines.append(f'| [{item["id"]}]({quote(path)}) | {item["files"]} | {item["category"]} |')
    lines += ["", "## Lookup and preservation", "",
        "`python3 tools/library.py find QUERY` searches original paths, copied paths, and ZIP member names.",
        "The `catalog/sources-*.jsonl` records retain SHA-256, size, original identity and before/after source stats.",
        "`catalog/content-index.jsonl` groups byte-identical copies without claiming mathematical equivalence.",
        "`catalog/archive-members.jsonl` inventories the original ZIP members; originals are retained intact.",
        "", "All research source copies are ordinary local files, not links to a live Session or temporary build.",
        "Historical scripts are reference material; execute a selected check in an isolated output directory only.",
        "", "## Explicit source gaps", "",
        "See [source discovery](../navigation/source-discovery.md#5-research-uploads-reviews-and-unavailable-originals).",
        "The later differently titled three-manuscript originals and the external twelve-round audit/evidence originals",
        "were not located locally. Their absence is recorded, not filled with invented reconstructions.",
        "Raw private execution contexts and unrelated system state are intentionally outside the scientific archive."]
    (ROOT / "archive/README.md").write_text("\n".join(lines) + "\n")
    summary = {"source_records": sum(len(v) for v in groups.values()), "distinct_sha256": len(groups),
               "distinct_zip_files_checked": zips, "zip_members": members, "zip_errors": errors}
    (ROOT / "catalog/index-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary))
    return int(bool(errors))

def find(query):
    term = query.casefold()
    count = 0
    for row in records():
        if term in (row["source"] + " " + row["archive"]).casefold():
            print(row["archive"] + "\t<-- " + row["source"])
            count += 1
    memberfile = ROOT / "catalog/archive-members.jsonl"
    if memberfile.exists():
        for line in memberfile.read_text().splitlines():
            row = json.loads(line)
            if term in row["member"].casefold():
                print(row["archive"] + "!" + row["member"])
                count += 1
    print(f"{count} matching source paths / members", file=sys.stderr)
    return 0

def verify():
    failures = []
    baseline = json.loads((ROOT / "catalog/baseline.json").read_text())
    allrows = list(records())
    for row in baseline["files"] + allrows:
        relative = row.get("path", row.get("archive"))
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size != row["bytes"] or sha(path) != row["sha256"]:
            failures.append({"path": relative, "error": "missing or changed bytes"})
    # Only new editorial links are validated here; historical source bytes stay intact.
    docs = [ROOT / "README.md"]
    for folder in ("navigation", "guidance", "continuation", "archive"):
        docs += sorted((ROOT / folder).glob("*.md"))
    links = 0
    for doc in docs:
        for raw in re.findall(r"(?<!!)\[[^\]]*\]\(([^)\n]+)\)", doc.read_text()):
            raw = raw.strip().strip("<>")
            if re.match(r"[a-zA-Z]+:", raw) or raw.startswith("#"):
                continue
            target = unquote(raw.split("#", 1)[0])
            if not target:
                continue
            links += 1
            if not (doc.parent / target).exists():
                failures.append({"path": str(doc.relative_to(ROOT)), "target": raw, "error": "broken local link"})
    resultfile = ROOT / "catalog/results.json"
    if resultfile.exists():
        catalogue = json.loads(resultfile.read_text())["results"]
        ids = {r["id"] for r in catalogue}
        if len(ids) != len(catalogue):
            failures.append({"error": "duplicate result ID"})
        for result in catalogue:
            for value in result["proof_paths"]:
                if not (ROOT / value.split("#")[0]).exists():
                    failures.append({"path": value, "error": "missing result source"})
            for dependency in result.get("depends_on", []):
                if dependency not in ids:
                    failures.append({"id": result["id"], "dependency": dependency, "error": "missing result dependency"})
    result = {"baseline_files": len(baseline["files"]), "archived_source_records": len(allrows),
              "new_navigation_links_checked": links, "failures": failures,
              "scope": "byte integrity and source/link presence, not mathematical correctness"}
    (ROOT / "catalog/verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False))
    return int(bool(failures))

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("index"); sub.add_parser("verify")
    search = sub.add_parser("find"); search.add_argument("query")
    args = parser.parse_args()
    return find(args.query) if args.command == "find" else globals()[args.command]()

if __name__ == "__main__":
    sys.exit(main())
