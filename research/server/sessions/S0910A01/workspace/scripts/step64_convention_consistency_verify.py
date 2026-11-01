#!/usr/bin/env python3
"""Structural verification for step64_convention_consistency_sweep.md and patched Step63."""
import json, sys
from pathlib import Path

NOTE64 = Path("Sessions/S0910A01/workspace/notes/step64_convention_consistency_sweep.md")
NOTE63 = Path("Sessions/S0910A01/workspace/notes/step63_curvature_variation_index_proof.md")
STEP58 = Path("Sessions/S0910A01/workspace/notes/step58_all_order_continuation_proof.md")
texts = {"64": NOTE64.read_text(), "63": NOTE63.read_text(), "58": STEP58.read_text()}
checks = []

def check(name, cond):
    checks.append({"name": name, "passed": bool(cond)})

# Step64 core convention
check("canonical_t_minus_g", "T=\\operatorname{Rm}-G" in texts["64"])
check("ric_g_negative", "g^{il}G_{ijkl}=-g_{jk}" in texts["64"])
check("ric_t_equals_e", "\\operatorname{Ric}(T)=\\operatorname{Ric}+g=E" in texts["64"])
check("legacy_reflection_conditional", "G_{old}=-G" in texts["64"] and "specific universal-shift definition" in texts["64"])
check("aux_properties_not_unique", "would not follow from the two properties" in texts["64"] and "Ricci-free" in texts["64"])
check("operator_norm_choice", "operator-normalized curvature norm" in texts["64"] and "one quarter" in texts["64"])
check("full_contraction_alternative", "2n/(n-1)" in texts["64"])
check("canonical_cross_term_minus", "-2\\langle\\operatorname{Rm},G\\rangle" in texts["64"])
check("correct_dt_g", "\\partial_tG=-\\frac{2a}{n-1}(E\\owedge g)" in texts["64"])
check("pure_scaling_repair", "\\partial_tG=-4G" in texts["64"] and "\\partial_tT=-2\\operatorname{Rm}+4G=-2T+2G" in texts["64"])
check("energy_survival_statement", "bounded by `C a F_T^2`" in texts["64"] and "C a F_T^3" in texts["64"])
check("sole_remaining_existence", "per-datum" in texts["64"] and "existence" in texts["64"] and "epsilon,nu -> 0" in texts["64"])

# Patched Step63 should not contain the old PASS table for T=-2T.
check("step63_withdraws_old_homogeneous", "false homogeneous line" in texts["63"] and "no role" in texts["63"])
check("step63_operator_norm", "operator-normalized curvature norm" in texts["63"] and "n/(2(n-1))" in texts["63"])
check("step63_no_old_pass_table", "| $\\partial_t T_{ijkl}$ | $-2T_{ijkl}$" not in texts["63"])

# Step58 annotation and schematic zero-order wording
check("step58_stationarity_annotated", "Step 64 sweep note" in texts["58"] and "self-referential" in texts["58"])
check("step58_linear_term_schematic", "universal zero-order reaction" in texts["58"] and "F_T\\ge1" in texts["58"])

passed = sum(c["passed"] for c in checks)
for c in checks:
    print(("[PASS]" if c["passed"] else "[FAIL]"), c["name"])
print(f"\n=== Summary: {passed}/{len(checks)} passed ===")

out = Path("Sessions/S0910A01/workspace/data/step64_convention_consistency_verify.json")
out.write_text(json.dumps({"checks": checks, "passed": passed, "total": len(checks)}, indent=2))
print(f"Wrote {out}")
sys.exit(0 if passed == len(checks) else 1)
