#!/usr/bin/env python3
"""Structural verification of step65_per_datum_existence_theorem.md."""
import json, re, sys

NOTE = "Sessions/S0910A01/workspace/notes/step65_per_datum_existence_theorem.md"
OUT  = "Sessions/S0910A01/workspace/data/step65_per_datum_existence_verify.json"

with open(NOTE) as f:
    text = f.read()

checks = []

def check(name, cond):
    checks.append({"name": name, "pass": bool(cond)})

# 1. Convention page present
check("canonical_convention_stated",
      "T=\\operatorname{Rm}-G" in text and "\\operatorname{Ric}(G)=-g" in text)

# 2. General sigma
check("sigma_general",
      "\\sigma\\in\\mathbb R" in text or "sigma\\in\\mathbb R" in text)

# 3. Geometric equation with sigma
check("geometric_eq_sigma",
      "\\operatorname{Ric}_g-\\sigma g" in text)

# 4. Doubly regularized system present
check("doubly_regularized_system",
      "(\\beta^2+\\varepsilon)" in text and "\\nu\\bar\\Delta\\beta" in text)

# 5. Maximum principle for beta
check("beta_max_principle",
      "0\\le\\beta(t)\\le 1" in text or "0\\le\\beta(t)\\le1" in text)

# 6. Principal symbol diagonal
check("principal_symbol_diagonal",
      "diagonal" in text.lower() and "\\sigma_{\\rm princ}" in text)

# 7. Strong parabolicity with named constant
check("strong_parabolicity",
      "\\min(\\varepsilon\\lambda" in text and "Legendre" in text)

# 8. Named theorem stated
check("named_theorem_A",
      "Theorem A" in text and "strongly parabolic" in text)

# 9. Hypothesis verification checklist
check("hypothesis_verification",
      text.count("$\\checkmark$") >= 4 or text.count("checkmark") >= 4)

# 10. Tame hierarchy referenced
check("tame_hierarchy",
      "C_{m,R,|\\sigma|}" in text and "independent of" in text.lower())

# 11. Lie term corrected weight
check("lie_term_beta2_not_beta4",
      "\\beta^2/(\\beta^2+\\varepsilon)\\le1" in text or
      "\\frac{\\beta^2}{\\beta^2+\\varepsilon}" in text)

# 12. Transport coupling uses beta4
check("transport_coupling_beta4",
      "\\beta^4/(\\beta^2+\\varepsilon)" in text)

# 13. All-order continuation argument
check("all_order_continuation",
      "all $H^m$ norms stay bounded" in text or
      "all $H^m$ norms" in text or
      "All-order continuation" in text)

# 14. Common time T0 independent of epsilon,nu
check("T0_independent",
      "T_0=T_0(g_0,\\chi,\\bar g,\\sigma,n)" in text)

# 15. Smooth limit by Arzela-Ascoli
check("smooth_limit",
      "Arzel" in text and "diagonal" in text.lower())

# 16. Regularization residual vanishes
check("residual_vanishes",
      "\\varepsilon_\\ell" in text and "\\to0" in text)

# 17. Pullback recovers geometric flow
check("pullback",
      "\\varphi_t^*G" in text or "g(t)=\\varphi_t^*G(t)" in text)

# 18. Theorem statement present
check("theorem_statement",
      "Per-datum existence" in text and "Theorem" in text)

# 19. Three levels of uniformity
check("three_uniformity_levels",
      "Level 1" in text and "Level 2" in text and "Level 3" in text)

# 20. No standard theorem for degenerate system
check("no_degenerate_citation",
      "No standard parabolic theorem is cited for the exact" in text or
      "no standard parabolic theorem" in text.lower())

# 21. Uniqueness not claimed for degenerate limit
check("uniqueness_softened",
      "subsequential compactness" in text or
      "need not be the unique limit" in text)

# 22. Endpoint closure handled
check("endpoint_closure",
      "closed interval" in text and "restarting" in text)

# 23. No IL dependence in construction
check("no_IL_dependence",
      "no Ricci pinching" in text.lower() or
      "uses no Ricci pinching" in text)

# 24. Sign general scope
check("sign_general_scope",
      "\\sigma=-1" in text and "\\sigma=1" in text and "\\sigma=0" in text)

passed = sum(1 for c in checks if c["pass"])
total = len(checks)
for c in checks:
    tag = "PASS" if c["pass"] else "FAIL"
    print(f"[{tag}] {c['name']}")
print(f"\n=== Summary: {passed}/{total} passed ===")

with open(OUT, "w") as f:
    json.dump({"checks": checks, "passed": passed, "total": total}, f, indent=2)
print(f"Wrote {OUT}")
sys.exit(0 if passed == total else 1)
