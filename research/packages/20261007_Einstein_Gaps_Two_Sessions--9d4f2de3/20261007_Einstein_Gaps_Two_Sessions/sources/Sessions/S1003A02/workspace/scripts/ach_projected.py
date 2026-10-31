"""Projected (unstable-mode-free) shooting for SU(2)-diagonal Einstein metrics Ric=-6g on the
O(-1) bolt, targeting asymptotically complex hyperbolic (ACH) ends.

Metric g = dt^2 + sum a_i^2 s_i^2, ds_i = 2 s_j^s_k; bolt in slot 3 (a3 = t + ..., a1(0)=a2(0)=b),
d = p4 - q4 the free t^4 anisotropy (series from einstein_bolt_series.py).

Compact ACH variables for fibre slot f with the other slots (g,h) in cyclic order:
    W = (y_f, y_g, y_h, kappa, q, zeta),  kappa = a_f/(a_g a_h),  q = log(a_g/a_h),
    zeta = 1/(a_g a_h).
Exact autonomous system (derived in workspace/notes/step15_ach_projected_shooting.md):
    y_i' = 6 - y_i (y_f+y_g+y_h) + Pot_i,
    Pot_f = 2k^2 - 8 z^2 sinh^2 q / k^2,
    Pot_g = -2k^2 + 4 z e^{-q} + 4 z^2 sinh(2q)/k^2,
    Pot_h = -2k^2 + 4 z e^{+q} - 4 z^2 sinh(2q)/k^2,
    k' = k (y_f - y_g - y_h),  q' = y_g - y_h,  z' = -z (y_g + y_h).
ACH_f is the curve of equilibria E(q) = (2,1,1,1,q,0); spectrum {2, -2, -4, -6, -8, 0}
(-8 = constraint-violating mode, 0 = neutral Rossi mode).  The separatrix condition is
U = l_u . (W - E(q)) = 0 on a transverse section zeta = zeta_*, with l_u the left eigenvector
for the unstable eigenvalue 2 (independent of q except through its zeta component).
Limiting Rossi ratio: rho_inf = exp(Phi~), Phi~ = q + (y_g - y_h)/4 - zeta sinh q + O(zeta^2, |W-E|^2).

CLI:
  python ach_projected.py check                 # algebraic checks, eigen-structure
  python ach_projected.py branch b1,b2,...      # solve U=0 for each b (fibre slot 1), rho_inf
  python ach_projected.py cont b_start b_end n  # natural continuation with fold detection
  python ach_projected.py scan3                 # distance of bolt orbits to ACH3 / ACH1 strata
Outputs: workspace/data/ach_projected/*.json
"""
import json, sys, math
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from einstein_bolt_shoot import Bolt, rhs, pots, constraint  # noqa: E402

OUT = HERE.parent / 'data' / 'ach_projected'
OUT.mkdir(parents=True, exist_ok=True)

CYC = {0: (1, 2), 1: (2, 0), 2: (0, 1)}


def to_compact(z6, f):
    g, h = CYC[f]
    L, y = z6[:3], z6[3:]
    return np.array([y[f], y[g], y[h], math.exp(L[f]-L[g]-L[h]), L[g]-L[h], math.exp(-L[g]-L[h])])


def compact_rhs(W):
    yf, yg, yh, k, q, z = W
    S = yf + yg + yh
    Pf = 2*k**2 - 8*z**2*math.sinh(q)**2/k**2
    Pg = -2*k**2 + 4*z*math.exp(-q) + 4*z**2*math.sinh(2*q)/k**2
    Ph = -2*k**2 + 4*z*math.exp(q) - 4*z**2*math.sinh(2*q)/k**2
    return np.array([6-yf*S+Pf, 6-yg*S+Pg, 6-yh*S+Ph, k*(yf-yg-yh), yg-yh, -z*(yg+yh)])


