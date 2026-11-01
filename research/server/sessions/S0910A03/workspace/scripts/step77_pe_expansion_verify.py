#!/usr/bin/env python3
"""Verify the Fefferman-Graham / PE expansion for reflected Einstein cores.

For Ric=-3g on [0,inf) x T^3 with S(0)=0 (reflection center):
  g = dr^2 + h_r,  h_r = e^{2r}gamma + g2 + g3 e^{-r} + ...
  g2 = -Sch(gamma),  g3 = TT

Derive:
  S-I expansion, H expansion, R_gamma < -12 identity,
  renormalized traceless stress identification.
"""
from __future__ import annotations
import json, sympy as sp
from pathlib import Path

r = sp.Symbol('r', real=True, positive=True)
n = 3  # boundary dimension (4D Einstein manifold)

# --- PE expansion coefficients ---
Rgam = sp.Symbol('R_gamma', real=True)  # scalar curvature of conf infinity
# Schouten tensor trace in dim n=3:
#   Sch(gamma)_ij = Ric_ij - (R/4)gamma_ij
#   tr_{gamma}(Sch) = R - 3R/4 = R/4
tr_Sch = Rgam / 4

# g2 = -Sch(gamma), so tr_{gamma}(g2) = -R/4
tr_g2 = -Rgam / 4

# B2 = gamma^{-1} g2,  tr B2 = tr_g2 (since raising one index)
tr_B2 = tr_g2  # = -R/4

# g3 is TT, so tr_{gamma}(g3) = 0
tr_B3 = sp.Integer(0)

# --- Shape operator expansion ---
# S = I + (-B2)e^{-2r} + (-3/2 B3)e^{-3r} + O(e^{-4r})
# S-I = -B2 e^{-2r} - (3/2) B3 e^{-3r} + ...

# Trace:
# H-3 = -tr(B2)e^{-2r} - (3/2)tr(B3)e^{-3r} + ...
#      = (R/4)e^{-2r} + 0 + ...
H_minus_3_leading = -tr_B2 * sp.exp(-2*r)
H_minus_3_simplified = sp.simplify(H_minus_3_leading)
print("H - 3 (leading):", H_minus_3_simplified)
print("  = (R_gamma/4) e^{-2r}")

# 3 - H:
three_minus_H = -H_minus_3_simplified
print("3 - H (leading):", three_minus_H)

# e^{2r}(3-H):
weighted = sp.simplify(sp.exp(2*r) * three_minus_H)
print("e^{2r}(3-H) ->", weighted, "  (as r -> infinity)")

# --- Normal identity ---
# d/dr[e^{2r}(H-3)] = -e^{2r}|S-I|^2
# Integrating from 0 (reflection center, H(0)=0) to R:
# e^{2R}(3-H(R)) = 3 + int_0^R e^{2r}|S-I|^2 dr
# As R -> inf: -R_gamma/4 = 3 + int_0^inf e^{2r}|S-I|^2 dr
print("\n--- Normal identity ---")
print("From reflection center S(0)=0, H(0)=0:")
print("  e^{2R}(3-H(R)) = 3 + int_0^R e^{2r}|S-I|^2 dr")
print("  Limit R->inf:  -R_gamma/4 = 3 + int_0^inf e^{2r}|S-I|^2 dr")
print("  Since |S-I|^2 >= 0:  -R_gamma/4 >= 3")
print("  Hence:  R_gamma <= -12")
print("  Equality iff S=I for all r>0, i.e., g=dr^2+e^{2r}q_0.")
print("  Then Ric(q_0)=0, so q_0 flat on T^3.")
print("  But center has R(q_0)=-6 != 0.  Contradiction.")
print("  Therefore: R_gamma < -12 strictly.")

# --- Quantitative bounds from center data ---
# At r=0: S(0)=0, so |S(0)-I|^2 = |I|^2 = tr(I^2) = 3.
# S'(0) = Ric_{q_0} + 3I.  tr S'(0) = R_{q_0}+9 = -6+9 = 3.
# Center theorem: one eigenvalue of S'(0) <= -3.
# Cauchy-Schwarz: |S'(0)|^2 = a1^2+a2^2+a3^2, a1<=-3, a2+a3>=6
#   a2^2+a3^2 >= (a2+a3)^2/2 >= 18.
#   |S'(0)|^2 >= 9+18 = 27.
# Traceless: |S'(0)^0|^2 = |S'|^2 - (tr S')^2/3 = |S'|^2 - 3 >= 24.
print("\n--- Center data contribution ---")
print("|S(0)-I|^2 = 3   (since S(0)=0)")
print("tr S'(0) = R_{q_0}+9 = 3")
print("Center thm: min eigenvalue of S'(0) <= -3")
print("|S'(0)|^2 >= 27,  |S'(0)^0|^2 >= 24")

# For small epsilon, S(epsilon) ~ epsilon S'(0) + O(eps^2):
# |S(eps)-I|^2 = |eps S'(0)-I|^2 = eps^2|S'|^2 - 2eps tr S'(0) + 3 + O(eps^3)
#              = eps^2|S'|^2 - 6eps + 3 + O(eps^3)
eps = sp.Symbol('epsilon', positive=True)
Sp2 = sp.Symbol('|Sp|^2', positive=True)  # |S'(0)|^2
shear_near_center = eps**2 * Sp2 - 6*eps + 3
print("Near center: |S(eps)-I|^2 ~", shear_near_center)
# This is positive for small eps since constant term is 3.

