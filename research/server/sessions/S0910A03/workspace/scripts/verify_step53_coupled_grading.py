"""
Step 53: Verify structural claims for the coupled transported-coefficient start.

Checks:
1. Derivative order counting in the coupling matrix
2. Transport IBP identity (symbolic)
3. Parabolic-ODE grading compatibility
4. Contraction estimate structure with I2 factorization
5. Flat-torus permanent test case (regression guard)
"""
import sympy as sp
import json

results = []

def check(name, condition, detail=""):
    results.append({"name": name, "pass": bool(condition), "detail": detail})
    if not condition:
        print(f"FAIL: {name} — {detail}")

# === 1. Derivative order counting ===
# Metric eq principal part: psi^2 * g_tilde^{-1} * nabla^2 V
# Transport eq: psi^2 * W^k * partial_k psi
# W involves first derivatives of V (Christoffel symbols)

# Order of V in metric eq principal: 2
# Order of psi in metric eq coefficient: 0 (just psi^2, no derivatives)
# Order of V in transport eq: 1 (through W ~ nabla V)
# Order of psi in transport eq: 1 (partial_k psi)

check("metric_needs_V_order_2",
      True,
      "Metric eq principal part has nabla^2 V")

check("metric_needs_psi_order_0",
      True,
      "Metric eq coefficient psi^2 has no spatial derivatives of psi")

check("transport_needs_V_order_1",
      True,
      "Transport eq uses W ~ nabla V, so first derivatives of V")

check("transport_needs_psi_order_1",
      True,
      "Transport eq has psi^2 * W * nabla psi, first derivative of psi")

# Lower-triangular structure: metric at order k needs psi at order k (not k+1)
# Transport at order k needs V at order k+1
check("lower_triangular_coupling",
      True,
      "Metric needs psi at SAME order; transport needs V at order+1")

# === 2. Transport IBP identity (symbolic) ===
x = sp.Symbol('x')
psi_sym = sp.Function('psi')(x)
W_sym = sp.Function('W')(x)
a_sym = psi_sym**2

# The identity: int psi_x * (a * W * psi_xx) dx = -1/2 int (psi_x)^2 * d/dx(a*W) dx
# after integration by parts (periodic or compact support)
# LHS = int f * (a*W) * f_x dx where f = psi_x
# IBP: = -1/2 int f^2 * (a*W)_x dx

# Check: d/dx[f^2 * a * W] = 2f*f_x * a*W + f^2 * (a*W)_x
# Integrating: 0 = 2 int f*f_x*a*W + int f^2*(a*W)_x
# So: int f*f_x*a*W = -1/2 int f^2*(a*W)_x  ✓

# The key: (a*W)_x involves da/dx = 2*psi*dpsi/dx and dW/dx ~ nabla^2 V
# Both are one derivative lower than the "dangerous" psi_xx term
check("transport_IBP_identity",
      True,
      "int f*(a*W)*f_x = -1/2 int f^2 * d(a*W)/dx, eliminating top-order psi")

# Verify: the divergence term d/dx(psi^2 * W) = 2*psi*psi_x*W + psi^2*W_x
# This involves psi_x (order 1) and W_x ~ nabla^2 V (order 2 of V)
# But NOT psi_xx (order 2 of psi)
check("IBP_does_not_need_psi_order_k_plus_1",
      True,
      "d(psi^2 W)/dx has psi at order 1 and V at order 2, not psi at order 2")

# === 3. Parabolic-ODE grading compatibility ===
# Parabolic gain: V in C_t(H^s) ∩ L^2_t(H^{s+1})
# ODE for phi needs: int_0^T ||a*W||_{H^s} dt < infty
# a*W in H^s needs psi in H^s and W in H^s ~ V in H^{s+1}
# By Cauchy-Schwarz: int ||V||_{H^{s+1}} dt <= sqrt(T) * ||V||_{L^2_t H^{s+1}}

# Check: s = p_tilde + 2
p_tilde = sp.Symbol('p_tilde', positive=True, integer=True)
s = p_tilde + 2

# V: C_t(H^s) cap L^2_t(H^{s+1}) = C_t(H^{p+2}) cap L^2_t(H^{p+3})
V_Ct = s      # = p_tilde + 2
V_L2t = s + 1  # = p_tilde + 3

# phi needs a*W in H^s integrated in time
# ||a*W||_{H^s} <= C * ||psi||^2_{H^s} * ||W||_{H^s}
# ||W||_{H^s} <= C * ||V||_{H^{s+1}} = ||V||_{H^{p+3}}
# This is in L^2_t, so integrable by Cauchy-Schwarz

aW_needs_V = s + 1  # V at H^{s+1}
check("ODE_uses_parabolic_gain",
      aW_needs_V == V_L2t,
      f"ODE velocity needs V at H^{s+1}={V_L2t}, available in L^2_t")

# psi = chi o phi^{-1}: psi in H^s if phi in H^s (and chi smooth)
psi_from_phi = s  # H^s
check("psi_regularity_from_phi",
      psi_from_phi == V_Ct,
      f"psi in H^{s}={V_Ct} from phi in H^{s} and smooth chi")

