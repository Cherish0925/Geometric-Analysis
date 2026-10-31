"""Numerical minimisation of the cell cost P = int |Ric0|^2 over general
(non-Kahler) U(2)-invariant metrics on the blown-up ball glued to complex
hyperbolic space (Ric=-6g) at x = X.

Metric: g = dx^2/(4G) + F s3^2 + x(s1^2+s2^2), x in [x0, X].
  F = Kb exp(phi p1), G = Kb exp(phi p2),
  Kb = (1-psi)(x-x0) + psi (x+x^2),  psi = xi^2(3-2xi), xi=(x-x0)/(X-x0),
  phi = (1-xi)^3, p1,p2 Chebyshev series in xi, constraint p1(0)+p2(0)=0
  (bolt regularity F'(x0)G'(x0)=1).  Metric is C^1 in (F,G) at X, i.e. an
  H^2 metric; P is finite and smooth metrics approximate it.
Reports P/(8 pi^2).  Kahler reference (exact optimum): 1+6x0+O(x0^2).
Usage: python u2_cell_opt.py x0 X deg
"""
import sys, os, json
import numpy as np
import sympy as sp
from numpy.polynomial import chebyshev as C
from scipy.optimize import minimize
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u2_xcoord as UX

xs, Fs, F1s, F2s, Gs, G1s = UX.x, UX.F, UX.F1, UX.F2, UX.G, UX.G1
ric0f = sp.lambdify((xs, Fs, F1s, F2s, Gs, G1s), UX.exprs['ric0sq'], 'numpy')
sf = sp.lambdify((xs, Fs, F1s, F2s, Gs, G1s), UX.exprs['s'], 'numpy')
wpf = sp.lambdify((xs, Fs, F1s, F2s, Gs, G1s), UX.exprs['wpsq_c'], 'numpy')

def build(x0, X, nq=600):
    # quadrature in eta with xi = eta^2 (clusters nodes at the bolt)
    e, w = np.polynomial.legendre.leggauss(nq)
    eta = 0.5*(e+1); weta = 0.5*w
    xi = eta**2; dxi = 2*eta*weta
    L = X - x0
    xx = x0 + L*xi
    return xi, xx, dxi*L, L

def kahler_opt(xx, x0, X):
    """Exact optimal Kahler cell K = x + H, H = c1 x^3/4 - c2/2 + al x^2 + be/x."""
    M = np.array([[x0**3/4, -0.5, x0**2, 1/x0], [3*x0**2/4, 0, 2*x0, -1/x0**2],
                  [X**3/4, -0.5, X**2, 1/X], [3*X**2/4, 0, 2*X, -1/X**2]])
    c1, c2, al, be = np.linalg.solve(M, np.array([-x0, 0, X**2, 2*X]))
    K = xx + c1*xx**3/4 - c2/2 + al*xx**2 + be/xx
    K1 = 1 + 3*c1*xx**2/4 + 2*al*xx - be/xx**2
    K2 = 6*c1*xx/4 + 2*al + 2*be/xx**3
    return K, K1, K2

def fields(c1, c2, xi, xx, x0, L):
    # derivatives wrt x of everything
    Kb, Kb1, Kb2 = kahler_opt(xx, x0, x0 + L)
    phi = (1-xi)**3; phi1 = -3*(1-xi)**2/L; phi2 = 6*(1-xi)/L**2
    out = []
    for cc in (c1, c2):
        p = C.chebval(2*xi-1, cc); dc = C.chebder(cc); ddc = C.chebder(dc)
        p1 = C.chebval(2*xi-1, dc)*2/L if len(cc) > 1 else 0*xi
        p2 = C.chebval(2*xi-1, ddc)*4/L**2 if len(cc) > 2 else 0*xi
        q = phi*p; q1 = phi1*p + phi*p1; q2 = phi2*p + 2*phi1*p1 + phi*p2
        E = np.exp(q)
        f0 = Kb*E; f1 = (Kb1 + Kb*q1)*E; f2 = (Kb2 + 2*Kb1*q1 + Kb*(q2 + q1**2))*E
        out.append((f0, f1, f2))
    return out

def unpack(z, deg):
    c1 = z[:deg]; c2 = np.concatenate([[0.0], z[deg:2*deg-1]])
    # enforce p1(-1)+p2(-1)=0 by adjusting c2[0]
    c2[0] = -(C.chebval(-1, c1) + C.chebval(-1, np.concatenate([[0.0], c2[1:]])))
    return c1, c2

def cost(z, deg, geom, x0, ret=False):
    xi, xx, wx, L = geom
    c1, c2 = unpack(z, deg)
    (F, F1, F2), (G, G1, _) = fields(c1, c2, xi, xx, x0, L)
    if np.any(F <= 0) or np.any(G <= 0):
        return 1e6
    dens = ric0f(xx, F, F1, F2, G, G1)*xx*np.sqrt(F/G)
    P = np.pi**2*np.sum(dens*wx)/(8*np.pi**2)
    if ret:
        s = sf(xx, F, F1, F2, G, G1); wp = wpf(xx, F, F1, F2, G, G1)
        dv = np.pi**2*xx*np.sqrt(F/G)*wx
        Fcell = np.sum((s**2/12 + 4*wp)*dv)
        return P, Fcell, dict(xi=xi, x=xx, F=F, G=G, s=s)
    return P if np.isfinite(P) else 1e6

if __name__ == '__main__':
    x0 = float(sys.argv[1]); X = float(sys.argv[2]); deg = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    geom = build(x0, X)
    z0 = np.zeros(2*deg-1)
    P0 = cost(z0, deg, geom, x0)
    res = minimize(cost, z0, args=(deg, geom, x0), method='BFGS', options=dict(maxiter=4000, gtol=1e-10))
    P, Fc, info = cost(res.x, deg, geom, x0, ret=True)
    # Ball comparison: F_ball = int_0^X (s^2/4) dV with s=-24: 144 * pi^2 * X^2/2... dV = pi^2 x dx
    Fball = 144*np.pi**2*X**2/2
    print(json.dumps(dict(x0=x0, X=X, deg=deg, P_base=P0, P_min=P, kahler_ref=1+6*x0,
                          check_P_minus_1_vs_dF=[P-1, (Fc-Fball)/(8*np.pi**2)],
                          success=bool(res.success), nit=int(res.nit))))
    here = os.path.dirname(os.path.abspath(__file__))
    np.save(os.path.join(here, '..', 'data', f'u2cell_x0{x0}_X{X}_deg{deg}.npy'), res.x)
