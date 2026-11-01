"""Reproduce bounded checks for the 2026-09-23 first-line increment."""

from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
DOCS = ["line1_unified_v2", "line1_scalar_band_remainder", "line1_kahler_energy"]
CHECKS = ["check_line1_remainders.py", "line1_scalar_band_check.py",
          "check_lebrun_closure.py"]


def main():
    result = {"date": "2026-09-23", "baseline": "046166b",
              "scope": "finite algebra, unchanged sources, local links, and typesetting",
              "programs": [], "documents": [], "limitations": [
                  "No new independent proof of the inherited bundle Hessian/calibration lemma.",
                  "No certification of worldwide novelty or a complete Yau26 branch.",
                  "The literature inventory retains each source's original verification level.",
              ]}
    for name in CHECKS:
        run = subprocess.run([sys.executable, name], cwd=ROOT, text=True,
                             capture_output=True, timeout=60)
        result["programs"].append({"program": name, "exit_code": run.returncode,
                                   "stdout": run.stdout, "stderr": run.stderr})
        assert run.returncode == 0, (name, run.stderr)
    total_links = 0
    for name in DOCS:
        md = (ROOT / f"{name}.md").read_text()
        checked_links = []
        for link in re.findall(r"\]\(([^)]+)\)", md):
            if link.startswith(("http:", "https:", "#")):
                continue
            target = link.split("#", 1)[0]
            assert (ROOT / target).exists(), (name, target)
            checked_links.append(target)
        total_links += len(checked_links)
        log_path = ROOT / f"{name}.log"
        if not log_path.exists():
            log_path = ROOT / "line1_build_logs" / f"{name}.log"
        log = log_path.read_text(errors="replace")
        bad = [line for line in log.splitlines() if re.search(
            r"Overfull|Missing character|Undefined control|undefined references|LaTeX Error", line)]
        assert not bad, (name, bad)
        info = subprocess.check_output(["pdfinfo", f"{name}.pdf"], cwd=ROOT, text=True)
        pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
        result["documents"].append({
            "name": name, "pages": pages, "checked_links": checked_links,
            "md_sha256": hashlib.sha256((ROOT / f"{name}.md").read_bytes()).hexdigest(),
            "tex_sha256": hashlib.sha256((ROOT / f"{name}.tex").read_bytes()).hexdigest(),
            "pdf_sha256": hashlib.sha256((ROOT / f"{name}.pdf").read_bytes()).hexdigest(),
            "typesetting_errors": bad,
        })
    sources = json.loads((ROOT / "line1_sources_20260923/manifest.json").read_text())
    for item in sources["files"]:
        path = ROOT / "line1_sources_20260923" / item["name"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
    result["unchanged_source_files"] = len(sources["files"])
    result["checked_local_links"] = total_links
    result["result"] = "pass"
    (ROOT / "line1_verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: {len(CHECKS)} programs, {len(DOCS)} documents, "
          f"{total_links} local links, {len(sources['files'])} source hashes.")


if __name__ == "__main__":
    main()
