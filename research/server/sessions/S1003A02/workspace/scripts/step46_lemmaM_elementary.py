#!/usr/bin/env python3
"""Step 46: elementary (ODE + Kato) proof data for Lemma M on CH^2, hol. sect. curvature -4.

Input : none.  Output: workspace/data/step46_lemmaM_elementary.json
Checks
 (1) symbolic: g = dr^2 + sinh^2 r (s1^2+s2^2) + sinh^2 r cosh^2 r s3^2 (unit-S^3 left-invariant
     forms, d s3 = 2 s1^s2) has Ric = -6 g; eta = (1/2) sinh^2 r s3 satisfies |d eta|^2 = 2 and
     d eta = e0^e3 + e1^e2 (Kaehler form); |eta|^2 = tanh^2 r / 4.
     Radial-gauge K^{-1} connection A = 6 i eta  =>  V(r) = |A|^2 = 9 tanh^2 r.
 (2) symbolic: f = cosh^{-3} r is an L^2 eigenfunction of the radial operator
     -f'' - (3 coth r + tanh r) f' + 9 tanh^2 r f with eigenvalue 12 (lowest Landau level).
 (3) numeric: zero-energy Green functions (radial, flux-normalised) of
       K^{-1} line:  -Delta_r + 9 tanh^2 r        (decay 2+sqrt13)
       scalar:       -Delta_r + mu, mu=6,12       (decay 2+sqrt(4+mu); L^1 norm = 1/mu exactly)
     and L^1 norms: ||G_line||_1, the identity int tanh^2 G_line = 1/9, gradient norms ||G'||_1,
     and the one-form correction kernel d_x d_y h, h=G_6-G_12, with operator norm
     max(|h''|, |h'|/sinh r, 2|h'|/sinh 2r) (mixed Hessian of distance on CH^2).
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp, quad

out = {}
# ---------------- (1) symbolic geometry ----------------
r, th, ph, ps = sp.symbols('r theta phi psi', real=True)
X = [r, th, ph, ps]
# left-invariant forms on SU(2) as coordinate covectors (components along dr,dth,dph,dps)
S1 = sp.Matrix([0, sp.sin(ps), -sp.cos(ps)*sp.sin(th), 0]) / 2
S2 = sp.Matrix([0, sp.cos(ps), sp.sin(ps)*sp.sin(th), 0]) / 2
S3 = sp.Matrix([0, 0, sp.cos(th), 1]) / 2
DR = sp.Matrix([1, 0, 0, 0])
a, b = sp.sinh(r), sp.sinh(r)*sp.cosh(r)
E = [DR, a*S1, a*S2, b*S3]            # orthonormal coframe
G = sp.zeros(4)
for e in E:
    G += e*e.T
G = sp.simplify(G)
def ext_d(v):  # d of 1-form v: (dv)_{ij} = d_i v_j - d_j v_i
    return sp.Matrix(4, 4, lambda i, j: sp.diff(v[j], X[i]) - sp.diff(v[i], X[j]))
def wedge(u, v):
    return u*v.T - v*u.T
dS3 = sp.simplify(ext_d(S3))
out['dS3_equals_2_S1_wedge_S2_sign'] = None
for sgn in (1, -1):
    if sp.simplify(dS3 - sgn*2*wedge(S1, S2)) == sp.zeros(4):
        out['dS3_equals_2_S1_wedge_S2_sign'] = sgn
Ginv = sp.simplify(G.inv())
# Christoffel and Ricci
Gam = [[[sp.simplify(sum(Ginv[i, l]*(sp.diff(G[l, j], X[k]) + sp.diff(G[l, k], X[j]) - sp.diff(G[j, k], X[l]))
                         for l in range(4))/2) for k in range(4)] for j in range(4)] for i in range(4)]
def ric(j, k):
    s = 0
    for i in range(4):
        s += sp.diff(Gam[i][j][k], X[i]) - sp.diff(Gam[i][j][i], X[k])
        for l in range(4):
            s += Gam[i][i][l]*Gam[l][j][k] - Gam[i][k][l]*Gam[l][j][i]
    return sp.simplify(s)
Ric = sp.Matrix(4, 4, ric)
_pts = [{r: 0.37, th: 1.1, ph: 0.4, ps: 2.3}, {r: 1.9, th: 0.6, ph: 2.0, ps: -0.7}, {r: 3.1, th: 2.4, ph: 1.0, ps: 0.2}]
out['Ric_plus_6g_max_abs_at_samples'] = max(float(abs(sp.N((Ric + 6*G)[i, j].subs(p)))) for p in _pts
                                            for i in range(4) for j in range(4))
eta = sp.sinh(r)**2*S3/2
deta = sp.simplify(ext_d(eta))
omega = wedge(E[0], E[3]) + wedge(E[1], E[2])
omega_m = wedge(E[0], E[3]) - wedge(E[1], E[2])
out['d_eta_equals_e03_plus_e12'] = bool(sp.simplify(deta - omega) == sp.zeros(4))
out['d_eta_equals_e03_minus_e12'] = bool(sp.simplify(deta - omega_m) == sp.zeros(4))
# |2-form|^2 with convention sum_{i<j}
def norm2_form(F):
    return sp.simplify(sum(F[i, j]*F[k, l]*Ginv[i, k]*Ginv[j, l] for i in range(4) for j in range(4)
                           for k in range(4) for l in range(4))/2)
_n2 = norm2_form(deta)
out['norm2_d_eta_at_samples'] = [float(sp.N(_n2.subs(p))) for p in _pts]
eta2 = sp.simplify((eta.T*Ginv*eta)[0])
out['norm2_eta'] = str(sp.simplify(eta2.rewrite(sp.exp)).rewrite(sp.tanh)) if False else str(sp.simplify(eta2))
V = sp.simplify(36*eta2)
out['V_line_equals_9tanh2'] = bool(sp.simplify(V - 9*sp.tanh(r)**2) == 0)
J = sp.sinh(r)**3*sp.cosh(r)
detG = sp.simplify(G.det())
out['sqrt_det_over_angular_equals_J_over_8_sin'] = str(sp.simplify(sp.sqrt(detG)/(J*sp.sin(th))))
# ---------------- (2) Landau ground state ----------------
f = sp.cosh(r)**-3
Lf = -sp.diff(f, r, 2) - (3/sp.tanh(r) + sp.tanh(r))*sp.diff(f, r) + 9*sp.tanh(r)**2*f
out['cosh^-3_eigenvalue'] = str(sp.simplify(Lf/f))

# ---------------- (3) numerics ----------------
AREA = 2*np.pi**2                 # vol(unit S^3); geodesic sphere area = AREA*J(r)
Jn = lambda x: np.sinh(x)**3*np.cosh(x)
def green(Vfun, mu_inf, R=14.0, r_min=1e-7):
    """radial zero-energy Green function, decaying, normalised by -AREA*J f'(0+) = 1"""
    def rhs(x, y):  # y=(f, p=J f')
        return [y[1]/Jn(x), Jn(x)*Vfun(x)*y[0]]
    f0 = np.exp(-mu_inf*R)
    sol = solve_ivp(rhs, (R, r_min), [f0, -mu_inf*f0*Jn(R)], rtol=1e-12, atol=1e-300,
                    dense_output=True, method='DOP853')
    p0 = sol.y[1, -1]
    c = -1.0/(AREA*p0)
    fun = lambda x: c*sol.sol(x)[0]
    dfun = lambda x: c*sol.sol(x)[1]/Jn(x)
    return fun, dfun, sol
