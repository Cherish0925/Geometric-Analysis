"""Step 56c: tower of propagated constraints for SU(2)-invariant AKE.

Usage: EPS=+-1 MODE=single|two|three NMAX python step56_ake_tower.py
single: Omega = w1 (X1=1); two: X3=0; three: general.
Numerically samples the constraint variety {H=0, sumX=1, K1..Kn=0} at lam=-3
by Levenberg-Marquardt from random starts and reports Jacobian ranks,
next-constraint residual, and q=|nabla Omega|^2.  Exact symbolic tower is saved.
"""
import sympy as sp, numpy as np, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import step56_ake_propagate as P

mode = os.environ.get('MODE', 'single'); NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 5
sa, sb, sc, A_, B_, C_ = P.sa, P.sb, P.sc, P.A_, P.B_, P.C_
X = P.X; lam = P.lam
sub = {}
if mode == 'single': sub = {X[0]: 1, X[1]: 0, X[2]: 0}
elif mode == 'two': sub = {X[2]: 0}
vars_ = [sa, sb, sc, A_, B_, C_] + [x for x in X if x not in sub]
def num(e):
    return sp.numer(sp.together(e))
K = [sp.together(sum(X[i]*P.MU[i] for i in range(3)).subs(sub))]
if mode == 'single': K = [num(P.MU[0])]
tower = [K[0]]
for n in range(1, NMAX + 1):
    d = P.Dt(tower[-1]).subs(sub)
    d = num(sp.together(d))
    # reduce modulo previous: keep raw numerator (exact), factor lightly
    tower.append(sp.expand(d))
    print('K', n+1, 'terms', len(sp.Add.make_args(tower[-1])), flush=True)
cons = [num(P.H)] + tower
if mode != 'single': cons = [sum(X[i] for i in range(3)).subs(sub) - 1] + cons
lamv = float(os.environ.get("LAM","-3"))
fs = [sp.lambdify(vars_, c.subs(lam, lamv), 'numpy') for c in cons]
jac = [[sp.lambdify(vars_, sp.diff(c.subs(lam, lamv), v), 'numpy') for v in vars_] for c in cons]
qf = sp.lambdify(vars_, P.q.subs(sub), 'numpy')
rng = np.random.default_rng(1)
results = []
for ncon in range(2, len(cons)):
    use = list(range(ncon))
    nxt = ncon
    best = []
    for trial in range(60):
        z = rng.normal(size=len(vars_)); z[:3] = np.abs(z[:3]) + 0.5
        if mode != 'single': z[6:] = np.abs(z[6:])
        for it in range(200):
            F = np.array([fs[i](*z) for i in use], float)
            Jm = np.array([[jac[i][j](*z) for j in range(len(vars_))] for i in use], float)
            if np.linalg.norm(F) < 1e-13: break
            dz = np.linalg.lstsq(Jm, -F, rcond=None)[0]
            z = z + dz
            if np.any(~np.isfinite(z)): break
        F = np.array([fs[i](*z) for i in use], float)
        if np.all(np.isfinite(F)) and np.linalg.norm(F) < 1e-10 and np.all(z[:3] > 1e-3):
            Jm = np.array([[jac[i][j](*z) for j in range(len(vars_))] for i in use], float)
            rk = np.linalg.matrix_rank(Jm, tol=1e-8)
            nv = abs(fs[nxt](*z)) if nxt < len(cons) else None
            best.append(dict(z=z.tolist(), rank=int(rk), next=float(nv), q=float(qf(*z))))
    results.append(dict(ncon=ncon, found=len(best), samples=best[:6]))
    qs = [s['q'] for s in best]; nx = [s['next'] for s in best]
    print('constraints', ncon, 'found', len(best), 'ranks', sorted(set(s['rank'] for s in best)),
          'max|next|', max(nx) if nx else None, 'min|next|', min(nx) if nx else None,
          'q range', (min(qs), max(qs)) if qs else None, flush=True)
os.makedirs(os.path.join(os.path.dirname(__file__), '../data/step56'), exist_ok=True)
json.dump(dict(mode=mode, eps=P.eps, tower=[str(k) for k in tower], results=results),
          open(os.path.join(os.path.dirname(__file__), f'../data/step56/tower_{mode}_eps{P.eps}_lam{lamv}.json'), 'w'), indent=1)
