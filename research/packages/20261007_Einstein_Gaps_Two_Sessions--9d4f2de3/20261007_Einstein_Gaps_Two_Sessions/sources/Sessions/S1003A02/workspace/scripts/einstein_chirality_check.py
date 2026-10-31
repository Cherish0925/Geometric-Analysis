"""Pointwise Weyl-chirality check for the Step-13 Einstein bolt shoots.

The Einstein ODE is integrated as in einstein_bolt_shoot.py.  At selected times we
reconstruct a local quadratic jet
  dt^2 + sum_i a_i(t)^2 sigma_i^2
and evaluate the two Weyl blocks with the independent coordinate/JAX curvature
routine from o11_rotated_cell.py.  Curvature only uses the 2-jet, so the local
quadratic reconstruction is exact at its centre up to roundoff.

Also checks the complex-hyperbolic model.  Output is a compact JSON artifact.
"""
import json
from pathlib import Path
import numpy as np
import jax
import jax.numpy as jnp
jax.config.update("jax_enable_x64", True)
from scipy.integrate import solve_ivp

from einstein_bolt_shoot import Bolt, rhs
from o11_rotated_cell import euler_E, curvature_scalars

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RUNS = ROOT / "data" / "einstein_bolt_runs"
OUT = ROOT / "data" / "einstein_bolt_chirality.json"


def local_curvature(a, ap, app):
    """Return (s,|Ric0|^2,|W_A|^2,|W_B|^2) from one radial 2-jet."""
    a = jnp.asarray(a, dtype=jnp.float64)
    ap = jnp.asarray(ap, dtype=jnp.float64)
    app = jnp.asarray(app, dtype=jnp.float64)
    def axes(r):
        return a + ap*r + 0.5*app*r*r
    def metric(y):
        aa = axes(y[0])
        E = euler_E(y[1:])
        g = jnp.zeros((4, 4), dtype=jnp.float64).at[0, 0].set(1.0)
        return g.at[1:, 1:].set(E.T @ jnp.diag(aa*aa) @ E)
    y = jnp.array([0.0, 0.37, 1.13, 0.71], dtype=jnp.float64)
    return np.asarray(curvature_scalars(metric, y), dtype=float)


def jet_from_state(z):
    L = np.asarray(z[:3], float); yy = np.asarray(z[3:], float)
    dy = np.asarray(rhs(0.0, z)[3:], float)
    a = np.exp(L); ap = a*yy; app = a*(dy + yy*yy)
    return a, ap, app


def check_ch(times=(0.25, 0.8, 1.7)):
    rows = []
    for t in times:
        s, c = np.sinh(t), np.cosh(t)
        a = np.array([s, s*c, s])
        ap = np.array([c, np.cosh(2*t), c])
        app = np.array([s, 2*np.sinh(2*t), s])
        curv = local_curvature(a, ap, app)
        rows.append(dict(t=t, scalar=curv[0], ric0sq=curv[1], WA2=curv[2], WB2=curv[3]))
    return rows


def load_record(path, index=0):
    recs = json.loads(Path(path).read_text())
    return recs[index] if isinstance(recs, list) else recs


def check_bolt(record_path, index=0, sample_times=None):
    rec = load_record(record_path, index)
    b = float(rec["b"]); d = float(rec["d_lo"])
    bolt = Bolt(1); t0 = 2e-3
    sol = solve_ivp(rhs, (t0, 6.0), bolt.init(b, d, t0), method="DOP853",
                    rtol=2e-13, atol=2e-14, dense_output=True)
    if sample_times is None:
        tm = float(rec["t_min"])
        sample_times = [0.08, 0.2, 0.5, 1.0, min(2.0, 0.65*tm), tm]
    rows = []
    for t in sample_times:
        z = sol.sol(float(t)); a, ap, app = jet_from_state(z)
        curv = local_curvature(a, ap, app)
        rows.append(dict(t=float(t), axes=a.tolist(), y=z[3:].tolist(),
                         scalar=curv[0], ric0sq=curv[1], WA2=curv[2], WB2=curv[3],
                         chirality_ratio=float(min(curv[2], curv[3])/max(curv[2], curv[3]))))
    return dict(source=str(record_path), index=index, b=b, d=d,
                constraint_end=None, rows=rows)


def main():
    cases = [
        (RUNS / "bisR_0.8,0.85_n1.json", 0),
        (RUNS / "bisR_0.35,0.45_n1.json", 0),
        (RUNS / "bis_3,4_n1.json", 1),
    ]
    out = {"CH": check_ch(), "bolt_cases": [check_bolt(p, i) for p, i in cases]}
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
