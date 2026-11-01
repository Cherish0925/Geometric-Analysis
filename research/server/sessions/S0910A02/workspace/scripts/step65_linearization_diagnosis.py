#!/usr/bin/env python3
"""Step 65: Diagnose the linearization of Ric under conformal perturbation.

The goal: understand why g_corr = t*(g_EH - (t*Lambda/8)*r^2*g_EH) has O(1) defect
when we "verified" that h = -(Lambda/8)*r^2*g satisfies Delta_L h = Lambda*g.

The resolution must be one of:
(a) The Lichnerowicz Laplacian formula I used is wrong for the conformal ansatz.
(b) The linearized Ricci is NOT simply Delta_L (there are additional terms).
(c) The relationship between h (first-order perturbation) and the conformal factor
    involves a different scaling.

Let me compute the EXACT first variation of Ric under g_s = g + s*h with h = c*r^2*g.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step65_linearization_diagnosis.json"

print("=== Linearization diagnosis ===")

r, s, a, Lam = sp.symbols('r s a Lambda', positive=True)
W = 1 - a**4/r**4

# EH metric (diagonal at evaluation point)
g00 = 1/W
g11 = r**2/4
g33 = r**2*W/4

# Perturbed metric: g_s = g_EH + s*h where h = c*r^2*g_EH
# So g_s = (1 + s*c*r^2)*g_EH
# Let phi = 1 + s*c*r^2
c = sp.symbols('c')
phi = 1 + s*c*r**2

# g_s components
gs00 = phi*g00
gs11 = phi*g11
gs33 = phi*g33
gs_diag = [gs00, gs11, gs11, gs33]

# Compute Ricci of g_s exactly
coords_labels = ['r', 't1', 't2', 't3']  # r, theta, phi, psi

# Christoffel of g_s (diagonal, r-dependent)
# Gamma^0_00 = d_r(gs00)/(2*gs00)
# Gamma^0_ii = -d_r(gs_ii)/(2*gs00)  for i=1,2,3
# Gamma^i_i0 = Gamma^i_0i = d_r(gs_ii)/(2*gs_ii)

Gam_s = {}
Gam_s[(0,0,0)] = sp.diff(gs00, r)/(2*gs00)
for i, gi in [(1, gs11), (2, gs11), (3, gs33)]:
    Gam_s[(0,i,i)] = -sp.diff(gi, r)/(2*gs00)
    Gam_s[(i,i,0)] = sp.diff(gi, r)/(2*gi)
    Gam_s[(i,0,i)] = Gam_s[(i,i,0)]

# Ricci components for diagonal metric
# Ric_00 = sum_k [d_k Gamma^k_00 - d_0 Gamma^k_0k] + sum_{k,l} [Gamma^k_kl Gamma^l_00 - Gamma^k_0l Gamma^l_0k]
# With only radial dependence:
# Ric_00 = -d_0(Gamma^0_00 + sum_i Gamma^i_i0) + Gamma^0_00*Gamma^0_00 + sum_i Gamma^i_i0*Gamma^0_00 
#         + sum_i (Gamma^0_ii*Gamma^i_00... 

# Let me compute more carefully.
# Ric_ij = d_k Gamma^k_ij - d_j Gamma^k_ik + Gamma^k_ij Gamma^l_kl... no.
# Standard: R^l_ikj = d_k Gamma^l_ij - d_j Gamma^l_ik + Gamma^l_mk Gamma^m_ij - Gamma^l_mj Gamma^m_ik
# Ric_ij = R^k_ikj = d_k Gamma^k_ij - d_j Gamma^k_ik + Gamma^k_mk Gamma^m_ij - Gamma^k_mj Gamma^m_ik

# For diagonal metric with only r-dependence, the angular Christoffels vanish at the point.
# But the r-derivatives of the angular Christoffels may contribute... 
# At theta=pi/2, phi=0, psi=0 with a diagonal metric depending only on r,
# the only nonzero Christoffels are Gamma^0_00, Gamma^0_ii, Gamma^i_i0=Gamma^i_0i.
# The angular Christoffels (Gamma^i_jk with all i,j,k != 0) vanish at this specific point
# IF the metric is exactly diagonal there and the off-diagonal terms vanish.
# For EH at theta=pi/2, this is true.

# So at the evaluation point:
# Ric_00 = d_0(Gamma^0_00) - d_0(Gamma^0_00 + sum_i Gamma^i_i0) + 
#          Gamma^0_00*Gamma^0_00 + sum_i Gamma^i_i0*Gamma^0_00 + 
#          sum_i Gamma^0_ii*Gamma^i_00... 
# Wait, I need to be more careful.

# Ric_00 = d_k Gamma^k_00 - d_0 Gamma^k_0k + Gamma^k_mk Gamma^m_00 - Gamma^k_m0 Gamma^m_0k
# First term: d_k Gamma^k_00 = d_0 Gamma^0_00 (only k=0 contributes since angular Gamma^i_00=0)
# Second term: d_0 Gamma^k_0k = d_0(Gamma^0_00 + Gamma^1_01 + Gamma^2_02 + Gamma^3_03)
# Third term: Gamma^k_mk Gamma^m_00 = Gamma^0_00*(Gamma^0_00 + Gamma^1_01 + Gamma^2_02 + Gamma^3_03)
# Fourth term: Gamma^k_m0 Gamma^m_0k = Gamma^0_00*Gamma^0_00 + sum_i Gamma^i_i0*Gamma^i_0i + sum_i Gamma^0_ii*Gamma^0_ii... no.
# Gamma^k_m0 Gamma^m_0k: for k=0,m=0: Gamma^0_00*Gamma^0_00
#   for k=i,m=0: Gamma^i_00*Gamma^0_0i = 0 (Gamma^i_00=0 for i!=0)
#   for k=0,m=i: Gamma^0_i0*Gamma^i_00 = 0
#   for k=i,m=j: Gamma^i_j0*Gamma^j_0i = sum_i (Gamma^i_i0)^2 (for j=i, Gamma^i_i0*Gamma^i_0i = (Gamma^i_i0)^2)
# So Gamma^k_m0 Gamma^m_0k = (Gamma^0_00)^2 + sum_i (Gamma^i_i0)^2

# Ric_00 = d_r(Gamma^0_00) - d_r(Gamma^0_00 + sum_i Gamma^i_i0) 
#         + Gamma^0_00*(Gamma^0_00 + sum_i Gamma^i_i0) - (Gamma^0_00)^2 - sum_i (Gamma^i_i0)^2
# = -sum_i d_r(Gamma^i_i0) + Gamma^0_00*sum_i Gamma^i_i0 - sum_i (Gamma^i_i0)^2

# Similarly for Ric_jj (j != 0):
# Ric_jj = d_k Gamma^k_jj - d_j Gamma^k_jk + Gamma^k_mk Gamma^m_jj - Gamma^k_mj Gamma^m_jk
# First: d_k Gamma^k_jj = d_0 Gamma^0_jj (angular Gamma^i_jj = 0 for i != 0 at point)
# Second: d_j Gamma^k_jk = 0 (no angular dependence at point)
# Third: Gamma^k_mk Gamma^m_jj = Gamma^0_00*Gamma^0_jj + sum_i Gamma^i_i0*Gamma^i_jj*delta... 
# For m=0: Gamma^k_0k Gamma^0_jj = (Gamma^0_00 + sum_i Gamma^i_i0)*Gamma^0_jj
# For m=i (i!=0): Gamma^k_ik Gamma^i_jj; Gamma^i_jj = 0 at point for i!=0
# So third = (Gamma^0_00 + sum_i Gamma^i_i0)*Gamma^0_jj
# Fourth: Gamma^k_mj Gamma^m_jk
# k=0,m=0: Gamma^0_0j Gamma^0_j0 = 0 (Gamma^0_0j=0 for j!=0)
# k=0,m=i: Gamma^0_ij Gamma^i_j0; Gamma^0_ij = 0 for i!=j, =Gamma^0_jj for i=j
#   -> Gamma^0_jj*Gamma^j_j0
# k=i,m=0: Gamma^i_0j Gamma^0_ji = Gamma^i_0j*Gamma^0_ji; Gamma^0_ji=0 for i!=j, so Gamma^j_0j*Gamma^0_jj
#   -> Gamma^j_j0*Gamma^0_jj  (same as above)
# k=i,m=i: Gamma^i_ij Gamma^i_ji = Gamma^i_ij*Gamma^i_ji; for i=j: Gamma^j_jj*Gamma^j_jj... but Gamma^j_jj=0
#   for i!=j: 0
# k=i,m=j: Gamma^i_jj Gamma^j_ji = 0
# So fourth = 2*Gamma^0_jj*Gamma^j_j0

# Ric_jj = d_r(Gamma^0_jj) + (Gamma^0_00 + sum_i Gamma^i_i0)*Gamma^0_jj - 2*Gamma^0_jj*Gamma^j_j0

# ============================================================
# Compute with the perturbed metric
# ============================================================

G000 = Gam_s[(0,0,0)]
Gi0_list = [Gam_s[(i,i,0)] for i in [1,2,3]]
G0ii_list = [Gam_s[(0,i,i)] for i in [1,2,3]]

Ric00 = -sum(sp.diff(Gi0_list[i], r) for i in range(3)) + G000*sum(Gi0_list) - sum(G**2 for G in Gi0_list)
Ric00 = sp.simplify(Ric00)

Ric11 = sp.diff(G0ii_list[0], r) + (G000 + sum(Gi0_list))*G0ii_list[0] - 2*G0ii_list[0]*Gi0_list[0]
Ric11 = sp.simplify(Ric11)

Ric33 = sp.diff(G0ii_list[2], r) + (G000 + sum(Gi0_list))*G0ii_list[2] - 2*G0ii_list[2]*Gi0_list[2]
Ric33 = sp.simplify(Ric33)

print("Ricci of perturbed metric g_s = (1 + s*c*r^2)*g_EH:")
print(f"  Ric_00 = {sp.simplify(Ric00)}")
print()

# Expand in s
Ric00_s = sp.series(Ric00, s, 0, 2)
Ric11_s = sp.series(Ric11, s, 0, 2)
Ric33_s = sp.series(Ric33, s, 0, 2)

print("Series expansion in s:")
print(f"  Ric_00 = {Ric00_s}")
print(f"  Ric_11 = {Ric11_s}")
print(f"  Ric_33 = {Ric33_s}")

# The first-order coefficient is the linearized Ricci applied to h = c*r^2*g
# dRic_00/ds|_{s=0} = coefficient of s^1
dRic00 = sp.diff(Ric00, s).subs(s, 0)
dRic11 = sp.diff(Ric11, s).subs(s, 0)
dRic33 = sp.diff(Ric33, s).subs(s, 0)

print()
print("Linearized Ricci dRic/ds at s=0 (applied to h = c*r^2*g):")
print(f"  dRic_00 = {sp.simplify(dRic00)}")
print(f"  dRic_11 = {sp.simplify(dRic11)}")
print(f"  dRic_33 = {sp.simplify(dRic33)}")

# Compare with Lambda*g components and with -8c*g components
print()
print("Target (Lambda*g): Lambda*g_00 =", sp.simplify(Lam*g00))
print("-8c*g (my earlier claim): -8c*g_00 =", sp.simplify(-8*c*g00))

# Check: is dRic/ds = -8c*g? 
check00 = sp.simplify(dRic00 - (-8*c*g00))
check11 = sp.simplify(dRic11 - (-8*c*g11))
check33 = sp.simplify(dRic33 - (-8*c*g33))
print()
print("Check dRic/ds = -8c*g?")
print(f"  dRic_00 - (-8c*g_00) = {check00}")
print(f"  dRic_11 - (-8c*g_11) = {check11}")
print(f"  dRic_33 - (-8c*g_33) = {check33}")

# The ANSWER to the diagnosis:
# If dRic/ds != -8c*g, then my earlier "verification" was wrong.
# The error is likely in the claim that Delta_L(c*r^2*g) = -Delta(c*r^2)*g.
# In fact, Delta_L h = -nabla^2 h + 2 Rm.h, and for h = c*r^2*g:
# -nabla^2(c*r^2*g) = -Delta(c*r^2)*g (using nabla g = 0)
# 2 Rm.(c*r^2*g) = 2*c*r^2*Rm.g = 2*c*r^2*Ric = 0 (Ricci-flat)
# So Delta_L(c*r^2*g) = -Delta(c*r^2)*g = -8c*g.
# BUT the LINEARIZED RICCI is NOT Delta_L!
# The linearized Ricci is:
# dRic_ij/ds = (1/2)*(-nabla^2 h_ij - nabla_i nabla_j tr(h) + nabla_i nabla^k h_kj + nabla_j nabla^k h_ki) + Rm terms
# = (1/2)*(Delta_L h)_ij + (1/2)*(terms involving tr(h) and div(h))
# The Lichnerowicz Delta_L is only PART of the linearized Ricci.
# The additional terms (involving tr(h) and div(h)) are NOT zero for h = c*r^2*g.

# This is the error: I conflated the Lichnerowicz Laplacian with the linearized Ricci operator.
# The correct linearized Ricci (Lichnerowicz) is:
# (D Ric)_ij[h] = (1/2)*Delta_L h_ij - (1/2)*nabla_i nabla_j tr(h) + (1/2)*(nabla_i div(h)_j + nabla_j div(h)_i)
# For h = c*r^2*g: tr(h) = 4*c*r^2, div(h)_j = nabla^k(c*r^2*g_kj) = c*2r*delta^r_j*... 
# = c*nabla_j(r^2) = 2c*r*delta_j^r (in the radial direction)
# These terms do NOT vanish.

print()
print("=== DIAGNOSIS ===")
print("The linearized Ricci is NOT just the Lichnerowicz Laplacian Delta_L.")
print("For h = c*r^2*g, the trace and divergence terms contribute:")
tr_h = 4*c*r**2
div_h_r = 2*c*r  # radial component of div(h)
print(f"  tr(h) = {tr_h}")
print(f"  div(h)_r = {div_h_r}")
print(f"  Hess(tr(h))_00 = {sp.simplify(sp.diff(tr_h, r, 2))}")
print("These terms modify the linearized equation and explain the O(1) defect.")

# The correct equation for the Biquard correction is:
# dRic[h] = Lambda*g + obstructions
# where dRic is the FULL linearized Ricci, not just Delta_L.
# The full linearized Ricci on a Ricci-flat background is:
# dRic_ij[h] = -(1/2)*nabla^2 h_ij - (1/2)*nabla_i nabla_j tr(h) + (1/2)*nabla_i div(h)_j + (1/2)*nabla_j div(h)_i + Rm_{ikjl} h^{kl}

# For h = c*r^2*g:
# nabla^2 h_ij = nabla^2(c*r^2*g_ij) = Delta(c*r^2)*g_ij = 8c*g_ij
# nabla_i nabla_j tr(h) = nabla_i nabla_j(4*c*r^2)
# div(h)_j = c*nabla_j(r^2) (using nabla g = 0)
# nabla_i div(h)_j + nabla_j div(h)_i = 2*c*nabla_i nabla_j(r^2)
# So dRic[h] = -(1/2)*8c*g_ij - (1/2)*4c*nabla_i nabla_j(r^2) + (1/2)*2c*nabla_i nabla_j(r^2) + Rm.h
# = -4c*g_ij - c*nabla_i nabla_j(r^2) + 0 (Ricci-flat, Rm.h involves Ric contraction? No!)

# WAIT: Rm_{ikjl} h^{kl} with h = c*r^2*g:
# = c*r^2*Rm_{ikjl}*g^{kl} = c*r^2*(-Ric_{ij}) = 0 (Ricci-flat, but with sign)
# Actually Rm_{ikjl}*g^{kl} = g^{kl} R_{ikjl} = R_{ij} (Ricci contraction) = 0.
# So the Rm term IS zero.

# dRic[h] = -4c*g_ij - c*nabla_i nabla_j(r^2)
# For this to equal Lambda*g_ij, we need:
# -4c*g_ij - c*nabla_i nabla_j(r^2) = Lambda*g_ij
# But nabla_i nabla_j(r^2) is NOT proportional to g_ij in general!
# nabla_0 nabla_0(r^2) = d^2(r^2)/dr^2 - Gamma^0_00*d(r^2)/dr = 2 - Gamma^0_00*2r
# nabla_i nabla_j(r^2) for i=j!=0: -Gamma^0_ii*2r
# These are different from the (0,0) component.
# So dRic[h] is NOT proportional to g, confirming that h = c*r^2*g is NOT
# a solution of the linearized Einstein equation.

print()
print("CONCLUSION: h = c*r^2*g does NOT solve the linearized Einstein equation.")
print("The Hessian of tr(h) and the divergence terms break the proportionality.")
print("The Biquard solution h has a NON-TRIVIAL PROFILE (not proportional to g).")
print("It must be computed by solving the full coupled ODE system.")

data = {
    "status": "diagnosed",
    "error": "Conflated Lichnerowicz Laplacian Delta_L with full linearized Ricci operator",
    "correct_equation": "dRic[h] = -(1/2)nabla^2 h - (1/2)Hess(tr h) + sym grad(div h) + Rm.h = Lambda*g",
    "why_conformal_fails": "h = c*r^2*g gives Hess(tr h) not proportional to g, breaking the equation",
    "biquard_h": "has non-trivial radial profile; must solve coupled ODEs",
    "linearized_ricci_of_cr2g": {
        "dRic_00": str(sp.simplify(dRic00)),
        "dRic_11": str(sp.simplify(dRic11)),
        "dRic_33": str(sp.simplify(dRic33)),
    },
}
OUT.write_text(json.dumps(data, indent=2))
print(f"\nOutput: {OUT}")
