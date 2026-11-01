"""
Step 52: Independent verification of A03's flat T4 falsification
and DeTurck pullback issue for the normalized cutoff flow.

Mathematical target:
  Flow: dt g = -2 chi^2 (Ric + g)
  Chi = (1 + cos x1)/2  on flat T^4 with period 2pi
  a = chi^2

Questions:
  1. Does the cutoff Hessian create curvature from flat initial data?
  2. What is the leading-order L^2 curvature energy?
  3. Is the DeTurck pullback compatible with fixed cutoff?
"""
import numpy as np
from fractions import Fraction
import json

results = {}

# === 1. Flat T4 curvature creation ===

# chi = (1 + cos x1)/2,  a = chi^2 = (1 + cos x1)^2/4
# Compute Hess(a) on flat T4 (only x1 dependence)

# a(x1) = (1 + cos x1)^2 / 4
# a' = -(1 + cos x1) sin x1 / 2
# a'' = (-cos x1(1+cos x1) + sin^2 x1) / 2
#      = (-cos x1 - cos^2 x1 + sin^2 x1) / 2
#      = (-cos x1 - cos 2x1) / 2

# Hess(a) has only (1,1) component = a''(x1)
# All other components vanish (a depends only on x1, flat metric)

# Variation of Rm from dt g = -2a g (since Ric=0 at t=0):
# dt R_{ijkl} = (g KN Hess(a))_{ijkl}
# where (h KN k)_{ijkl} = h_{ik}k_{jl} + h_{jl}k_{ik} - h_{il}k_{jk} - h_{jk}k_{il}

# For g KN Hess(a) with Hess(a)_{jl} = H delta_{j1} delta_{l1}:
# Nonzero components: R_{1m1m} = H for m=2,3,4
# Plus symmetry-related components

# |g KN Hess(a)|^2 in the curvature tensor norm convention:
# Using R_{ijkl} with full symmetries, independent components are R_{1m1m} = H
# for m=2,3,4. In the standard norm:
# |Rm|^2 = sum over independent bivector pairs = 2 sum_{i<j,k<l} R_{ijkl}^2
#         (with the factor depending on convention)

# For the KN product of g with a rank-1 symmetric tensor H e1 x e1:
# The curvature tensor has:
# R_{1m1m} = H for m=2,3,4 (and all symmetry-related components)
# Total norm: |Rm|^2 = 2 * sum_{m=2,3,4} H^2 = 6 H^2
# Wait - let me be more careful with conventions.

# The KN product (g owedge k)_{ijkl} = g_{ik}k_{jl} + g_{jl}k_{ik} - g_{il}k_{jk} - g_{jk}k_{il}
# For k = H e1⊗e1:
# (g owedge k)_{1m1m} = g_{11}k_{mm} + g_{mm}k_{11} - g_{1m}k_{m1} - g_{m1}k_{1m}
# = 0 + H - 0 - 0 = H  for m≠1
# (g owedge k)_{1m1m} = 1·0 + 1·H - 0 - 0 = H  [g_{11}=1, k_{mm}=0, g_{mm}=1, k_{11}=H]

# The norm of a curvature tensor R:
# |R|^2 = sum_{i,j,k,l} R_{ijkl}^2  (all indices running)
# With the symmetries R_{ijkl} = R_{klij} = -R_{jikl} = -R_{ijlk},
# the nonzero terms for our tensor:
# R_{1m1m} = H, R_{m1m1} = H, R_{1mm1} = -H, R_{m11m} = -H
# For each m in {2,3,4}: 4 terms each = H^2, total per m: 4H^2
# Total: 3 * 4H^2 = 12H^2

# So |g owedge Hess(a)|^2 = 12 (a''(x1))^2

# This matches A03's claim.
results["norm_formula"] = "|g owedge Hess(a)|^2 = 12 (a''(x1))^2"

# Now integrate over T4 (period 2pi in each coordinate, 4 coordinates):
# int_{T4} 12 (a'')^2 dV = 12 * (2pi)^3 * int_0^{2pi} (a'')^2 dx1

# a'' = -(cos x1 + cos 2x1)/2
# (a'')^2 = (cos x1 + cos 2x1)^2 / 4
# = (cos^2 x1 + 2 cos x1 cos 2x1 + cos^2 2x1) / 4

