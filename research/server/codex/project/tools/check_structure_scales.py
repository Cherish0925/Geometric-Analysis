#!/usr/bin/env python3
"""Render the new proofs and run only their stated finite algebra tests."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path

from render_realization_continuation import render
from check_global_data_realization import check

ROOT = Path(__file__).resolve().parents[1]
NAMES = [
    "20260924_global_structure_and_scales",
    "20260924_thin_monodromy_alternative",
    "20260924_nonlinear_slow_moduli",
    "20260924_moduli_energy_gauge",
    "20260924_harmonic_zero_scale",
]
CHECKS = ["check_thin_monodromy.py", "check_nonlinear_slow_moduli.py",
          "check_moduli_energy_gauge.py"]

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as pool:
        documents = list(pool.map(render, NAMES))
        checks = list(pool.map(check, CHECKS))
    record = {
        "scope": "Typesetting and bounded exact algebra; no automatic certification of global topology, elliptic estimates, priority, or Yau26.",
        "documents": documents,
        "finite_checks": checks,
    }
    target = ROOT / "verification" / "20260924_structure_scales_checks.json"
    target.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, indent=2))
