"""Step 37c: angular localization of the cap excess of the congruence-transported cell.

For shells (r0,r1), evaluate the defect density (per Euclidean measure, times shell volume)
of G=L bar_g L with outer=cap and outer=ch on the same Sobol nodes, and bin the
difference by c2=(|z1|^2-|z2|^2)/r^2 (c2=+1: divisor directions, c2=-1: normal directions).
Output JSON with per-bin mean excess contribution to D/(8 pi^2).
"""
import json, math, sys
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import step36_cap_perp_transplant as s36  # noqa: E402
import step37_cap_congruence_transport as s37  # noqa: E402
from perp_dual_cost import load_record  # noqa: E402

rec = load_record(sys.argv[1]); out = sys.argv[2]
a, b = 0.45, 0.7
res = {}
fs = {}
for o in ["cap", "ch"]:
    cell, zz, prof, metric, Rc = s37.build(rec, o, a, b)
    fs[o] = jax.jit(jax.vmap(s36.point_fields(metric, s36.ricci_of(metric)), in_axes=(0, None, None, None)))
K = 8*np.pi**2
bins = np.linspace(-1, 1, 9)
for (r0, r1) in [(0.45, 0.7), (0.7, 1.2), (1.2, 2.0), (2.0, 3.0), (3.0, 4.0), (4.0, 5.0), (5.0, 6.0), (6.0, 7.645)]:
    pts, vol = s36.qmc_annulus(r0, r1, 13, 5)
    vals = {o: np.concatenate([np.asarray(fs[o](jnp.asarray(pts[i:i+2048]), jnp.zeros(3), a, b)) for i in range(0, len(pts), 2048)]) for o in fs}
    z1 = pts[:, 0]**2+pts[:, 1]**2; z2 = pts[:, 2]**2+pts[:, 3]**2
    c2 = (z1-z2)/(z1+z2)
    d = (vals["cap"][:, 0]-vals["ch"][:, 0])*vol/len(pts)/K
    dP = (vals["cap"][:, 1]-vals["ch"][:, 1])*vol/len(pts)/K
    idx = np.clip(np.digitize(c2, bins)-1, 0, len(bins)-2)
    per = [float(d[idx == k].sum()) for k in range(len(bins)-1)]
    res[f"{r0}-{r1}"] = dict(total_excess=float(d.sum()), total_excess_P=float(dP.sum()),
                             excess_by_c2_bin=per, ch=float(vals["ch"][:, 0].sum()*vol/len(pts)/K),
                             cap=float(vals["cap"][:, 0].sum()*vol/len(pts)/K))
    print(r0, r1, json.dumps(res[f"{r0}-{r1}"]), flush=True)
Path(out).write_text(json.dumps(dict(bins=bins.tolist(), a=a, b=b, shells=res,
                                     note="c2=+1 divisor directions; uniform Euclidean measure on S^3 gives uniform c2"), indent=1)+"\n")
