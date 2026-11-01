#!/usr/bin/env python3
"""Step 69 structural regression check for the Step 68 assembly repairs.

This script only checks that the patched assembly records the corrected
mathematical interfaces; it is not a proof of the PDE theorem.
"""
import json
import os
import re
import sys

assembly_path = "Sessions/S0910A01/workspace/notes/step68_restricted_IL_canonical_assembly.md"
landscape_path = "Sessions/S0910A01/workspace/notes/step68_global_yau26_landscape.md"
out_path = "Sessions/S0910A01/workspace/data/step69_regression_repair_verify.json"

with open(assembly_path, "r", encoding="utf-8") as f:
    assembly = f.read()
with open(landscape_path, "r", encoding="utf-8") as f:
    landscape = f.read()

checks = []

def check(name, cond, detail=""):
    checks.append({"name": name, "pass": bool(cond), "detail": detail})
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f": {detail}" if detail else ""))

check(
    "no_false_sobolev_non_growth_claim",
    "Sobolev\nconstant $\\mathcal S_\\alpha$ does not grow" not in assembly
    and "sectional curvature, which are initially bounded" not in assembly,
    "removed Step68 collapse/sectional-curvature regression",
)
check(
    "records_collapse_cancelling_product",
    "Only their product is sequence-uniformly small" in assembly
    and "\\mathcal S_\\alpha(0)H_{2,\\alpha}(0)^{1/2}" in assembly,
)
check(
    "records_sobolev_volume_scaling",
    "\\operatorname{Vol}(U_\\alpha)^{-1/2}" in assembly,
)
check(
    "records_full_curvature_budget",
    "\\int F_T^2\\le C_0'A_i" in assembly
    or "\\int F_T^2\\le C A_i" in assembly,
)
check(
    "records_buffer_maximal_radius",
    "R_0\\ge L_\\eta r" in assembly and "supremum only over radii" in assembly,
)
check(
    "denies_initial_sectional_bound",
    "No pointwise sectional\ncurvature bound is assumed at time zero" in assembly,
)
check(
    "single_global_cutoff_existence",
    "single\nglobal smooth cutoff" in assembly and "T_{0,i}" in assembly,
)
check(
    "integrated_q2_before_pointwise_Y",
    "This integrated estimate is what is used near time zero" in assembly
    and "does not come\nfrom the later pointwise bound" in assembly,
)
check(
    "positive_time_slab_Y",
    "on $[\\tau_k,t]$ with $\\tau_k\\ge t/2$" in assembly
    and "\\int_{\\tau_k}^{t}\\mathcal S^2Y" in assembly,
)
check(
    "seed_is_time_integrated_J6",
    "I_0=\\int_{t/2}^tJ_6(s)ds\\le CtJ_6(0)" in assembly,
)
check(
    "uniformity_record_no_sobolev_or_sectional_uniformity",
    "neither\n  $\\mathcal S_\\alpha(0)$ nor initial sectional curvature is assumed uniformly" in assembly,
)
check(
    "landscape_negative_branch_scope",
    "defeat the negative branch" in landscape
    and "would not by itself\nrefute" in landscape,
)
check(
    "landscape_positive_proof_not_IL_required",
    "not a\nrequirement imposed by Yau26 itself" in landscape,
)

passed = sum(c["pass"] for c in checks)
print(f"\n=== Summary: {passed}/{len(checks)} passed ===")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({"step": 69, "checks": checks, "passed": passed, "total": len(checks)}, f, indent=2)
print(f"Wrote {out_path}")

sys.exit(0 if passed == len(checks) else 1)
