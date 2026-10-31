"""Two-chirality pathwise lower bounds along saturation trajectories.

For a diagonal annulus, both localized chiral identities
   P_hat[a,t] = b_pm(t) - b_pm(a) + (1/2pi^2) int |W^pm|^2 + (1/96pi^2) int s^2
hold, hence for every convex weight lam in [0,1]
   P_hat[a,t] >= b_lam(t) - b_lam(a),  b_lam = lam b_+ + (1-lam) b_-.
Since b_lam is affine in lam, the best pathwise bound is
   max_t max(b_+(t)-b_+(a), b_-(t)-b_-(a)).
This script evaluates the bound on optimized trajectories and checks the b_- normalization
on CH orbits (2-3 sinh^4 t) and on the round flat orbit (2).
Usage: python chiral_two_sided_bound.py file1.json ...
Output: workspace/data/saturation_control/two_sided_bounds.json
"""
import json, math, sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE.parent/'data'/'saturation_control'/'two_sided_bounds.json'


def charges(X):
    x, z, p, chi, eta = X
    q = -3*math.log(z); beta = x+q/2; xi = chi+eta/2
    af = math.exp(2*beta/3); ag = math.exp(-beta/3+q/2); ah = math.exp(-beta/3-q/2)
    pf = af*(p+2*xi/3); pg = ag*(p-xi/3+eta/2); ph = ah*(p-xi/3-eta/2)
    gf = (ag*ag+ah*ah-af*af)/(ag*ah); gg = (ah*ah+af*af-ag*ag)/(ah*af); gh = (af*af+ag*ag-ah*ah)/(af*ag)
    u = np.array([pf-gf, pg-gg, ph-gh]); w = np.array([pf+gf, pg+gg, ph+gh])
    return 2-u@u-np.prod(u), w@w-np.prod(w)-2


def ch_state(t):
    s, c = math.sinh(t), math.cosh(t)
    r = s*c**(1/3)
    return [math.log(c), 1.0, r*(c/s+math.tanh(t)/3), r*math.tanh(t), 0.0]


def main(paths):
    checks = {'CH': [[t, *charges(ch_state(t)), 2-9*math.sinh(t)**4, 2-3*math.sinh(t)**4] for t in (0.3, 0.7, 1.5)]}
    rows = []
    for f in paths:
        r = json.loads(Path(f).read_text())
        X = np.array(r['X'])
        if 'cumulative_cost' in r:
            cum = np.array(r['cumulative_cost'])
        else:  # trapezoid reconstruction from node controls
            U = np.array(r['U']); h = r['T']/r['N']
            L = 3*U[:, 0]**2/16+U[:, 1]**2/6+U[:, 2]**2/8
            cum = np.concatenate([[0], np.cumsum(h*(L[1:]+L[:-1])/2)])
        bb = np.array([charges(xx) for xx in X])
        dp = bb[:, 0]-bb[0, 0]; dm = bb[:, 1]-bb[0, 1]
        rows.append({'file': Path(f).name, 'cost': r['cost'], 'bplus0': bb[0, 0], 'bminus0': bb[0, 1],
                     'max_dbplus': float(dp.max()), 'max_dbminus': float(dm.max()),
                     'two_sided_bound': float(max(dp.max(), dm.max())),
                     'max_bminus': float(bb[:, 1].max()),
                     'min_slack_minus': float(np.min((cum-dm)[1:])), 'min_slack_plus': float(np.min((cum-dp)[1:]))})
    out = {'checks': checks, 'rows': rows}
    print(json.dumps(out, indent=1))
    OUT.write_text(json.dumps(out, indent=1)+'\n')


if __name__ == '__main__':
    main(sys.argv[1:])
