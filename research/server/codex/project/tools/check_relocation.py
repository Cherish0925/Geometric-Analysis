#!/usr/bin/env python3
"""Run selected finite checks without rewriting inherited proof artifacts."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "check_line1_compactified_pencil.py", "check_line1_bauer_furuta_geography.py",
    "check_line1_allowed_branch_escape.py", "check_line1_rank_one_entropy_scope.py",
    "check_line1_functional_pencil.py", "check_line1_energy_envelope_gap.py",
    "check_line1_two_chirality_topology.py", "check_line1_einstein_spectral_application.py",
    "round4_all_sign_check.py", "round11_closed_gluing_check.py",
    "round12_global_check.py", "round17_product_operator_check.py",
]

def main():
    out = ROOT / "verification/relocation-checks"
    out.mkdir(parents=True, exist_ok=False)
    scripts = [ROOT / "mathematics/current" / name for name in SCRIPTS]
    scripts.append(ROOT / "continuation/check_compact_realization_scaling.py")
    def run(path):
        if not path.is_file():
            return {"script": str(path.relative_to(ROOT)), "error": "missing selected check"}
        try:
            result = subprocess.run([sys.executable, str(path)], cwd=path.parent,
                capture_output=True, text=True, timeout=60)
            (out / (path.stem + ".log")).write_text(result.stdout + result.stderr)
            return {"script": str(path.relative_to(ROOT)), "returncode": result.returncode,
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        except subprocess.TimeoutExpired:
            return {"script": str(path.relative_to(ROOT)), "error": "60-second limit"}
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(run, scripts))
    report = {"scope": "selected exact/finite checks after relocation, not PDE/topology or full-package certification",
              "checks": results}
    (out / "results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return int(any(r.get("returncode") != 0 for r in results))

if __name__ == "__main__":
    sys.exit(main())
