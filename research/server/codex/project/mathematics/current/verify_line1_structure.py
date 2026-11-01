"""Bounded finite verification and source integrity for the structure increment."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "line1_structure_evidence"
PAPERS = ["line1_yamabe_endpoint", "line1_canonical_shear"]
PROGRAMS = ["line1_yamabe_endpoint_check.py", "line1_canonical_shear_check.py",
            "round11_closed_gluing_check.py", "round15_rigidity_check.py",
            "round21_analytic_check.py"]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(exist_ok=True)
    result = {"baseline": "ef6a282", "programs": [], "documents": [],
              "local_links": 0, "scope": "finite identities and artifact integrity"}
    for name in PROGRAMS:
        run = subprocess.run([sys.executable, name], cwd=ROOT, text=True,
                             capture_output=True, timeout=90)
        result["programs"].append({"name": name, "sha256": digest(ROOT/name),
                                  "exit_code": run.returncode,
                                  "stdout": run.stdout, "stderr": run.stderr})
        assert run.returncode == 0, (name, run.stdout, run.stderr)
    for stem in PAPERS + ["START_LINE1_STRUCTURE_20260923",
                          "line1_structure_verification"]:
        for link in re.findall(r"\]\(([^)]+)\)", (ROOT/(stem+".md")).read_text()):
            if link.startswith(("http:", "https:", "#")):
                continue
            target = ROOT/link.split("#", 1)[0]
            if target == OUT/"results.json":
                continue  # This file is created after all checks pass.
            assert target.exists(), (stem, link)
            result["local_links"] += 1
    for stem in PAPERS:
        log = (OUT/(stem+".log")).read_text(errors="replace")
        bad = [line for line in log.splitlines() if re.search(
            r"Overfull|Missing character|Undefined control|undefined references|LaTeX Error|^!",
            line)]
        assert not bad, (stem, bad)
        info = subprocess.check_output(["pdfinfo", str(ROOT/(stem+".pdf"))], text=True)
        pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
        result["documents"].append({"stem": stem, "pages": pages,
            "hashes": {ext: digest(ROOT/(stem+"."+ext)) for ext in ("md", "tex", "pdf")},
            "typesetting_errors": bad})
    manifest = json.loads((ROOT/"line1_sources_20260923/manifest.json").read_text())
    for item in manifest["files"]:
        assert digest(ROOT/"line1_sources_20260923"/item["name"]) == item["sha256"]
    result["unchanged_uploaded_sources"] = len(manifest["files"])
    result["result"] = "pass"
    result["interpretation"] = "Finite checks do not certify global PDE or topology. See proof reviews."
    (OUT/"results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(f"PASS: {len(PROGRAMS)} programs, {len(PAPERS)} papers, "
          f"{result['local_links']} local links, {len(manifest['files'])} source hashes.")


if __name__ == "__main__":
    main()
