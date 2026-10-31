"""Large-bolt face limit of the ACH1 Einstein separatrix.

Bisect the AH/SING transition near d ~ 0.9 b for large b and read Phi~ (Rossi) and the
rescaled face variables at fixed t.  Tests the face-limit law
    zeta(t) ~ zeta_1(t)/b,  kappa(t) -> kappa_1(t),  Phi~ - log b -> phi_1(t)
that makes large-bolt standard-CR cells pay a Rossi shift of size log b at volume W ~ b^2.
Output: workspace/data/ach_fate/large_bolt_face_limit.json
"""
import json, math, sys
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ach_fate_enum import run  # noqa: E402
from ach_projected import md_to_Ly, to_compact  # noqa: E402

OUT = HERE.parent/'data'/'ach_fate'/'large_bolt_face_limit.json'
rows = []
for b in [float(v) for v in (sys.argv[1:] or ['20', '50', '100', '200'])]:
    lo, hi = 0.80*b, 1.0*b
    flo, fhi = run(b, lo)[0], run(b, hi)[0]
    if flo == fhi:
        rows.append({'b': b, 'error': f'no bracket {flo} {fhi}'}); print(rows[-1]); continue
    for _ in range(55):
        mid = 0.5*(lo+hi)
        fm = run(b, mid)[0]
        if fm == flo: lo = mid
        else: hi = mid
    d = lo if flo == 'AH' else hi
    fate, s = run(b, d, dense=True)
    ts = [0.25, 0.5, 1.0, 1.5, 2.0, 3.0]
    samp = []
    for t in ts:
        if t > s.t[-1]: break
        z = md_to_Ly(s.sol(t)); C = to_compact(z, 0)
        phi = C[4]+(C[1]-C[2])/4-C[5]*math.sinh(C[4])
        W = math.exp(sum(z[:3]))
        samp.append({'t': t, 'kappa': C[3], 'zeta_b': C[5]*b, 'yf': C[0], 'yg': C[1], 'yh': C[2],
                     'Phi_minus_logb': phi-math.log(b), 'W_over_b2': W/b**2})
    rows.append({'b': b, 'd': d, 'd_over_b': d/b, 'fate_at_d': fate, 'samples': samp})
    print(json.dumps(rows[-1]))
OUT.write_text(json.dumps(rows, indent=1)+'\n')
