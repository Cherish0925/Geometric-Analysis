"""Figure: best numerical conformal-triaxial cell cost vs the Theorem-1 (conformally Kahler) bound.
Inputs: data/cell_sweep1/*.jsonl, data/cell_stage2/*.json. Output: figures/cell_cost_vs_bound.png"""
import json, glob, os, collections
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(here, '..', 'data')
best = collections.defaultdict(lambda: 1e99)
for f in glob.glob(D + '/cell_sweep1/*.jsonl'):
    for l in open(f):
        x = json.loads(l)
        if x['pen'] < 1e-8:
            best[(x['Rc'], x['mu'])] = min(best[(x['Rc'], x['mu'])], x['j'])
for f in glob.glob(D + '/cell_stage2/*.json'):
    x = json.loads(open(f).read())
    best[(x['Rc'], x['mu'])] = min(best[(x['Rc'], x['mu'])], x['j_full_best'])
fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
for Rc in sorted({k[0] for k in best}):
    mus = sorted(m for (R, m) in best if R == Rc and m <= 0.31)
    js = [best[(Rc, m)] for m in mus]
    bd = [(2 + m)**2 / (1 - m**2 / Rc**4) for m in mus]
    ax[0].plot(mus, [j - 4 for j in js], 'o-', label=f'R={Rc}')
    ax[1].plot(mus, [j - b for j, b in zip(js, bd)], 'o-', label=f'R={Rc}')
m = [1e-3, 0.3]
ax[0].plot(m, [4 * x for x in m], 'k--', lw=1, label='4 mu (area term)')
for a in ax:
    a.set_xscale('log'); a.set_xlabel('mu = r0^2  (exceptional area pi*mu)'); a.legend(fontsize=8)
ax[0].set_yscale('log'); ax[0].set_ylabel('j_best - 4   (j = J/2pi^2; threshold 4)')
ax[1].set_yscale('symlog', linthresh=1e-5)
ax[1].set_ylabel('j_best - (2+mu)^2/(1-mu^2/R^4)')
ax[0].set_title('Best conformal triaxial one-bolt cell cost above threshold')
ax[1].set_title('Excess over the conformally Kahler bound')
fig.tight_layout()
os.makedirs(os.path.join(here, '..', 'figures'), exist_ok=True)
fig.savefig(os.path.join(here, '..', 'figures', 'cell_cost_vs_bound.png'), dpi=160)
print('min excess over bound:', min(best[k] - (2 + k[1])**2 / (1 - k[1]**2 / k[0]**4) for k in best))
print('min j-4:', min(best[k] - 4 for k in best))
