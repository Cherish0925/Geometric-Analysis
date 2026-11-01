#!/usr/bin/env python3
"""Step 67: explicit test of Lemma 67.1 (D(p - |c1^-|^2) = 0 at cscK) and of the
sign of the second variation of p - q^2 (the question c_K vs 2) on the cscK
product S^2(K1=1) x S^2(K2=a), a != 1, along the non-Kaehler Hermitian family

   g_t = (1 + t f(th)) g_{S^2_1}  +  (1 - t f(th)) a^{-1} g_{S^2_2},
   f = P_l(cos th)   (Legendre, l = 1,2,3,...).

Exact facts used (derived in the companion note):
  * harmonic SD form  w+ = b (F/G) sin th dth^dphi + b vol_2  (closed and SD for
    every such metric); hence with I = int_0^pi (F/G) sin th dth,
        |c1^+|^2 = (2+I)^2/I,  c1^2 = 8,  q^2 = |c1^-|^2 = (2-I)^2/I.
  * P = int |Ric^0|^2 dmu = 8 pi^2 int_0^pi |Ric^0|^2 F G sin th dth  (sin th2 integrated: 4 pi;
    phi: 2 pi), p = P/(8 pi^2).
At t = 0: p = q^2 = 2(1-a)^2/a.
Since g_t is not constant-scalar, the Yamabe representative lowers p and keeps q:
a negative second variation of p - q^2 here implies a negative one on the slice
(c_K < 2); a positive one is inconclusive.
Output: workspace/data/step67_product_hessian.json
"""
import json
from pathlib import Path
import sympy as sp

th, th2, ph, ph2, t = sp.symbols('theta theta2 phi phi2 t', real=True)
a = sp.Symbol('a', positive=True)

def ricci_diag(gdiag, coords):
    n = len(coords); g = sp.diag(*gdiag); gi = sp.diag(*[1/x for x in gdiag])
    Gam = [[[sp.simplify(sum(gi[i, l]*(sp.diff(g[l, j], coords[k]) + sp.diff(g[l, k], coords[j])
                                         - sp.diff(g[j, k], coords[l]))/2 for l in range(n)))
             for k in range(n)] for j in range(n)] for i in range(n)]
    Ric = sp.zeros(n)
    for j in range(n):
        for k in range(n):
            r = 0
            for i in range(n):
                r += sp.diff(Gam[i][j][k], coords[i]) - sp.diff(Gam[i][j][i], coords[k])
                for l in range(n):
                    r += Gam[i][i][l]*Gam[l][j][k] - Gam[i][k][l]*Gam[l][j][i]
            Ric[j, k] = sp.simplify(r)
    return g, gi, Ric

def run(l, aval):
    f = sp.legendre(l, sp.cos(th))
    F = 1 + t*f; G = (1 - t*f)/aval
    gd = [F, F*sp.sin(th)**2, G, G*sp.sin(th2)**2]
    g, gi, Ric = ricci_diag(gd, [th, ph, th2, ph2])
    s = sum(gi[i, i]*Ric[i, i] for i in range(4))
    R0 = Ric - s/4*g
    norm2 = sum(gi[i, i]*gi[j, j]*R0[i, j]**2 for i in range(4) for j in range(4))
    dens = sp.simplify(norm2*F*G*sp.sin(th)*sp.sin(th2)/sp.sin(th2))  # th2-dependence cancels
    dens2 = sp.series(dens, t, 0, 3).removeO()
    c = [sp.simplify(dens2.coeff(t, k)) for k in range(3)]
    pk = [float(sp.integrate(sp.expand(ck), (th, 0, sp.pi))) for ck in c]   # p = int_0^pi dens dth
    I = sp.series(sp.integrate(sp.series(F/G*sp.sin(th), t, 0, 3).removeO(), (th, 0, sp.pi)), t, 0, 3).removeO()
    q2 = sp.series((2 - I)**2/I, t, 0, 3).removeO()
    qk = [float(sp.nsimplify(q2).coeff(t, k)) for k in range(3)]
    # constant-scalar check
    s_series = sp.series(s, t, 0, 2).removeO()
    return dict(l=l, a=float(aval), p=pk, q2=qk, D1=pk[1]-qk[1], H2=pk[2]-qk[2],
                s0=float(sp.simplify(s_series.coeff(t, 0))), s1=str(sp.simplify(s_series.coeff(t, 1))))

if __name__ == '__main__':
    res = []
    for aval in [sp.Rational(1, 2), sp.Integer(3), sp.Rational(1, 5)]:
        for l in [1, 2, 3]:
            r = run(l, aval); res.append(r); print(json.dumps(r), flush=True)
    p = Path(__file__).resolve().parents[1]/'data'/'step67_product_hessian.json'
    p.write_text(json.dumps(res, indent=1))
