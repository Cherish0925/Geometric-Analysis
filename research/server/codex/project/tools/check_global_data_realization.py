#!/usr/bin/env python3
"""Render this continuation and record its bounded finite checks, not PDE certification."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

from render_realization_continuation import render

ROOT = Path(__file__).resolve().parents[1]
NAMES = [
    "20260924_global_data_realization",
    "20260924_ricci_monodromy_realization",
    "20260924_cycle_holonomy_realization",
    "20260924_integrable_kernel_cyclic_repair",
    "20260924_harmonic_contact_milnor_matching",
]
CHECKS = ["check_cycle_holonomy.py", "check_integrable_kernel_cyclic_repair.py"]


def check(name):
    source = ROOT / "continuation" / name
    result = subprocess.run([sys.executable, str(source)], cwd=ROOT,
                            text=True, capture_output=True, check=True)
    return {"source": str(source.relative_to(ROOT)),
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "exit_code": result.returncode,
            "output": result.stdout, "stderr": result.stderr}


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as pool:
        documents = list(pool.map(render, NAMES))
        checks = list(pool.map(check, CHECKS))
    record = {"scope": "Typesetting and explicitly bounded algebra tests; not certification of nonlinear, global or classical-input arguments.",
              "documents": documents, "finite_checks": checks}
    path = ROOT / "verification" / "20260924_global_data_checks.json"
    path.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, indent=2))
