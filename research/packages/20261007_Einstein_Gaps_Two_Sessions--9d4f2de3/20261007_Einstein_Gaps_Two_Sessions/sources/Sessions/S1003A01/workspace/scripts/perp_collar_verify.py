"""Independent verification of large-collar perpendicular CH cells with P or J below 8 pi^2.

For a record from perp_collar_scan.py (x0, X, deg, z):
  (1) peer coordinate-curvature P, J at several quadrature sizes (nq);
  (2) the Cartan-verified spin formula (1.4) of the Step-7 note for P and the independent scalar square,
      with split Gauss quadrature in log x;
  (3) the relative calibration identity  P/(8pi^2) = 1 + S1+S2+S3+cubic;
  (4) metric positivity (F, G, x e^{+-w}) on a fine grid, bolt jets F(x0)=G(x0)=0, F'G'(x0)=1, w(x0)=0,
      and exact collar values at X.
Usage: python perp_collar_verify.py RECORD [out.json]
"""
import sys, json
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
here = Path(__file__).resolve().parent
sys.path.insert(0, str(here))
from perp_dual_cost import DualCell
import perp_spin_diagnostics as psd

rec = json.loads(Path(sys.argv[1]).read_text().strip().splitlines()[-1])
x0, X, deg = rec['x0'], rec['X'], rec['deg']
z = jnp.array(rec['z'])
out = dict(source=sys.argv[1], x0=x0, X=X, deg=deg, target=rec['target'])
curv = {}
for nq in (600, 1200, 2400):
    c = DualCell(x0, X, deg, deg, nq); c.aligned = False; c.wpow = 2
    p, j, q = [float(v) for v in c.costs(z)]
    curv[nq] = dict(P=p, J=j)
out['curvature_code'] = curv
c = DualCell(x0, X, deg, deg, 600); c.aligned = False; c.wpow = 2
for n in (1200, 3000):
    e, w = np.polynomial.legendre.leggauss(n // 3)
    pieces = [(0.0, 0.05), (0.05, 0.4), (0.4, 1.0)]
    us = np.concatenate([a + (b - a) * (e + 1) / 2 for a, b in pieces])
    wu = np.concatenate([(b - a) * w / 2 for a, b in pieces])
    xs = x0 * np.exp(c.ell * us); W = wu * c.ell * xs
    vals = jax.vmap(lambda x: psd.point(c, z, x))(jnp.asarray(xs))
    u, C, s1, s2, s3, cub, psq, scal = [np.asarray(v) for v in vals[:8]]
    I = lambda y: float(np.sum(W * y))
    out[f'spin_n{n}'] = dict(P=I(psq), J=I(psq) + I(scal), relative=1 + I(s1) + I(s2) + I(s3) + I(cub),
                            S1=I(s1), S2=I(s2), S3=I(s3), cubic=I(cub),
                            cubic_neg=I(np.minimum(cub, 0)), cubic_pos=I(np.maximum(cub, 0)),
                            C_bolt=float(C[0]), C_collar=float(C[-1]))
prof = c.prof_factory(z)
xg = x0 * np.exp(c.ell * np.linspace(0, 1, 20001)[1:])
Gs, hs = jax.vmap(prof)(jnp.asarray(xg))
d = np.asarray(jax.vmap(jnp.diag)(hs))
out['min_over_x'] = dict(G=float(np.min(np.asarray(Gs) / (xg - x0 + 1e-300))),
                         F=float(np.min(d[:, 0] / (xg - x0 + 1e-300))),
                         h2=float(np.min(d[:, 1] / xg)), h3=float(np.min(d[:, 2] / xg)))
Fp = jax.grad(lambda x: prof(x)[1][0, 0]); Gp = jax.grad(lambda x: prof(x)[0])
out['bolt'] = dict(F=float(prof(x0)[1][0, 0]), G=float(prof(x0)[0]), FpGp=float(Fp(x0) * Gp(x0)),
                   w=float(np.log(prof(x0)[1][2, 2] / prof(x0)[1][1, 1])))
GX, hX = prof(X)
out['collar'] = dict(G=float(GX), G_CH=X + X**2, h=[float(v) for v in jnp.diag(hX)], h_CH=[X, X, X + X**2],
                     dG=float(Gp(X)), dG_CH=1 + 2 * X)
text = json.dumps(out, indent=1); print(text)
if len(sys.argv) > 2: Path(sys.argv[2]).write_text(text)
