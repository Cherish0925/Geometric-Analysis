"""Shooting the bolt-regular SU(2)-invariant Einstein metrics (Ric = -6g) on the O(-n) bolt.

Uses the regular series from einstein_bolt_series.py (data/einstein_bolt/series_n{n}.json):
two free parameters b = a1(0) = a2(0) (bolt radius) and the t^4 anisotropy d = p4 - q4
(a1 - a2 = d t^4 + O(t^6)).  d = 0 is the biaxial (U(2)-invariant) sub-family.

Integration in L_i = log a_i, y_i = L_i':
  y_i' = 6 - y_i^2 - y_i (y_j + y_k) + Pot_i,
  Pot_i = 2 e^{2L_i-2L_j-2L_k} - 8 e^{-2L_i} sinh^2(L_j - L_k),
constraint y1y2+y2y3+y3y1 = 6 + (1/2) sum Pot_i (monitored).
Asymptotic types: AH (y -> sqrt2 (1,1,1)); ACH with fibre slot k (y -> 1, with y_k -> 2,
kappa_k = a_k/(a_i a_j) -> 1, Rossi ratio rho = a_i/a_j -> const); collapse/singular.

CLI: python einstein_bolt_shoot.py scan  -> grid over (b, d), writes data/einstein_bolt/scan_n1.json
"""
import json, sys, math
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / 'data' / 'einstein_bolt'
RUNS = HERE.parent / 'data' / 'einstein_bolt_runs'


def load_series(n):
    raw = json.loads((DATA / f'series_n{n}.json').read_text())
    sol = {k: eval(v, dict(sp.__dict__)) for k, v in raw.items() if not k.startswith('_')}
    return sol, raw['_free'], raw['_N']


class Bolt:
    def __init__(self, n=1):
        self.n = n
        sol, free, N = load_series(n)
        self.N = N
        b = sp.Symbol('b', positive=True)
        fr = [sp.Symbol(f) for f in free]
        # map free symbols (any naming) -> we parametrize by (b, d) with d = p4 - q4
        names = {str(s) for s in sol}
        allsym = set()
        for v in sol.values():
            allsym |= v.free_symbols
        self.freesyms = sorted([s for s in allsym if str(s) != 'b'], key=str)
        bS = [s for s in allsym if str(s) == 'b']
        self.bsym = bS[0] if bS else b
        rigid = len(self.freesyms) == 0
        assert len(self.freesyms) <= 1, self.freesyms
        f = self.freesyms[0] if not rigid else sp.Symbol('fdummy')
        def coef(name):
            if name in sol:
                return sol[name]
            return sp.Symbol(name) if name != str(f) else f
        P = [coef(f'p{k}') for k in range(1, N+1)]
        Q = [coef(f'q{k}') for k in range(1, N+1)]
        R = [coef(f'r{k}') for k in range(2, N+2)]
        # resolve symbols with names equal to free symbol
        def fix(e):
            if isinstance(e, sp.Symbol) and str(e) == str(f):
                return f
            return e
        if rigid:
            self._fs = lambda b, d: 0.0
        else:
            dexpr = sp.expand(P[3] - Q[3])
            # d is linear in f: f = (d - c0)/c1
            c1 = sp.diff(dexpr, f); c0 = sp.simplify(dexpr - c1*f)
            self._fs = sp.lambdify((self.bsym, sp.Symbol('d')), (sp.Symbol('d') - c0)/c1)
        args = (self.bsym, f)
        self._P = sp.lambdify(args, P); self._Q = sp.lambdify(args, Q); self._R = sp.lambdify(args, R)

    def init(self, b, d, t0):
        fv = self._fs(b, d)
        P = self._P(b, fv); Q = self._Q(b, fv); R = self._R(b, fv)
        N = self.N
        a = [b + sum(P[k-1]*t0**k for k in range(1, N+1)),
             b + sum(Q[k-1]*t0**k for k in range(1, N+1)),
             self.n*t0 + sum(R[k-2]*t0**k for k in range(2, N+2))]
        da = [sum(k*P[k-1]*t0**(k-1) for k in range(1, N+1)),
              sum(k*Q[k-1]*t0**(k-1) for k in range(1, N+1)),
              self.n + sum(k*R[k-2]*t0**(k-1) for k in range(2, N+2))]
        L = [math.log(x) for x in a]
        y = [da[i]/a[i] for i in range(3)]
        return np.array(L + y)