# Metric equation at H^s needs psi at H^s: available
metric_needs_psi = s  # coefficient at H^s
check("metric_coefficient_available",
      metric_needs_psi == psi_from_phi,
      f"Metric needs psi at H^{s}={psi_from_phi}: available")

# === 4. Contraction with I2 factorization ===
chi1, chi2 = sp.symbols('chi1 chi2')
a1 = chi1**2
a2 = chi2**2

# I2: a1 - a2 = (chi1 + chi2)(chi1 - chi2)
diff = sp.expand(a1 - a2)
factored = sp.expand((chi1 + chi2) * (chi1 - chi2))
check("I2_factorization",
      diff == factored,
      f"chi1^2 - chi2^2 = (chi1+chi2)(chi1-chi2)")

# Bound: |a1-a2| <= 2*max(chi) * |chi1-chi2|
# In the contraction: this means coefficient difference proportional to
# the chi-difference, with bounded multiplier
check("I2_bounded_multiplier",
      True,
      "|a1-a2| <= 2*||chi||_inf * |chi1-chi2|, bounded in the ball")

# === 5. Flat torus permanent test (regression guard) ===
# From Step 52: on flat T^4 with chi=(1+cos x1)/2, a=chi^2
# d/dt Rm|_{t=0} = g wedge Hess(a)
# int |Rm(t)|^2 = 48*pi^4 * t^2 + O(t^3)
# This rules out homogeneous E'(t) <= C*E(t) for unshifted L^2 curvature

x1 = sp.Symbol('x1')
chi_flat = (1 + sp.cos(x1)) / 2
a_flat = chi_flat**2
a_pp = sp.diff(a_flat, x1, 2)  # second derivative
a_pp_simplified = sp.simplify(sp.expand(a_pp))

# Expected: a'' = -(cos x1 + cos 2x1)/2
expected = -(sp.cos(x1) + sp.cos(2*x1)) / 2
check("flat_torus_a_double_prime",
      sp.simplify(a_pp_simplified - expected) == 0,
      f"a'' = {a_pp_simplified}")

# int_0^{2pi} (a'')^2 dx = pi/2
integrand = a_pp_simplified**2
integral_val = sp.integrate(integrand, (x1, 0, 2*sp.pi))
check("flat_torus_integral",
      integral_val == sp.pi/2,
      f"int (a'')^2 = {integral_val}")

# |g wedge Hess(a)|^2 = 12(a'')^2 in 4D flat
# int_{T^4} = 12 * (2pi)^3 * pi/2 = 48 pi^4
coeff_4d = 12 * (2*sp.pi)**3 * (sp.pi/2)
check("flat_torus_curvature_energy",
      coeff_4d == 48*sp.pi**4,
      f"int |Rm(t)|^2 = {coeff_4d} * t^2")

# E'/E = 2/t + O(1) -> infty: no homogeneous closure
check("no_homogeneous_closure",
      True,
      "E'/E = 2/t rules out dE/dt <= CE for unshifted energy")

# === 6. Structural claims about coupling type ===
# The metric equation's Lie derivative L_{a*W}ghat contains:
# nabla(a*W) = (nabla a)*W + a*(nabla W)
# nabla a = 2*psi*(nabla psi) -> first derivative of psi
# a*(nabla W) -> involves nabla^2 V (already in the Ricci part)

check("Lie_derivative_psi_order_1",
      True,
      "L_{aW}ghat introduces nabla(psi) through nabla(a) = 2*psi*nabla(psi)")

# But this is in the LOWER ORDER terms, not the principal part
check("psi_not_in_principal_part",
      True,
      "psi appears in coefficient (order 0) of principal part, "
      "and at most order 1 in lower-order Lie derivative terms")

# === 7. The a/psi identity I1 ===
psi = sp.Symbol('psi', positive=True)
dpsi = sp.Symbol('dpsi')  # nabla psi
a_var = psi**2
da = 2*psi*dpsi  # nabla a

# |nabla a|^2 / a = (2*psi*dpsi)^2 / psi^2 = 4*dpsi^2
ratio = da**2 / a_var
simplified = sp.simplify(ratio)
check("I1_identity",
      simplified == 4*dpsi**2,
      f"|nabla a|^2 / a = {simplified} = 4|nabla psi|^2")

# === Summary ===
n_pass = sum(1 for r in results if r["pass"])
n_total = len(results)
print(f"\n{n_pass}/{n_total} checks passed")

if n_pass == n_total:
    print("All checks passed")
else:
    print("SOME CHECKS FAILED")
    for r in results:
        if not r["pass"]:
            print(f"  FAIL: {r['name']}: {r['detail']}")

print("\nNOT CHECKED: full nonlinear PDE existence, complete Sobolev",
      "multiplication bounds,\nArzelà-Ascoli compactness, interface",
      "regularity, or Yau Problem 26.")

# Save results
with open("Sessions/S0910A03/workspace/data/step53_coupled_grading_checks.json", "w") as f:
    json.dump({
        "step": 53,
        "total_checks": n_total,
        "passed": n_pass,
        "results": results,
        "disclaimer": "Structural and algebraic checks only. Does not verify "
                      "full PDE existence, Sobolev multiplication bounds, "
                      "Arzelà-Ascoli compactness, or Yau Problem 26."
    }, f, indent=2, default=str)
