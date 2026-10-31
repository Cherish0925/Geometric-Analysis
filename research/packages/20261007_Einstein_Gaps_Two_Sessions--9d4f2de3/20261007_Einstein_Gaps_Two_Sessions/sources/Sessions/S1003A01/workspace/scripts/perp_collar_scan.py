"""Collar-radius dependence of the fixed-slot perpendicular complex-hyperbolic cell.

The exact infimum over cells with exact CH collar beyond X is nonincreasing in X (a cell with
collar X is admissible for every X' > X).  The second-order perpendicular margin seen at X = 1
must therefore be tested for its X-dependence: a margin that shrinks to zero or changes sign as
X grows would locate the subthreshold mechanism in the background-response (spectral) channel.
Usage: python perp_collar_scan.py x0 X deg target nq out.json
"""
import sys, json, time
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
here = Path(__file__).resolve().parent
sys.path.insert(0, str(here))
from perp_dual_cost import DualCell
from scipy.optimize import minimize

x0, X, deg, target, nq, out = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), sys.argv[6]
c = DualCell(x0, X, deg, deg, nq)
c.aligned = False; c.wpow = 2
f = jax.jit(lambda z: c.target(z, target)); g = jax.jit(jax.grad(lambda z: c.target(z, target)))
z0 = np.zeros(c.nparam); t0 = time.time()
res = minimize(lambda z: float(f(jnp.array(z))), z0, jac=lambda z: np.array(g(jnp.array(z))),
               method='L-BFGS-B', options=dict(maxiter=6000, ftol=1e-16, gtol=1e-12, maxls=80))
p, j, q = [float(v) for v in c.costs(jnp.array(res.x))]
rec = dict(x0=x0, X=X, deg=deg, target=target, nq=nq, P=p, J=j, scalar=q,
           P_margin_over_x0sq=(p - 1) / x0**2, J_margin_over_x0sq=(j - 1) / x0**2,
           success=bool(res.success), nit=int(res.nit), grad_inf=float(np.max(np.abs(res.jac))),
           z=[float(v) for v in res.x], sec=time.time() - t0)
print(json.dumps(rec)); Path(out).write_text(json.dumps(rec) + '\n')
