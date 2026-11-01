#!/usr/bin/env python3
"""Step 71 bounded regression-repair checks.

This script is not a proof checker.  It guards against the concrete
regressions identified after Step 70:
  * defect Moser must keep Step 62 weights and time-integrated arithmetic;
  * selected-support Euler bound must use Noether as an upper bound on c2;
  * route records must not rely on the superseded sup-time/plateau-only story.
"""
import json
import sys
from pathlib import Path

ROOT = Path("Sessions/S0910A01/workspace")
defect_path = ROOT / "notes/step70_defect_moser_real_exponent.md"
support_path = ROOT / "notes/step70_selected_support_lemma.md"
assembly_path = ROOT / "notes/step68_restricted_IL_canonical_assembly.md"
out_path = ROOT / "data/step71_regression_repairs_verify.json"

defect = defect_path.read_text()
support = support_path.read_text()
assembly = assembly_path.read_text()

checks = []
def check(name, cond, detail=""):
    checks.append({"name": name, "pass": bool(cond), "detail": detail})
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f": {detail}" if detail else ""))

# Defect Moser repairs.
check("defect_uses_step62_J_weight", "a^{p-2}s_\\varepsilon^{p/2}" in defect,
      "J_p retains a^(p-2), not fixed a^2")
check("defect_uses_step62_z_weight", "a^{(p-1)/2}s_\\varepsilon^{p/4}" in defect,
      "Sobolev variable retains a^((p-1)/2)")
check("defect_large_p_controls_aE_transition", "transition region" in defect and "a|E|" in defect,
      "large-p limit sees aE on 0<a<1")
check("defect_distinguishes_radial_and_sobolev", "Sobolev-gradient energy is not the radial dissipation alone" in defect,
      "Q_p not confused with full Sobolev gradient")
check("defect_three_factor_identity_step62", "(aF^3)^{1/3}" in defect and "a^{p-2}" in defect and "z_{p,\\varepsilon}^{4/3}" in defect,
      "three-factor identity matches Step62 weights")
check("defect_no_sup_time_route", "sup-time" not in defect.lower(),
      "sup-time recurrence removed")
check("defect_retains_Lk_three_halves", "L_j^{3/2}" in defect and "t^{-1/2}" in defect,
      "Moser product retains L_k^(3/2)")
check("defect_integrated_seed", "I_0:=\\int_{t/2}^{t}J_6" in defect and "CtJ_6(0)" in defect,
      "time-integrated seed used")
check("defect_final_endpoint", "\\left({r^2\\over t}\\right)^{1/3}" in defect,
      "final endpoint exponent restored by substituting seed")

# Selected-support repairs.
check("support_complex_hypothesis_explicit", "minimal complex surface of general type" in support and "not an assertion for arbitrary symplectic" in support,
      "Noether argument scoped to complex IL blocks")
check("support_noether_upper_c2", "c_2(X_j)\\le12(1+p_g(X_j))-K_j^2" in support and "\\le5K_j^2+36" in support,
      "Noether gives c2 <= 5K^2+36")
check("support_wrong_noether_removed", "c_1^2\\le5c_2-36" not in support,
      "old lower-bound implication removed")
check("support_volume_before_qOA", support.find("\\operatorname{Vol}(M_i)\n\\le\\frac{4\\pi^2A_i") < support.find("0\\le q_i\\le J_i"),
      "volume upper bound obtained before using q_i=O(A_i)")
check("support_no_duplicate_budget", support.count("Concluding the curvature budget") == 1,
      "duplicate old budget block removed")
check("support_shifted_budget", "\\int F_T^2" in support and "C_0'A_i" in support,
      "shifted curvature budget retained")

# Assembly pointer repairs.
check("assembly_mentions_step62_weights", "J_p=\\int\\eta^2a^{p-2}|E|^p" in assembly and "aE" in assembly,
      "assembly records corrected Moser hierarchy")
check("assembly_mentions_Lk_factor", "L_k^{3/2}" in assembly and "t^{-1/2}I_0^{1/6}" in assembly,
      "assembly records corrected time arithmetic")
check("assembly_not_sup_time", "sup-time" not in assembly.lower(),
      "assembly does not inherit superseded sup-time route")

n_pass = sum(c["pass"] for c in checks)
n_total = len(checks)
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps({"step": 71, "checks": checks, "passed": n_pass, "total": n_total}, indent=2))
print(f"\n=== Summary: {n_pass}/{n_total} passed ===")
print(f"Wrote {out_path}")
sys.exit(0 if n_pass == n_total else 1)
