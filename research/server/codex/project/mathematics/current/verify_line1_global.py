"""Reproduce this increment's finite checks and render its research notes.

This is artifact/finite-algebra verification, not a verifier for the cited
gauge, topology, or elliptic theorems. Run in the isolated research checkout.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys


parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parent
out = args.output.resolve()
out.mkdir(parents=True, exist_ok=False)
render = out / "render"
render.mkdir()

checks = [
    "compactified_pencil", "bauer_furuta_geography",
    "allowed_branch_escape", "rank_one_entropy_scope",
    "functional_pencil", "energy_envelope_gap",
    "two_chirality_topology", "einstein_spectral_application",
]
if (root / "check_line1_aspherical_no_bubbles.py").exists():
    checks.append("aspherical_no_bubbles")
notes = [
    "compactified_pencil", "bauer_furuta_geography",
    "allowed_branch_escape", "rank_one_entropy_scope",
    "aspherical_no_bubbles",
]
results = []
for name in checks:
    script = root / f"check_line1_{name}.py"
    result = subprocess.run([sys.executable, str(script)], cwd=root,
                            text=True, capture_output=True, timeout=120)
    (out / f"{name}.log").write_text(result.stdout + result.stderr)
    results.append({"script": script.name, "returncode": result.returncode,
                    "sha256": hashlib.sha256(script.read_bytes()).hexdigest()})
    print(f"{script.name}: exit {result.returncode}", flush=True)

missing_links = []
compiled = []
for name in notes:
    stem = f"line1_{name}"
    source = root / f"{stem}.md"
    if not source.is_file():
        raise FileNotFoundError(source)
    for target in re.findall(r"\[[^\]]*\]\(\s*([^\s)]+)\s*\)", source.read_text()):
        if not target.startswith(("http:", "https:", "#")):
            local = target.split("#", 1)[0]
            if not (root / local).exists():
                missing_links.append({"source": source.name, "target": target})
    command = ["pandoc", "--from=markdown+tex_math_single_backslash",
               "--standalone", "--metadata-file=line1_paper.yaml",
               str(source), "--output", str(root / f"{stem}.tex")]
    conversion = subprocess.run(command, cwd=root, text=True,
                                capture_output=True, timeout=120)
    (out / f"{name}.pandoc.log").write_text(conversion.stdout + conversion.stderr)
    if conversion.returncode:
        raise RuntimeError(f"Pandoc failed: {source.name}")
    for run in (1, 2):
        command = ["xelatex", "-interaction=nonstopmode", "-halt-on-error",
                   f"-output-directory={render}", str(root / f"{stem}.tex")]
        result = subprocess.run(command, cwd=root, text=True,
                                capture_output=True, timeout=120)
        (out / f"{name}.xelatex{run}.log").write_text(result.stdout + result.stderr)
        if result.returncode:
            raise RuntimeError(f"XeLaTeX failed: {stem}, run {run}")
    latex_log = (render / f"{stem}.log").read_text()
    critical = [line for line in latex_log.splitlines()
                if "Missing character:" in line or "undefined" in line.lower()]
    shutil.copyfile(render / f"{stem}.pdf", root / f"{stem}.pdf")
    info = subprocess.run(["pdfinfo", str(root / f"{stem}.pdf")],
                          text=True, capture_output=True, check=True)
    pages = int(re.search(r"^Pages:\s+(\d+)", info.stdout, re.M).group(1))
    compiled.append({"source": source.name, "pages": pages,
                     "critical_warnings": critical,
                     "overfull_boxes": latex_log.count("Overfull ")})
    print(f"{stem}: {pages} pages; critical warnings={len(critical)}", flush=True)

artifacts = {}
for name in notes:
    for extension in ("md", "tex", "pdf"):
        path = root / f"line1_{name}.{extension}"
        artifacts[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
report = {
    "baseline_commit": "4401d28",
    "scope": "Finite algebra, local proof links, compilation and artifact identity; not PDE or novelty certification.",
    "checks": results,
    "compiled": compiled,
    "missing_local_links": missing_links,
    "artifacts": artifacts,
}
(out / "results.json").write_text(json.dumps(report, indent=2) + "\n")
failed = any(item["returncode"] for item in results)
failed |= bool(missing_links) or any(item["critical_warnings"] for item in compiled)
raise SystemExit(bool(failed))
