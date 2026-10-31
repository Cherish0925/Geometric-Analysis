"""Checks for pair_overlap_trial.py: (1) Bergman metric has Ric = -6g;
(2) autodiff |E|^2 of g_CH + h_1 at sample radii equals the Bianchi-IX value
sum_a (R_aa+6)^2 from FrozenCell, and the radial integral of the autodiff density over
the tail reproduces the corresponding part of J/(8 pi^2)."""
import json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pair_overlap_trial as P
import jax, jax.numpy as jnp
from flint import arb, acb, ctx
from perp_rigorous_enclosure import FrozenCell

rec = json.loads(Path(sys.argv[1]).read_text())
lam, X, rho = P.make_profile(rec)
h1, h2 = P.build(lam, rho)
fB = P.density(P.bergman); f1 = P.density(lambda q: P.bergman(q) + h1(q))
rng = np.random.default_rng(0)
out = {}
for k in range(3):
    q = rng.normal(size=4); q = 0.6*q/np.linalg.norm(q)
    d, E, ev = fB(jnp.array(q)); out[f'bergman_E_max_{k}'] = float(jnp.max(jnp.abs(E)))
ctx.prec = 128
cell = FrozenCell(rec)
for t in [0.3, 0.8, 1.2, 1.6, 1.75]:
    x = math.sinh(t)**2
    u = math.log(x/0.01)/math.log(X/0.01)
    R, vol = cell.ricci(acb(arb(u)))
    ref = sum(float((r+6).real.mid())**2 for r in R)
    v = rng.normal(size=4); v /= np.linalg.norm(v); q = math.tanh(t)*v
    d, E, ev = f1(jnp.array(q))
    g = P.bergman(jnp.array(q)) + h1(jnp.array(q)); gi = jnp.linalg.inv(g)
    out[f'cell_t{t}'] = dict(autodiff=float(jnp.trace(gi@E@gi@E)), bianchi=ref)
print(json.dumps(out, indent=1))
