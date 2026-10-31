"""Explicit smooth (C^infinity) U(2) Kaehler countercell in a Fubini-Study collar.

K(x) = x + kappa x^2 + (1-chi(x)) (alpha + beta/x),  alpha = -x0 - 3 kappa x0^2, beta = 2 kappa x0^3,
i.e. u = xK - x^2 - kappa x^3 = (1-chi) h,  h = alpha x + beta.
For chi = 0 (x <= a) this is the exact cscK (s = 4 lambda) profile with ordinary bolt K(x0)=0, K'(x0)=1;
for chi = 1 (x >= X) it is exactly the complex space form.  chi is the standard C^infinity step on [a,X].
By the exact period identity:  P/(8pi^2) = (1+3 kappa x0)^2 + (1/2) int_a^X u''^2/x dx,
J/(8pi^2) = (1+3 kappa x0)^2 + int_a^X u''^2/x dx.  Positivity of K is checked on a fine grid
(K/(x-x0) bounded below) and analytically near the bolt via the cscK factorization
K_cscK = x0 (y-1)[1 + kappa x0 (y-1)(y+2)/y],  y = x/x0.
"""
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 30


def step(z):
    if z <= 0: return mp.mpf(0)
    if z >= 1: return mp.mpf(1)
    f = lambda s: mp.e**(-1 / s) if s > 0 else mp.mpf(0)
    return f(z) / (f(z) + f(1 - z))


def cell(x0, X, a, kappa):
    x0, X, a, kappa = map(mp.mpf, (x0, X, a, kappa))
    al = -x0 - 3 * kappa * x0**2; be = 2 * kappa * x0**3
    chi = lambda x: step((x - a) / (X - a))
    u = lambda x: (1 - chi(x)) * (al * x + be)
    K = lambda x: x + kappa * x**2 + (1 - chi(x)) * (al + be / x)
    upp = lambda x: mp.diff(u, x, 2)
    I = mp.quad(lambda x: upp(x)**2 / x, mp.linspace(a, X, 9))
    topo = (1 + 3 * kappa * x0)**2
    grid = [x0 * (1 + mp.mpf(10)**(-6)) * (X / x0)**(mp.mpf(i) / 4000) for i in range(4001)]
    mk = min(K(x) / (x - x0) for x in grid)
    return dict(x0=float(x0), X=float(X), a=float(a), kappa=float(kappa), topo=float(topo), I=float(I),
                P=float(topo + I / 2), J=float(topo + I), min_K_over_x_minus_x0=float(mk),
                Kp_bolt=float(mp.diff(K, x0)))


rows = []
for x0, X, a in [(0.01, 0.5, 0.25), (0.01, 0.5, 0.1), (0.003, 0.5, 0.1), (0.03, 0.6, 0.2), (0.05, 0.8, 0.3)]:
    r = cell(x0, X, a, -1); rows.append(r); print(json.dumps(r))
out = Path(__file__).resolve().parents[1] / 'data' / 'kahler_cells' / 'smooth_fs_countercells.json'
out.write_text(json.dumps(rows, indent=1))
