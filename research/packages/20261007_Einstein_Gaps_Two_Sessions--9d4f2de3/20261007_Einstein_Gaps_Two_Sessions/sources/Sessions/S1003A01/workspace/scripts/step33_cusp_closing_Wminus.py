"""Step 33: anti-self-dual energy of the exact cusp-closing Kahler-Einstein model.

Calabi ansatz over a flat torus T^2 (coordinates x,y, area a), circle coordinate psi of period
2*pi*Lp, connection eta = dpsi + x dy (d eta = dx^dy):
    g = tau (dx^2+dy^2) + dtau^2/Theta + Theta eta^2,   omega = tau dx^dy + dtau^eta.
Kahler-Einstein Ric = -g  <=>  (tau Theta)' = 2 tau^2  <=>  Theta = (2/3) tau^2 - c/tau.
c = 0 is the CH cusp (W^- = 0); c > 0 closes the cusp at tau0 = (3c/2)^(1/3) with
Theta'(tau0) = 2 tau0.  Output: s, |W|^2 (operator convention |W|^2 = W_abcd W^abcd / 4),
|W^-|^2 = |W|^2 - s^2/24, and the closed-form integral of |W^-|^2 over tau0 <= tau < infinity
per unit (area x circle-period), compared with (8 pi^2/3) e, e = Euler number of the circle bundle.
Usage: python step33_cusp_closing_Wminus.py [--out PATH]
"""
import argparse, json
from pathlib import Path
import sympy as sp

tau, x, y, psi, c = sp.symbols('tau x y psi c', positive=True)
Th = sp.Rational(2, 3)*tau**2 - c/tau
X = [tau, x, y, psi]
# eta = dpsi + x dy
g = sp.zeros(4)
g[0, 0] = 1/Th
g[1, 1] = tau
g[2, 2] = tau + Th*x**2
g[2, 3] = g[3, 2] = Th*x
g[3, 3] = Th
gi = sp.simplify(g.inv())
n = 4
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[cc]) + sp.diff(g[d, cc], X[b]) - sp.diff(g[b, cc], X[d]))
                         for d in range(n))/2) for cc in range(n)] for b in range(n)] for a in range(n)]
# R^a_{bcd}
def Rup(a, b, cc, d):
    e = sp.diff(Gam[a][b][d], X[cc]) - sp.diff(Gam[a][b][cc], X[d])
    e += sum(Gam[a][cc][k]*Gam[k][b][d] - Gam[a][d][k]*Gam[k][b][cc] for k in range(n))
    return e
R = sp.MutableDenseNDimArray.zeros(n, n, n, n)
for a in range(n):
    for b in range(n):
        for cc in range(n):
            for d in range(n):
                if cc < d:
                    v = sp.simplify(sum(g[a, k]*Rup(k, b, cc, d) for k in range(n)))
                    R[a, b, cc, d] = v; R[a, b, d, cc] = -v
Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(gi[a, cc]*R[a, b, cc, d] for a in range(n) for cc in range(n))))
s = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(n) for b in range(n)))
einstein_res = sp.simplify(Ric + g)
# Weyl
P = (Ric - s*g/6)/2   # Schouten tensor in dim 4: (Ric - s g/6)/2
W = sp.MutableDenseNDimArray.zeros(n, n, n, n)
for a in range(n):
    for b in range(n):
        for cc in range(n):
            for d in range(n):
                W[a, b, cc, d] = R[a, b, cc, d] - (P[a, cc]*g[b, d] + P[b, d]*g[a, cc] - P[a, d]*g[b, cc] - P[b, cc]*g[a, d])
Wsq = 0
for a in range(n):
    for b in range(n):
        for cc in range(n):
            for d in range(n):
                if W[a, b, cc, d] == 0:
                    continue
                Wu = sum(gi[a, i]*gi[b, j]*gi[cc, k]*gi[d, l]*W[i, j, k, l]
                         for i in range(n) for j in range(n) for k in range(n) for l in range(n)
                         if W[i, j, k, l] != 0)
                Wsq += W[a, b, cc, d]*Wu
Wsq = sp.simplify(Wsq/4)
Wm = sp.simplify(Wsq - s**2/24)
vol = sp.simplify(sp.sqrt(g.det()))   # = tau  (dvol = tau dtau dx dy dpsi)
tau0 = (sp.Rational(3, 2)*c)**sp.Rational(1, 3)
dens = sp.simplify(Wm*vol)
I = sp.simplify(sp.integrate(dens, (tau, tau0, sp.oo)))
# Topology: circle bundle with d eta = dx^dy, psi-period 2 pi Lp, torus area a:
#   Euler number e = a/(2 pi Lp) (|degree|).  Smoothness at tau0 with angle 2pi:
#   Theta'(tau0)/2 * Lp = 1  =>  Lp = 1/tau0.   Integral over N = I * a * 2 pi Lp.
a_, Lp = sp.symbols('a Lp', positive=True)
e = a_/(2*sp.pi*Lp)
B_N = sp.simplify((I*a_*2*sp.pi*Lp).subs(Lp, 1/tau0))
pred = sp.simplify((8*sp.pi**2/3*e).subs(Lp, 1/tau0))
out = dict(scalar=str(s), einstein_residual_zero=bool(einstein_res == sp.zeros(n)), vol_density=str(vol),
           Wsq=str(Wsq), Wminus_sq=str(sp.factor(Wm)), int_Wminus_per_unit=str(I),
           B_N_smooth_closing=str(B_N), eight_pi2_e_over_3=str(pred), ratio=str(sp.simplify(B_N/pred)))
txt = json.dumps(out, indent=1); print(txt)
ap = argparse.ArgumentParser(); ap.add_argument('--out'); A = ap.parse_args()
if A.out:
    Path(A.out).write_text(txt + '\n')
