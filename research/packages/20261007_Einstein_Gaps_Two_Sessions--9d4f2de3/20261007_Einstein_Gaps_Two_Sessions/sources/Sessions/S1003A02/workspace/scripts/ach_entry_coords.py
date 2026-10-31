"""Rescaled block coordinates (ub, s1b, s2b, ab) = (u, s1, s2, ah)/zeta of solved ACH1 separatrices on
transverse sections zeta = zeta0 (non-rigorous floating evaluation; for choosing block parameters K, zeta0
and the d-bracket that a validated integrator must enclose).
CLI: python ach_entry_coords.py b zeta0 -> prints JSON for the root d* and for d*(1 -+ eps)."""
import json, sys, math
import numpy as np
from ach_projected import solve_d, Ufun

def coords(W):
    yf, yg, yh, k, q, z = W
    dyf, ds, dk, a = yf - 2, yg + yh - 2, k - 1, yg - yh
    u = dyf - ds + 6*dk - 2*math.cosh(q)*z
    s1 = dyf - ds - 2*dk + 2*math.cosh(q)*z
    s2 = 2*dyf + 3*ds + 2*dk - 4*math.cosh(q)*z
    ah = a + 4*math.sinh(q)*z
    return dict(ub=u/z, s1b=s1/z, s2b=s2/z, ab=ah/z, q=q, zeta=z)

if __name__ == '__main__':
    b, z0 = float(sys.argv[1]), float(sys.argv[2])
    dg = float(sys.argv[3])
    ds, r = solve_d(b, dg, 0, z0, rel=1e-3)
    out = dict(b=b, zeta0=z0, d_star=ds, at_root=coords(r['W']))
    for eps in (1e-12, 1e-10, 1e-8):
        for sgn in (-1, 1):
            U, rr = Ufun(b, ds*(1 + sgn*eps), 0, z0)
            out[f'eps{sgn*eps:g}'] = coords(rr['W']) if rr['hit'] else 'nohit'
    print(json.dumps(out, indent=1))
