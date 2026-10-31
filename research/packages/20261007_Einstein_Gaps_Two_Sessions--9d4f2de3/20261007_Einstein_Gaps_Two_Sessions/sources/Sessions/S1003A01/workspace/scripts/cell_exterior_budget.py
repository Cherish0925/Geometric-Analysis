"""Exterior Einstein-defect budgets for a frozen perpendicular CH cell.

For a cluster made from translated copies g_CH+h_i, suppose the other tails vanish on a
protected core r<r_c of each copy. Positivity gives

    J(cluster) >= sum_i J_i(r<r_c),
    sum_i J(cell_i)-J(cluster) <= sum_i J_i(r>=r_c).

This script computes the one-cell right-hand budget for r_c=rho-w and for selected fixed
cuts.  It is a numerical interpretation tool, not a rigorous enclosure.  Curvature is
evaluated by the cancellation-free FrozenCell formulas used by the Arb certificate.
"""
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy.integrate import cumulative_trapezoid
from flint import acb, arb, ctx
from perp_rigorous_enclosure import FrozenCell


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('record')
    ap.add_argument('--w', default='0.1,0.4,0.6,0.8,1.0,1.2,1.4,1.5,1.6')
    ap.add_argument('--cuts', default='0.8,1.0,1.2')
    ap.add_argument('--n', type=int, default=8001)
    ap.add_argument('--out')
    a = ap.parse_args()
    ctx.prec = 80
    rec = json.loads(Path(a.record).read_text())
    cell = FrozenCell(rec)
    X = float(rec['X']); x0 = 0.01; ell = math.log(X/x0)
    rho = math.asinh(math.sqrt(X)); rbolt = math.asinh(math.sqrt(x0))
    u = np.linspace(0.0, 1.0, a.n)
    dens = np.empty_like(u)
    for k, uk in enumerate(u):
        R, vol = cell.ricci(acb(arb(float(uk))))
        rr = np.array([float(z.real.mid()) for z in R])
        dens[k] = float(vol.real.mid())*np.sum((rr+6.0)**2)
    cum = np.concatenate([[0.0], cumulative_trapezoid(dens, u)])
    total_grid = float(cum[-1])
    total_ref = float(rec.get('J', total_grid))

    def at_cut(r):
        if r <= rbolt: uc = 0.0
        elif r >= rho: uc = 1.0
        else: uc = math.log(math.sinh(r)**2/x0)/ell
        core = float(np.interp(uc, u, cum))
        # use the grid total for an internally consistent positive budget; report reference too
        tail = total_grid-core
        return dict(r_cut=r, u_cut=uc, core_J_over_8pi2=core,
                    exterior_J_over_8pi2=tail,
                    exterior_fraction_of_J=tail/total_grid)

    ws=[]
    for w in [float(s) for s in a.w.split(',') if s]:
        rc=rho-w
        row=at_cut(rc); row.update(w=w, admissible=bool(rc>rbolt))
        ws.append(row)
    cuts=[at_cut(float(s)) for s in a.cuts.split(',') if s]
    out=dict(record=a.record, rho=rho, r_bolt=rbolt, n=a.n,
             total_J_grid_over_8pi2=total_grid, total_J_record_over_8pi2=total_ref,
             grid_minus_record=total_grid-total_ref, overlap_depths=ws, fixed_cuts=cuts)
    text=json.dumps(out,indent=1); print(text)
    if a.out: Path(a.out).write_text(text+'\n')

if __name__=='__main__': main()
