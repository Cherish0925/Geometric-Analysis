"""Floating-point design of the two-endpoint Wazewski passage at b=4/5.

For fixed time T, compute block coordinates (ub,s1b,s2b,ab,q,zeta) of the bolt orbit as a function
of d (fibre slot 1, same formulas as ach_bolt_capd.cpp), and locate d_minus, d_plus with
ub(T) = -target, +target.  Output: workspace/data/ach_capd/passage_design.json
"""
import json, math, sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ach_projected import rhs_md, init_md  # noqa: E402

OUT = HERE.parent / 'data' / 'ach_capd'


def block_coords(X):
    m, de, L3, ym, eta, y3 = X
    L1, L2 = m + de/2, m - de/2
    y1, y2 = ym + eta/2, ym - eta/2
    k = math.exp(L1 - L2 - L3); q = L2 - L3; z = math.exp(-L2 - L3)
    dyf, ds, dk, a = y1 - 2, y2 + y3 - 2, k - 1, y2 - y3
    ch, sh = math.cosh(q), math.sinh(q)
    u = dyf - ds + 6*dk - 2*ch*z; s1 = dyf - ds - 2*dk + 2*ch*z
    s2 = 2*dyf + 3*ds + 2*dk - 4*ch*z; ah = a + 4*sh*z
    phi = q + (y2 - y3)/4 - z*sh
    return dict(ub=u/z, s1b=s1/z, s2b=s2/z, ab=ah/z, q=q, zeta=z, phi=phi, rho=math.exp(phi))


def at_T(d, T, b=0.8, t0=0.01):
    s = solve_ivp(rhs_md, (t0, T), init_md(b, d, t0), method='DOP853', rtol=1e-13, atol=1e-30)
    return block_coords(s.y[:, -1])


if __name__ == '__main__':
    T = float(sys.argv[1]); target = float(sys.argv[2]) if len(sys.argv) > 2 else 0.75
    dstar = 0.28699961889
    c0 = at_T(dstar, T)
    h = 1e-9
    slope = (at_T(dstar + h, T)['ub'] - at_T(dstar - h, T)['ub'])/(2*h)
    dz = brentq(lambda d: at_T(d, T)['ub'], dstar - 5e-8, dstar + 5e-8, xtol=1e-17)
    dp = brentq(lambda d: at_T(d, T)['ub'] - target*np.sign(slope), dz, dz + 2*target/abs(slope), xtol=1e-17)
    dm = brentq(lambda d: at_T(d, T)['ub'] + target*np.sign(slope), dz - 2*target/abs(slope), dz, xtol=1e-17)
    res = dict(T=T, target=target, slope_dub_dd=slope, d_zero=dz, d_upper_ub=dp, d_lower_ub=dm,
               at_zero=at_T(dz, T), at_up=at_T(dp, T), at_lo=at_T(dm, T), at_dstar=c0)
    print(json.dumps(res, indent=1))
    (OUT / f'passage_design_T{T:g}.json').write_text(json.dumps(res, indent=1))
