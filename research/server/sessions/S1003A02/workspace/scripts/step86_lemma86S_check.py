"""Step 86: numerical check of Lemma 86.S (continuity of the human defect D under Ricci-flat ALE resolution).

Model: the round Einstein orbifold S^4/{+-1} (Ric = 3g, two A_1 points) resolved by two Eguchi-Hanson
spaces of scale a, which gives a smooth metric on CP^2 # CP^2 (package Prop. 58.O example).
Everything is U(2)-invariant, so the metric is  F(u)^2 du^2 + A(u)^2 s3^2 + B(u)^2 (s1^2 + s2^2)
with Euler-angle forms s_i (flat R^4 = du^2 + u^2/4 (s1^2+s2^2+s3^2)).

  round:  F = 1, A = B = sin(u)/2                      (Ric = 3g)
  EH:     F = (1-a^4/u^4)^(-1/2), A = (u/2)(1-a^4/u^4)^(1/2), B = u/2   (Ric = 0)
  glued:  each of F, A, B = chi * round + (1-chi) * EH, chi = cutoff of u/rho, rho = a^(2/3)
          (tau = 4, rho = eps^(tau/(tau+2))), on u in [a, pi/2], doubled by the u -> pi-u symmetry.

Output: D(g_a) = 4 - (int s)^2 / (Vol * int |Ric|^2) for a list of a, the fitted exponent, and the
convention checks (Ricci of the three exact profiles).  The angular volume constant cancels in D.
Writes workspace/data/step86/lemma86S_check.json.
"""
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import quad

OUT = Path(__file__).resolve().parents[1] / 'data' / 'step86'
OUT.mkdir(parents=True, exist_ok=True)

# ---------- symbolic Ricci of F^2 du^2 + A^2 s3^2 + B^2 (s1^2 + s2^2) ----------
u, th, ph, ps = sp.symbols('u theta phi psi', real=True)
F, A, B = [sp.Function(n)(u) for n in ('F', 'A', 'B')]
X = [u, th, ph, ps]
s1 = [0, sp.sin(ps), -sp.cos(ps) * sp.sin(th), 0]
s2 = [0, sp.cos(ps), sp.sin(ps) * sp.sin(th), 0]
s3 = [0, 0, sp.cos(th), 1]
g = sp.zeros(4, 4)
g[0, 0] = F**2
for i in range(4):
    for j in range(4):
        g[i, j] += A**2 * s3[i] * s3[j] + B**2 * (s1[i] * s1[j] + s2[i] * s2[j])
g = sp.simplify(g)
gi = sp.simplify(g.inv())
Gam = [[[sp.simplify(sum(gi[k, l] * (sp.diff(g[l, i], X[j]) + sp.diff(g[l, j], X[i]) - sp.diff(g[i, j], X[l]))
                         for l in range(4)) / 2) for j in range(4)] for i in range(4)] for k in range(4)]
Ric = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        e = 0
        for k in range(4):
            e += sp.diff(Gam[k][i][j], X[k]) - sp.diff(Gam[k][i][k], X[j])
            for l in range(4):
                e += Gam[k][k][l] * Gam[l][i][j] - Gam[k][j][l] * Gam[l][i][k]
        Ric[i, j] = sp.simplify(e)
Rup = gi * Ric
scal = sp.simplify(Rup.trace())
ric2 = sp.simplify((Rup * Rup).trace())
# both are functions of u only; evaluate at a generic angle to drop residual angle dependence
scal = sp.simplify(scal.subs({th: sp.Rational(7, 10), ps: sp.Rational(3, 10)}))
ric2 = sp.simplify(ric2.subs({th: sp.Rational(7, 10), ps: sp.Rational(3, 10)}))

f0, f1, f2, a0, a1, a2, b0, b1, b2 = sp.symbols('f0 f1 f2 a0 a1 a2 b0 b1 b2')
rep = {sp.Derivative(F, (u, 2)): f2, sp.Derivative(A, (u, 2)): a2, sp.Derivative(B, (u, 2)): b2}
rep1 = {sp.Derivative(F, u): f1, sp.Derivative(A, u): a1, sp.Derivative(B, u): b1}
rep0 = {F: f0, A: a0, B: b0}
def red(e):
    return sp.simplify(e.subs(rep).subs(rep1).subs(rep0))
scal_r, ric2_r = red(scal), red(ric2)
args = (f0, f1, f2, a0, a1, a2, b0, b1, b2)
S_fun = sp.lambdify(args, scal_r, 'numpy')
R2_fun = sp.lambdify(args, ric2_r, 'numpy')

def profiles_check():
    uu = sp.Symbol('uu', positive=True)
    aa = sp.Symbol('aa', positive=True)
    tests = {
        'flat': (sp.Integer(1), uu / 2, uu / 2),
        'round': (sp.Integer(1), sp.sin(uu) / 2, sp.sin(uu) / 2),
        'EH': ((1 - aa**4 / uu**4)**sp.Rational(-1, 2), uu / 2 * (1 - aa**4 / uu**4)**sp.Rational(1, 2), uu / 2),
    }
    res = {}
    for name, (Ff, Af, Bf) in tests.items():
        sub = {f0: Ff, f1: sp.diff(Ff, uu), f2: sp.diff(Ff, uu, 2), a0: Af, a1: sp.diff(Af, uu), a2: sp.diff(Af, uu, 2),
               b0: Bf, b1: sp.diff(Bf, uu), b2: sp.diff(Bf, uu, 2)}
        res[name] = {'s': str(sp.simplify(scal_r.subs(sub))), 'Ric2': str(sp.simplify(ric2_r.subs(sub)))}
    return res