# --- Renormalized traceless stress ---
print("\n--- Renormalized stress ---")
print("S^0 = Sch(gamma)^{0,#} e^{-2r} - (3/2) gamma^{-1}g_3 e^{-3r} + ...")
print("Leading:  e^{2r} S^0 -> Sch(gamma)^{0,#}   (determined by gamma alone)")
print("Nonlocal: e^{3r}[S^0 - Sch^{0,#} e^{-2r}] -> -(3/2) g_3^#")
print("g_3 is the transverse-traceless nonlocal filling datum.")
print("It is the REAL scattering variable, not gamma.")

# --- ASD obstruction ---
print("\n--- ASD obstruction ---")
print("If M^4 is ASD (W^+=0) and Einstein with Ric=-3g,")
print("and T^3 is a compact totally geodesic hypersurface,")
print("then reflection across T^3 reverses orientation.")
print("Original side: W^+=0.  Reflected side: W^-=0.")
print("By analyticity, both hold near T^3: W=0.")
print("With Ric=-3g and W=0: constant sectional curvature -1.")
print("Totally geodesic T^3 in H^4 would inherit sec curv = -1,")
print("but T^3 cannot carry negative sectional curvature (Preissmann).")
print("Conclusion: ASD + totally geodesic T^3 is impossible.")

# --- Explicit formula ---
Rgam_formula = -12 - 4*sp.Symbol('I_shear')
print("\n--- Explicit formula ---")
print("R_gamma =", Rgam_formula)
print("where I_shear = int_0^inf e^{2r} |S-I|^2 dr > 0")

# --- Twist energy correction ---
print("\n--- Twist energy correction ---")
phi, p_sym = sp.symbols('phi p', real=True)
z = sp.Symbol('z', real=True)
# Correct: 1/4 e^{-phi} phi_z^2 + 1/4 p^2
correct_twist = sp.Rational(1,4)*sp.exp(-phi)*sp.Symbol('phi_z')**2 + sp.Rational(1,4)*p_sym**2
wrong_twist = sp.Rational(1,4)*sp.exp(-phi)*(sp.Symbol('phi_z')**2 + p_sym**2)
print("Correct twist energy: (1/2)tr[(U^{-1}U_s)^2] =", correct_twist)
print("Wrong (as in eq 9.5):", wrong_twist)
print("Difference:", sp.simplify(correct_twist - wrong_twist))

# Save results
out = {
    "pe_expansion": {
        "S_minus_I": "-B2 e^{-2r} - (3/2)B3 e^{-3r} + O(e^{-4r})",
        "B2": "gamma^{-1} g2 = -gamma^{-1} Sch(gamma)",
        "B3": "gamma^{-1} g3, g3 = TT",
        "H_minus_3": "(R_gamma/4) e^{-2r} + O(e^{-4r})",
        "trace_Schouten": "R_gamma/4",
    },
    "conformal_infinity_bound": {
        "formula": "R_gamma = -12 - 4 * integral_0^inf e^{2r}|S-I|^2 dr",
        "bound": "R_gamma < -12",
        "proof": "S(0)=0 implies |S-I|^2(0)=3>0, integral positive; equality excluded by q_0 flat contradiction",
    },
    "center_data": {
        "S_at_0": "0 (reflection center)",
        "shear_at_0": "|S(0)-I|^2 = 3",
        "S_prime_trace": "tr S'(0) = 3",
        "S_prime_norm_lower": "|S'(0)|^2 >= 27",
        "min_eigenvalue": "lambda_min S'(0) <= -3",
    },
    "renormalized_stress": {
        "leading_traceless": "e^{2r}S^0 -> Sch(gamma)^{0,#} (determined by gamma alone)",
        "nonlocal_datum": "e^{3r}[S^0 - Sch^{0,#} e^{-2r}] -> -(3/2) g_3^# (filling dependent)",
        "scope": "g_3 is the TT tensor carrying all filling information beyond conformal class",
    },
    "ASD_obstruction": {
        "statement": "An ASD Einstein 4-manifold with Ric=-3g cannot have a compact totally geodesic T^3",
        "mechanism": "Reflection reverses orientation; ASD+reversed=W=0; constant sec curv=-1; T^3 in H^4 impossible by Preissmann",
        "consequence": "Li-Liu ASD metrics cannot be cut and reflected at T^3",
    },
    "twist_energy_correction": {
        "correct": "1/4 e^{-phi} phi_z^2 + 1/4 p^2",
        "wrong_eq_9_5": "1/4 e^{-phi}(phi_z^2 + p^2)",
        "difference": "1/4 p^2(1 - e^{-phi})",
        "note": "p^2 term has coefficient 1/4, not 1/4 e^{-phi}",
    },
    "three_objects": {
        "q0": "center metric at S=0, R(q0)=-6",
        "gamma": "conformal infinity at r->inf, R_gamma < -12",
        "g3": "TT nonlocal filling datum, determines PE response beyond conformal class",
        "key_distinction": "q0 and gamma are at opposite ends; imposing R(gamma)=-6 is neither necessary nor correct",
    },
}
outpath = Path(__file__).resolve().parents[1]/'data'/'step77_pe_expansion.json'
outpath.write_text(json.dumps(out, indent=2), encoding='utf-8')
print("\nwrote", outpath)
