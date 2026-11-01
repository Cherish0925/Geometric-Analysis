#!/usr/bin/env python3
"""Structural verification of step63_curvature_variation_index_proof.md."""
import json, re, sys

NOTE = "Sessions/S0910A01/workspace/notes/step63_curvature_variation_index_proof.md"
with open(NOTE) as f:
    text = f.read()

checks = []

def check(name, condition):
    checks.append({"name": name, "passed": bool(condition)})

# 1. KN product convention defined
check("kn_product_defined",
      "\\varphi \\owedge \\psi" in text and "1.0" in text)

# 2. T = Rm - G (not +G)
check("t_definition_minus_g",
      "T_{ijkl} = R_{ijkl} - G_{ijkl}" in text)

# 3. Ric(G) = -g stated
check("ric_g_negative",
      "\\operatorname{Ric}(G) = -g" in text)

# 4. Ric(T) = E via subtraction
check("ric_t_equals_e",
      "\\operatorname{Ric}(T) = \\operatorname{Ric} - (-g) = E" in text)

# 5. Pure scaling lemma for all-lower Riemann
check("pure_scaling_riemann_lemma",
      "\\partial_t R_{ijkl} = -2R_{ijkl}" in text)

# 6. Curvature variation formula (3.11)
check("curvature_variation_311",
      "a\\Delta_L R_{ijkl}" in text and "(\\nabla^2 a) * E" in text)

# 7. Conformal Hessian coefficient is -1 (not -1/2)
check("conformal_hessian_coefficient",
      "-((\\nabla^2 a) \\owedge g)" in text and "-\\frac{1}{2}" not in text.split("3.8")[0].split("3.7")[-1] if "3.7" in text and "3.8" in text else False)

# 8. Ricci-part Hessian signs corrected
check("ricci_hessian_signs",
      "-(\\nabla_i\\nabla_k a)R_{lj}" in text)

# 9. Conf Hessian has four terms
conf_section = ""
if "4.3" in text:
    idx = text.index("4.3")
    conf_section = text[idx-200:idx+200]
check("conf_hessian_four_terms",
      "+ (\\nabla_i\\nabla_l a)g_{jk}" in conf_section or "+ (\\nabla_i\\nabla_l a)g_{jk}" in text)

# 10. Lemma 4.1 derivative structure bound
check("lemma_41_derivative_bound",
      "|\\nabla B| \\le C F_T\\,|\\nabla\\operatorname{Rm}|" in text
      or "|\\nabla B| \\le CF_T|\\nabla\\operatorname{Rm}|" in text)

# 11. Signed IBP with cutoff vanishing
check("signed_ibp_cutoff_vanishing",
      "vanishes identically" in text and "supp" in text and "d\\eta" in text)

# 12. Young absorption with |nabla a|^2/a
check("young_absorption",
      "|\\nabla a|^2/a" in text and "\\varepsilon'' D_2" in text)

# 13. H2 inequality with metric drift
check("h2_inequality_metric_drift",
      "C_V\\|aE\\|_\\infty H" in text and "8.2" in text)

# 14. Sobolev transport A = e^{8V_*}
check("sobolev_transport_explicit",
      "A = e^{8V_*}" in text)

# 15. Corrected pure-scaling section present; old homogeneous T law withdrawn
check("corrected_pure_scaling_section",
      "Pure-scaling checks" in text and "partial_tG_{ijkl}" in text and "not homogeneous" in text)
check("old_homogeneous_t_withdrawn",
      "false homogeneous line" in text and "no role" in text)

# 16. Operator-normalized curvature norm recorded
check("operator_normalized_norm",
      "operator-normalized curvature norm" in text and "n/(2(n-1))" in text)

# 17. Scope statement
check("scope_statement",
      "restricted" in text and "Ishida" in text and "four-dimensional" in text)

# 18. Per-datum existence noted as remaining
check("per_datum_existence_remaining",
      "Per-datum existence" in text and "sole remaining" in text.lower())

# 19. Bianchi inequality cited
check("bianchi_inequality",
      "|\\nabla E| = |\\nabla\\operatorname{Ric}| \\le C|\\nabla\\operatorname{Rm}|" in text
      or "|\\nabla\\operatorname{Ric}| \\le C|\\nabla\\operatorname{Rm}|" in text)

# 20. Volume form variation
check("volume_form_variation",
      "\\partial_t(d\\mu) = -a\\,\\tau\\,d\\mu" in text)

# Report
passed = sum(1 for c in checks if c["passed"])
total = len(checks)
for c in checks:
    status = "[PASS]" if c["passed"] else "[FAIL]"
    print(f"{status} {c['name']}")
print(f"\n=== Summary: {passed}/{total} passed ===")

OUT = "Sessions/S0910A01/workspace/data/step63_curvature_variation_verify.json"
with open(OUT, "w") as f:
    json.dump({"checks": checks, "passed": passed, "total": total}, f, indent=2)
print(f"Wrote {OUT}")
sys.exit(0 if passed == total else 1)