# Integrals over [0, 2pi]:
# int cos^2 x dx = pi
# int 2 cos x cos 2x dx = int (cos(-x) + cos(3x)) dx = 0
# int cos^2 2x dx = pi

# So int_0^{2pi} (a'')^2 dx = (pi + 0 + pi)/4 = pi/2

integral_app_sq = np.pi / 2  # int_0^{2pi} (a'')^2 dx1
vol_T3 = (2*np.pi)**3  # volume of the remaining 3 coordinates

leading_coefficient = 12 * vol_T3 * integral_app_sq
# = 12 * 8pi^3 * pi/2 = 48 pi^4

results["int_dtRm_squared"] = {
    "formula": "12 * (2pi)^3 * pi/2 = 48 pi^4",
    "numerical": 48 * np.pi**4,
    "check": 12 * (2*np.pi)**3 * np.pi/2
}

print(f"Leading L^2 curvature coefficient: {leading_coefficient:.6f}")
print(f"48 pi^4 = {48 * np.pi**4:.6f}")
print(f"Match: {abs(leading_coefficient - 48*np.pi**4) < 1e-10}")

# Numerical verification by quadrature
from scipy import integrate

def integrand_app_sq(x):
    """(a'')^2 where a''(x) = -(cos x + cos 2x)/2"""
    return ((np.cos(x) + np.cos(2*x))/2)**2

I_num, err = integrate.quad(integrand_app_sq, 0, 2*np.pi)
print(f"\nNumerical int (a'')^2: {I_num:.10f}")
print(f"Exact pi/2:           {np.pi/2:.10f}")
print(f"Match: {abs(I_num - np.pi/2) < 1e-10}")

results["numerical_quadrature"] = {
    "int_app_sq": I_num,
    "exact": np.pi/2,
    "relative_error": abs(I_num - np.pi/2) / (np.pi/2)
}

# === 2. Verify this rules out homogeneous energy estimate ===

# If E(t) = int |Rm(t)|^2 dmu(t) = C t^2 + O(t^3), then
# E'(t) = 2Ct + O(t^2), and E'(t)/E(t) = 2/t + O(1)
# This diverges as t -> 0, so no estimate E'(t) <= C0 E(t) holds.
# Yang's homogeneous Moser theory requires dE/dt <= C E for the 
# critical exponent p=n/2 to close the iteration.

results["homogeneous_closure_false"] = {
    "reason": "E(t) ~ Ct^2 near t=0 gives E'/E ~ 2/t -> infinity",
    "consequence": "No homogeneous energy estimate E' <= CE at critical exponent",
    "note": "The (2p-n)=0 cancellation concerns only constant homothety, not spatial Hessian"
}

# === 3. DeTurck pullback analysis ===

# Yang/Xu solve the gauge-fixed (DeTurck) equation:
#   dt g_hat = -2a(Ric_{g_hat} + g_hat) + L_{aW} g_hat
#
# The DeTurck diffeomorphism phi_t satisfies:
#   dt phi = -(aW) o phi
#
# Pullback: g = phi^* g_hat
#   dt g = phi^*(-2a(Ric_{g_hat} + g_hat))
#        = -2 phi^*(a(Ric_{g_hat} + g_hat))
#        = -2 (a o phi^{-1} o phi)(Ric_{phi^*g_hat} + phi^*g_hat)
#        = -2 (a o phi^{-1} o phi)(Ric_g + g)
#
# Wait, that's wrong. Let me be precise.
# phi^*(f T) = (f o phi^{-1}) phi^*(T) for a scalar f and tensor T.
# No! phi^*(f T) = (f o phi) does NOT apply directly.
#
# Actually, for pullback:
# (phi^* T)(X,Y) = T(phi_* X, phi_* Y)
# So phi^*(f T)(X,Y) = (fT)(phi_* X, phi_* Y) = f(phi(p)) T(phi_* X, phi_* Y)
# Wait, f is evaluated at the point phi(p), not p. So:
# phi^*(fT) = (f o phi) · phi^*T
#
# So: dt(phi^* g_hat) = phi^*(dt g_hat + L_{aW} g_hat) - L_{aW o phi} (phi^* g_hat)
# Hmm, this is getting complicated with the exact pullback formulas.
#
# The key point is simpler. In Xu's formulation, the DeTurck equation is solved
# in a fixed coordinate system. The pullback by phi gives the geometric flow.
# For the standard Ricci flow dt g = -2 Ric, the DeTurck trick works because
# Ric is a natural tensor: phi^* Ric(g_hat) = Ric(phi^* g_hat).
# The pullback gives dt(phi^*g_hat) = -2 Ric(phi^*g_hat), which is the geometric flow.
#
# For dt g = -2a(Ric + g), the issue is the factor 'a':
# phi^*(a(Ric_ghat + ghat)) = (a o phi)(Ric_{phi^*ghat} + phi^*ghat)
# = (a o phi)(Ric_g + g)
#
# This is NOT = a(Ric_g + g) unless a o phi = a.
#
# In general, phi_t is not the identity, so a o phi_t ≠ a.
# The geometric flow one gets is:
#   dt g = -2(a o phi_t)(Ric_g + g)
# with a TRANSPORTED cutoff a_t = a o phi_t, not the fixed cutoff a.

