"""Step 8 figure: first-order O11 cell cost vs relative angle.
Envelope of the diabatic (Step 6 rotating-eigenframe) and adiabatic/fixed-slot
(Step 8) families, compared with the law  (P-1)/x0 = 6 cos^2 theta = -R^+(zeta,zeta),
split into 4dW+/x0 = 2(3cos^2-1) and dS/12/x0 = 2.
Output: figures/o11_first_order_law.png, data/o11perp/first_order_law.csv
"""
import json, glob, os, math
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__))
D6 = os.path.join(here, '..', 'data', 'o11rot'); D8 = os.path.join(here, '..', 'data', 'o11perp')
rows = []
for f in glob.glob(os.path.join(D6, 'grid_x0*_th*.json')):
    try: d = json.load(open(f))
    except Exception: continue
    if 'opt' not in d: continue
    rows.append(('diabatic', d['x0'], d['theta'], d['opt']['P'], d['opt']['fourdWp'], d['opt']['dS12']))
for f in glob.glob(os.path.join(D8, '*.json')):
    try: d = json.load(open(f))
    except Exception: continue
    name = os.path.basename(f)
    if name.startswith('aligned'): th = 0.0; fam = 'fixedslot_aligned'
    elif name.startswith('perp'): th = math.pi/2; fam = 'fixedslot_perp'
    else: th = d['theta']; fam = 'adiabatic'
    rows.append((fam, d['x0'], th, d['opt']['P'], d['opt']['fourdWp_A'], d['opt']['dS12']))
with open(os.path.join(D8, 'first_order_law.csv'), 'w') as fo:
    fo.write('family,x0,theta,P,fourdWp,dS12,slope\n')
    for r in sorted(rows, key=lambda r: (r[1], r[2], r[0])):
        fo.write('%s,%g,%.7f,%.10f,%.8f,%.8f,%.5f\n' % (r + ((r[3]-1)/r[1],)))
fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
tt = np.linspace(0, math.pi/2, 200)
for x0, mk in [(0.01, 'o'), (0.003, 's'), (0.001, '^')]:
    best = {}
    for r in rows:
        if abs(r[1]-x0) < 1e-12:
            k = round(r[2], 4)
            if k not in best or r[3] < best[k][3]: best[k] = r
    ks = sorted(best)
    ax[0].plot(ks, [(best[k][3]-1)/x0 for k in ks], mk+'-', label='best cell, x0=%g' % x0)
    ax[1].plot(ks, [best[k][4]/x0 for k in ks], mk+'-', color='C0', alpha=0.4+0.2*(x0 < 0.005))
    ax[1].plot(ks, [best[k][5]/x0 for k in ks], mk+'--', color='C3', alpha=0.4+0.2*(x0 < 0.005))
ax[0].plot(tt, 6*np.cos(tt)**2, 'k', lw=2, label=r'$6\cos^2\theta=-R^+(\zeta,\zeta)$')
ax[0].set_xlabel(r'relative angle $\theta$ between $\omega_{\rm Burns}$ and $\omega_{\rm CH}$')
ax[0].set_ylabel(r'$(P(U)/8\pi^2-1)/x_0$'); ax[0].legend(fontsize=8); ax[0].set_title('first-order joint cell cost')
ax[1].plot(tt, 2*(3*np.cos(tt)**2-1), 'C0', lw=2, label=r'$4\Delta W_+/x_0\to2(3\cos^2\theta-1)$')
ax[1].plot(tt, 2+0*tt, 'C3', lw=2, label=r'$\Delta S/12/x_0\to2$')
ax[1].axhline(0, color='gray', lw=0.5)
ax[1].set_xlabel(r'$\theta$'); ax[1].set_ylabel('per unit $x_0$ (units of $8\pi^2$)'); ax[1].legend(fontsize=8)
ax[1].set_title('Weyl/scalar split of the best cells')
fig.tight_layout()
fig.savefig(os.path.join(here, '..', 'figures', 'o11_first_order_law.png'), dpi=160)
print(len(rows), 'rows')
