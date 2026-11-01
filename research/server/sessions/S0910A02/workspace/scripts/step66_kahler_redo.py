#!/usr/bin/env python3
"""Step 66 (Part A redo): careful symbolic Kaehler checks.

The first pass had two issues:
  (a) u_K' claimed 2 r^5/(r^4-a^4) giving i dd-bar(u_K)=2 omega_K exactly, but the
      regularized cousin utilde_K failed -- a genuine sign/derivative discrepancy to resolve.
  (b) The master identity residual was nonzero, likely because eps was substituted into
      Aphi, Bphi (which do NOT depend on eps) AND the sp.series+diff chain re-expanded
      derivatives incorrectly. Redo the linearization with a clean two-metric approach:
      build Ricci for g_eps = EH + eps*h(phi) DIRECTLY (4x4 with h substituted as a
      perturbation of the frame metric), Taylor-expand in eps symbolically, extract O(eps).

This redo is minimal and trustworthy:
  1. Recompute A_f, B_f for f=r^2, u_K, utilde_K from FIRST PRINCIPLES via d d^c, to
     settle which (if any) potential gives exactly 2 omega_K.
  2. Linearization: define perturbed metric symbolically with eps multiplying the
     (1+eps) frame perturbations, compute Ricci, series-expand to O(eps), subtract
     EH background (eps=0 value), compare with the i dd-bar(Delta_K phi) prediction.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step66_kahler_redo.json"

r, a, eps = sp.symbols('r a eps', positive=True)
W = 1 - a**4/r**4
th, ph, ps = sp.symbols('theta phi psi', real=True)

res = {}

# ---- Part 1: first-principles d d^c on EH ----
# Coframe: e1=(r/2) s1, e2=(r/2) s2, e3=(r sqrtW/2) s3, e0=dr/sqrtW.
# J e0 = e3, J e1 = e2.  s3 evaluated: s3 = dpsi + cos(theta) dphi.
# d^c f = -df o J.  df = f' dr.  dr(J X) = g(dr, J X) = -g(J dr, X) = -sqrtW * g(e3, X)
#   => dr o J = -sqrtW e3 = -sqrtW (r sqrtW/2) s3 = -(r W/2) s3.
# d^c f = f' (r W/2) s3.
# i dd-bar f = d(d^c f) = (f' r W/2)' dr ^ s3 + (f' r W/2) d s3.
# d s3 = d(dpsi + cos th dphi) = -sin th dth ^ dphi.
# s1 ^ s2 = (sin ps dth - cos ps sin th dph) ^ (-cos ps dth - sin ps sin th dph)
#         = -(sin^2 ps + cos^2 ps) sin th dth^dph = - sin th dth ^ dphi.  So d s3 = s1^s2.
# dr = sqrtW e0, s3 = 2 e3/(r sqrtW): dr^s3 = sqrtW e0 ^ 2e3/(r sqrtW) = (2/r) e0^e3.
# s1^s2 = (2e1/r)^(2e2/r) = (4/r^2) e1^e2.
# i dd-bar f = (f' r W/2)' (2/r) e0^e3 + (f' r W/2)(4/r^2) e1^e2.
# A_f = (2/r)(f' r W/2)' ; B_f = (4/r^2)(f' r W/2) = 2 f' W / r.
# NOTE: my pass-1 code used A_f = (f' r W/2)'/r and B_f = f' W/r  -> BOTH OFF BY FACTOR 1/2.
# That rescaling cancels in proportionality tests (A=B unaffected) but affects absolute values.

def Acoef(fp):
    return sp.simplify((2/r)*sp.diff(fp*r*W/2, r))

def Bcoef(fp):
    return sp.simplify(2*fp*W/r)

cands = {
    "r2": 2*r,
    "uK_guess1": 2*r**5/(r**4-a**4),
    "uK_guess2": 2*r**3/(r**2+a**2),
    "utilde": r*(a**2+2*r**2)/(a**2+r**2),
}
for name, fp in cands.items():
    A_, B_ = Acoef(fp), Bcoef(fp)
    res[name] = {"A": sp.simplify(A_), "B": sp.simplify(B_),
                 "prop": bool(sp.simplify(A_-B_)==0),
                 "equals_2": bool(sp.simplify(A_-2)==0 and sp.simplify(B_-2)==0)}
    print(f"{name}: f' = {fp}")
    print(f"   A = {res[name]['A']},  B = {res[name]['B']},  prop={res[name]['prop']}, A=B=2? {res[name]['equals_2']}")

# Integrate the candidate that works
print("\n-- integrate working candidates --")
for name in ["uK_guess1", "uK_guess2"]:
    fp = cands[name]
    F = sp.integrate(fp, r)
    print(f"{name}: F = {sp.simplify(F)}")

# ---- Part 2: clean linearization, master identity ----
# Build EH + eps*h as a 4x4 metric directly in (r,th,ph,ps), h = Aphi (e0^2+e3^2) + Bphi (e1^2+e2^2).
print("\n-- master identity linearization --")
phi = sp.Function('phi')(r)
Aphi = (2/r)*sp.diff(phi*r*W/2, r)
Bphi = 2*phi*W/r
# frame components of the perturbation
s1 = [sp.sin(ps), -sp.cos(ps)*sp.sin(th), 0]
s2 = [-sp.cos(ps), -sp.sin(ps)*sp.sin(th), 0]
s3 = [0, sp.cos(th), 1]
# EH metric matrix
gm = sp.zeros(4,4)
gm[0,0] = 1/W
for i in range(3):
    for j in range(3):
        gm[1+i,1+j] = (r**2/4)*(s1[i]*s1[j] + s2[i]*s2[j] + W*s3[i]*s3[j])
# perturbation matrix h = Aphi*(e0^2 + e3^2) + Bphi*(e1^2+e2^2)
# e0 = dr/sqrtW -> e0^2 = dr^2/W ; e1^2+e2^2 = (r^2/4)(s1^2+s2^2) ; e3^2 = (r^2 W/4) s3^2
hm = sp.zeros(4,4)
hm[0,0] = Aphi/W
for i in range(3):
    for j in range(3):
        hm[1+i,1+j] = (r**2/4)*(Bphi*(s1[i]*s1[j]+s2[i]*s2[j]) + Aphi*W*s3[i]*s3[j])

geps = gm + eps*hm
ginv = sp.simplify(geps.inv())
coords = [r, th, ph, ps]
n = 4
Gamma = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            s = sp.Integer(0)
            for l in range(n):
                s += ginv[i,l]*(sp.diff(geps[l,j],coords[k])+sp.diff(geps[l,k],coords[j])-sp.diff(geps[j,k],coords[l]))
            Gamma[i][j][k] = s/2
Ric = [[sp.Integer(0)]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        s = sp.Integer(0)
        for k in range(n):
            s += sp.diff(Gamma[k][i][j],coords[k])-sp.diff(Gamma[k][i][k],coords[j])
            for l in range(n):
                s += Gamma[k][k][l]*Gamma[l][i][j]-Gamma[k][j][l]*Gamma[l][i][k]
        Ric[i][j] = sp.trigsimp(sp.expand(s))

# Frame components
R00 = sp.simplify(Ric[0][0]*W)
R11 = sp.trigsimp(Ric[1][1]*4/r**2)
R33 = sp.trigsimp(Ric[3][3]*4/(r**2*W))

def oeps(expr):
    e0v = sp.simplify(expr.subs(eps,0))
    e1v = sp.simplify(sp.diff(expr, eps).subs(eps,0))
    return e0v, e1v

for nm, RR in [("R00",R00),("R11",R11),("R33",R33)]:
    e0v, e1v = oeps(RR)
    print(f"{nm}: zeroth = {e0v}")
    res[f"{nm}_zeroth"] = e0v

# dRic components (O(eps) part)
_, dR00 = oeps(R00); _, dR11 = oeps(R11); _, dR33 = oeps(R33)
# Delta_K phi = Aphi + Bphi ; i dd-bar(Delta_K phi) = A_{dK} e0^e3 + B_{dK} e1^e2
dK = Aphi + Bphi
AdK = (2/r)*sp.diff(dK*r*W/2, r)
BdK = 2*dK*W/r
id00 = sp.simplify(dR00 + AdK)
id11 = sp.simplify(dR11 + BdK)
id33 = sp.simplify(dR33 + AdK)
print("dR00 + A_{DeltaK phi} =", id00)
print("dR11 + B_{DeltaK phi} =", id11)
print("dR33 + A_{DeltaK phi} =", id33)
res["master"] = {"id00": id00, "id11": id11, "id33": id33,
                 "holds": bool(id00==0 and id11==0 and id33==0)}

res["status"] = "ok"
OUT.write_text(json.dumps(res, indent=2, default=str))
print("\nOutput:", OUT)
