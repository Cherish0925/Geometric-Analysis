"""Complete fate enumeration of O(-1) bolt Einstein orbits at fixed b (anisotropy-resolving variables).

For d on a signed logarithmic grid, classify the forward orbit as AH (y -> sqrt2), SING (blow-up event),
or OTHER.  Every change of fate between neighbouring grid points brackets a separatrix; each is bisected
(60 steps, relative) and the bisected orbit is read: closest approach (over t) to each ACH_k equilibrium
curve E_k(q) = (y_k=2, others 1, kappa_k = 1), and the Rossi readout Phi~ at closest approach.
CLI: python ach_fate_enum.py b  -> data/ach_fate/fate_b<b>.json
"""
import json, sys, math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from ach_projected import init_md, rhs_md, md_to_Ly, CYC, to_compact

OUT = Path(__file__).resolve().parents[1] / 'data' / 'ach_fate'
OUT.mkdir(parents=True, exist_ok=True)
T = 16.0


def run(b, d, dense=False):
    X0 = init_md(b, d, 2e-3)
    def ev_big(t, X):
        return 60.0 - max(abs(v) for v in md_to_Ly(X)[3:]) * (t > 0.5)
    ev_big.terminal = True
    s = solve_ivp(rhs_md, (2e-3, T), X0, method='DOP853', rtol=1e-12, atol=1e-30, events=[ev_big],
                  dense_output=dense)
    z = md_to_Ly(s.y[:, -1])
    if s.status == 1:
        fate = 'SING'
    elif np.allclose(z[3:], math.sqrt(2), atol=2e-2):
        fate = 'AH'
    else:
        fate = 'OTHER'
    return fate, s


def readout(s):
    tt = np.linspace(s.t[0], s.t[-1], 6000)
    Z = np.array([md_to_Ly(x) for x in s.sol(tt).T])
    out = {}
    for f in range(3):
        W = np.array([to_compact(z, f) for z in Z])
        dev = np.sqrt((W[:, 0]-2)**2 + (W[:, 1]-1)**2 + (W[:, 2]-1)**2 + (W[:, 3]-1)**2)
        i = int(np.argmin(dev))
        phi = W[i, 4] + (W[i, 1]-W[i, 2])/4 - W[i, 5]*math.sinh(W[i, 4])
        out[f'ACH{f+1}'] = dict(min_dev=float(dev[i]), t=float(tt[i]), zeta=float(W[i, 5]), rho=math.exp(phi))
    return out


def enum(b):
    mags = np.geomspace(1e-12, 1e3, 181)
    ds = np.concatenate([-mags[::-1], [0.0], mags])
    fates = [run(b, float(d))[0] for d in ds]
    seps = []
    for i in range(len(ds)-1):
        if fates[i] != fates[i+1]:
            lo, hi, flo = float(ds[i]), float(ds[i+1]), fates[i]
            for _ in range(60):
                mid = 0.5*(lo+hi) if lo*hi <= 0 else math.copysign(math.sqrt(lo*hi), lo)
                if mid in (lo, hi):
                    break
                if run(b, mid)[0] == flo:
                    lo = mid
                else:
                    hi = mid
            fl, sl = run(b, lo, dense=True)
            seps.append(dict(d_lo=lo, d_hi=hi, fates=[fates[i], fates[i+1]], read=readout(sl)))
    return dict(b=b, n=len(ds), fate_counts={k: fates.count(k) for k in set(fates)}, separatrices=seps)


if __name__ == '__main__':
    b = float(sys.argv[1])
    r = enum(b)
    print(json.dumps(r))
    (OUT / f'fate_b{b:g}.json').write_text(json.dumps(r, indent=1))