def sym_structure():
    yf, yg, yh, k, q, z = sp.symbols('y_f y_g y_h kappa q zeta')
    S = yf+yg+yh
    F = sp.Matrix([6-yf*S+2*k**2-8*z**2*sp.sinh(q)**2/k**2,
                   6-yg*S-2*k**2+4*z*sp.exp(-q)+4*z**2*sp.sinh(2*q)/k**2,
                   6-yh*S-2*k**2+4*z*sp.exp(q)-4*z**2*sp.sinh(2*q)/k**2,
                   k*(yf-yg-yh), yg-yh, -z*(yg+yh)])
    X = sp.Matrix([yf, yg, yh, k, q, z])
    J = F.jacobian(X).subs({yf: 2, yg: 1, yh: 1, k: 1, z: 0})
    J = sp.simplify(J)
    lam = sp.symbols('lam')
    cp = sp.factor((J - lam*sp.eye(6)).det())
    # left eigenvector for eigenvalue 2
    ns = (J.T - 2*sp.eye(6)).nullspace()
    lu = sp.simplify(ns[0] / ns[0][0])
    # constraint C = yf yg + yg yh + yh yf - 6 - (1/2) sum Pot
    Pot = [F[i] - (6 - [yf, yg, yh][i]*S) for i in range(3)]
    C = yf*yg + yg*yh + yh*yf - 6 - sp.Rational(1, 2)*sum(Pot)
    dC = sp.simplify(sum(sp.diff(C, X[i])*F[i] for i in range(6)) + 2*S*C)
    return dict(J=J, charpoly=cp, l_u=lu, C=C, dC_plus_2SC=dC)


_LU = None


def l_unstable(q):
    global _LU
    if _LU is None:
        st = sym_structure()
        qs = sp.Symbol('q')
        _LU = sp.lambdify(qs, list(st['l_u']))
    return np.array(_LU(q), dtype=float)


def U_and_phi(W):
    q = W[4]
    E = np.array([2, 1, 1, 1, q, 0.0])
    U = float(l_unstable(q) @ (W - E))
    phi = q + (W[1]-W[2])/4 - W[5]*math.sinh(q)
    dev = float(np.linalg.norm((W - E)[:4]))
    return U, phi, dev


BOLT = None


def bolt():
    global BOLT
    if BOLT is None:
        BOLT = Bolt(1)
    return BOLT


# ---- anisotropy-resolving variables -------------------------------------------------------
# X = (m, delta, L3, ym, eta, y3), L1 = m + delta/2, L2 = m - delta/2, y1 = ym + eta/2, y2 = ym - eta/2.
# The bolt anisotropy delta = log(a1/a2) = (d/b) t^4 + ... is carried with full relative
# precision; its equation uses the cancellation-free identity
#   Pot1 - Pot2 = 8 e^{-2 L3} sinh(2 delta) - 8 e^{-L1-L2} sinh(delta).
def rhs_md(t, X):
    m, de, L3, ym, eta, y3 = X
    L = [m + de/2, m - de/2, L3]
    y = [ym + eta/2, ym - eta/2, y3]
    P = pots(L)
    S = y[0] + y[1] + y[2]
    dP12 = 8*math.exp(-2*L3)*math.sinh(2*de) - 8*math.exp(-L[0]-L[1])*math.sinh(de)
    dym = 6 - ym*S + 0.5*(P[0] + P[1])
    deta = -eta*S + dP12
    dy3 = 6 - y3*S + P[2]
    return np.array([ym, eta, y3, dym, deta, dy3])


def md_to_Ly(X):
    m, de, L3, ym, eta, y3 = X
    return np.array([m + de/2, m - de/2, L3, ym + eta/2, ym - eta/2, y3])


_DIFF = None


def init_md(b, d, t0):
    """Bolt initial data in (m, delta, ...) with delta from the exact series difference."""
    B = bolt()
    fv = B._fs(b, d)
    P = np.array(B._P(b, fv), dtype=float); Q = np.array(B._Q(b, fv), dtype=float)
    R = np.array(B._R(b, fv), dtype=float)
    N = B.N
    k = np.arange(1, N+1)
    a2 = b + np.sum(Q*t0**k); da2 = np.sum(k*Q*t0**(k-1))
    D = np.sum((P-Q)*t0**k); dD = np.sum(k*(P-Q)*t0**(k-1))   # a1 - a2 and its derivative
    a3 = t0 + np.sum(R*t0**np.arange(2, N+2)); da3 = 1 + np.sum(np.arange(2, N+2)*R*t0**np.arange(1, N+1))
    de = math.log1p(D/a2)
    a1 = a2 + D; da1 = da2 + dD
    m = math.log(a2) + de/2
    y1, y2 = da1/a1, da2/a2
    eta = (dD*a2 - D*da2)/(a1*a2)          # = y1 - y2 without cancellation
    return np.array([m, de, math.log(a3), 0.5*(y1+y2), eta, da3/a3])


