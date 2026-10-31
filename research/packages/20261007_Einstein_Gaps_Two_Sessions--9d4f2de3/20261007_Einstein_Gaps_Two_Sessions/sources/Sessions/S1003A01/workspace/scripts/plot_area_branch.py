"""Figure: bolt-area dependence of the perpendicular CH cell branch (S1003A01 Step 15).
Left: J6/(8 pi^2) of optimized cells versus x0 = b^2 for each collar X.
Right: neutral-observable data at X=64: compliance R_G versus log(1/x0) and the share of P
certified by the bolt-carried Green observable (data/neutral_flux/nf_*X64*).
Writes figures/area_branch.png and data/perp_area/area_table.csv.
"""
import json, glob, math, re
from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
H = Path(__file__).resolve().parents[1]
rows = []
for f in glob.glob(str(H/'data/perp_area/x0*_X*_d*.json')):
    r = json.loads(Path(f).read_text()); rows.append((r['x0'], r['X'], r['deg'], r['J'], r['P'], r['grad_inf']))
for f in ['x0.01_X8_J_d8', 'x00.01_X16_J_d8', 'continued_X16_to_X32_J_d12', 'continued_X32_to_X64_J_d16']:
    r = json.loads((H/'data/perp_collar'/(f+'.json')).read_text()); rows.append((.01, r['X'], r['deg'], r['J'], r['P'], r.get('grad_inf', 0)))
rows.sort()
np.savetxt(H/'data/perp_area/area_table.csv', np.array(rows), delimiter=',', header='x0,X,deg,J,P,grad_inf', comments='')
fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
for X in [8, 16, 32, 64, 128, 256]:
    pts = sorted({(r[0], r[3]) for r in rows if r[1] == X and not (X == 64 and r[2] == 20)})
    if pts:
        ax[0].plot([p[0] for p in pts], [p[1] for p in pts], 'o-', label=f'X={X}')
ax[0].axhline(1, color='k', lw=.6); ax[0].set_xscale('log'); ax[0].set_ylim(.994, 1.02)
ax[0].set_xlabel(r'bolt parameter $x_0=b^2$'); ax[0].set_ylabel(r'$J_6/(8\pi^2)$ of optimized cell')
ax[0].set_title('perpendicular CH cells: bolt-area branch'); ax[0].legend(fontsize=8)
nf = []
for f in glob.glob(str(H/'data/neutral_flux/nf_*X64*.json')):
    r = json.loads(Path(f).read_text())[0]; nf.append((r['x0'], r['compliance_RG'], r['CS_bound_from_G']/r['P_over_8pi2'], r['IG']['int_GWE']))
nf.sort(); nf = np.array(nf)
L = np.log(1/nf[:, 0])
ax[1].plot(L, nf[:, 1], 's-', label=r'compliance $R_G=\int G^2W\,dt$')
c = np.polyfit(L, nf[:, 1], 1)
ax[1].plot(L, np.polyval(c, L), ':', label=f'fit slope {c[0]:.3f} (flat-core value 1/8)')
ax[1].plot(L, nf[:, 2], 'o-', label=r'certified share $(\int GWE)^2/(8R_G P)$')
ax[1].plot(L, nf[:, 3], '^-', label=r'$\int G W E\,dt$')
ax[1].set_xlabel(r'$\log(1/x_0)$'); ax[1].set_title('bolt-carried neutral observable, X=64'); ax[1].legend(fontsize=7)
fig.tight_layout(); fig.savefig(H/'figures/area_branch.png', dpi=160)
print('fit', c.tolist())
