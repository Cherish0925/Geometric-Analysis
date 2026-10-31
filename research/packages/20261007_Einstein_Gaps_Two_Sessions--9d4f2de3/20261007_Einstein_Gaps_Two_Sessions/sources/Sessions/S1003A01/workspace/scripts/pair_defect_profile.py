"""Radial decomposition of the Einstein defect E = Ric + 6g of the frozen perpendicular cell
into U(2)-invariant and weight-two parts (S1003A01 Step 13).

E = diag(E0, E1, E2, E3) in the cell orthonormal frame (radial, bolt slot, contact slot,
CH fibre).  Under the residual U(1) phase the contact-plane block splits as
    m = (E1+E2)/2 (invariant),   d = (E1-E2)/2 (weight two),
so |E|^2 = E0^2 + E3^2 + 2 m^2 + 2 d^2.  Writes CSV of r, E0, m, d, E3, and the cumulative
energies of the invariant and weight-two parts (normalised by 8 pi^2), plus a figure.
Usage: python pair_defect_profile.py RECORD.json OUTPREFIX
"""
import json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
from flint import arb, acb, ctx
from perp_rigorous_enclosure import FrozenCell
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

rec = json.loads(Path(sys.argv[1]).read_text()); pre = sys.argv[2]
ctx.prec = 80
cell = FrozenCell(rec)
X = float(rec['X']); x0 = 0.01; ell = math.log(X/x0)
us = np.linspace(0.0005, 1.0, 1600)
rows = []
for u in us:
    R, vol = cell.ricci(acb(arb(float(u))))
    E = [float((r+6).real.mid()) for r in R]; v = float(vol.real.mid())
    x = x0*math.exp(ell*u)
    rows.append([u, math.asinh(math.sqrt(x)), E[0], (E[1]+E[2])/2, (E[1]-E[2])/2, E[3], v])
A = np.array(rows)
u, r, E0, m, d, E3, vol = A.T
inv = vol*(E0**2 + E3**2 + 2*m*m); wt2 = vol*2*d*d
cinv = np.concatenate([[0], np.cumsum(0.5*(inv[1:]+inv[:-1])*np.diff(u))])
cw2 = np.concatenate([[0], np.cumsum(0.5*(wt2[1:]+wt2[:-1])*np.diff(u))])
out = np.column_stack([u, r, E0, m, d, E3, cinv, cw2])
np.savetxt(pre + '.csv', out, delimiter=',', header='u,r_CH,E0,m,d,E3,cum_inv_over_8pi2,cum_wt2_over_8pi2', comments='')
summ = dict(total_inv=float(cinv[-1]), total_wt2=float(cw2[-1]),
            tail_r_gt_1=dict(inv=float(cinv[-1]-np.interp(1.0, r, cinv)), wt2=float(cw2[-1]-np.interp(1.0, r, cw2))),
            d_sign_changes_r=[float(r[i]) for i in range(1, len(r)) if d[i]*d[i-1] < 0])
Path(pre + '_summary.json').write_text(json.dumps(summ, indent=1)+'\n'); print(json.dumps(summ, indent=1))
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
msk = r > 0.6
for y, lab in [(E0, r'$E_{00}$ (radial)'), (m, r'$m=(E_{11}+E_{22})/2$'), (d, r'$d=(E_{11}-E_{22})/2$ (weight two)'), (E3, r'$E_{33}$ (CH fibre)')]:
    ax[0].plot(r[msk], y[msk], label=lab)
ax[0].axhline(0, color='k', lw=.5); ax[0].set_xlabel(r'CH geodesic radius $r$'); ax[0].set_ylabel(r'orthonormal component of $\mathrm{Ric}+6g$')
ax[0].set_title('tail defect of the certified $X=8$ cell'); ax[0].legend(fontsize=8)
ax[1].semilogy(r, np.maximum(cinv[-1]-cinv, 1e-16), label='invariant energy beyond r')
ax[1].semilogy(r, np.maximum(cw2[-1]-cw2, 1e-16), label='weight-two energy beyond r')
ax[1].set_xlabel(r'$r$'); ax[1].set_ylabel(r'$\int_{r}^{\rho}|E|^2\,dV/(8\pi^2)$'); ax[1].legend(fontsize=8)
fig.tight_layout(); fig.savefig(pre + '.png', dpi=160)
