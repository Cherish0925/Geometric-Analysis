#!/usr/bin/env python3
"""
End-to-end nonlinear test of BUN:third-bound in the CORE model (limiting profiles, no cut-offs):
   G_eps      = dt^2 + cosh^2 t dy^2 + du^2 + (cosh u dx + m du)^2,  m = eps*(2/pi)*tau(t)*sech^2 u,
                tau(t) = (gd(t)+pi/2)/pi   (so tau' = sech t/pi,  zeta' = sech^3 u/(pi/2))
   Gt_eps     = G_eps + eps^2 K,   K = A g1 + B f T1 + C T2   (A, C from c3_pde_numeric.py, B closed form).
The full Ricci tensor is obtained symbolically from the coordinate metric with generic A(t,u), C(t,u);
A, C and their derivatives (central differences of the PDE solution) are then substituted numerically.
Reports sup over the core window of the operator norm of g^{-1}(Ric+g) for both metrics.
Expected:  sup|Phi(G_eps)| / eps^2 -> 2/pi^4 = 0.020532 ;   sup|Phi(Gt_eps)| / eps^3 bounded.
"""
import sys
import numpy as np
import sympy as sp
DATA = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/yau26/work/audit_bundle/AC_solution.npz'

t, y, u, x, eps, k_on = sp.symbols('t y u x epsilon k_on', real=True)
X = [t, y, u, x]; n = 4
A = sp.Function('A')(t, u); C = sp.Function('C')(t, u)
c0 = 2 / sp.pi**2
f = sp.sech(t)**2; r = sp.sech(u)**2
gdu = sp.atan(sp.sinh(u)); gdt = sp.atan(sp.sinh(t))
B = c0**2 / 8 * (r + sp.pi**2 / 4 - gdu**2)
tau = (gdt + sp.pi / 2) / sp.pi
m = eps * (2 / sp.pi) * tau * r
e2 = k_on * eps**2                       # k_on = 0: uncorrected, 1: corrected

g = sp.zeros(4, 4)
g[0, 0] = 1 + e2 * (A + B * f)
g[1, 1] = sp.cosh(t)**2 * (1 + e2 * (A - B * f))
g[2, 2] = 1 + m**2 + e2 * C
g[2, 3] = g[3, 2] = m * sp.cosh(u)
g[3, 3] = sp.cosh(u)**2 * (1 - e2 * C)

det23 = g[2, 2] * g[3, 3] - g[2, 3]**2
ginv = sp.zeros(4, 4)
ginv[0, 0] = 1 / g[0, 0]; ginv[1, 1] = 1 / g[1, 1]
ginv[2, 2] = g[3, 3] / det23; ginv[3, 3] = g[2, 2] / det23; ginv[2, 3] = ginv[3, 2] = -g[2, 3] / det23

