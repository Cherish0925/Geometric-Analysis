"""Cross-check of the exact Kaehler period identity against the peer's independent coordinate-curvature
code (S1003A02 o11_rotated_cell.Cell, read-only import).  The peer base profile (z=0) is exactly the
four-constant extremal Kaehler interpolation, so its P must equal
   (1+3 kappa x0)^2 + (1/2) I_min(x0,X,kappa)   from kahler_cell_infimum.py.
"""
import sys, json
from pathlib import Path
here = Path(__file__).resolve()
sys.path.insert(0, str(here.parents[3] / 'S1003A02' / 'workspace' / 'scripts'))
sys.path.insert(0, str(here.parent))
import numpy as np
import jax.numpy as jnp
from o11_rotated_cell import Cell, PI
from o11_general_bulk_cell import kahler_K_signed
from kahler_cell_infimum import extremal

out = []
for x0, X, k in [(0.001, 0.25, -1.0), (0.01, 0.25, -1.0), (0.01, 0.25, 1.0), (0.05, 0.5, -1.0)]:
    K = kahler_K_signed(x0, X, k)
    c = Cell(x0, X, 8, 0, 0, 0.05, 600, K=K)
    P_curv = float(c.P(jnp.zeros(c.nparam), 0.0))
    s, r0, wa, wb, dv = c.fields(jnp.zeros(c.nparam), 0.0)
    J_curv = P_curv + float(jnp.sum((s + 24 * k)**2 / 4 * dv * c.wx)) / (8 * PI**2)
    ex = extremal(x0, X, k)
    row = dict(x0=x0, X=X, kappa=k, P_curvature_code=P_curv, P_period_formula=ex['P_inf'],
               J_curvature_code=J_curv, J_period_formula=ex['J_inf'])
    out.append(row); print(json.dumps(row))
(here.parents[1] / 'data' / 'kahler_cells' / 'peer_crosscheck.json').write_text(json.dumps(out, indent=1))
