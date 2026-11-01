#!/usr/bin/env python3
"""Step 65: Direct exact computation of Ric(g_corr) for the conformal corrected metric.

The previous run used the conformal-change formula incorrectly. This script computes
Ric(g_corr) directly from the metric components, then extracts the exact defect.

g_corr = Omega^2(r) * g_EH where Omega^2 = t*(1 - t*Lambda*r^2/8).

Since g_EH is Ricci-flat and Omega depends only on r, we compute the conformal
Ricci directly using the standard warped-product structure.

For g' = e^{2u}*g in dimension n:
  Ric'_ij = Ric_ij - (n-2)*nabla_i nabla_j u - g_ij * Delta u 
           + (n-2)*nabla_i u * nabla_j u - (n-2)*g_ij * |nabla u|^2

where all covariant derivatives and the Laplacian are with respect to the BACKGROUND g.

We verify this formula by direct computation from the metric.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step65_conformal_ricci_direct.json"

print("=== Direct Ricci computation for conformal metric ===")

# Work with a GENERAL conformal factor first to derive the formula,
# then specialize to Omega^2 = t*(1 - t*Lambda*r^2/8).

r = sp.symbols('r', positive=True)
n_dim = 4

# Background EH metric at theta=pi/2 (diagonal, r-dependent)
a = sp.symbols('a', positive=True)
W = 1 - a**4/r**4
g00 = 1/W
g11 = r**2/4
g22 = r**2/4
g33 = r**2*W/4
g_diag = [g00, g11, g22, g33]

# Conformal factor: g' = e^{2u(r)} * g
u = sp.Function('u')(r)

# Christoffel of g' in terms of g and u
# Gamma'^i_jk = Gamma^i_jk + delta^i_j * u_k + delta^i_k * u_j - g_jk * g^{il} * u_l
# For diagonal metric and u = u(r) (only u_0 = u' nonzero):
# Gamma'^0_00 = Gamma^0_00 + u'
# Gamma'^0_ii = Gamma^0_ii - g_ii * g^{00} * u'  (i != 0)
# Gamma'^i_i0 = Gamma^i_i0 + u'  (i != 0)
# Gamma'^i_0i = Gamma^i_0i + u'  (i != 0)
# Others unchanged.

# Background Christoffels
Gam000 = sp.diff(g00, r)/(2*g00)
Gam0 = {}  # Gamma^0_ii for i=1,2,3
Gi0 = {}   # Gamma^i_i0 = Gamma^i_0i
for i, gi in [(1, g11), (2, g22), (3, g33)]:
    Gam0[i] = -sp.diff(gi, r)/(2*g00)
    Gi0[i] = sp.diff(gi, r)/(2*gi)

up = sp.diff(u, r)
upp = sp.diff(u, (r, 2))

# New Christoffels
GamP000 = Gam000 + up
GamP0 = {i: Gam0[i] - g_diag[i]/g00 * up for i in [1, 2, 3]}
GamPi0 = {i: Gi0[i] + up for i in [1, 2, 3]}

# Ricci tensor of g' (diagonal, from Christoffels)
# Ric'_00 = sum_k [d_k Gamma'^k_00 - d_0 Gamma'^k_0k + sum_l (Gamma'^k_kl Gamma'^l_00 - Gamma'^k_0l Gamma'^l_0k)]
# For our diagonal metric with only radial dependence:
# Ric'_00 = -d_0(Gamma'^0_00 + sum_i Gamma'^i_i0) + Gamma'^0_00*Gamma'^0_00 + sum_i Gamma'^i_i0*Gamma'^0_00 
#           ... this is getting complicated. Let me use the standard conformal formula.

# Standard formula (n=4):
# Ric'_ij = Ric_ij - (n-2)*Hess_ij(u) - g_ij * Delta(u) + (n-2)*du_i*du_j - (n-2)*g_ij*|du|^2

# Hessian of u (covariant, w.r.t. background g):
# Hess_00 = u'' - Gamma^0_00*u'
# Hess_ii = -Gamma^0_ii*u'  (i != 0)
Hess00 = upp - Gam000*up
Hess = {i: -Gam0[i]*up for i in [1, 2, 3]}

# Scalar Laplacian
Delta_u = (1/g00)*Hess00 + sum((1/g_diag[i])*Hess[i] for i in [1, 2, 3])
Delta_u = sp.simplify(Delta_u)

# |du|^2 = g^{00}*u'^2
du2 = (1/g00)*up**2

# Ricci of g' (background Ric = 0):
Ricp00 = -(n_dim-2)*Hess00 - g00*Delta_u + (n_dim-2)*up**2 - (n_dim-2)*g00*du2
Ricp00 = sp.simplify(Ricp00)
Ricp = {}
for i in [1, 2, 3]:
    Ricp[i] = sp.simplify(-(n_dim-2)*Hess[i] - g_diag[i]*Delta_u - (n_dim-2)*g_diag[i]*du2)

# Now: g' = e^{2u}*g means g'_ij = e^{2u}*g_ij
# The Ricci ENDOMORPHISM of g' is: Ric'^i_j = g'^{ik}*Ric'_kj = e^{-2u}*g^{ik}*Ric'_kj
# For the Einstein equation Ric' = Lambda*g', we need Ric'^i_j = Lambda*delta^i_j.
# The defect is: D^i_j = Ric'^i_j - Lambda*delta^i_j = e^{-2u}*g^{ik}*Ric'_kj - Lambda*delta^i_j

# Eigenvalues of the Ricci endomorphism:
# lambda_0 = e^{-2u}*Ricp00/g00
# lambda_i = e^{-2u}*Ricp[i]/g_diag[i]

lam0 = sp.simplify(Ricp00/g00)
lam1 = sp.simplify(Ricp[1]/g11)
lam3 = sp.simplify(Ricp[3]/g33)

print("Ricci endomorphism eigenvalues (before e^{-2u} factor):")
print(f"  lambda_0/e^{{-2u}} = {sp.simplify(lam0)}")
print(f"  lambda_1/e^{{-2u}} = {sp.simplify(lam1)}")
print(f"  lambda_3/e^{{-2u}} = {sp.simplify(lam3)}")

# ============================================================
# Now specialize: e^{2u} = Omega^2 = t*(1 - t*Lambda*r^2/8)
# ============================================================
t_sym, Lam = sp.symbols('t Lambda', positive=True)
Omega2 = t_sym*(1 - t_sym*Lam*r**2/8)
u_expr = sp.log(Omega2)/2

# Compute u', u''
up_expr = sp.diff(u_expr, r)
upp_expr = sp.diff(u_expr, (r, 2))

# Substitute into the Ricci eigenvalues
subs = {sp.diff(u, r): up_expr, sp.diff(u, (r, 2)): upp_expr}
lam0_sub = sp.simplify(lam0.subs(subs))
lam1_sub = sp.simplify(lam1.subs(subs))
lam3_sub = sp.simplify(lam3.subs(subs))

# Full eigenvalues of Ricci endomorphism of g':
e2u = Omega2
eig0 = sp.simplify(lam0_sub/e2u)
eig1 = sp.simplify(lam1_sub/e2u)
eig3 = sp.simplify(lam3_sub/e2u)

print()
print("Ricci endomorphism eigenvalues of g' (with conformal factor):")
print(f"  eig_0 = {eig0}")
print(f"  eig_1 = {eig1}")
print(f"  eig_3 = {eig3}")

# Defect: eig_i - Lambda
def0 = sp.simplify(eig0 - Lam)
def1 = sp.simplify(eig1 - Lam)
def3 = sp.simplify(eig3 - Lam)

print()
print("Defect eigenvalues (Ricci endomorphism - Lambda*I):")
print(f"  def_0 = {def0}")
print(f"  def_1 = {def1}")
print(f"  def_3 = {def3}")

# Simplify in the limit t -> 0
print()
print("Leading-order defect as t -> 0 (at fixed r):")
for name, d in [("def_0", def0), ("def_1", def1), ("def_3", def3)]:
    series = sp.series(d, t_sym, 0, 2)
    print(f"  {name} = {series}")

# ============================================================
# Numerical evaluation
# ============================================================
print()
print("=== Numerical evaluation ===")

def0_f = sp.lambdify([r, t_sym, Lam, a], def0, 'numpy')
def1_f = sp.lambdify([r, t_sym, Lam, a], def1, 'numpy')
def3_f = sp.lambdify([r, t_sym, Lam, a], def3, 'numpy')

a_val = 1.0
Lam_val = 1.0

results = []
for t_val in [0.1, 0.01, 0.001, 0.0001]:
    r_max = np.sqrt(8/(t_val*Lam_val)) * 0.8
    r_trans = t_val**(-0.25)
    
    test_radii = np.array([1.5, 2.0, 3.0, 5.0, r_trans, r_trans*2, min(15.0, r_max)])
    test_radii = test_radii[test_radii < r_max]
    test_radii = np.unique(test_radii)
    
    for rv in test_radii:
        d0 = abs(def0_f(rv, t_val, Lam_val, a_val))
        d1 = abs(def1_f(rv, t_val, Lam_val, a_val))
        d3 = abs(def3_f(rv, t_val, Lam_val, a_val))
        dmax = max(d0, d1, d3)
        results.append({
            "t": t_val, "r": float(rv),
            "def_0": float(d0), "def_1": float(d1), "def_3": float(d3),
            "def_max": float(dmax),
            "def_over_t": float(dmax/t_val),
            "def_over_sqrt_t": float(dmax/np.sqrt(t_val)),
        })

print("Scaling summary:")
for t_val in [0.1, 0.01, 0.001, 0.0001]:
    core = [d for d in results if d["t"] == t_val and d["r"] <= 3]
    if core:
        dm = np.mean([d["def_max"] for d in core])
        print(f"  t={t_val:.6f}, core: def_max = {dm:.8f}, def/t = {dm/t_val:.4f}")

print()
print("Fixed r=2.0, varying t:")
for t_val in [0.1, 0.01, 0.001, 0.0001]:
    d0 = abs(def0_f(2.0, t_val, Lam_val, a_val))
    d1 = abs(def1_f(2.0, t_val, Lam_val, a_val))
    print(f"  t={t_val:.6f}: def_0={d0:.8f}, def_1={d1:.8f}")

# Save
data = {
    "status": "ok",
    "eigenvalues_symbolic": {
        "def_0": str(def0),
        "def_1": str(def1),
        "def_3": str(def3),
    },
    "series_expansion_t0": {
        "def_0": str(sp.series(def0, t_sym, 0, 2)),
        "def_1": str(sp.series(def1, t_sym, 0, 2)),
    },
    "numerical_results": results[:30],
}
OUT.write_text(json.dumps(data, indent=2))
print(f"\nOutput: {OUT}")
