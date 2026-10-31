import json, math, sys
from pathlib import Path
import numpy as np
from scipy.integrate import cumulative_simpson
sys.path.insert(0, '.')
from flint import arb, acb, ctx
from perp_rigorous_enclosure import FrozenCell
ctx.prec = 80
rec = json.loads(Path('../data/perp_collar/x0.01_X8_J_d8.json').read_text())
x0 = .01; X = 8.; ell = math.log(X/x0); cell = FrozenCell(rec, x0=x0)
for n in [4001, 12001]:
    v = np.linspace(0, 1, n)[:12]; v[0] = 1e-7
    out = []
    for vv in v:
        u = vv*vv; R, vol, pr = cell.ricci(acb(arb(u)), want_profile=True)
        f = lambda z: float(z.real.mid())
        x = f(pr['x']); y = x0*math.expm1(ell*u)
        F = y*f(pr['FH']); G = y*f(pr['GH']); w = f(pr['w'])
        out.append([x, y, F, G, w])
    x, y, F, G, w = np.array(out).T
    dtdv = ell*x*v/np.sqrt(G)
    t = cumulative_simpson(dtdv, x=v, initial=0.0)
    W = np.sqrt(F*x*x*np.exp(w))
    print(n, 'dtdv', dtdv[:4], 't', t[1:4], 'v*dtdv0', v[1:4]*dtdv[0])
    print(' a1/t', np.sqrt(F[1:6])/t[1:6], ' W/(b2 t)', W[1:6]/(x0*t[1:6]))
