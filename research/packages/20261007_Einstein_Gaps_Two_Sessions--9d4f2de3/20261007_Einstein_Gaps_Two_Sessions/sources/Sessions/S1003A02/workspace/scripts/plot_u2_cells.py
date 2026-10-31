"""Figure: U(2) blow-up cell cost P/(8 pi^2) vs bolt size x0 (Ric=-6g units).
Input: workspace/data/u2grid/u2_cell_grid2.jsonl ; output: workspace/figures/u2_cell_cost.png"""
import json, os
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(here, '..', 'data', 'u2grid', 'u2_cell_grid2.jsonl')) if l.strip()]
fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
for X, m in [(2.0, 'o'), (10.0, 's'), (50.0, '^')]:
    r = sorted([q for q in rows if q['X'] == X], key=lambda q: q['x0'])
    x0 = np.array([q['x0'] for q in r])
    ax[0].loglog(x0, [q['P_min'] - 1 for q in r], m + '-', label=f'non-Kähler U(2) min, X={X:g}')
    ax[0].loglog(x0, [q['P_kahler'] - 1 for q in r], m + ':', color='gray', alpha=.6)
    ax[1].semilogx(x0, [(q['P_min'] - 1)/q['x0'] for q in r], m + '-', label=f'X={X:g}')
xx = np.geomspace(1e-4, 10, 50)
ax[0].loglog(xx, 6*xx, 'k--', lw=1, label='6 x0 (Kähler first order)')
ax[0].set_xlabel('bolt size x0 = area(E)/π  [Ric = -6g]'); ax[0].set_ylabel('P_cell/(8π²) - 1')
ax[0].set_title('Cell cost above the Burns value 8π² (dotted: exact Kähler optimum)')
ax[0].legend(fontsize=7)
ax[1].axhline(6, color='k', ls='--', lw=1)
ax[1].set_xlabel('x0'); ax[1].set_ylabel('(P_cell/(8π²) - 1)/x0'); ax[1].set_title('effective slope; → 6 as x0 → 0')
ax[1].legend(fontsize=7)
plt.tight_layout()
out = os.path.join(here, '..', 'figures', 'u2_cell_cost.png')
plt.savefig(out, dpi=160); print(out)
