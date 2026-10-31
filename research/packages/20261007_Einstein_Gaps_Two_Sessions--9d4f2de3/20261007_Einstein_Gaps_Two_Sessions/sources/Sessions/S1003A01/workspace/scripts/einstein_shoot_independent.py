"""Independent bolt-regular Einstein shooting (Ric = -6g) for diagonal Bianchi IX, S1003A01 Step 15.

Conventions of this Session (FrozenCell): slot 1 collapses at the O(-1) bolt, a1 = t + O(t^3),
a2 = b + O(t^2), a3 = b + O(t^2); slot 3 is the CH Kaehler direction of the collar.
(Peer S1003A02: their a3 = our a1, their a1 = our a3, Rossi ratio rho = a2/a1 here.)
Einstein ODE:  a_i'' = a_i [ (alg_i + 6) - L_i (L_j + L_k) ],  alg_i = 2(a_i^4-(a_j^2-a_k^2)^2)/W^2.
The regular series is derived here with sympy from scratch (odd a1, even a2, a3).
Usage: python einstein_shoot_independent.py  (writes data/einstein_shoot/indep.json)
"""
import json, math
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

OUT = Path(__file__).resolve().parents[1]/'data'/'einstein_shoot'; OUT.mkdir(parents=True, exist_ok=True)
t, b = sp.symbols('t b', positive=True)
N = 7
P = sp.symbols('p3 p5 p7'); Q = sp.symbols('q2 q4 q6'); R = sp.symbols('r2 r4 r6')
a1 = t + P[0]*t**3 + P[1]*t**5 + P[2]*t**7
a2 = b + Q[0]*t**2 + Q[1]*t**4 + Q[2]*t**6
a3 = b + R[0]*t**2 + R[1]*t**4 + R[2]*t**6
A = [a1, a2, a3]; W2 = (a1*a2*a3)**2
eqs = []
for i in range(3):
    j, k = (i+1) % 3, (i+2) % 3
    e = (sp.diff(A[i], t, 2)*W2 + sp.diff(A[i], t)*(sp.diff(A[j], t)*A[j]*A[i]**2*A[k]**2 + sp.diff(A[k], t)*A[k]*A[i]**2*A[j]**2)
         - 6*A[i]*W2 - 2*A[i]*(A[i]**4 - (A[j]**2 - A[k]**2)**2))
    eqs.append(sp.expand(e))
sol = {}; free = []
unk = list(P) + list(Q) + list(R)
for order in range(0, 7):   # orders >= 7 involve coefficients beyond the truncation
    cur = [sp.factor(sp.expand(e.coeff(t, order)).subs(sol)) for e in eqs]
    cur = [c for c in cur if c != 0]
    if not cur: continue
    syms = sorted((set().union(*[c.free_symbols for c in cur]) & set(unk)) - set(sol) - set(free), key=str)
    if not syms:
        assert all(sp.simplify(c) == 0 for c in cur), (order, cur); continue
    ss = sp.solve(cur, syms, dict=True)
    assert ss, (order, cur)
    s0 = ss[0]; sol.update(s0); sol = {kk: sp.factor(v.subs(sol)) for kk, v in sol.items()}
    free += [x for x in syms if x not in s0]
print('free parameters besides b:', free)
for k in sorted(sol, key=str):
    if str(k) in ('p3', 'q2', 'r2', 'q4', 'r4', 'p5'):
        print(k, '=', sol[k])
rest = {x: 0 for x in unk if x not in sol and x not in free}   # beyond determined order
print('unsolved (set to 0, enter at O(t^6) or higher):', list(rest))
fs = [sp.lambdify((b, *free, t), expr.subs(sol).subs(rest)) for expr in A]
dfs = [sp.lambdify((b, *free, t), sp.diff(expr, t).subs(sol).subs(rest)) for expr in A]
aniso = sp.lambdify((b, *free), sp.simplify((Q[1] - R[1]).subs(sol)))
assert len(free) == 1, free
dsym = free[0]


def rhs(_, y):
    a = y[:3]; ad = y[3:]; L = ad/a; W2 = (a[0]*a[1]*a[2])**2
    out = np.empty(6); out[:3] = ad
    for i in range(3):
        j, k = (i+1) % 3, (i+2) % 3
        alg = 2*(a[i]**4 - (a[j]**2 - a[k]**2)**2)/W2
        out[3+i] = a[i]*((alg + 6) - L[i]*(L[j] + L[k]))
    return out


def shoot(bv, dv, t0=0.02, T=7.0):
    y0 = [f(bv, dv, t0) for f in fs] + [f(bv, dv, t0) for f in dfs]
    ev = lambda _, y: min(y[:3]) - 1e-6
    ev.terminal = True
    sol = solve_ivp(rhs, (t0, T), y0, rtol=1e-11, atol=1e-13, events=ev, dense_output=True)
    return sol


def classify(s):
    if s.status == 1: return 'S', None
    a = s.y[:3, -1]; L = s.y[3:, -1]/a
    return ('ACHlike' if L[2] > 1.6 and L[0] < 1.3 else 'AH'), L


def separatrix(bv, lo, hi, it=60):
    clo, _ = classify(shoot(bv, lo)); chi, _ = classify(shoot(bv, hi))
    if clo == chi: return None
    for _ in range(it):
        m = 0.5*(lo + hi); cm, _ = classify(shoot(bv, m))
        if cm == clo: lo = m
        else: hi = m
    return 0.5*(lo + hi), clo, chi


res = []
for bv in [0.29, 0.55, 0.7, 0.8, 0.9, 1.1, 2.0]:
    ds = np.linspace(-3, 3, 121)*max(1, bv**2)
    cls = [classify(shoot(bv, d))[0] for d in ds]
    trans = [(ds[i], ds[i+1], cls[i], cls[i+1]) for i in range(len(ds)-1) if cls[i] != cls[i+1]]
    for lo, hi, c1, c2 in trans:
        sp_ = separatrix(bv, lo, hi)
        if not sp_: continue
        dstar = sp_[0]
        s = shoot(bv, dstar, T=7.0)
        tt = np.linspace(0.5, s.t[-1], 400); Y = s.sol(tt)
        rho = Y[1]/Y[0]; L = Y[3:]/Y[:3]
        # plateau: where the fast slot grows at rate ~2 and slow at ~1 (ACH); rho minimum and median there
        msk = (np.abs(L[2] - 2) < 0.15) & (np.abs(L[0] - 1) < 0.15) & (np.abs(L[1] - 1) < 0.15)
        rec = dict(b=bv, r4_star=dstar, q4_minus_r4=float(aniso(bv, dstar)), sides=[c1, c2], plateau_points=int(msk.sum()),
                   rho_plateau_median=float(np.median(rho[msk])) if msk.any() else None,
                   rho_plateau_min=float(rho[msk].min()) if msk.any() else None,
                   t_end=float(s.t[-1]))
        print(rec, flush=True); res.append(rec)
(OUT/'indep.json').write_text(json.dumps(res, indent=1) + '\n')
