"""Run bounded verification of this research increment, including export checks."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
DOCS = ["line1_energy_selection", "line1_conformal_neck", "line1_non_kahler_bridge"]
PROGRAMS = ["check_line1_energy_selection.py", "line1_conformal_neck_check.py",
            "line1_ricci_remainder_check.py", "check_line1_neck_coordinates.py",
            "line1_scalar_band_check.py", "check_line1_remainders.py",
            "check_lebrun_closure.py"]
OUT = ROOT / "line1_bridge_evidence"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(exist_ok=True)
    result = {"baseline": "0263799", "scope": "finite checks and artifact integrity",
              "programs": [], "documents": [], "local_links": 0}
    for program in PROGRAMS:
        run = subprocess.run([sys.executable, program], cwd=ROOT,
                             text=True, capture_output=True, timeout=90)
        result["programs"].append({"name": program, "sha256": digest(ROOT/program),
                                  "exit_code": run.returncode,
                                  "stdout": run.stdout, "stderr": run.stderr})
        assert run.returncode == 0, (program, run.stdout, run.stderr)
    for stem in DOCS + ["START_LINE1_BRIDGE_20260923"]:
        path = ROOT / (stem + ".md")
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if link.startswith(("https:", "http:", "#")):
                continue
            assert (ROOT / link.split("#", 1)[0]).exists(), (stem, link)
            result["local_links"] += 1
    for stem in DOCS:
        logpath = ROOT/(stem+".log")
        if not logpath.exists():
            logpath = OUT/(stem+".log")
        log = logpath.read_text(errors="replace")
        bad = [x for x in log.splitlines() if re.search(
            r"Overfull|Missing character|Undefined control|undefined references|LaTeX Error|^!", x)]
        assert not bad, (stem, bad)
        if logpath.parent != OUT:
            (OUT/(stem+".log")).write_text(log)
        info = subprocess.check_output(["pdfinfo", str(ROOT/(stem+".pdf"))], text=True)
        pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
        result["documents"].append({"stem": stem, "pages": pages,
             "hashes": {ext: digest(ROOT/(stem+"."+ext)) for ext in ("md","tex","pdf")},
             "typesetting_errors": bad})
    sources = json.loads((ROOT/"line1_sources_20260923/manifest.json").read_text())
    for item in sources["files"]:
        assert digest(ROOT/"line1_sources_20260923"/item["name"]) == item["sha256"]
    result["unchanged_original_sources"] = len(sources["files"])
    result["limitations"] = [
        "Finite checks do not certify global PDE or topology.",
        "The fixed-metric form-budget theorem uses the inherited Hessian lemma.",
        "No worldwide novelty certification or new Yau26 branch is claimed.",
    ]
    result["result"] = "pass"
    (OUT/"results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(f"PASS: {len(PROGRAMS)} programs, {len(DOCS)} papers, "
          f"{result['local_links']} local links, {len(sources['files'])} source hashes.")


if __name__ == "__main__":
    main()
