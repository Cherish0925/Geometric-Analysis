"""Run scoped finite checks and validate this research package's local links."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
CHECKS = [
    "check_line1_functional_pencil.py",
    "line1_composed_application_check.py",
    "line1_integral_rigidity_paper_check.py",
    "round21_analytic_check.py",
    "round3_monopole_input_check.py",
    "round4_rigidity_check.py",
    "round4_all_sign_check.py",
    "round5_rigidity_check.py",
    "check_lebrun_closure.py",
]
PAPERS = [
    "line1_functional_pencil",
    "line1_composed_application",
    "line1_integral_rigidity_paper",
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    # A second run must not overwrite earlier evidence.
    output.mkdir(parents=True, exist_ok=False)
    report = {"scope": "finite algebra, manuscript files and local links; not PDE or novelty certification", "checks": []}
    for script in CHECKS:
        command = [sys.executable, str(ROOT / script)]
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=120)
        (output / (Path(script).stem + ".log")).write_text(result.stdout + result.stderr)
        report["checks"].append({"script": script, "returncode": result.returncode})
        if result.returncode:
            (output / "results.json").write_text(json.dumps(report, indent=2))
            raise SystemExit(f"FAILED: {script}; see {output}")
    report["manuscripts"] = []
    link_count = 0
    for paper in PAPERS:
        files = {}
        for suffix in (".md", ".tex", ".pdf"):
            path = ROOT / (paper + suffix)
            if not path.is_file():
                raise SystemExit(f"Missing manuscript: {path.name}")
            files[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
        for link in re.findall(r"\]\(([^)]+)\)", (ROOT / (paper + ".md")).read_text()):
            if link.startswith(("http://", "https://", "#")):
                continue
            target = link.split("#", 1)[0]
            if not (ROOT / target).is_file():
                raise SystemExit(f"Broken local link in {paper}: {link}")
            link_count += 1
        report["manuscripts"].append(files)
    report["local_links_checked"] = link_count
    report["status"] = "passed"
    (output / "results.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
