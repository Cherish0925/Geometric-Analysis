"""Figure and table for the overlapping-tail pair interaction sweep (S1003A01 Step 13).
Reads data/pair_overlap/sweep_X8/w*_s0.json; writes figures/pair_overlap_interaction_X8.png and
data/pair_profile/pair_overlap_table_X8.csv with the phase decomposition
dJ(theta) ~ I0 + I4 cos(4 theta)  (I0 = dJ(pi/8), I4 = (dJ(0) - dJ(pi/4))/2)."""
import json, glob
from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
here = Path(__file__).resolve().parent
rows = []
for f in glob.glob(str(here/'../data/pair_overlap/sweep_X8/w*_s0.json')):
    rows += json.load(open(f))
ws = sorted({r['w'] for r in rows})
T = []
for w in ws:
    v = {round(r['theta'], 4): r for r in rows if r['w'] == w}
    a, b, c = v[0.0], v[0.3927], v[0.7854]
    I0 = b['dJ']; I4 = (a['dJ'] - c['dJ'])/2
    T.append([w, a['dJ'], b['dJ'], c['dJ'], I0, I4, min(a['dJ'], c['dJ']), a['J1_lens'],
              max(abs(r['dJ']-r['quad']) for r in (a, b, c)), a['min_eig']])
T = np.array(T)
np.savetxt(here/'../data/pair_profile/pair_overlap_table_X8.csv', T, delimiter=',',
           header='w,dJ_th0,dJ_thpi8,dJ_thpi4,I0,I4,min_dJ,J1_lens,max_nonlinear_remainder,min_eig_coords', comments='')
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(T[:, 0], T[:, 1], 'o-', label=r'$\theta=0$')
ax[0].plot(T[:, 0], T[:, 2], 's-', label=r'$\theta=\pi/8$ ($\approx I_0$)')
ax[0].plot(T[:, 0], T[:, 3], '^-', label=r'$\theta=\pi/4$')
ax[0].axhline(0, color='k', lw=.5); ax[0].set_yscale('symlog', linthresh=1e-9)
ax[0].set_xlabel(r'overlap depth $w=2\rho-d$'); ax[0].set_ylabel(r'$[J(g_{12})-2J(g_1)]/(8\pi^2)$')
ax[0].set_title('frozen certified cells, overlapping CH tails'); ax[0].legend(fontsize=8)
ax[1].semilogy(T[:, 0], -T[:, 6], 'o-', label='best-phase saving')
ax[1].semilogy(T[:, 0], T[:, 7], 's--', label=r'tail energy in lens $\int_L|E_1|^2/(8\pi^2)$')
ax[1].semilogy(T[:, 0], np.maximum(T[:, 8], 1e-16), 'x:', label='|nonlinear remainder|')
ax[1].set_xlabel(r'$w$'); ax[1].legend(fontsize=8); ax[1].set_title('saving vs Cauchy-Schwarz scale')
fig.tight_layout(); fig.savefig(here/'../figures/pair_overlap_interaction_X8.png', dpi=160)
print(np.array2string(T, precision=4))