def shoot_section(b, d, f=0, zeta_star=1e-4, T=40.0, t0=2e-3, dense=False):
    """Integrate from the bolt until zeta_f = zeta_star; return compact state there."""
    X0 = init_md(b, d, t0)
    g, h = CYC[f]
    def ev_sec(t, X):
        z = md_to_Ly(X)
        return -z[g] - z[h] - math.log(zeta_star)
    ev_sec.terminal = True; ev_sec.direction = -1
    def ev_big(t, X):
        return 60.0 - max(abs(v) for v in md_to_Ly(X)[3:]) * (t > 0.5)
    ev_big.terminal = True
    s = solve_ivp(rhs_md, (t0, T), X0, method='DOP853', rtol=1e-13, atol=1e-30, events=[ev_sec, ev_big],
                  dense_output=dense)
    hit = len(s.t_events[0]) > 0
    zz = md_to_Ly(s.y_events[0][0] if hit else s.y[:, -1])
    W = to_compact(zz, f)
    out = dict(hit=bool(hit), t=float(s.t_events[0][0]) if hit else float(s.t[-1]), W=W,
               con=float(constraint(zz)))
    if dense:
        out['_sol'] = s
    return out


def Ufun(b, d, f=0, zeta_star=1e-4):
    r = shoot_section(b, d, f, zeta_star)
    if not r['hit']:
        return np.nan, r
    U, phi, dev = U_and_phi(r['W'])
    r.update(U=U, phi=phi, dev=dev)
    return U, r


def solve_d(b, d_guess, f=0, zeta_star=1e-4, rel=1e-3):
    """Bracket and solve U(b,d)=0 near d_guess."""
    grid = d_guess*(1 + rel*np.linspace(-1, 1, 21))
    vals = [Ufun(b, float(x), f, zeta_star)[0] for x in grid]
    for i in range(len(grid)-1):
        if np.isfinite(vals[i]) and np.isfinite(vals[i+1]) and vals[i]*vals[i+1] < 0:
            ds = brentq(lambda x: Ufun(b, x, f, zeta_star)[0], grid[i], grid[i+1], xtol=1e-16, rtol=1e-15,
                        maxiter=200)
            U, r = Ufun(b, ds, f, zeta_star)
            return ds, r
    return None, dict(grid=[float(x) for x in grid], vals=[float(v) for v in vals])


