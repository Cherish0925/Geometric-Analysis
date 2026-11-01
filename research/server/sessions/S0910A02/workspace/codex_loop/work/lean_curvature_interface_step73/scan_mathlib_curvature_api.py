#!/usr/bin/env python3
"""Reproducible source audit for curvature-related names in locked Mathlib."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from pathlib import Path


TARGETS = {
    "levi_civita": r"Levi[-_ ]?Civita|levi[-_ ]?civita|leviCivita",
    "riemann_curvature": r"Riemann(?:ian)?Curvature|riemann(?:ian)?Curvature|RiemannTensor|riemannTensor",
    "ricci": r"\bRicci\b|\bricci\b",
    "scalar_curvature": r"ScalarCurvature|scalarCurvature|scalar curvature",
    "sectional_curvature": r"SectionalCurvature|sectionalCurvature|sectional curvature",
    "christoffel": r"\bChristoffel\b|\bchristoffel\b",
    "generic_curvature": r"\bCurvature\b|\bcurvature\b",
}

REAL_API_IDENTIFIERS = [
    "Bundle.ContMDiffRiemannianMetric",
    "RiemannianBundle",
    "CovariantDerivative",
    "ContMDiffCovariantDerivative",
    "IsMetricCompatible",
    "derivMetricTensor",
    "torsion",
    "LinearMap.trace",
    "IsPosSemidef",
    "CompactSpace",
    "ConnectedSpace",
    "Boundaryless",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def matches_for(regex: re.Pattern[str], files: list[Path], root: Path) -> list[dict[str, object]]:
    hits: list[dict[str, object]] = []
    for path in files:
        for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if regex.search(line):
                hits.append({
                    "file": path.relative_to(root).as_posix(),
                    "line": number,
                    "text": line.strip(),
                })
    return hits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    project = os.environ.get("QIUSHI_PROOF_LEAN_PROJECT")
    if not project:
        raise SystemExit("QIUSHI_PROOF_LEAN_PROJECT is not set")
    project_root = Path(project).resolve()
    mathlib_root = project_root / ".lake/packages/mathlib/Mathlib"
    files = sorted(mathlib_root.rglob("*.lean"))

    pattern_results: dict[str, object] = {}
    for label, pattern in TARGETS.items():
        hits = matches_for(re.compile(pattern), files, mathlib_root)
        pattern_results[label] = {"count": len(hits), "matches": hits}

    identifier_results: dict[str, object] = {}
    for identifier in REAL_API_IDENTIFIERS:
        hits = matches_for(re.compile(re.escape(identifier)), files, mathlib_root)
        identifier_results[identifier] = {"count": len(hits), "matches": hits[:50]}

    manifest = project_root / "lake-manifest.json"
    toolchain = project_root / "lean-toolchain"
    manifest_data = json.loads(manifest.read_text(encoding="utf-8"))
    mathlib_package = next(
        package for package in manifest_data["packages"] if package["name"] == "mathlib"
    )
    result = {
        "scope": "all *.lean files under the locked Mathlib/ source tree; comments included",
        "mathlib_source_file_count": len(files),
        "project_lock": {
            "lake_manifest_sha256": sha256(manifest),
            "lean_toolchain": toolchain.read_text(encoding="utf-8").strip(),
            "lean_toolchain_sha256": sha256(toolchain),
            "mathlib_input_rev": mathlib_package.get("inputRev"),
            "mathlib_git_rev": mathlib_package.get("rev"),
        },
        "curvature_name_patterns": pattern_results,
        "available_api_identifier_occurrences": identifier_results,
        "interpretation_note": (
            "A zero pattern count is source evidence, not a proof that no semantically equivalent API "
            "can exist under an unrelated name. The companion Lean environment-name scan and "
            "declaration probe address that residual risk."
        ),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
