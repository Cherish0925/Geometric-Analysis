#!/usr/bin/env python3
"""
Check of (C2): BUN:double / BUN:balanced-profiles / BUN:cancellation / BUN:exact-second.

Uses the defect matrix verified in c1_ricci_slow.py (valid for ANY a(u), b(t) with a''=a, b''=b,
any zeta(u), z(t)), with
    a = eps cosh u, b = beta cosh t, beta = eps^2,
    zeta' = chi_R sech^3 u / I_R,  z' = tau' = chi_L sech t / J_L.
We
  (i)   verify symbolically the two cancellation identities (BUN:cancellation);
  (ii)  verify int sech^3 = pi/2, int sech = pi, and the rates I_R = pi/2 - O(eps^3), J_L = pi - O(eps^2);
  (iii) evaluate sup over (t,u) of the EXACT operator norm sqrt(v^4/4 + alpha^2 + beta_^2) and compare
        with eps^2/(2 I_R^2 J_L^2) and with (2/pi^4) eps^2; report for which eps the centre dominates.
"""
import sympy as sp
import numpy as np
import mpmath as mp

# ---------------- (i) symbolic cancellation
u, t, eps, I, J = sp.symbols('u t epsilon I J', positive=True)
chiR = sp.Function('chi_R')(u); chiL = sp.Function('chi_L')(t)
a = eps * sp.cosh(u)
zeta_p = chiR * sp.sech(u)**3 / I
tau_p = chiL * sp.sech(t) / J
Q = a * zeta_p
v = Q * tau_p
print("v =", sp.simplify(v))
lin_u = sp.simplify(sp.diff(v, u) + 2 * sp.tanh(u) * v - eps * sp.diff(chiR, u) * chiL * sp.sech(u)**2 * sp.sech(t) / (I * J))
lin_t = sp.simplify(sp.diff(v, t) + sp.tanh(t) * v - eps * chiR * sp.diff(chiL, t) * sp.sech(u)**2 * sp.sech(t) / (I * J))
print("v_u + 2 tanh u v - claimed =", sp.simplify(lin_u.rewrite(sp.exp)))
print("v_t +   tanh t v - claimed =", sp.simplify(lin_t.rewrite(sp.exp)))

# ---------------- (ii) integrals
x = sp.Symbol('x', real=True)
print("int sech^3 =", sp.integrate(sp.sech(x)**3, (x, -sp.oo, sp.oo)) if False else mp.quad(lambda y: mp.sech(y)**3, [-mp.inf, 0, mp.inf]), " pi/2 =", mp.pi / 2)
print("int sech   =", mp.quad(lambda y: mp.sech(y), [-mp.inf, 0, mp.inf]), " pi =", mp.pi)

def rho(xv):
    """fixed cutoff: 0 for x<=1/4, 1 for x>=1 (C^infty)."""
    y = (xv - 0.25) / 0.75
    if y <= 0: return 0.0
    if y >= 1: return 1.0
    f = mp.e**(-1 / y); g_ = mp.e**(-1 / (1 - y))
    return float(f / (f + g_))
def rho_p(xv):
    y = (xv - 0.25) / 0.75
    if y <= 1e-4 or y >= 1 - 1e-4: return 0.0
    # derivative of f/(f+g) w.r.t. y, divided by 0.75
    f = mp.e**(-1 / y); g_ = mp.e**(-1 / (1 - y))
    fp = f / y**2; gp = -g_ / (1 - y)**2
    return float((fp * (f + g_) - f * (fp + gp)) / (f + g_)**2 / 0.75)

def wfun(xv): return mp.asinh(1 / mp.sinh(xv / 2))

print("\n   eps        R        L      pi/2-I_R     (pi/2-I_R)/eps^3    pi-J_L    (pi-J_L)/eps^2")
rows = []
for e_ in [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0005, 0.0002, 0.0001]:
    R = float(wfun(e_) - 2); L = float(wfun(e_**2) - 2)
    IR = 2 * mp.quad(lambda y: rho(R - y) * mp.sech(y)**3, [0, max(R - 1, 0), R - 0.25])
    JL = 2 * mp.quad(lambda y: rho(L - y) * mp.sech(y), [0, max(L - 1, 0), L - 0.25])
    rows.append((e_, R, L, float(IR), float(JL)))
    print("  %.4g   %7.3f  %7.3f   %.3e      %.4f           %.3e   %.4f" % (
        e_, R, L, float(mp.pi / 2 - IR), float((mp.pi / 2 - IR) / e_**3), float(mp.pi - JL), float((mp.pi - JL) / e_**2)))

# ---------------- (iii) exact sup of operator norm
print("\n   eps      delta_exact/eps^2   centre/eps^2   2/pi^4      band_max/eps^3    centre dominates?   (delta-2eps^2/pi^4)/eps^4")
for (e_, R, L, IR, JL) in rows:
    c = e_ / (IR * JL)
    centre = c**2 / 2
    # band in u (chi_R' != 0, R-|u| in [1/4,1]); band in t likewise. Evaluate on grid, t or u free.
    best_band = 0.0
    us = np.linspace(max(R - 1, 0), R - 0.25, 400)
    ts = np.linspace(max(L - 1, 0), L - 0.25, 400)
    sech = lambda y: 1 / np.cosh(y)
    chiRu = np.array([rho(R - y) for y in us]); chiRpu = np.array([-rho_p(R - y) for y in us])
    chiLt = np.array([rho(L - y) for y in ts]); chiLpt = np.array([-rho_p(L - y) for y in ts])
    # u-band, t in core (chi_L=1, chi_L'=0): maximise over t at t=0
    vv = c * chiRu * sech(us)**2; al = c * chiRpu * sech(us)**2 / 2
    best_band = max(best_band, np.max(np.sqrt(vv**4 / 4 + al**2)))
    # t-band, u in core at u=0
    vv = c * chiLt * sech(ts); be = c * chiLpt * sech(ts) / 2
    best_band = max(best_band, np.max(np.sqrt(vv**4 / 4 + be**2)))
    delta = max(centre, best_band)
    print("  %.4g    %.6f           %.6f      %.6f     %8.3f          %s              %.3f" % (
        e_, delta / e_**2, centre / e_**2, 2 / np.pi**4, best_band / e_**3, centre >= best_band,
        (delta - 2 * e_**2 / np.pi**4) / e_**4))