results["deturck_pullback"] = {
    "standard_ricci_flow": "phi^* Ric(ghat) = Ric(phi^* ghat), so pullback works",
    "normalized_cutoff_flow": "phi^*(a(Ric_ghat+ghat)) = (a o phi)(Ric_g+g), NOT a(Ric_g+g)",
    "conclusion": "DeTurck pullback gives transported-cutoff flow, not fixed-cutoff flow",
    "fix": "Need coupled system: (ghat, ahat=a o phi^{-1}) with ahat transport equation"
}

# === 4. Assessment of the coupled system ===

# The correct gauge-fixed system is (A03's eq 5.2):
# dt ghat = -2 ahat (Ric_ghat + ghat) + L_{ahat W} ghat
# dt ahat = ahat W(ahat)  [transport equation]
# ghat(0) = g0, ahat(0) = a
#
# This is a coupled degenerate parabolic (metric) + first-order transport (scalar)
# system. The metric equation has Xu's degenerate principal part with coefficient
# ahat (not a fixed function!). The scalar equation has one spatial derivative
# through the DeTurck vector field W, which involves Gamma - Gamma_tilde.
#
# Key question: does Xu's fixed-point argument extend to this coupled system?
#
# The frozen problem: for fixed U (metric) and alpha (scalar coefficient):
#   dt V = (alpha + epsilon) U^{-1} * nabla^2 V + D(U,V) + B(U,nabla U) - 2 alpha V
#   dt beta = beta W(beta)
#
# The scalar equation is ODE-like once W is given (from U). The metric equation
# has the degenerate principal part with coefficient alpha (frozen from previous iterate).
#
# Plausibility assessment:
# - The scalar transport equation has no spatial derivative of beta in the principal part;
#   it's driven by the DeTurck vector field, which depends on nabla U (one derivative of metric).
# - High Sobolev estimates for the coupled system need cross-estimates:
#   ||beta||_{H^m} terms enter the metric equation through the coefficient,
#   and ||V||_{H^m} terms enter the scalar equation through W.
# - The contraction estimate needs the coupling to be subordinate to the principal part.
# - The epsilon-regularization affects only the metric principal part, not the scalar equation.
#
# Assessment: The coupled system is MORE complex than Xu's original construction,
# but the scalar equation is lower-order (first-order transport). The coupling is
# through coefficients, not through the principal part. This is the standard
# situation for coupled parabolic-transport systems, which are well-studied.
# However, the DEGENERACY of the principal part (coefficient alpha -> 0 at the
# support boundary) adds a specific difficulty that must be handled.

results["coupled_system_assessment"] = {
    "system_type": "coupled degenerate parabolic (metric) + first-order transport (scalar)",
    "metric_equation": "Xu-type with coefficient ahat (not fixed a)",
    "scalar_equation": "dt ahat = ahat W(ahat), first-order transport by DeTurck field",
    "coupling_type": "through coefficients, NOT principal parts",
    "main_difficulty": "ahat degenerates (-> 0 at support boundary) and evolves",
    "plausibility": "standard coupled parabolic-transport theory applies in principle, "
                    "but the degenerate coefficient evolution must be handled explicitly",
    "status": "NOT yet proved; requires new coupled fixed-point argument"
}

# === 5. Impact on the negative chain ===

# A1 (start): NOT proved. Fixed-cutoff geometric flow needs coupled system.
# A2 (first-exit): CANNOT be checked without A1. Even if start exists,
#     H2 preservation must handle genuine cutoff forcing (flat T4 falsifies
#     homogeneous closure).
# A3 (metric comparison): downstream of A1+A2.
# A4 (continuation): separate from start, but only useful after start exists.
# Terminal density/contradiction: downstream of everything.