def pots(L):
    L1, L2, L3 = L
    out = []
    for i in range(3):
        j, k = (i+1) % 3, (i+2) % 3
        Li, Lj, Lk = L[i], L[j], L[k]
        out.append(2*math.exp(2*Li-2*Lj-2*Lk) - 8*math.exp(-2*Li)*math.sinh(Lj-Lk)**2)
    return out


def rhs(t, z):
    L = z[:3]; y = z[3:]
    Pt = pots(L)
    dy = [6 - y[i]**2 - y[i]*(y[(i+1) % 3] + y[(i+2) % 3]) + Pt[i] for i in range(3)]
    return np.concatenate([y, dy])


def rhs_sym(t, z):
    """rhs restricted exactly to the biaxial subspace a1 = a2."""
    z = np.array(z, dtype=float)
    z[0] = z[1] = 0.5*(z[0]+z[1]); z[3] = z[4] = 0.5*(z[3]+z[4])
    r = rhs(t, z)
    r[0] = r[1] = 0.5*(r[0]+r[1]); r[3] = r[4] = 0.5*(r[3]+r[4])
    return r


def constraint(z):
    L = z[:3]; y = z[3:]
    return y[0]*y[1] + y[1]*y[2] + y[2]*y[0] - 6 - 0.5*sum(pots(L))


def ev_small(t, z):
    return min(z[:3]) + 40.0  # a_i -> 0 (recollapse)
ev_small.terminal = True


def ev_big(t, z):
    return 60.0 - max(abs(v) for v in z[3:]) * (t > 0.5)
ev_big.terminal = True


def shoot(bolt, b, d, T=14.0, t0=2e-3, dense=False):
    z0 = bolt.init(b, d, t0)
    s = solve_ivp(rhs, (t0, T), z0, method='DOP853', rtol=1e-12, atol=1e-13,
                  events=[ev_small, ev_big], dense_output=dense)
    z = s.y[:, -1]
    tt = s.t
    L = s.y[:3]; y = s.y[3:]
    out = dict(b=b, d=d, tend=float(tt[-1]), status=int(s.status),
               y_end=[float(v) for v in z[3:]],
               con0=float(constraint(z0)), con_end=float(constraint(z)))
    # ACH indicators for each fibre slot k: kappa_k = a_k/(a_i a_j), rho_k = a_i/a_j
    for k in range(3):
        i, j = (k+1) % 3, (k+2) % 3
        kap = np.exp(L[k] - L[i] - L[j])
        rho = np.exp(L[i] - L[j])
        out[f'kappa{k+1}_end'] = float(kap[-1]); out[f'rho{k+1}_end'] = float(rho[-1])
        # time spent with y_k in (1.8,2.2) and others in (0.8,1.2)
        m = (np.abs(y[k]-2) < .2) & (np.abs(y[i]-1) < .2) & (np.abs(y[j]-1) < .2)
        out[f'ach{k+1}_time'] = float(np.sum(np.diff(tt)[m[1:]])) if len(tt) > 1 else 0.0
    out['AH'] = bool(s.status == 0 and np.allclose(z[3:], math.sqrt(2), atol=2e-2))
    if dense:
        out['_sol'] = s
    return out


