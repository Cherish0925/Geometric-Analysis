#!/usr/bin/env python3
"""Run standalone bounded checks; --output must be a new result directory.

Example: python scripts/reproduce.py --output /tmp/yau26-checks-new
Exit 0: all selected checks pass; 1: mathematical/runtime check failed;
2: invalid arguments or unavailable output destination. No Session files,
external services, shell commands, or spectral frameworks are accessed.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

# Disable source-tree bytecode writes even when invoked without python -B.
sys.dont_write_bytecode = True


GROUPS = ("uniform_gap", "weyl10", "ed_ricci", "cz_spike", "four_node",
          "ot_critical", "ah_matching", "two_pole")


def write_json(path, value):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write("\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path, help="new result directory; existing paths are refused")
    parser.add_argument("--group", action="append", choices=GROUPS, help="repeat to select groups; default: all eight")
    parser.add_argument("--mutation", choices=("four-node-zero",), help="intentional failure control; must include four_node")
    args = parser.parse_args()
    selected = list(dict.fromkeys(args.group or GROUPS))
    if args.mutation and "four_node" not in selected:
        parser.error("--mutation requires the four_node group")
    try:
        args.output.mkdir(parents=True, exist_ok=False)
    except OSError as exc:
        parser.error(f"cannot create new output directory: {exc}")

    root = Path(__file__).resolve().parent
    report = {"schema": "qiushi-yau26.reproduction.v1", "status": "running",
              "started_utc": datetime.now(timezone.utc).isoformat(), "selected_groups": selected,
              "mutation": args.mutation, "versions": {"python": platform.python_version()},
              "inputs": {}, "groups": [],
              "scope": "bounded symbolic and fixture checks, not a formal proof of the research papers or a spectral tail certificate"}
    started = time.monotonic()
    try:
        import numpy as np
        import sympy as sp
        import math_checks
        import independent_checks

        report["versions"].update({"numpy": np.__version__, "sympy": sp.__version__})
        for rel in ("reproduce.py", "math_checks.py", "independent_checks.py", "source_archive.py", "data/four_node_fixture.json"):
            report["inputs"][rel] = {"sha256": hashlib.sha256((root/rel).read_bytes()).hexdigest()}
        for name in selected:
            group_started = time.monotonic()
            print(f"Checking {name}...", file=sys.stderr, flush=True)
            try:
                module = independent_checks if name in {"ot_critical", "ah_matching", "two_pole"} else math_checks
                fn = getattr(module, name)
                value = fn(mutation=args.mutation) if name == "four_node" else fn()
                value.update({"group": name, "status": "passed", "elapsed_seconds": time.monotonic()-group_started})
            except Exception as exc:
                value = {"group": name, "status": "failed", "error_type": type(exc).__name__,
                         "error": str(exc), "elapsed_seconds": time.monotonic()-group_started}
            write_json(args.output/f"{name}.json", value)
            report["groups"].append({"group": name, "status": value["status"], "result": f"{name}.json"})
        report["status"] = "passed" if all(g["status"] == "passed" for g in report["groups"]) else "failed"
    except Exception as exc:
        report.update({"status": "failed", "error_type": type(exc).__name__, "error": str(exc)})
    report["elapsed_seconds"] = time.monotonic()-started
    write_json(args.output/"manifest.json", report)
    print(json.dumps({"status": report["status"], "output": str(args.output.resolve()), "groups": report["groups"]}, ensure_ascii=False))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())