results["negative_chain_status"] = {
    "A1_start": "NOT proved. Coupled system (5.2) is the correct target.",
    "A2_first_exit": "Cannot verify without A1. Genuine cutoff forcing invalidates "
                     "Step51's homogeneous L^p closure.",
    "A3_metric_comparison": "Downstream of A1+A2.",
    "A4_continuation": "Separate from start; shifted T/U/C may survive independently.",
    "terminal_density": "Downstream of all above.",
    "overall": "The negative chain breaks at A1 (start module). The coupled "
               "metric-transport system is the correct repair target. This is "
               "a non-trivial extension of Xu/Yang but structurally plausible."
}

# === 6. What the critical-product analysis tells us independently ===

# Even if start were proved, the H2 first-exit analysis faces:
# (a) The cutoff Hessian creates an additive forcing term proportional to
#     |Hess(a)|^2 ~ r_*^{-4} (from |nabla chi| ~ 1/r_*).
# (b) The critical product bar_beta = S * H_2^{1/2} is O(A^{1/2}) for
#     IL manifolds with topological parameter A.
# (c) Yang's Theorem 9.2 at p=n/2 requires bar_beta < c(n)^{-1}, which
#     is NOT universally satisfied for large A.
# (d) However, for FIXED topology (fixed A), bar_beta is a fixed constant,
#     and the metric comparison gives delta_0 ~ c/A^{1/2}.

# The critical-product computation:
# r_* = c(A/K_0)^{1/4},  K_0 = Vol^{-1} int |Rm|^2 -> 3/2 for critical IL
# Sobolev constant: S = C(4, K r_*^2) r_*^2 Vol(B_{r_*})^{-1/2}
# Local energy: int_{B_{r_*}} |Rm|^2 <= 4 K_0 Vol(B_{r_*})
# Critical product: bar_beta <= S * (4 K_0 Vol)^{1/2} = 2 K_0^{1/2} r_*^2 * C(4, K r_*^2)

# For K=1 (from Ric >= -3g), K r_*^2 = r_*^2 ~ c^2 (A/K_0)^{1/2} ~ c^2 sqrt(2A/3)
# When K r_*^2 >> 1 (large A), the Maheux-Saloff-Coste constant degrades exponentially
# But for FIXED topology, all constants are finite and the flow can still be controlled

# Metric comparison constraint:
# I(T) = int_0^T ||aE(t)||_inf dt <= (3C delta/2) theta^{2/3} r_*^2
# For I(T) <= 1/100: delta <= c/(theta^{2/3} r_*^2) ~ c/(A^{1/2})

results["critical_product_analysis"] = {
    "bar_beta_scaling": "O(A^{1/2}) for IL family with topological parameter A",
    "yang_threshold": "c(4)^{-1} is a universal constant, so threshold may be exceeded for large A",
    "fixed_topology": "All constants finite; per-manifold theorem with delta_0 ~ c/sqrt(A)",
    "metric_comparison_constraint": "delta_0 <= c/sqrt(A) from metric drift integral",
    "uniform_gap": "NO uniform gap across IL family (delta_0 -> 0 as A -> infinity)",
    "per_manifold_gap": "YES, delta_0(M) > 0 for each fixed M, if start+H2 proved"
}

# Save results
import os
_here = os.path.dirname(os.path.abspath(__file__))
_ws = os.path.dirname(_here)
output_path = os.path.join(_ws, "data", "step52_flat_T4_and_deturck_audit.json")
with open(output_path, 'w') as f:
    json.dump(results, f, indent=2, default=str)

print(f"\n=== Summary ===")
print(f"1. Flat T4 L^2 curvature creation: CONFIRMED (48 pi^4 t^2 + O(t^3))")
print(f"2. Homogeneous energy estimate at critical exponent: FALSIFIED")
print(f"3. DeTurck pullback preserves fixed cutoff: FALSE")
print(f"4. Coupled system (5.2): correct target, NOT yet proved")
print(f"5. Negative chain A1: BROKEN at start module")
print(f"6. Critical product for fixed topology: O(A^(1/2)), giving delta_0 ~ c/A^(1/2)")
print(f"\nResults saved to {output_path}")
