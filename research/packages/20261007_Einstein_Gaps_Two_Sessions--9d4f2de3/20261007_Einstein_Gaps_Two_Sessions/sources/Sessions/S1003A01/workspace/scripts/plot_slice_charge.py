"""Figure: slice charge T/(8pi^2), flux Y and Kaehler defect Pi along representative cells,
and summary of the zero-flux certificate ratio 8pi^2 Pi(t*) / int_inside F.
Output: figures/slice_charge_profiles.png, data/transgression/zero_flux_summary.json
"""
import json, math, os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import profile_charge as pc

here = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(here, '..', 'data')
rows = [json.loads(l) for l in open(os.path.join(D, 'transgression', 'profile_charge_lines.jsonl')) if l.startswith('{')]
first, best = [], []
for r in rows:
    if r['zero_flux']:
        z0 = r['zero_flux'][0]
        first.append(z0['Pi'] / z0['intF_over_8pi2'])
        best.append(min(z['Pi'] / z['intF_over_8pi2'] for z in r['zero_flux']))
summ = {'n_profiles': len(rows), 'n_with_zero': len(first),
        'max_first_zero_ratio': max(first), 'max_best_zero_ratio': max(best),
        'n_first_zero_ratio_ge_1': int(sum(x >= 1 for x in first))}
print(summ)
json.dump(summ, open(os.path.join(D, 'transgression', 'zero_flux_summary.json'), 'w'), indent=1)

cases = [('cell_sweep1/run_3.0_0.001_full_0.0.jsonl', 0, r'$\mu=10^{-3},R=3$ (near-optimal)'),
         ('cell_sweep1/run_2.0_0.1_full_0.0.jsonl', 0, r'$\mu=0.1,R=2$ (near-optimal)'),
         ('cell_qsearch_small/musmall.jsonl', None, r'$\mu=0.01$, forced $q>0$'),
         ('cell_qsearch/main_mu01.jsonl', None, r'$\mu=0.1$, forced $q>0$')]
fig, ax = plt.subplots(1, 3, figsize=(15, 4.2))
for f, idx, lab in cases:
    L = [json.loads(l) for l in open(os.path.join(D, f))]
    if idx is None:
        idx = int(np.argmin([x['j'] for x in L]))
    rec = L[idx]
    o, (rn, T, H, vol) = pc.analyse(rec)
    x = rn / math.sqrt(rec['mu'])
    ax[0].semilogx(x, T / (8 * math.pi**2), label=lab + f', j={rec["j"]:.3f}')
    ax[1].semilogx(x, (H - 8 * math.pi**2 + T - 0) / (8 * math.pi**2) - T / (8 * math.pi**2) + 1, label=lab)
    ax[2].semilogx(x, H / (2 * math.pi**2), label=lab)
ax[0].set_xlabel(r'$r/\sqrt{\mu}$'); ax[0].set_ylabel(r'$T(r)/8\pi^2$'); ax[0].set_ylim(-0.1, 3)
ax[0].axhline(0, color='k', lw=.5); ax[0].legend(fontsize=7); ax[0].set_title('slice charge (bolt=1, flat=0)')
ax[1].set_xlabel(r'$r/\sqrt{\mu}$'); ax[1].set_ylabel(r'$\int_{\rm in}|Ric+g|^2/8\pi^2$')
ax[1].axhline(1, color='k', lw=.5, ls='--'); ax[1].set_title('inner energy (threshold = 1)'); ax[1].set_ylim(0, 3)
ax[2].set_xlabel(r'$r/\sqrt{\mu}$'); ax[2].set_ylabel(r'$j_{\rm partial}$'); ax[2].axhline(4, color='k', lw=.5, ls='--')
ax[2].set_title('cumulative cost'); ax[2].set_ylim(0, 12)
plt.tight_layout()
os.makedirs(os.path.join(here, '..', 'figures'), exist_ok=True)
plt.savefig(os.path.join(here, '..', 'figures', 'slice_charge_profiles.png'), dpi=160)
