"""Collect data/o11rot/grid_*.json -> table (CSV) + figure.
Outputs: data/o11rot/summary.csv, figures/o11_rotation_slope.png
Columns: x0, theta, P_opt, slope=(P_opt-1)/x0, excess_over_theta0/x0, 4dW+, dS/12, resid, nit, msg
"""
import json, glob, os, csv
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(here, '..', 'data', 'o11rot')
rows = []
for f in glob.glob(os.path.join(D, 'grid_*.json')):
    d = json.load(open(f)); o = d['opt']
    rows.append(dict(x0=d['x0'], theta=d['theta'], P=o['P'], Pbase=d['base']['P'], dW=o['fourdWp'], dS=o['dS12'],
                     resid=o['resid'], nit=d['nit'], msg=d['msg'][:12]))
rows.sort(key=lambda r: (r['x0'], r['theta']))
P0 = {r['x0']: r['P'] for r in rows if r['theta'] == 0}
with open(os.path.join(D, 'summary.csv'), 'w', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['x0', 'theta', 'P_opt', 'slope', 'excess_over_x0', 'excess_over_x0_sin2', 'fourdWp', 'dS12', 'resid', 'nit', 'msg'])
    for r in rows:
        ex = (r['P'] - P0[r['x0']])/r['x0']; s2 = np.sin(r['theta'])**2
        w.writerow([r['x0'], round(r['theta'], 6), f"{r['P']:.8f}", f"{(r['P']-1)/r['x0']:.4f}", f"{ex:.4f}",
                    f"{ex/s2:.4f}" if s2 > 0 else '', f"{r['dW']:.6f}", f"{r['dS']:.6f}", f"{r['resid']:.1e}", r['nit'], r['msg']])
        print(r['x0'], round(r['theta'], 4), f"P={r['P']:.6f} slope={(r['P']-1)/r['x0']:.3f} ex/x0={ex:.3f}",
              f"ex/(x0 sin2)={ex/s2:.3f}" if s2 > 0 else '', f"4dW+={r['dW']:.5f} dS/12={r['dS']:.5f} res={r['resid']:.1e}")
fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
for x0 in sorted(P0):
    rs = [r for r in rows if r['x0'] == x0]
    th = np.array([r['theta'] for r in rs]); sl = np.array([(r['P']-1)/x0 for r in rs])
    ax[0].plot(th, sl, 'o-', label=f'$x_0={x0}$')
    ax[1].plot(np.sin(th)**2, np.array([(r['P']-P0[x0])/x0 for r in rs]), 'o-', label=f'$x_0={x0}$')
ax[0].axhline(6, color='k', ls=':', lw=1, label='Kähler slope 6')
ax[0].set_xlabel(r'relative angle $\theta$ between $\omega_{\rm Burns}$ and $\omega_{\rm CH}$')
ax[0].set_ylabel(r'$(P(U)/8\pi^2-1)/x_0$ (optimized)')
ax[0].legend(fontsize=8); ax[0].set_title('first-order cell cost vs relative orientation')
ax[1].set_xlabel(r'$\sin^2\theta$'); ax[1].set_ylabel(r'$[P(\theta)-P(0)]/(8\pi^2 x_0)$')
ax[1].legend(fontsize=8); ax[1].set_title('rotation penalty (upper bounds on the optimum)')
fig.tight_layout()
fig.savefig(os.path.join(here, '..', 'figures', 'o11_rotation_slope.png'), dpi=160)
