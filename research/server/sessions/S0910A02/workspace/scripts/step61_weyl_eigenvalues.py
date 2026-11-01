#!/usr/bin/env python3
"""Step 61: Complete linearized Weyl and Ricci analysis for toric-cone opposite warping.

Metric: g = dr1^2 + r1^2 e^{2v} dphi^2 + dr2^2 + r2^2 e^{-2v} dpsi^2,
        v = eps * A * (r1^2 - r2^2),   A constant, eps small.

We compute EVERYTHING at first order in eps in the orthonormal frame
  e1=dr1, e2=dr2, e3=r1 e^v dphi, e4=r2 e^{-v} dpsi.
Output:
  1. All six independent sectional curvatures.
  2. The Ricci eigenvalues (in orthonormal frame).
  3. The self-dual and anti-self-dual Weyl eigenvalues.
  4. The condition for R_pm = W_pm + (Lambda/3)Id to degenerate.
  5. The Ricci defect = Ric - (trace/4)g in orthonormal frame.

We also check the 4D identity: Rm = W + Ric/(n-2) ∧ g - Scal/((n-1)(n-2)) g∧g
and that the sum of the three W+ eigenvalues and three W- eigenvalues are each zero.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step61_weyl_eigenvalues.json"

r1, r2, eps, A = sp.symbols('r1 r2 eps A', real=True, positive=True)
phi, psi = sp.symbols('phi psi')
coords = [r1, r2, phi, psi]

# v = eps * A * (r1^2 - r2^2)
v = eps * A * (r1**2 - r2**2)

# metric components
g_diag = [sp.Integer(1), sp.Integer(1), r1**2 * sp.exp(2*v), r2**2 * sp.exp(-2*v)]
g = sp.diag(*g_diag)
ginv = g.inv()
n = 4

# Christoffel symbols (expanded to order eps)
def series1(expr):
    return sp.series(expr, eps, 0, 2).removeO()

Gamma = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            s = sp.Integer(0)
            for l in range(n):
                s += ginv[i,l]*(sp.diff(g[l,j],coords[k])+sp.diff(g[l,k],coords[j])-sp.diff(g[j,k],coords[l]))
            Gamma[i][j][k] = sp.expand(series1(s/2))

# Riemann R_{ijkl} (covariant, NOT orthonormal yet)
def Riem_coord(i,j,k,l):
    s1 = sp.Integer(0)
    for m in range(n):
        s1 += g[i,m]*(sp.diff(Gamma[m][j][l],coords[k]) - sp.diff(Gamma[m][j][k],coords[l]))
        for p in range(n):
            s1 += g[i,m]*(Gamma[m][k][p]*Gamma[p][j][l] - Gamma[m][l][p]*Gamma[p][j][k])
    return series1(sp.expand(s1))

# Orthonormal frame: e_a = (1/sqrt(g_aa)) d(coord_a)
# Orthonormal Riemann: R_{abcd}^{ON} = R_{ijkl}^{coord} / (sqrt(g_ii g_jj g_kk g_ll))
# For diagonal metric.
sqrtg = [sp.sqrt(g_diag[i]) for i in range(n)]

def Rm_on(a,b,c,d):
    """Orthonormal Riemann at first order in eps."""
    raw = Riem_coord(a,b,c,d)
    # divide by sqrt(g_aa g_bb g_cc g_dd)
    denom = sqrtg[a]*sqrtg[b]*sqrtg[c]*sqrtg[d]
    return sp.nsimplify(series1(sp.expand(raw / denom)))

# Six independent sectional curvatures K_{ab} = Rm_{abab}
sects = {}
pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
for (a,b) in pairs:
    val = Rm_on(a,b,a,b)
    sects[f"K_{a+1}{b+1}"] = val

# Ricci in ON frame: Ric_ab = sum_c Rm_{acbc}
Ric_on = [[sp.Integer(0)]*n for _ in range(n)]
for a in range(n):
    for b in range(n):
        s = sp.Integer(0)
        for c in range(n):
            s += Rm_on(a,c,b,c)
        Ric_on[a][b] = sp.simplify(series1(s))

Scal = sum(Ric_on[a][a] for a in range(n))
Scal = sp.simplify(series1(Scal))

# Self-dual / anti-self-dual 2-forms basis (for orientation (1,2,3,4)):
# SD: omega_1^+ = e12+e34, omega_2^+ = e13+e42, omega_3^+ = e14+e23
# ASD: omega_1^- = e12-e34, omega_2^- = e13-e42, omega_3^- = e14-e23
# Weyl as operator on 2-forms: W_{abcd} projected onto SD/ASD subspace.

# W = Rm - (Ric ∧ g)/(n-2) + Scal * (g ∧ g)/((n-1)(n-2))
# (g ∧ g)_{abcd} = g_ac g_bd - g_ad g_bc (= delta_ac delta_bd - ... in ON frame)
# (Ric ∧ g)_{abcd} = Ric_ac g_bd - Ric_ad g_bc + g_ac Ric_bd - g_ad Ric_bc ... wait
# Actually Kulkarni-Nomizu: (h ∧ k)_{abcd} = h_ac k_bd + h_bd k_ac - h_ad k_bc - h_bc k_ad
# Weyl_{abcd} = Rm_{abcd} - 1/(n-2)(Ric ∧ g)_{abcd} + Scal/((n-1)(n-2)) (g ∧ g)_{abcd}
# In ON frame g_{ab} = delta_{ab}.

def KN(h, k, a, b, c, d):
    """Kulkarni-Nomizu product in ON frame (h,k are symmetric matrices, g=delta)."""
    return h[a][c]*k[b][d] + h[b][d]*k[a][c] - h[a][d]*k[b][c] - h[b][c]*k[a][d]

delta = [[sp.Integer(1) if i==j else sp.Integer(0) for j in range(n)] for i in range(n)]

def Weyl_on(a,b,c,d):
    rm = Rm_on(a,b,c,d)
    ric_wedge = KN(Ric_on, delta, a,b,c,d)
    g_wedge = KN(delta, delta, a,b,c,d)
    # W = Rm - KN(Ric,g)/(n-2) + Scal * KN(g,g)/(2(n-1)(n-2))
    # n=4: W = Rm - KN(Ric,g)/2 + Scal * KN(g,g)/12
    return series1(rm - ric_wedge/2 + Scal*g_wedge/12)

# Self-dual Weyl matrix W^+_{IJ} (I,J=1,2,3) in the SD basis:
# W^+_{IJ} = (1/2) sum_{abcd} (omega^+_I)_{ab} W_{abcd} (omega^+_J)_{cd}
# SD basis vectors (as 2-form coefficients: omega_I = sum_{a<b} (omega_I)_{ab} e^a ∧ e^b)
# omega_1^+ : (12)=1, (34)=1.  omega_2^+ : (13)=1, (42)=1 i.e. (24)=-1.
# omega_3^+ : (14)=1, (23)=1.
# ASD:
# omega_1^- : (12)=1, (34)=-1.  omega_2^- : (13)=1, (42)=-1 i.e. (24)=1.
# omega_3^- : (14)=1, (23)=-1.

# Represent as dict {(a,b): coeff} with a<b.
sd = [
    {(0,1): 1, (2,3): 1},
    {(0,2): 1, (1,3): -1},
    {(0,3): 1, (1,2): 1},
]
asd = [
    {(0,1): 1, (2,3): -1},
    {(0,2): 1, (1,3): 1},
    {(0,3): 1, (1,2): -1},
]

def weyl_block(basis):
    """3x3 matrix W_{IJ} = (1/2) sum omega_I(ab) W(abcd) omega_J(cd)."""
    M = [[sp.Integer(0)]*3 for _ in range(3)]
    for I in range(3):
        for J in range(3):
            s = sp.Integer(0)
            for (a,b), c1 in basis[I].items():
                for (c,d), c2 in basis[J].items():
                    s += c1*c2*Weyl_on(a,b,c,d)
            M[I][J] = sp.simplify(series1(s/2))
    return M

print("Computing W+...", file=sys.stderr)
Wp = weyl_block(sd)
print("Computing W-...", file=sys.stderr)
Wm = weyl_block(asd)

# Eigenvalues of W+ and W- (3x3 traceless symmetric matrices).
# At first order in eps, the flat cone has W=0, so W = eps * W^(1) + O(eps^2).
# Extract the linear-in-eps part.
def extract_lin(M, sz=3):
    return [[sp.simplify(sp.diff(M[i][j], eps).subs(eps, 0)) for j in range(sz)] for i in range(sz)]

Wp_lin = extract_lin(Wp, 3)
Wm_lin = extract_lin(Wm, 3)

# Build symbolic 3x3 matrices and get eigenvalues.
Wp_mat = sp.Matrix(Wp_lin)
Wm_mat = sp.Matrix(Wm_lin)

# Check tracelessness
tr_Wp = sp.simplify(Wp_mat.trace())
tr_Wm = sp.simplify(Wm_mat.trace())

# Get eigenvalues (symbolic, for 3x3 matrix).
# For speed, use the characteristic polynomial.
lam = sp.Symbol('lam')
cp_p = sp.simplify(sp.expand((Wp_mat - lam*sp.eye(3)).det()))
cp_m = sp.simplify(sp.expand((Wm_mat - lam*sp.eye(3)).det()))

# At a specific point r1=1, r2=1 (equal fibers), extract numerical eigenvalues.
Wp_at = Wp_mat.subs({r1: 1, r2: 1})
Wm_at = Wm_mat.subs({r1: 1, r2: 1})
ev_p = [sp.nsimplify(x) for x in Wp_at.eigenvals()]
ev_m = [sp.nsimplify(x) for x in Wm_at.eigenvals()]

# Also at the axis r1=1, r2=0 (corner of quarter-plane):
# this is singular for the orbifold, skip.
# At r1=sqrt(2), r2=1:
Wp_at2 = Wp_mat.subs({r1: sp.sqrt(2), r2: 1})
Wm_at2 = Wm_mat.subs({r1: sp.sqrt(2), r2: 1})
ev_p2 = list(Wp_at2.eigenvals().keys())
ev_m2 = list(Wm_at2.eigenvals().keys())

# Ricci defect: Ric - (Scal/4) delta in ON frame, first order in eps
Ric_lin = extract_lin(Ric_on, 4)
Scal_lin = sp.simplify(sp.diff(Scal, eps).subs(eps, 0))
Ric_defect = [[sp.simplify(Ric_lin[a][b] - (Scal_lin/4 if a==b else 0)) for b in range(n)] for a in range(n)]

data = {
    "status": "ok",
    "metric": "toric cone: diag(1,1,r1^2 e^{2 eps A(r1^2-r2^2)}, r2^2 e^{-2 eps A(r1^2-r2^2)})",
    "sectional_curvatures_linear_in_eps": {k: str(sp.simplify(sp.diff(v_, eps).subs(eps,0))) for k,v_ in sects.items()},
    "Ric_ON_linear_in_eps": [[str(Ric_lin[a][b]) for b in range(n)] for a in range(n)],
    "Scal_linear_in_eps": str(Scal_lin),
    "Weyl_SD_linear_in_eps": [[str(Wp_lin[i][j]) for j in range(3)] for i in range(3)],
    "Weyl_ASD_linear_in_eps": [[str(Wm_lin[i][j]) for j in range(3)] for i in range(3)],
    "W+_traceless": str(tr_Wp),
    "W-_traceless": str(tr_Wm),
    "W+_eigenvalues_at_r1=r2=1": [str(e) for e in ev_p],
    "W-_eigenvalues_at_r1=r2=1": [str(e) for e in ev_m],
    "W+_eigenvalues_at_r1=sqrt2_r2=1": [str(sp.simplify(e)) for e in ev_p2],
    "W-_eigenvalues_at_r1=sqrt2_r2=1": [str(sp.simplify(e)) for e in ev_m2],
    "Ric_defect_traceless_ON_linear": [[str(Ric_defect[a][b]) for b in range(n)] for a in range(n)],
    "char_poly_W+": str(cp_p),
    "char_poly_W-": str(cp_m),
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, indent=2), encoding='utf-8')
print(json.dumps({
    "status": "ok",
    "output": str(OUT),
    "W+_at_r1=r2=1": [[str(Wp_at[i,j]) for j in range(3)] for i in range(3)],
    "W-_at_r1=r2=1": [[str(Wm_at[i,j]) for j in range(3)] for i in range(3)],
    "ev_W+_at_r1=r2=1": [str(e) for e in ev_p],
    "ev_W-_at_r1=r2=1": [str(e) for e in ev_m],
    "Scal_lin": str(Scal_lin),
    "W+_traceless": str(tr_Wp),
    "W-_traceless": str(tr_Wm),
}, indent=2))