Gam = [[[sum(ginv[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
             for l in range(n)) / 2 for k in range(n)] for j in range(n)] for i in range(n)]
Ric = sp.zeros(n, n)
for j in range(n):
    for l in range(j, n):
        Ric[j, l] = Ric[l, j] = sum(sp.diff(Gam[i][l][j], X[i]) - sp.diff(Gam[i][i][j], X[l])
                                    + sum(Gam[i][i][mm] * Gam[mm][l][j] - Gam[i][l][mm] * Gam[mm][i][j] for mm in range(n))
                                    for i in range(n))
Phi = Ric + g

# replace A, C and derivatives by plain symbols
names = {}
def sym_for(fun, nt, nu):
    key = (str(fun.func), nt, nu)
    if key not in names:
        names[key] = sp.Symbol("%s_%d%d" % key)
    return names[key]
reps = {}
for fun in (A, C):
    for nt in range(0, 4):
        for nu in range(0, 4):
            if nt + nu == 0 or nt + nu > 3: continue
            d = fun
            if nt: d = sp.diff(d, t, nt)
            if nu: d = sp.diff(d, u, nu)
            reps[d] = sym_for(fun, nt, nu)
# substitute highest derivatives first
ordered = sorted(reps.items(), key=lambda kv: -sum(c for _, c in kv[0].variable_count))
def strip(expr):
    for d, s_ in ordered:
        expr = expr.subs(d, s_)
    expr = expr.subs(A, sym_for(A, 0, 0)).subs(C, sym_for(C, 0, 0))
    return expr
Phi_s = Phi.applyfunc(strip); g_s = g.applyfunc(strip)
assert not Phi_s.has(sp.Derivative), "unreplaced derivative (needs higher order)"
syms = [t, u, eps, k_on] + [names[k] for k in sorted(names)]
print("derivative symbols used:", [str(names[k]) for k in sorted(names) if Phi_s.has(names[k])])
pairs = [(a_, b_) for a_ in range(4) for b_ in range(a_, 4)]
Phi_fn = sp.lambdify(syms, [Phi_s[a_, b_] for (a_, b_) in pairs], modules='numpy', cse=True)
g_fn = sp.lambdify(syms, [g_s[a_, b_] for (a_, b_) in pairs], modules='numpy', cse=True)

# ---------------- numerical data
dat = np.load(DATA)
A0, C0, tc, uc = dat['A'], dat['C'], dat['tc'], dat['uc']
h = tc[1] - tc[0]
# even extension in t and u so that central differences near 0 are right
def ext(F):
    F2 = np.concatenate([F[::-1, :], F], axis=0)
    return np.concatenate([F2[:, ::-1], F2], axis=1)
Ae, Ce = ext(A0), ext(C0)
te = np.concatenate([-tc[::-1], tc]); ue = np.concatenate([-uc[::-1], uc])
def derivs(F):
    out = {}
    Ft = np.gradient(F, h, axis=0, edge_order=2); Fu = np.gradient(F, h, axis=1, edge_order=2)
    out[(0, 0)] = F; out[(1, 0)] = Ft; out[(0, 1)] = Fu
    out[(2, 0)] = np.gradient(Ft, h, axis=0, edge_order=2); out[(0, 2)] = np.gradient(Fu, h, axis=1, edge_order=2)
    out[(1, 1)] = np.gradient(Ft, h, axis=1, edge_order=2)
    return out
dA, dC = derivs(Ae), derivs(Ce)
win = 9.0; stride = max(1, int(round(0.1 / h)))
it = np.where(np.abs(te) <= win)[0][::stride]; iu = np.where((ue >= 0) & (ue <= win))[0][::stride]
TT, UU = np.meshgrid(te[it], ue[iu], indexing='ij')
def pick(D, key):
    return D[key][np.ix_(it, iu)]
vals = {}
for key in sorted(names):
    D = dA if key[0] == 'A' else dC
    k2 = (key[1], key[2])
    vals[key] = pick(D, k2) if k2 in D else np.zeros_like(TT)

def supnorm(e_, on):
    args = [TT, UU, e_, float(on)] + [vals[k] for k in sorted(names)]
    P = Phi_fn(*args); Gm = g_fn(*args)
    Pn = np.zeros(TT.shape + (4, 4)); Gn = np.zeros(TT.shape + (4, 4))
    for idx_, (a_, b_) in enumerate(pairs):
        Pn[..., a_, b_] = Pn[..., b_, a_] = np.broadcast_to(np.asarray(P[idx_], dtype=float), TT.shape)
        Gn[..., a_, b_] = Gn[..., b_, a_] = np.broadcast_to(np.asarray(Gm[idx_], dtype=float), TT.shape)
    # op norm of g^{-1}Phi = max |generalised eigenvalue|: use Cholesky g = L L^T
    Lc = np.linalg.cholesky(Gn); Li = np.linalg.inv(Lc)
    Mx = Li @ Pn @ np.swapaxes(Li, -1, -2)
    ev = np.linalg.eigvalsh(Mx)
    opn = np.abs(ev).max(axis=-1)
    idx = np.unravel_index(np.argmax(opn), opn.shape)
    return opn.max(), (TT[idx], UU[idx])

print("\n   eps      sup|Phi(G)|/eps^2   (2/pi^4=%.6f)    sup|Phi(G+eps^2K)|/eps^3    argmax(t,u)" % (2 / np.pi**4))
print('grid h =', h)
for e_ in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
    s0, _ = supnorm(e_, 0); s1, where = supnorm(e_, 1)
    print("  %.3f     %.6f                              %.6f                 (%.2f, %.2f)" % (e_, s0 / e_**2, s1 / e_**3, where[0], where[1]))
