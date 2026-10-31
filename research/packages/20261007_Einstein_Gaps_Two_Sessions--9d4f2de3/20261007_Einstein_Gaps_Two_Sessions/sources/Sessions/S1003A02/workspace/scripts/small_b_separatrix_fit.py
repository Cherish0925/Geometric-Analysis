"""Small-bolt asymptotics of the perpendicular ACH Einstein separatrix on O(-1).

Reads data/ach_fate/fate_b*.json, extracts the positive separatrix d* (AH/SING change of smallest |d|)
and its closest-approach Rossi readout rho, and fits
   log d* = -kappa/b + gamma*log b + c
with kappa fixed to the matched-asymptotic prediction pi*sqrt(3/2) (collapsed Taub-bolt circle
a3 ~ 4n cosh(sqrt2 t), n = b/(2 sqrt3), q-mode rate 4/a3), and also with kappa free.
Output: data/small_b_separatrix_fit.json
"""
import json, math
from pathlib import Path
import numpy as np

D = Path(__file__).resolve().parents[1] / 'data'
rows = []
for f in sorted((D / 'ach_fate').glob('fate_b*.json')):
    r = json.loads(f.read_text())
    seps = [s for s in r['separatrices'] if set(s['fates']) == {'AH', 'SING'} and s['d_lo'] > 0]
    if not seps:
        continue
    s = min(seps, key=lambda s: s['d_lo'])
    acc = min(s['read'].values(), key=lambda v: v['min_dev'])
    rows.append(dict(b=r['b'], d=s['d_lo'], rho=acc['rho'], min_dev=acc['min_dev']))
rows.sort(key=lambda x: x['b'])
kappa = math.pi*math.sqrt(1.5)
use = [x for x in rows if x['b'] <= 0.4 and x['min_dev'] < 1e-2]
b = np.array([x['b'] for x in use]); ld = np.log([x['d'] for x in use])
A = np.vstack([np.log(b), np.ones_like(b)]).T
g_fixed, c_fixed = np.linalg.lstsq(A, ld + kappa/b, rcond=None)[0]
A3 = np.vstack([-1/b, np.log(b), np.ones_like(b)]).T
k_free, g_free, c_free = np.linalg.lstsq(A3, ld, rcond=None)[0] if len(b) >= 3 else (None,)*3
out = dict(rows=rows, used=[x['b'] for x in use], kappa_pred=kappa,
           fixed_kappa_fit=dict(gamma=g_fixed, c=c_fixed,
                                residuals=list(ld - (-kappa/b + g_fixed*np.log(b) + c_fixed))),
           free_fit=dict(kappa=k_free, gamma=g_free, c=c_free),
           rho_times_b=[(x['b'], x['rho']*x['b']) for x in rows])
print(json.dumps(out, indent=1, default=float))
(D / 'small_b_separatrix_fit.json').write_text(json.dumps(out, indent=1, default=float))