def branch(bs, guesses):
    out = []
    for b, dg in zip(bs, guesses):
        rec = dict(b=b)
        for zs in (1e-3, 1e-4, 1e-5):
            ds, r = solve_d(b, dg, 0, zs, rel=2e-2 if zs == 1e-3 else 1e-3)
            if ds is None:
                rec[f'z{zs:g}'] = dict(found=False, info=r); continue
            dg = ds
            rec[f'z{zs:g}'] = dict(found=True, d=ds, t_sec=r['t'], dev=r['dev'], U=r['U'], phi=r['phi'],
                                   rho=math.exp(r['phi']), kappa=float(r['W'][3]), con=r['con'])
        print(json.dumps(rec), flush=True)
        out.append(rec)
    return out


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'check':
        st = sym_structure()
        print('J =', st['J'])
        print('charpoly =', st['charpoly'])
        print('l_u =', list(st['l_u']))
        print('dC/dt + 2 S C =', st['dC_plus_2SC'])
        # numerical check of compact rhs against L,y rhs
        rng = np.random.default_rng(1)
        err = 0.0
        for _ in range(20):
            z6 = np.concatenate([rng.normal(size=3), rng.normal(size=3)])
            for f in range(3):
                g, h = CYC[f]
                W = to_compact(z6, f); dW = compact_rhs(W)
                dz = rhs(0, z6)
                L, y = z6[:3], z6[3:]
                pred = np.array([dz[3+f], dz[3+g], dz[3+h], W[3]*(y[f]-y[g]-y[h]), y[g]-y[h], -W[5]*(y[g]+y[h])])
                err = max(err, float(np.max(np.abs(pred - dW))/(1+np.max(np.abs(pred)))))
        print('compact rhs vs (L,y) rhs max rel err:', err)
        (OUT / 'structure.json').write_text(json.dumps({k: str(v) for k, v in st.items()} | {'rhs_err': err}, indent=1))
    elif mode == 'branch':
        import csv
        rows = list(csv.DictReader(open(HERE.parent / 'data' / 'einstein_bolt_runs' / 'ach_family_summary.csv')))
        bs = [float(v) for v in sys.argv[2].split(',')] if len(sys.argv) > 2 else [float(r['b']) for r in rows]
        tab = {float(r['b']): float(r['d_star']) for r in rows}
        bb = np.array(sorted(tab)); dd = np.array([tab[x] for x in bb])
        guesses = [float(np.exp(np.interp(math.log(b), np.log(bb), np.log(dd)))) for b in bs]
        res = branch(bs, guesses)
        tag = sys.argv[3] if len(sys.argv) > 3 else 'branch'
        (OUT / f'{tag}.json').write_text(json.dumps(res, indent=1))
    elif mode == 'cont':
        # natural continuation of the ACH1 curve d*(b) in log b from a solved point (b0,d0)
        b0, d0, b_end = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
        nstep = int(sys.argv[5]); tag = sys.argv[6]
        zs = 1e-4
        hist = [(math.log(b0), math.log(d0))]
        out = []
        h = (math.log(b_end) - math.log(b0))/nstep
        lb = math.log(b0)
        while (h < 0 and lb > math.log(b_end)) or (h > 0 and lb < math.log(b_end)):
            lbn = lb + h
            if len(hist) >= 2:
                (x1, y1), (x2, y2) = hist[-2], hist[-1]
                ld = y2 + (y2-y1)/(x2-x1)*(lbn-x2)
            else:
                ld = hist[-1][1]
            ds, r = solve_d(math.exp(lbn), math.exp(ld), 0, zs, rel=2e-2)
            if ds is None:
                ds, r = solve_d(math.exp(lbn), math.exp(ld), 0, zs, rel=3e-1)
            if ds is None:
                h /= 2
                print('shrink step', h, flush=True)
                if abs(h) < 1e-4:
                    print('continuation stopped (possible fold) at b', math.exp(lb), flush=True); break
                continue
            lb = lbn; hist.append((lb, math.log(ds)))
            rec = dict(b=math.exp(lb), d=ds, rho=math.exp(r['phi']), dev=r['dev'], t_sec=r['t'],
                       kappa=float(r['W'][3]), U=r['U'])
            print(json.dumps(rec), flush=True); out.append(rec)
        (OUT / f'cont_{tag}.json').write_text(json.dumps(out, indent=1))
    elif mode == 'roots':
        # all sign changes of U_f(b, d) over a wide signed log-grid of d, slots f = 0,1,2
        b = float(sys.argv[2]); f = int(sys.argv[3]); zs = float(sys.argv[4]) if len(sys.argv) > 4 else 1e-3
        mags = np.geomspace(1e-14, 1e3, 341)
        ds = np.concatenate([-mags[::-1], [0.0], mags])
        vals = []
        for d in ds:
            U, r = Ufun(b, float(d), f, zs)
            vals.append((float(d), U, r.get('dev', None), r['hit']))
        roots = []
        for (d1, U1, e1, h1), (d2, U2, e2, h2) in zip(vals[:-1], vals[1:]):
            if np.isfinite(U1) and np.isfinite(U2) and U1*U2 < 0:
                roots.append(dict(d1=d1, d2=d2, U1=U1, U2=U2, dev1=e1, dev2=e2))
        mind = min([v[2] for v in vals if v[2] is not None], default=None)
        rec = dict(b=b, slot=f+1, zeta=zs, n_hit=int(sum(v[3] for v in vals)), n=len(vals), min_dev=mind,
                   roots=roots)
        print(json.dumps(rec), flush=True)
        (OUT / f'roots_b{b:g}_f{f+1}.json').write_text(json.dumps(dict(rec, scan=vals), indent=0))