def classify(o):
    if o['status'] == 1:
        return 'singular'
    if o['AH']:
        return 'AH'
    y = o['y_end']
    for k in range(3):
        if abs(y[k]-2) < .05 and all(abs(y[m]-1) < .05 for m in range(3) if m != k):
            return f'ACH{k+1}'
    return 'other'


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'scan'
    bolt = Bolt(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    if mode == 'scan':
        bs = np.geomspace(0.05, 4.0, 25)
        ds = np.concatenate([-np.geomspace(1e3, 1e-2, 21), [0.0], np.geomspace(1e-2, 1e3, 21)])
        res = []
        for b in bs:
            for d in ds:
                try:
                    o = shoot(bolt, float(b), float(d))
                    o['type'] = classify(o)
                except Exception as e:  # noqa
                    o = dict(b=float(b), d=float(d), type='error', err=str(e))
                res.append(o)
            row = [r['type'][:5] for r in res[-len(ds):]]
            print(f'b={b:.3f}', ' '.join(row), flush=True)
        (RUNS / f'scan_n{bolt.n}.json').write_text(json.dumps(res, indent=0))
    elif mode == 'biax':
        # exact U(2)-invariant sub-family (a1 = a2 enforced in the data): AH squashing s = lim a3/a1
        bs = [float(v) for v in sys.argv[3].split(',')]
        out = []
        for b in bs:
            z0 = bolt.init(b, 0.0, 2e-3)
            z0[0] = z0[1] = 0.5*(z0[0]+z0[1]); z0[3] = z0[4] = 0.5*(z0[3]+z0[4])
            s = solve_ivp(rhs_sym, (2e-3, 16.0), z0, method='DOP853', rtol=1e-12, atol=1e-13,
                          events=[ev_small, ev_big], dense_output=True)
            tt = np.linspace(s.t[0], s.t[-1], 3000); Z = s.sol(tt)
            L = Z[:3]; y = Z[3:]
            dev3 = np.sqrt((y[0]-1)**2 + (y[1]-1)**2 + (y[2]-2)**2)
            rec = dict(b=b, status=int(s.status), y_end=[float(v) for v in s.y[3:, -1]],
                       squash_end=float(np.exp(L[2]-L[0])[-1]),
                       kappa3_max=float(np.max(np.exp(L[2]-L[0]-L[1]))),
                       min_dev_ACH3=float(dev3.min()), t_min=float(tt[np.argmin(dev3)]),
                       asym_end=float(L[0][-1]-L[1][-1]))
            print(json.dumps(rec), flush=True); out.append(rec)
        (RUNS / f'biax_n{bolt.n}.json').write_text(json.dumps(out, indent=1))
    elif mode == 'one':
        b, d = float(sys.argv[3]), float(sys.argv[4])
        o = shoot(bolt, b, d); o['type'] = classify(o)
        print(json.dumps(o, indent=1))
    elif mode == 'bisect':
        # for each b: find the AH -> singular transition in d > 0 and bisect it;
        # report the plateau near ACH1 (fibre slot 1) and its Rossi ratio a2/a3.
        bs = [float(v) for v in sys.argv[3].split(',')]
        T = float(sys.argv[4]) if len(sys.argv) > 4 else 14.0
        out = []
        for b in bs:
            ds = np.geomspace(1e-10, 10, 111)
            prev = None; lo = hi = None
            for d in ds:
                ty = classify(shoot(bolt, b, float(d), T=T))
                if prev == 'AH' and ty != 'AH':
                    lo, hi = dprev, float(d); hity = ty; break
                prev, dprev = ty, float(d)
            if lo is None:
                print('b', b, 'no transition; last type', prev, flush=True); out.append(dict(b=b, found=False)); continue
            for _ in range(70):
                mid = 0.5*(lo+hi)
                if mid in (lo, hi):
                    break
                ty = classify(shoot(bolt, b, mid, T=T))
                if ty == 'AH':
                    lo = mid
                else:
                    hi = mid
            o = shoot(bolt, b, lo, T=T, dense=True); s = o.pop('_sol')
            oh = shoot(bolt, b, hi, T=T)
            tt = np.linspace(s.t[0], s.t[-1], 4000); Z = s.sol(tt)
            L = Z[:3]; y = Z[3:]
            dev = np.sqrt((y[0]-2)**2 + (y[1]-1)**2 + (y[2]-1)**2)
            imin = int(np.argmin(dev))
            m = dev < 0.05
            rec = dict(b=b, found=True, d_lo=lo, d_hi=hi, hi_type=hity, min_dev=float(dev[imin]), t_min=float(tt[imin]),
                       plateau_len=float(np.sum(m)*(tt[1]-tt[0])),
                       kappa1_at_min=float(np.exp(L[0]-L[1]-L[2])[imin]),
                       rossi_a2_over_a3_at_min=float(np.exp(L[1]-L[2])[imin]),
                       y_at_min=[float(v) for v in y[:, imin]],
                       lo_end=o['y_end'], hi_end=oh['y_end'], con_end=o['con_end'])
            if m.any():
                rr = np.exp(L[1]-L[2])[m]; kk = np.exp(L[0]-L[1]-L[2])[m]
                rec['rossi_plateau_range'] = [float(rr.min()), float(rr.max())]
                rec['kappa1_plateau_range'] = [float(kk.min()), float(kk.max())]
            print(json.dumps(rec), flush=True)
            out.append(rec)
        tag = sys.argv[5] if len(sys.argv) > 5 else 'bisect'
        (RUNS / f'{tag}_n{bolt.n}.json').write_text(json.dumps(out, indent=1))
