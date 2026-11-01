#!/usr/bin/env python3
"""Step 66 (Part A): Symbolic verification of the Kaehler reduction on Eguchi-Hanson.

Strategist's check (verify, not assume):
  (i)   i dd-bar(r^2) vs omega_K: naive claim FAILS by an ASD term.
  (ii)  u_K = r^2 + (a^2/2) ln((r^2-a^2)/(r^2+a^2))  satisfies i dd-bar(u_K) = 2 omega_K exactly.
  (iii) bolt-smooth regularization utilde_K = r^2 - (a^2/2) ln((r^2+a^2)/2) also gives 2 omega_K
        (differs from u_K by a pluriharmonic function off the bolt).
  (iv)  MASTER IDENTITY: for radial phi, dRic[h_sym(phi)] = -(i dd-bar(Delta_K phi))(.,J.)
        where h_sym(phi) = A_phi (e0^2+e3^2) + B_phi (e1^2+e2^2), computed by exact
        symbolic linearization of the Bianchi-IX Ricci formulas about EH.

Conventions: EH in Brioschi form g = dr^2/W + (r^2/4)(s1^2+s2^2+W s3^2), W = 1-a^4/r^4,
orthonormal coframe e0 = dr/sqrt(W), e1 = (r/2)s1, e2 = (r/2)s2, e3 = (r sqrt(W)/2) s3.
Kaehler form omega_K = e0^e3 + e1^e2, J: e_0->e_3, e_1->e_2.
For radial f: i dd-bar f = A_f e0^e3 + B_f e1^e2 with
  A_f = (f' r W/2)'/r,  B_f = f' r W / r^2   [derived from d d^c with d^c f = (f' r W/2) s3]
Kaehler Laplacian: Delta_K f = A_f + B_f  (= half the Riemannian Laplacian).
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step66_kahler_symbolic.json"

r, a = sp.symbols('r a', positive=True)
W = 1 - a**4/r**4
f = sp.Function('f')

def Acoef(expr):
    return sp.simplify(sp.diff(expr*r*W/2, r)/r)

def Bcoef(expr):
    return sp.simplify(expr*r*W/r**2)

results = {}

# ---------- (i) naive check: i dd-bar(r^2) ----------
u = r**2
A_u, B_u = Acoef(u), Bcoef(u)
results["naive_r2"] = {
    "A": sp.simplify(A_u), "B": sp.simplify(B_u),
    "is_proportional_to_omegaK": bool(sp.simplify(A_u - B_u) == 0),
    "ASD_discrepancy": sp.simplify(A_u - B_u),
}
print("(i) i dd-bar(r^2): A =", results["naive_r2"]["A"], " B =", results["naive_r2"]["B"])
print("    proportional to omega_K?", results["naive_r2"]["is_proportional_to_omegaK"],
      " ASD term =", results["naive_r2"]["ASD_discrepancy"])

# ---------- (ii) exact Kaehler potential ----------
uK = r**2 + (a**2/sp.Integer(2))*sp.log((r**2-a**2)/(r**2+a**2))
uKp = sp.diff(uK, r)
A_uK, B_uK = Acoef(uKp), Bcoef(uKp)
results["uK"] = {
    "u_prime": sp.simplify(uKp),
    "A": sp.simplify(A_uK), "B": sp.simplify(B_uK),
    "is_2omegaK": bool(sp.simplify(A_uK - 2) == 0 and sp.simplify(B_uK - 2) == 0),
}
print("(ii) u_K':", results["uK"]["u_prime"], " A =", results["uK"]["A"], " B =", results["uK"]["B"],
      " i dd-bar(u_K) = 2 omega_K?", results["uK"]["is_2omegaK"])

# ---------- (iii) bolt-smooth regularization ----------
utilde = r**2 - (a**2/sp.Integer(2))*sp.log((r**2+a**2)/2)
utildep = sp.diff(utilde, r)
A_ut, B_ut = Acoef(utildep), Bcoef(utildep)
results["utildeK"] = {
    "u_prime": sp.simplify(utildep),
    "A": sp.simplify(A_ut), "B": sp.simplify(B_ut),
    "is_2omegaK": bool(sp.simplify(A_ut - 2) == 0 and sp.simplify(B_ut - 2) == 0),
}
print("(iii) utilde_K':", results["utildeK"]["u_prime"], " A =", results["utildeK"]["A"],
      " B =", results["utildeK"]["B"], " i dd-bar(utilde_K) = 2 omega_K?", results["utildeK"]["is_2omegaK"])

# ---------- Bianchi-IX Ricci, symbolic in G1,G2,G3 ----------
print("\nComputing Bianchi-IX Ricci symbolically (G1,G2,G3 functions of r)...")
th, ph, ps = sp.symbols('theta phi psi', real=True)
G1, G2, G3 = sp.symbols('G1 G2 G3', positive=True, cls=sp.Function)
g1, g2, g3 = G1(r), G2(r), G3(r)
coords = [r, th, ph, ps]
# metric: g = G1 dr^2 + G2 (dth^2 + sin^2 th dph^2) + G3 (dps + cos th dph)^2
gm = sp.Matrix([
    [g1, 0, 0, 0],
    [0, g2, 0, 0],
    [0, 0, g2*sp.sin(th)**2 + g3*sp.cos(th)**2, g3*sp.cos(th)],
    [0, 0, g3*sp.cos(th), g3],
])
ginv = sp.simplify(gm.inv())
n = 4
Gamma = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            s = sp.Integer(0)
            for l in range(n):
                s += ginv[i, l]*(sp.diff(gm[l, j], coords[k]) + sp.diff(gm[l, k], coords[j]) - sp.diff(gm[j, k], coords[l]))
            Gamma[i][j][k] = s/2
Ric = [[sp.Integer(0)]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        s = sp.Integer(0)
        for k in range(n):
            s += sp.diff(Gamma[k][i][j], coords[k]) - sp.diff(Gamma[k][i][k], coords[j])
            for l in range(n):
                s += Gamma[k][k][l]*Gamma[l][i][j] - Gamma[k][j][l]*Gamma[l][i][k]
        Ric[i][j] = sp.trigsimp(sp.expand(s))

# Frame components: R00 = Ric_rr / G1 ; R11 = Ric_thth / G2 ; R33 = e_3 component.
# e_3 = (1/sqrt(G3)) d/dpsi  -> R33 = Ric_psps / G3.
R00 = sp.simplify(Ric[0][0]/g1)
R11 = sp.trigsimp(Ric[1][1]/g2)
R33 = sp.trigsimp(Ric[3][3]/g3)
print("  R00 =", R00)
print("  R11 =", R11)
print("  R33 =", R33)

# ---------- EH flatness check ----------
subEH = {G1(r): 1/W, G2(r): r**2/4, G3(r): r**2*W/4}
def subsd(expr):
    e = expr.subs(subEH)
    e = sp.simplify(e)
    # replace derivatives
    for G, val in [(G1, 1/W), (G2, r**2/4), (G3, r**2*W/4)]:
        e = e.replace(sp.Derivative(G(r), r), sp.diff(val, r))
        e = e.replace(sp.Derivative(G(r), (r, 2)), sp.diff(val, (r, 2)))
    return sp.simplify(e)

flat00, flat11, flat33 = subsd(R00), subsd(R11), subsd(R33)
print("  EH: R00 =", flat00, " R11 =", flat11, " R33 =", flat33)
results["EH_flat_in_bianchi_IX"] = bool(flat00 == 0 and flat11 == 0 and flat33 == 0)

# ---------- (iv) master identity: linearize about EH ----------
# Perturbation from phi(r): H1 = A_phi/W, H2 = B_phi r^2/4, H3 = A_phi r^2 W/4.
# We instead directly compute dRic for the perturbed metric
#   g = (1+eps*Aphi)/W dr^2 + (1+eps*Bphi)(r^2/4)(s1^2+s2^2) + (1+eps*Aphi)(r^2 W/4) s3^2
# i.e. G1 = (1+eps*Aphi)/W, G2 = (1+eps*Bphi) r^2/4, G3 = (1+eps*Aphi) r^2 W/4,
# extract O(eps), and compare with -A_{Delta_K phi}, -B_{Delta_K phi}.
eps = sp.symbols('eps')
phi = sp.Function('phi')(r)
Aphi = sp.diff(phi*r*W/2, r)/r
Bphi = phi*r*W/r**2
dK = Aphi + Bphi  # Delta_K phi
AdK = sp.diff(dK*r*W/2, r)/r   # A-coefficient of i dd-bar(Delta_K phi)
BdK = dK*r*W/r**2              # B-coefficient

subP = {G1(r): (1+eps*Aphi)/W, G2(r): (1+eps*Bphi)*r**2/4, G3(r): (1+eps*Aphi)*r**2*W/4}
def lin(expr):
    e = expr.subs(subP)
    # expand derivatives of perturbed G's
    vals = {G1: (1+eps*Aphi)/W, G2: (1+eps*Bphi)*r**2/4, G3: (1+eps*Aphi)*r**2*W/4}
    for G, val in vals.items():
        e = e.replace(sp.Derivative(G(r), (r, 2)), sp.diff(val, (r, 2)))
        e = e.replace(sp.Derivative(G(r), r), sp.diff(val, r))
    e = sp.series(e, eps, 0, 2).removeO()
    return sp.simplify(sp.diff(e, eps).subs(eps, 0))

print("\nLinearizing Ricci about EH (this may take a few minutes)...")
dR00 = lin(R00)
print("  dR00 done")
dR11 = lin(R11)
print("  dR11 done")
dR33 = lin(R33)
print("  dR33 done")

id00 = sp.simplify(dR00 + AdK)
id11 = sp.simplify(dR11 + BdK)
id33 = sp.simplify(dR33 + AdK)
print("  dR00 + A_{Delta_K phi} =", id00)
print("  dR11 + B_{Delta_K phi} =", id11)
print("  dR33 + A_{Delta_K phi} =", id33)
results["master_identity"] = {
    "dR00_plus_A_dK": id00, "dR11_plus_B_dK": id11, "dR33_plus_A_dK": id33,
    "holds": bool(id00 == 0 and id11 == 0 and id33 == 0),
}

results["status"] = "ok"
OUT.write_text(json.dumps(results, indent=2, default=str))
print("\nOutput:", OUT)