# ---------- numerical gluing ----------
def chi(x):  # smooth step: 0 for x<=1, 1 for x>=2
    def h(t):
        return np.where(t > 0, np.exp(-1 / np.maximum(t, 1e-300)), 0.0)
    t = x - 1.0
    return h(t) / (h(t) + h(1 - t))

def dchi(x, k):
    hstep = 1e-4
    if k == 1:
        return (chi(x + hstep) - chi(x - hstep)) / (2 * hstep)
    return (chi(x + hstep) - 2 * chi(x) + chi(x - hstep)) / hstep**2

def glued(uv, a, rho):
    x = uv / rho
    c, c1, c2 = chi(x), dchi(x, 1) / rho, dchi(x, 2) / rho**2
    q = 1 - a**4 / uv**4
    FE, AE, BE = q**-0.5, uv / 2 * q**0.5, uv / 2
    FE1 = -0.5 * q**-1.5 * (4 * a**4 / uv**5)
    FE2 = 0.75 * q**-2.5 * (4 * a**4 / uv**5)**2 - 0.5 * q**-1.5 * (-20 * a**4 / uv**6)
    AE1 = 0.5 * q**0.5 + uv / 2 * 0.5 * q**-0.5 * (4 * a**4 / uv**5)
    AE2 = (0.5 * 0.5 * q**-0.5 * (4 * a**4 / uv**5)) * 2 + uv / 2 * (
        -0.25 * q**-1.5 * (4 * a**4 / uv**5)**2 + 0.5 * q**-0.5 * (-20 * a**4 / uv**6))
    BE1, BE2 = 0.5, 0.0
    FR, FR1, FR2 = 1.0, 0.0, 0.0
    AR, AR1, AR2 = np.sin(uv) / 2, np.cos(uv) / 2, -np.sin(uv) / 2
    def mix(R0, R1, R2, E0, E1, E2):
        v0 = c * R0 + (1 - c) * E0
        v1 = c1 * (R0 - E0) + c * R1 + (1 - c) * E1
        v2 = c2 * (R0 - E0) + 2 * c1 * (R1 - E1) + c * R2 + (1 - c) * E2
        return v0, v1, v2
    Fv = mix(FR, FR1, FR2, FE, FE1, FE2)
    Av = mix(AR, AR1, AR2, AE, AE1, AE2)
    Bv = mix(AR, AR1, AR2, BE, BE1, BE2)
    return Fv, Av, Bv

def defect(a):
    rho = a**(2 / 3)
    def vol_dens(uv):
        (F0, _, _), (A0, _, _), (B0, _, _) = glued(uv, a, rho)
        return F0 * A0 * B0**2
    def s_dens(uv):
        (F0, F1, F2), (A0, A1, A2), (B0, B1, B2) = glued(uv, a, rho)
        return S_fun(F0, F1, F2, A0, A1, A2, B0, B1, B2) * F0 * A0 * B0**2
    def r2_dens(uv):
        (F0, F1, F2), (A0, A1, A2), (B0, B1, B2) = glued(uv, a, rho)
        return R2_fun(F0, F1, F2, A0, A1, A2, B0, B1, B2) * F0 * A0 * B0**2
    top = np.pi / 2
    # inner EH region (u < rho): Ricci-flat exactly; only volume contributes.  F*A = u/2 there.
    V = quad(lambda uv: uv / 2 * (uv / 2)**2, a, rho, limit=200)[0] + quad(vol_dens, rho, top, limit=400, points=[2 * rho])[0]
    S = quad(s_dens, rho, top, limit=400, points=[2 * rho])[0]
    R2 = quad(r2_dens, rho, top, limit=400, points=[2 * rho])[0]
    # doubling by symmetry cancels in D
    D = 4 - S**2 / (V * R2)
    return dict(a=a, rho=rho, Vol=V, int_s=S, int_Ric2=R2, D=D)

if __name__ == '__main__':
    checks = profiles_check()
    print(json.dumps(checks, indent=1))
    rows = [defect(a) for a in (0.2, 0.1, 0.05, 0.025, 0.0125)]
    for r in rows:
        print(r)
    la = np.log([r['a'] for r in rows]); lD = np.log([abs(r['D']) for r in rows])
    slope = float(np.polyfit(la[1:], lD[1:], 1)[0])
    Vround = quad(lambda uv: (np.sin(uv) / 2)**3, 0, np.pi / 2)[0]
    print('fitted exponent of D in a:', slope, ' (Lemma 86.S bound: rho^4 = a^(8/3) -> 2.667)')
    json.dump(dict(convention_checks=checks, rows=rows, fitted_exponent=slope,
                   round_reference=dict(Vol=Vround, int_s=12 * Vround, int_Ric2=36 * Vround)),
              open(OUT / 'lemma86S_check.json', 'w'), indent=1, default=float)
