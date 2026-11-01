"""Reproduce the new finite checks without overwriting prior evidence."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
CHECKS = (
    "line1_variable_calibration_check.py",
    "check_line1_negative_selection.py",
    "check_line1_energy_envelope_gap.py",
    "line1_period_inertia_check.py",
)
PAPERS = (
    "line1_variable_calibration",
    "line1_variable_negative_selection",
    "line1_energy_envelope_gap",
    "line1_period_inertia",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    report = {
        "scope": "new finite algebra and manuscript hashes, not PDE or priority certification",
        "checks": [],
        "manuscripts": {},
    }
    for name in CHECKS:
        command = [sys.executable, str(ROOT / name)]
        result = subprocess.run(command, cwd=ROOT, capture_output=True,
                                text=True, timeout=120)
        (output / (name + ".log")).write_text(result.stdout + result.stderr)
        report["checks"].append({"script": name, "command": command,
                                 "returncode": result.returncode})
        if result.returncode:
            (output / "results.json").write_text(json.dumps(report, indent=2))
            raise SystemExit(f"Check failed: {name}; see {output}")
    for stem in PAPERS:
        for extension in (".md", ".tex", ".pdf"):
            path = ROOT / (stem + extension)
            if not path.is_file():
                raise SystemExit(f"Missing manuscript: {path.name}")
            report["manuscripts"][path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    report["status"] = "passed"
    (output / "results.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