def l1(fun, R=14.0):
    val = 0.0
    for lo, hi in [(1e-7, 1e-3), (1e-3, 1), (1, 4), (4, R)]:
        val += quad(lambda x: abs(fun(x))*AREA*Jn(x), lo, hi, limit=400, epsabs=1e-14, epsrel=1e-11)[0]
    return val
res = {}
mu_line = 2+np.sqrt(13)
gl, dgl, _ = green(lambda x: 9*np.tanh(x)**2, mu_line)
res['line_Kinv'] = {
    'decay_exponent': float(mu_line), 'L1_margin_over_e^{4r}': float(mu_line-4),
    'L1_norm_G': l1(gl), 'int_tanh2_G_should_be_1/9': l1(lambda x: np.tanh(x)**2*gl(x)),
    'L1_norm_dG_radial': l1(dgl),
    'check_r2_singularity_4pi2r2G_at_1e-3': float(4*np.pi**2*1e-6*gl(1e-3)),
}
for mu in (6, 12):
    m = 2+np.sqrt(4+mu)
    g_, dg_, _ = green(lambda x, mu=mu: mu+0*x, m)
    res[f'scalar_mu{mu}'] = {'decay_exponent': float(m), 'L1_norm_G': l1(g_), 'exact_1/mu': 1/mu,
                             'L1_norm_dG_radial': l1(dg_)}
    res[f'_fun{mu}'] = (g_, dg_)
g6, dg6 = res.pop('_fun6'); g12, dg12 = res.pop('_fun12')
# h = G6 - G12 ; h' and h'' from the ODE: h'' = mu-terms - (log J)' h'
def hp(x): return dg6(x) - dg12(x)
def hpp(x):
    lj = 3/np.tanh(x) + np.tanh(x)
    return (6*g6(x) - lj*dg6(x)) - (12*g12(x) - lj*dg12(x))
kern = lambda x: max(abs(hpp(x)), abs(hp(x))/np.sinh(x), 2*abs(hp(x))/np.sinh(2*x))
I_dd = l1(kern)
res['oneform_exact_correction'] = {
    'kernel': '(1/6) d_x d_y (G_6-G_12)', 'decay_exponent': float(2+np.sqrt(10)),
    'L1_norm_dd_h_opnorm': I_dd, 'L1_contribution_(1/6)I': I_dd/6,
    'h_prime_times_r_at_1e-4': float(hp(1e-4)*1e-4),
}
res['B1_inverse_Linfty_bound'] = 2*(1/6) + I_dd/6
res['N_inverse_Linfty_bounds_hol-4_units'] = {
    'one_forms_B1': 2/6 + I_dd/6, 'psi_parallel_real_(Delta+12)': 1/12, 'gauge_(Delta+6)': 1/6,
    'psi_perp_K^-1': res['line_Kinv']['L1_norm_G'],
}
out['numerics'] = res
path = Path(__file__).resolve().parents[1]/'data'/'step46_lemmaM_elementary.json'
path.write_text(json.dumps(out, indent=2, default=str)+'\n')
print(json.dumps(out, indent=2, default=str))
